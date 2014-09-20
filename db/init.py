from db import Database
import os

def main():

    db = Database()

    for root, dirs, files in os.walk('schema'):
        # moving experiments.sql to the end since it depends on other tables
        files.append(files.pop(files.index('experiments.sql')))
        
        for file in files:
            if file.endswith('.sql'):
                with open(os.path.join('schema', file), 'r') as table:
                    create_sql = table.read()
                    db.cursor.execute(create_sql)
                    db.connection.commit()

    db.close

if __name__ == "__main__":
    main()