DROP TABLE IF EXISTS designer;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS booking;

CREATE TABLE designer (
  id INTEGER PRIMARY KEY,
    name TEXT,
    certification TEXT,
    company TEXT
);

CREATE TABLE client (
  id INTEGER PRIMARY KEY,
    name TEXT,
    designer TEXT,
    address TEXT,
    email TEXT
);

CREATE TABLE booking (
  id INTEGER PRIMARY KEY,
    type TEXT,
    room TEXT,
    designer TEXT,
    client TEXT,
    consultation_date TEXT
);
