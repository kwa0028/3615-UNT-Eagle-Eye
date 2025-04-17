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

cur.execute("""CREATE TABLE IF NOT EXISTS teachers(
            name VARCHAR(30),
            class VARCHAR(30),
            college VARCHAR(30),
            average DOUBLE,
            one INTEGER,
            two INTEGER,
            three INTEGER,
            four INTEGER,
            five INTEGER,
            six INTEGER,
            seven INTEGER,
            eight INTEGER,
            nine INTEGER,
            ten INTEGER
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








def getAverage(): #returns average score for a particular teacher
    #name = user input (change to parameter)
    cur.execute("SELECT * FROM public.teachers;") #WHERE name = %s;", (name)
    teacher=cur.fetchall()

    for col in teacher:
        print(f"name: {col[0]}, One: {col[5]}, Two: {col[6]}, Three: {col[7]}") #Just for Testing
        scoreOne = col[5]
        scoreTwo = col[6]
        scoreThree = col[7]
        scoreFour = col[8]
        scoreFive = col[9]
        scoreSix = col[10]
        scoreSeven = col[11]
        scoreEight = col[12]
        scoreNine = col[13]
        scoreTen = col[14]
        reviewCount = scoreOne + scoreTwo + scoreThree + scoreFour + scoreFive + scoreSix + scoreSeven + scoreEight + scoreNine + scoreTen
        #Need to add something to make sure reviewCount!=0 (Probably an If statment)
        avg = (scoreOne * 1 + scoreTwo * 2 + scoreThree * 3 + scoreFour * 4 + scoreFive * 5 + 
               scoreSix * 6 + scoreSeven * 7 + scoreEight * 8 + scoreNine * 9 + scoreTen * 10) / reviewCount
        col[3]=avg
        print(f"{col[3]}")
    



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



#To Do
# Teacher File List
# Review Teacher - Allow for updating the number of reviews and such
# Add difficulty rating
# connect to Javascript
# Clean Up Code
