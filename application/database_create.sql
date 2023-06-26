
create database symptom_log;
use symptom_log;

create table symptom_log.user_data (
    user_id int not null serial primary key,
    username varchar(255) not null,
    password varchar(50) not null,
    firstname varchar(50) null,
    lastname varchar(50) null,
    email varchar(100) null
);

create table symptom_log.symptom_collection (
    symptom_id int not null SERIAL primary key,
    date date not null,
    time time not null,
    symptom_details varchar(255) not null,
    user_id int,
    FOREIGN KEY (user_id) REFERENCES user_data(user_id),
    summary_id int,
    FOREIGN KEY (summary_id) REFERENCES summary_collection(summary_id)
);

-- varchar(255) is the max length of a string in MySQL, example:
-- "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur quis est vel elit faucibus pulvinar. Sed suscipit, mi et eleifend laoreet, nisl libero bibendum justo, vitae scelerisque eros metus sit amet justo. Lorem."

create table symptom_log.summary_collection (
    summary_id int not null SERIAL primary key,
    symptoms_summary varchar(500) not null,
    symptoms_start_date date not null,
    symptoms_end_date date not null,
    user_id int,
    FOREIGN KEY (user_id) REFERENCES user_data(user_id)
);

-- To add a foreign key to a table post-creation, use the following syntax:
-- ALTER TABLE symptom_log.symptom_collection
-- ADD COLUMN user_id int,
-- ADD CONSTRAINT fk_symptom_collection_user_id FOREIGN KEY (user_id) REFERENCES user_data(user_id);
