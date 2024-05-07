"""
# Execute two bash commands using one BashOperator
"""

from airflow.decorators import dag
from airflow.operators.bash import BashOperator
from pendulum import datetime

import random


MY_NAME = "ZeroTech"
LARGE_NUMBER =  str(random.randint(1_000_000, 2_000_000_000))
ENV_VARIABLES = {"MY_NAME": MY_NAME, "A_LARGE_NUMBER": LARGE_NUMBER}


@dag(
    start_date=datetime(2022, 8, 1),
    tags=["bashOperator"],
    doc_md=__doc__,
    description="Play two bash commands with one BashOperator",
    schedule_interval=None,
    catchup=False,
)
def execute_two_commands():
    say_hello_and_create_a_secret_number = BashOperator(
        task_id="say_hello_and_create_a_secret_number",
        bash_command="echo Hello $MY_NAME! && echo $A_LARGE_NUMBER | rev  2>&1\
                    | tee $AIRFLOW_HOME/include/my_secret_number.txt",
        env=ENV_VARIABLES,
        append_env=True, #For using an environment variable from the Airflow environment, $AIRFLOW_HOME
    )

    say_hello_and_create_a_secret_number


execute_two_commands()
