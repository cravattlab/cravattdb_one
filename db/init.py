from config import PGSQL_DATABASE_NAME, PGSQL_DATABASE_USER, PGSQL_DATABASE_PASSWORD
import os, psycopg2, sys

def main():
    conn = psycopg2.connect(
        database = PGSQL_DATABASE_NAME,
        user = PGSQL_DATABASE_USER,
        password = PGSQL_DATABASE_PASSWORD
    )

    cur = conn.cursor()

    for root, dirs, files in os.walk('schema'):
        # moving experiments.sql to the end since it depends on other tables
        files.append(files.pop(files.index('experiments.sql')))
        
        for file in files:
            if file.endswith('.sql'):
                with open(os.path.join('schema', file), 'r') as table:
                    create_sql = table.read()

                cur.execute(create_sql)
                conn.commit()

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()