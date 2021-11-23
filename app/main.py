import prefect
import subprocess
from prefect import task, Flow
from prefect.schedules import IntervalSchedule
from datetime import timedelta, datetime



@task(max_retries=2, retry_delay=timedelta(seconds=10))
def sam():
    res = subprocess.run(['python','scrap.py'])


if __name__ == '__main__':
    schedule = IntervalSchedule(
    start_date=datetime.utcnow() + timedelta(seconds=30),
    interval=timedelta(minutes=1),
)
    with Flow("Sam", schedule=schedule) as flow:
        sam()

    flow.run()
    
