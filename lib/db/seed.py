import faker
import sqlite3


#DATABAE ACCESS
con = sqlite3.connect("lib/db/design_database.db")
cur = con.cursor()

res = cur.execute("SELECT * FROM designer")
print(res.fetchall())


#FAKE ENTRIES IN THE DATABASE 
fake = faker.Faker()

for i in range(1, 50):
    name = fake.name()
    certification = fake.name()
    company = fake.company()

    cur.execute(f'''
        INSERT INTO designer ( name, certification, studio) 
        VALUES ("{name}", "{certification}", "{company}");
    ''')

con.commit()

for i in range(1, 200):
    name = fake.name()
    designer = fake.name() 
    address = fake.address()
    email = fake.email()

    cur.execute(f'''
        INSERT INTO client (name, designer, address, email)
        VALUES ("{name}", "{designer}", "{address}", "{email}");
    ''')

con.commit()

for i in range(1, 500):
    type = fake.name() 
    room = fake.name() 
    designer = fake.name() 
    client = fake.name() 
    consultation_date = fake.date() 

    cur.execute(f'''
        INSERT INTO booking (type, room, designer, client, consultation_date)
        VALUES ("{type}", "{room}", "{designer}", "{client}", "{consultation_date}");
    ''')

con.commit()

