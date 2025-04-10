#pip install psycopg2
#In Querey ... SELECT * FROM public.students
import psycopg2

print(psycopg2.__version__)

conn = psycopg2.connect(host="localhost",dbname="postgres",user="postgres",password="eagleeye",port=5432)
cur = conn.cursor()

#Clears Table
#cur.execute("""DROP TABLE IF EXISTS public.students""")

cur.execute("""CREATE TABLE IF NOT EXISTS students(
            username VARCHAR(30),
            passwrd VARCHAR(30)
            )
            """)

#Sign Up
def signUp():
    username = input("Enter username:")
    #check if username is already listed
    password = input("Enter password:")
    #nested if statments to verify requirments)
    if(len(password)<10):
        print("Password must be at least 10 characters, and contain at least 1 special character. Please try again.")
        signUp()
    else:
        if('!'in password or '@'in password or '#'in password or'$'in password or '%'in password or '^'in password or '&'in password
            or '*'in password or '_'in password or '+'in password or '='in password or '?'in password or '/'in password or '~'in password
            or ';'in password or ','in password or '<'in password or '>'in password or '|'in password or "'"in password):
            cur.execute("""INSERT INTO public.students (username, passwrd) 
                VALUES (%s, %s)""", (username, password))
            conn.commit()
        else:
            print("Password must contian at least 1 special character")
            signUp()

def logIn():
    print("Log In:")
    cur.execute("SELECT * FROM public.students;")
    students = cur.fetchall()
    logGuess=input("Enter username:")
    passGuess=input("Enter password:")
    for index, student in enumerate(students):
        print(f"Index: {index}, Username: {student[0]}, Password: {student[1]}")  # student[0] is username, student[1] is password
        if(student[0]==logGuess):
            if(student[1]==passGuess):
                print("Signed In")
                break
            print("Wrong Password")
            break
        print("No such account, please sign up")

    

signUp()
logIn()

#Update Table
conn.commit()

#Print Table
cur.execute("SELECT * FROM public.students;")
print(cur.fetchall())

#clean up
cur.close()
conn.close()
