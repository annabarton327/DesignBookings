DROP TABLE IF EXISTS designers;

DROP TABLE IF EXISTS clients;

DROP TABLE IF EXISTS bookings;

CREATE TABLE designers (
  id INTEGER PRIMARY KEY,
  name TEXT,
  address TEXT,
  phone_number TEXT,
  company TEXT
);

CREATE TABLE clients (
  id INTEGER PRIMARY KEY,
  name TEXT,
  address TEXT,
  email TEXT
);

CREATE TABLE bookings (
  id INTEGER PRIMARY KEY,
  type TEXT,
  room TEXT,
  designer_id INTEGER,
  client_id INTEGER,
  consultation_date TEXT
);