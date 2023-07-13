-- Local DB only:
CREATE DATABASE stingsearch_app;
\c stingsearch_app

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
    username TEXT,
    email TEXT,
    password_digest TEXT
);

INSERT INTO users(username, email, password_digest) VALUES('Guest', 'guest', 'guest');

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
    message TEXT,
    date DATE
);

CREATE TABLE viewed(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    job_id INTEGER
);