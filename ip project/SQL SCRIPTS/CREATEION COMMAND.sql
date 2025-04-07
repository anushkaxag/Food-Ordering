 CREATE DATABASE online_food;
 USE online_food;
 
 CREATE TABLE users (
 id int PRIMARY KEY auto_increment  NOT NULL,
 name VARCHAR(20),
 email VARCHAR(30),
 phone varchar(10),
 password varchar(20)
 );
 
 create table restaurants(
 id int PRIMARY KEY auto_increment,
 name varchar(30),
 address varchar(100)
 );
 
 create table items(
 id int primary key auto_increment,
 restaurant_id int,
 name varchar(20),
 price float,
 FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
 );
 
 
 create table orders(
 id int primary key auto_increment,
 user_id int, 
 restaurant_id int, 
 delivery_address varchar(100), 
 status varchar(10),
 total float,
 FOREIGN KEY (USER_ID) REFERENCES USERS(ID),
 FOREIGN KEY (restaurant_id) REFERENCES restaurants(ID)
 );
 
 create table order_item(
 id int primary key auto_increment,
 order_id int, 
 item_id int, 
 quantity int, 
 FOREIGN KEY (order_id) REFERENCES orders(ID),
 FOREIGN KEY (item_id) REFERENCES ITEMS(ID)
 );

  INSERT INTO online_food.users(name, email, phone, password) 
values ('Anushka Agrawal', 'anushki@gmail.com', '7878480591', 'anushki' );
 
 INSERT INTO online_food.restaurants(id, name, address) 
values (1, 'Tan Suskh', "C-Scheme"), 
(2, 'Little Italy', "C-Scheme"), 
(3, 'Starbucks', "World Trade Park, JLN Marg");

INSERT INTO online_food.items(id, restaurant_id, name, price)
 values (1, 1, "Paneer Buttermasala", 330), 
  (2, 1, "Naan", 30),
  (3, 2, "Pasta", 430),
  (4, 3, "Coffee", 530),
  (5, 3, "Espresso", 730);