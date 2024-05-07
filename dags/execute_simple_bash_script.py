"""
# Execute a bash script file
"""

from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from pendulum import datetime


SIMPLE_BASH_SCRIPT_FILE = Variable.get("SIMPLE_BASH_SCRIPT_FILE")
SIMPLE_BASH_SCRIPT_FILE_PATH = "$AIRFLOW_HOME/" +  SIMPLE_BASH_SCRIPT_FILE + " "


@dag(start_date=datetime(2022, 8, 1),
    schedule="@daily",
    tags=["bashOperator"],
    doc_md=__doc__,
    description="Execute a bash script",
    schedule_interval=None,
    catchup=False,
)
def bash_script_dag():
    get_list_files = BashOperator(
        task_id="get_list_files",
        # Note the space at the end of the command!
        #bash_command="$AIRFLOW_HOME/include/my_bash_script.sh ",
        bash_command=SIMPLE_BASH_SCRIPT_FILE_PATH,
        # since the env argument is not specified, this instance of the
        # BashOperator has access to the environment variables of the Airflow
        # instance like AIRFLOW_HOME
    )

    get_list_files


bash_script_dag()
