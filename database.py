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
        else:
            print("Password must contian at least 1 special character")
            signUp()


signUp()


#Update Table
conn.commit()

#Print Table
cur.execute("SELECT * FROM public.students;")
print(cur.fetchall())

#clean up
cur.close()
conn.close()

#note
#Adds student objects chronologically, 
#unless usernames match in which case it's alphabetical