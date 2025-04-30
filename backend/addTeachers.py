import psycopg2

def seed_teachers():
    conn = psycopg2.connect(
        host="localhost",
        dbname="eagleeye_db",
        user="postgres",
        password="eagleeye",
        port=5432
    )
    cur = conn.cursor()

    # Optional: clear existing teachers table
    # cur.execute("DROP TABLE IF EXISTS public.teachers")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS teachers(
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

    cur.execute("""INSERT INTO teachers (name, class, college, average, one, two, three, four, five, six, seven, eight, nine, ten)
                VALUES ('Dr. Smith', 'CSCE1010', 'College of Engineering', 4.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)""")
    cur.execute("""INSERT INTO teachers (name, class, college, average, one, two, three, four, five, six, seven, eight, nine, ten)
                VALUES ('Dr. Johnson', 'MATH1710', 'College of Science', 4.2, 2, 3, 2, 3, 4, 2, 1, 0, 3, 2)""")
    cur.execute("""INSERT INTO teachers (name, class, college, average, one, two, three, four, five, six, seven, eight, nine, ten)
                VALUES ('Dr. Lee', 'PHYS1410', 'College of Arts and Sciences', 4.8, 0, 0, 1, 1, 1, 2, 3, 4, 5, 6)""")

    conn.commit()
    cur.close()
    conn.close()
    print("Teachers seeded successfully.")

if __name__ == "__main__":
    seed_teachers()
