import sys, os
sys.path.append('..')

from db import Database

db = Database()

def main():
    create_schema()
    seed_data()
    db.close()

def create_schema():
    files = [files for root, dirs, files in os.walk('schema')][0]
    # moving experiments.sql to the end since it depends on other tables
    files.append(files.pop(files.index('experiments.sql')))
    import_files('schema', files)

def seed_data():
    import_files('data', [files for root, dirs, files in os.walk('data')][0])

def import_files(path, files):
    for file in files:
        if file.endswith('.sql'):
            with open(os.path.join(path, file), 'r') as table:
                create_sql = table.read()
                db.cursor.execute(create_sql)
                db.connection.commit()

if __name__ == "__main__":
    main()