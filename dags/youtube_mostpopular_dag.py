from airflow.decorators import dag, task
from datetime import datetime
from pyyoutube import Client
import pandas as pd


@dag(start_date=datetime(2023, 1, 1), schedule="@daily", tags=["project", "gcp"])
def youtube_mostpopular_dag():
    """
    ### Add DAG info
    """

    @task()
    def get_youtube_data():
        """
        Task info
        """
        pass

    get_youtube_data()


youtube_mostpopular_dag()
