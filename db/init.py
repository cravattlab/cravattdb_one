from config import PGSQL_DATABASE_NAME, PGSQL_DATABASE_USER, PGSQL_DATABASE_PASSWORD
import os, psycopg2

conn = psycopg2.connect(
    database = PGSQL_DATABASE_NAME,
    user = PGSQL_DATABASE_USER,
    password = PGSQL_DATABASE_PASSWORD
)

cur = conn.cursor()

with open('db/schema/experiment.sql') as table:
    create_sql = table.read()