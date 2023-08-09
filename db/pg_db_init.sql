CREATE DATABASE DEMO;

GRANT ALL PRIVILEGES ON DATABASE DEMO to "postgres";

CREATE SCHEMA IF NOT EXISTS TEST;

CREATE TABLE TEST.items (
   id serial primary key,
   name varchar(200),
   created_ts timestamptz not null,
   updated_ts timestamptz not null
);


