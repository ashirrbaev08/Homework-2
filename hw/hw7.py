import sqlite3

connect = sqlite3.connect('students.db')

cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS students(
            name VARCHAR (40) NOT NULL,
            age INTEGER NOT NULL,
            course INTEGER
        )
''')

connect.commit()

def create_stundent(name,age,course=None):

    cursor.execute(
        'INSERT INTO students(name,age,course) VALUES(?,?,?)',
        (name,age,course)
    )
    connect.commit()
    print(f'Студент добавлен  {name}!')

# create_stundent("Karim",23,4)

def get_students():
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    # print(students)
    for i in students:
        print(f"NAME:{i[0]} AGE:{i[1]} COURSE:{i[2]}")
#
# get_students()

def update_students(row_id, name):

    cursor.execute(
        'UPDATE students SET name = ? WHERE rowid = ? ',
        (name,row_id)
    )
    connect.commit()
    print("Имя изменен!")

# update_students(row_id=2,name="Bektur")

def delete_user(row_id):
    cursor.execute(
        'DELETE FROM students WHERE rowid = ?',
        (row_id,)
    )
    connect.commit()
    print("Студент удален!")

# delete_user(3)

def get_by_rowid(row_id):
    cursor.execute(
        'SELECT rowid,name,age,course FROM students WHERE rowid = ? ',
        (row_id,)
    )
    student = cursor.fetchone()
    if student:
        print(f"ID:{student[0]} NAME:{student[1]} AGE:{student[2]} COURSE:{student[3]}")
    else:
        print("Студент не найден")

get_by_rowid(2)

