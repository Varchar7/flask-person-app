import sqlite3


db = sqlite3.connect("example.db")
cursor = db.cursor()
table_name = "PERSON"


def create_table(table_name):
    cursor.execute(
        f'''CREATE TABLE IF NOT EXISTS {table_name}
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT,
        EMAIL TEXT,AGE INT ,SALARY REAL) ''')


def fetch():
    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()
    for record in records:
        id, name, email, age, salary = record
        print("\nID : ", id)
        print("NAME : ", name)
        print("EMAIL : ", email)
        print("AGE : ", age)
        print("SALARY : ", salary, "\n")


def insert(query):
    cursor.execute(query)


def delete(id):
    cursor.execute(f"DELETE FROM {table_name} WHERE ID = {id}")


def commit():
    db.commit()


def update():
    fields = ["", "NAME", "EMAIL", "AGE", "SALARY"]
    for i in range(1, len(fields)):
        print(f"{i} FOR CHANGE PERSON {fields[i]}")

    field = int(input("GIVE YOUR CHOICE : "))
    field_id = int(input("GIVE ID TO UPDATE RECORD : "))
    query = f"UPDATE {table_name} SET {fields[field]}=? WHERE ID=?"
    new_field = input(f"GIVE NEW VALUE OF {fields[field]} :")
    cursor.execute(query, (new_field, field_id))


create_table(table_name)
while True:
    print("FOR CLOSE  0")
    print("FOR INSERT 1")
    print("FOR DELETE 2")
    print("FOR FETCH ALL 3")
    print("FOR COMMIT 4")
    print("FOR UPDATE 5\n")

    choice = input("YOUR CHOICE :")
    if choice == '0':
        db.close()
        break
    elif choice == '1':
        name = input("PERSON NAME :")
        email = input("PERSON EMAIL :")
        age = input("PERSON AGE :")
        salary = input("PERSON SALARY :")
        insert(
            f'''INSERT INTO {table_name}(NAME,EMAIL,AGE,SALARY)
             VALUES('{name}','{email}','{age}',{salary})''')
    elif choice == '2':
        id = input("PERSON ID :")
        delete(id)
    elif choice == '3':
        fetch()
    elif choice == '4':
        commit()
    elif choice == '5':
        update()
    else:
        print("WRONG CHOICE")
