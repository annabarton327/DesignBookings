import faker
import sqlite3
import random


# DATABAE ACCESS
con = sqlite3.connect("lib/db/design_database.db")
cur = con.cursor()


# FAKE ENTRIES IN THE DATABASE
fake = faker.Faker()

# 50 random designers
NUM_DESIGNERS = 50
for i in range(1, NUM_DESIGNERS):
    name = fake.name()
    company = fake.company()
    phone_number = fake.phone_number()
    address = fake.address()

    cur.execute(f'''
        INSERT INTO designers (name, address, phone_number, company)
        VALUES ("{name}", "{address}", "{phone_number}", "{company}");
    ''')

# 200 random clients
NUM_CLIENTS = 200
for i in range(1, NUM_CLIENTS):
    name = fake.name()
    address = fake.address()
    email = fake.email()

    cur.execute(f'''
        INSERT INTO clients (name, address, email)
        VALUES ("{name}", "{address}", "{email}");
    ''')

NUM_BOOKINGS = 500
for i in range(1, NUM_BOOKINGS):
    type = random.choice(
        ["Bohemian", "New Age", "Traditional", "California Chic", "Asian", "Coastal", "Contemporary", "County", "Industrial", "Modern", "Traditional"])
    room = random.choice(
        ["Kitchen", "Dining Room", "Basement", "Bedroom", "Living Room"])
    designer_id = random.randint(1, NUM_DESIGNERS-1)  # foreign key
    client_id = random.randint(1, NUM_CLIENTS-1)  # foreign key
    consultation_date = fake.date()

    cur.execute(f'''
        INSERT INTO bookings (type, room, designer_id, client_id, consultation_date)
        VALUES ("{type}", "{room}", "{designer_id}", "{client_id}", "{consultation_date}");
    ''')

con.commit()


