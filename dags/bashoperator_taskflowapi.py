"""
# Play the BashOperator with TaskFlow API
"""

from airflow.decorators import task, dag
from pendulum import datetime

LOOK_EXTERNAL_FILE = "./include" # The best way is to declare a variable from Airflow UI

@dag(
    dag_id="bashoperator_taskflow_api",  # You define you own name
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    tags=["bashOperator"],
    doc_md=__doc__,
    description="Play BashOperator with TaskFlow API",
    schedule_interval=None,
    catchup=False,
    # include path to look for external files
    template_searchpath=LOOK_EXTERNAL_FILE,
)
def bashoperator_taskflow_api():
    
    @task
    def upstream_task():
        dog_owner_data = {
            "names": ["Trevor", "Grant", "Marcy", "Carly", "Philip"],
            "dogs": [1, 2, 2, 0, 4],
        }

        return dog_owner_data

    """This decorator is especially useful when you want to run bash commands based on complex Python logic, 
        including inputs from upstream tasks."""
    @task.bash
    def bash_task(dog_owner_data):
        names_of_dogless_people = []
        for name, dog in zip(dog_owner_data["names"], dog_owner_data["dogs"]):
            if dog < 1:
                names_of_dogless_people.append(name)

        if names_of_dogless_people:
            if len(names_of_dogless_people) == 1:
                # this bash command is executed if only one person has no dog
                return f'echo "{names_of_dogless_people[0]} urgently needs a dog!"'
            else:
                names_of_dogless_people_str = " and ".join(names_of_dogless_people)
                # this bash command is executed if more than one person has no dog
                return f'echo "{names_of_dogless_people_str} urgently need a dog!"'
        else:
            # this bash command is executed if everyone has at least one dog
            return f'echo "All good, everyone has at least one dog!"'

    bash_task(dog_owner_data=upstream_task())
    
bashoperator_taskflow_api()