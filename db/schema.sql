-- Local DB only:
CREATE DATABASE careerhive_app;
\c careerhive_app

-- Run on local and web service
CREATE TABLE jobs(
    id SERIAL PRIMARY KEY,
    title TEXT,
    salary REAL,
    type TEXT,
    company TEXT,
    location TEXT,
    url TEXT,
    description TEXT,
    date_posted TIMESTAMP
);

INSERT INTO jobs(title, salary, type, company, location, url, description, date_posted)
VALUES
    ('Psychiatrist', 72000,'Full-time', 'Charterhouse Recruitment (Australia)', 'Gold Coast City
    ', 'https://www.jobleads.com/registration/job?campaignId=62&jobId=e5190deb2f742dc6a3516cb078043d547&jmId=999&utm_source=jooble%7Cr-jb%7Cc-au&utm_medium=job-external&utm_campaign=jobs&utm_content=jobmarket-id%3D999%7Clandingpage-id%3D158%7Cjob-id%3D5190deb2f742dc6a3516cb078043d547%7Cjob-workarea%3D05-03%7Cjob-hierarchy%3D04%7Cjob-salary-benchmark%3D04%7Cjob-industry%3D46%7Cjob-location%3Dgold-coast-city%7Cjobtitle%3Dpsychiatrist&jobjmlp=158&ccuid=46062991141', 'Charterhouse Medical are currently looking for a Locum Consultant Psychiatrist for an upcoming urgent locum placement as follows.', CURRENT_TIMESTAMP),
    ('Lawyer', 72000,'Full-time', 'Charterhouse Recruitment (Australia)', 'Gold Coast City
    ', 'https://www.jobleads.com/registration/job?campaignId=62&jobId=e5190deb2f742dc6a3516cb078043d547&jmId=999&utm_source=jooble%7Cr-jb%7Cc-au&utm_medium=job-external&utm_campaign=jobs&utm_content=jobmarket-id%3D999%7Clandingpage-id%3D158%7Cjob-id%3D5190deb2f742dc6a3516cb078043d547%7Cjob-workarea%3D05-03%7Cjob-hierarchy%3D04%7Cjob-salary-benchmark%3D04%7Cjob-industry%3D46%7Cjob-location%3Dgold-coast-city%7Cjobtitle%3Dpsychiatrist&jobjmlp=158&ccuid=46062991141', 'Charterhouse Medical are currently looking for a Locum Consultant Psychiatrist for an upcoming urgent locum placement as follows.', CURRENT_TIMESTAMP),
    ('Dean', 72000,'Full-time', 'Charterhouse Recruitment (Australia)', 'Gold Coast City
    ', 'https://www.jobleads.com/registration/job?campaignId=62&jobId=e5190deb2f742dc6a3516cb078043d547&jmId=999&utm_source=jooble%7Cr-jb%7Cc-au&utm_medium=job-external&utm_campaign=jobs&utm_content=jobmarket-id%3D999%7Clandingpage-id%3D158%7Cjob-id%3D5190deb2f742dc6a3516cb078043d547%7Cjob-workarea%3D05-03%7Cjob-hierarchy%3D04%7Cjob-salary-benchmark%3D04%7Cjob-industry%3D46%7Cjob-location%3Dgold-coast-city%7Cjobtitle%3Dpsychiatrist&jobjmlp=158&ccuid=46062991141', 'Charterhouse Medical are currently looking for a Locum Consultant Psychiatrist for an upcoming urgent locum placement as follows.', CURRENT_TIMESTAMP),
    ('GP', 72000,'Full-time', 'Charterhouse Recruitment (Australia)', 'Gold Coast City
    ', 'https://www.jobleads.com/registration/job?campaignId=62&jobId=e5190deb2f742dc6a3516cb078043d547&jmId=999&utm_source=jooble%7Cr-jb%7Cc-au&utm_medium=job-external&utm_campaign=jobs&utm_content=jobmarket-id%3D999%7Clandingpage-id%3D158%7Cjob-id%3D5190deb2f742dc6a3516cb078043d547%7Cjob-workarea%3D05-03%7Cjob-hierarchy%3D04%7Cjob-salary-benchmark%3D04%7Cjob-industry%3D46%7Cjob-location%3Dgold-coast-city%7Cjobtitle%3Dpsychiatrist&jobjmlp=158&ccuid=46062991141', 'Charterhouse Medical are currently looking for a Locum Consultant Psychiatrist for an upcoming urgent locum placement as follows.', CURRENT_TIMESTAMP),
    ('Dentist', 72000,'Full-time', 'Charterhouse Recruitment (Australia)', 'Gold Coast City
    ', 'https://www.jobleads.com/registration/job?campaignId=62&jobId=e5190deb2f742dc6a3516cb078043d547&jmId=999&utm_source=jooble%7Cr-jb%7Cc-au&utm_medium=job-external&utm_campaign=jobs&utm_content=jobmarket-id%3D999%7Clandingpage-id%3D158%7Cjob-id%3D5190deb2f742dc6a3516cb078043d547%7Cjob-workarea%3D05-03%7Cjob-hierarchy%3D04%7Cjob-salary-benchmark%3D04%7Cjob-industry%3D46%7Cjob-location%3Dgold-coast-city%7Cjobtitle%3Dpsychiatrist&jobjmlp=158&ccuid=46062991141', 'Charterhouse Medical are currently looking for a Locum Consultant Psychiatrist for an upcoming urgent locum placement as follows.', CURRENT_TIMESTAMP),
    ('Lecturer', 72000,'Full-time', 'Charterhouse Recruitment (Australia)', 'Gold Coast City
    ', 'https://www.jobleads.com/registration/job?campaignId=62&jobId=e5190deb2f742dc6a3516cb078043d547&jmId=999&utm_source=jooble%7Cr-jb%7Cc-au&utm_medium=job-external&utm_campaign=jobs&utm_content=jobmarket-id%3D999%7Clandingpage-id%3D158%7Cjob-id%3D5190deb2f742dc6a3516cb078043d547%7Cjob-workarea%3D05-03%7Cjob-hierarchy%3D04%7Cjob-salary-benchmark%3D04%7Cjob-industry%3D46%7Cjob-location%3Dgold-coast-city%7Cjobtitle%3Dpsychiatrist&jobjmlp=158&ccuid=46062991141', 'Charterhouse Medical are currently looking for a Locum Consultant Psychiatrist for an upcoming urgent locum placement as follows.', CURRENT_TIMESTAMP);

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password_digest TEXT
);

CREATE TABLE saved(
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    job_id INTEGER
);