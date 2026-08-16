import os
import psycopg2
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()


def get_connection():

    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT", 5432))
    )

    return connection


def create_table():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS metrics (

        id SERIAL PRIMARY KEY,

        cpu_usage FLOAT,

        memory_usage FLOAT,

        disk_usage FLOAT,

        network_sent BIGINT,

        network_received BIGINT,

        uptime FLOAT,

        created_at TIMESTAMP

    )
    """

    cursor.execute(query)

    connection.commit()

    cursor.close()
    connection.close()


def save_metrics(data):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO metrics
    (
        cpu_usage,
        memory_usage,
        disk_usage,
        network_sent,
        network_received,
        uptime,
        created_at
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["cpu"],
        data["memory"]["percent"],
        data["disk"]["percent"],
        data["network"]["bytes_sent"],
        data["network"]["bytes_received"],
        data["uptime"],
        datetime.now()
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()
