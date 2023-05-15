-- Local DB only:
CREATE DATABASE careerhive_app;
\c careerhive_app

-- Run on local and web service
CREATE TABLE jobs(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    company TEXT,
    contact TEXT,
    date DATE,
    salary INTEGER,
    employment_type TEXT,
    city TEXT,
    zipcode TEXT,
    country TEXT,
    title TEXT,
    description TEXT,
    logo TEXT
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password_digest TEXT
);

INSERT INTO users(first_name, last_name, email, password_digest) VALUES('Guest', 'Login', 'guest', 'guest');

CREATE TABLE saved(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    job_id INTEGER
);

CREATE TABLE applied(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    job_id INTEGER
);

CREATE TABLE reported(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    job_id INTEGER,
    message TEXT
);

CREATE TABLE viewed(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    job_id INTEGER
);