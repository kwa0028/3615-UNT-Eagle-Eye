#pip install psycopg2
#In Querey ... SELECT * FROM public.students
import psycopg2

print(psycopg2.__version__)

conn = psycopg2.connect(host="localhost",dbname="postgres",user="postgres",password="eagleeye",port=5432)
cur = conn.cursor()

#Clears Table
#cur.execute("""DROP TABLE IF EXISTS public.students""")
cur.execute("""DROP TABLE IF EXISTS public.teachers""")


cur.execute("""CREATE TABLE IF NOT EXISTS students(
            username VARCHAR(30),
            passwrd VARCHAR(30)
            )
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS teachers(
            name VARCHAR(30),
            class VARCHAR(30),
            college VARCHAR(30),
            average DOUBLE PRECISION,
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


#Students
def signUp(username, password):
    #check if username is already listed?
    cur.execute("SELECT * FROM public.students")
    studentList=cur.fetchall()
    for col in studentList:
        nameHolder=col[1]
        if nameHolder!=username:
            print("")
        else:
            print("Username already exists")
            #return 1

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

def logIn(logGuess,passGuess):
    print("Log In:")
    cur.execute("SELECT * FROM public.students;")
    students = cur.fetchall()
    for index, student in enumerate(students):
        print(f"Index: {index}, Username: {student[0]}, Password: {student[1]}")  # student[0] is username, student[1] is password
        if(student[0]==logGuess):
            if(student[1]==passGuess):
                print("Signed In")
                break
            print("Wrong Password")
            break
        print("No such account, please sign up")
    



#Teachers
def giveReview(name, score):    #requires teacher with this.name exists
    cur.execute("SELECT * FROM public.teachers WHERE name = %s;", (name,))
    teacher=cur.fetchall()
    
    print(f"Fetched teachers: {teacher}")
    print(f"Number of teacher records: {len(teacher)}")
    
    scoreHolder=0
    #using if else chain since python lacks switch case
    if score == 10:
        scoreHolder=teacher[0][13]
        scoreHolder+=1
        cur.execute("UPDATE public.teachers SET ten = %s WHERE name = %s;", (scoreHolder, name))
    elif score == 9:
        scoreHolder=teacher[0][12]
        scoreHolder+=1
        cur.execute("UPDATE public.teachers SET nine = %s WHERE name = %s;", (scoreHolder, name))
    elif score == 8:
        scoreHolder = teacher[0][11]
        scoreHolder += 1
        cur.execute("UPDATE public.teachers SET eight = %s WHERE name = %s;", (scoreHolder, name))
    elif score == 7:
        scoreHolder = teacher[0][10]
        scoreHolder += 1
        cur.execute("UPDATE public.teachers SET seven = %s WHERE name = %s;", (scoreHolder, name))
    elif score == 6:
        scoreHolder = teacher[0][9]
        scoreHolder += 1
        cur.execute("UPDATE public.teachers SET six = %s WHERE name = %s;", (scoreHolder, name))
    elif score == 5:
        scoreHolder = teacher[0][8]
        scoreHolder += 1
        cur.execute("UPDATE public.teachers SET five = %s WHERE name = %s;", (scoreHolder, name))
    elif score == 4:
        scoreHolder = teacher[0][7]
        scoreHolder += 1
        cur.execute("UPDATE public.teachers SET four = %s WHERE name = %s;", (scoreHolder, name))
    elif score == 3:
        scoreHolder = teacher[0][6]
        scoreHolder += 1
        cur.execute("UPDATE public.teachers SET three = %s WHERE name = %s;", (scoreHolder, name))
    elif score == 2:
        scoreHolder = teacher[0][5]
        scoreHolder += 1
        cur.execute("UPDATE public.teachers SET two = %s WHERE name = %s;", (scoreHolder, name))
    elif score==1: 
        scoreHolder = teacher[0][4]
        scoreHolder += 1
        cur.execute("UPDATE public.teachers SET one = %s WHERE name = %s;", (scoreHolder, name))
    else:
        print("You have selected a score out of range, please select from 1 to 10")
    conn.commit()


def getAverage(name): #returns average score for a particular teacher
    #name = user input (change to parameter)
    cur.execute("SELECT * FROM public.teachers WHERE name = %s;", (name,))
    teacher=cur.fetchall()

    for col in teacher:
        scoreOne = col[4]
        scoreTwo = col[5]
        scoreThree = col[6]
        scoreFour = col[7]
        scoreFive = col[8]
        scoreSix = col[9]
        scoreSeven = col[10]
        scoreEight = col[11]
        scoreNine = col[12]
        scoreTen = col[13]
        reviewCount = scoreOne + scoreTwo + scoreThree + scoreFour + scoreFive + scoreSix + scoreSeven + scoreEight + scoreNine + scoreTen
        if reviewCount!=0:
            avg = (scoreOne * 1 + scoreTwo * 2 + scoreThree * 3 + scoreFour * 4 + scoreFive * 5 + 
                   scoreSix * 6 + scoreSeven * 7 + scoreEight * 8 + scoreNine * 9 + scoreTen * 10) / reviewCount
        else:
            avg=0
        cur.execute("UPDATE public.teachers SET average = %s WHERE name = %s;", (avg, name))
    conn.commit()
    #return avg
    
def reviewCount(name):
    cur.execute("SELECT * FROM public.teachers WHERE name = %s;", (name,))
    teacher=cur.fetchall()
    for col in teacher:
        scoreOne = col[4]
        scoreTwo = col[5]
        scoreThree = col[6]
        scoreFour = col[7]
        scoreFive = col[8]
        scoreSix = col[9]
        scoreSeven = col[10]
        scoreEight = col[11]
        scoreNine = col[12]
        scoreTen = col[13]
        reviewCount = scoreOne + scoreTwo + scoreThree + scoreFour + scoreFive + scoreSix + scoreSeven + scoreEight + scoreNine + scoreTen
    return reviewCount



# IF teachers is empty
cur.execute("SELECT COUNT(*) FROM public.teachers;")
count = cur.fetchone()[0]
if count == 0:
    name="Jane Doe"
    className="Computer Science"
    coll = "College of Engineering"
    numHolder=0
    avgHolder=0.0
    cur.execute("""INSERT INTO public.teachers (name, class, college, average, one, two, three, four, five, six, seven, eight, nine, ten) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                      (name, className, coll, avgHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder))
    name="John Doe"
    className="Computer Science"
    coll = "College of Engineering"
    numHolder=0
    avgHolder=0.0
    cur.execute("""INSERT INTO public.teachers (name, class, college, average, one, two, three, four, five, six, seven, eight, nine, ten) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                      (name, className, coll, avgHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder))
    name="Hadiseh Gooran"
    className="Computer Science"
    coll = "College of Engineering"
    numHolder=0
    avgHolder=0.0
    cur.execute("""INSERT INTO public.teachers (name, class, college, average, one, two, three, four, five, six, seven, eight, nine, ten) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                      (name, className, coll, avgHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder, numHolder))







#Update Table
conn.commit()

#Print Table
#cur.execute("SELECT * FROM public.students;")
cur.execute("SELECT * FROM public.teachers;")
print(cur.fetchall())

#clean up
cur.close()
conn.close()



#To Do
# connect to Javascript
# Clean Up Code
