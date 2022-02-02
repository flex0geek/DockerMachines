# SQL Injection
## Run Docker
1. download the docker image
2. open folder using your terminal
3. run `docker-compose up`

The application will run in port 80 and Database on port 8888 you can modify these ports on file `docker-compose.yml`
![ports](https://github.com/flex0geek/DockerMachines/blob/main/sql_injection/img/ports.png)


## Setup DB
1. open DB manager on `localhost:8888`
2. login using `root/example`
3. create database with name `call`
![create db](https://github.com/flex0geek/DockerMachines/blob/main/sql_injection/img/1.create_db.png)

4. select the DB which you created and click on `SQL command`
![sql command](https://github.com/flex0geek/DockerMachines/blob/main/sql_injection/img/2.sql_command.png)

5. execute the following queries
```
CREATE TABLE `users` (
  `fullname` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL UNIQUE,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
);

CREATE TABLE `command` (
  `content` varchar(255) NOT NULL
);

INSERT INTO users VALUES('Admin User','admin','JustHARDpAsswd','admin@admin.com');
```
![execute](https://github.com/flex0geek/DockerMachines/blob/main/sql_injection/img/3.execute.png)


## Goal
1. don't look to the Source Code try it as a black box
2. don't use automation tools like SQLMap
3. write a script to admin's extract password from DB
4. there are 2 types of SQL injection in this machine try to find them.

# if you can't write the script read this section.
## Solution

if you can't write the script read this section.
I will attach 2 scripts in python to extract data from the database using direct queries, how to use script?
```
script.py <hostname:port> "<injection_query>"

Exp:
script.py localhost "select table_name from information_schema.tables where table_schema=database() limit 1,1"
```
if the query return an error or empty or more than one result the length will be None.

SQL Commands you may need
1. create table and columns
```
CREATE TABLE `users` (
  `fullname` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL UNIQUE,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
)
```
2. Insert admin's information
```
INSERT INTO users VALUES('Admin User','admin','JustHARDpAsswd','admin@admin.com')
```
3. To clear all data expect admin account
```
DELETE FROM users where username != 'admin'
```
