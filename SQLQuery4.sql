--assessment5-constraints and schema design

/*create users table with:
primary key
unique email
not null password
and foreign key between orders and users.*/

--create user table
create table users (
    user_id int primary key, 
    name varchar(50),
    email varchar(100) unique,
    password varchar(100) not null);

--inserts data into users
INSERT INTO users VALUES
(1,'Cheriti Patel', 'ptlcheriti@gmail.com', 'cheri@123'),
(2, 'Riya Patel', 'riyap@gmail.com', 'riya@123'),
(3, 'Rutu Patil', 'prutu@gmail.com', 'rutu@123'),
(4, 'Vrutti Patel', 'vrutt@gmail.com', 'vrutti@123');

-- Create orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    order_amount INT   
);

-- Add foreign key constraint
ALTER TABLE orders
ADD CONSTRAINT fk_user
FOREIGN KEY (user_id)
REFERENCES users(user_id);

--inserts orders data
INSERT INTO orders VALUES
(101, 1, '2025-01-05', 2500.00),
(102, 1, '2025-01-10', 1800.00),
(103, 2, '2025-01-12', 3200.00),
(104, 3, '2025-01-15', 1500.00),
(105, 3, '2025-01-18', 2700.00);

--create index on email column
create index idx_users_email
on users(email);

--create view to display user order summary
create view user_order_summary as 
select 
    u.user_id,
    u.name,
    u.email,
    count(o.order_id) as total_orders,
    sum(o.order_amount) as total_amount
from users u left join orders o 
on u.user_id = o.order_id
group by u.user_id , u.name, u.email;

select * from user_order_summary;