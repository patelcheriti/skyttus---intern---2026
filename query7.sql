--assessment7-real-world case study

--create customer table
create table customers (
customer_id int primary key,
name varchar(50),
city varchar(50));

--insert the data in customer table
INSERT INTO customers VALUES
(1, 'Cheriti Patel', 'Chikhli'),
(2, 'Rutu Patil', 'Ahmedabad'),
(3, 'Riya Patel', 'Bilimora'),
(4, 'Vrutti Patel', 'Navsari'),
(5, 'Snehal Patel', 'Valsad');

select * from customers;

--create product table
create table products (
product_id int primary key,
product_name varchar(100),
price decimal(10, 2));

--insert the data in product table
insert into products values
(101, 'Laptop', 50000),
(102, 'Mobile', 20000),
(103, 'Headphones', 3000),
(104, 'Smart Watch', 7000);

select * from products;

--create the order table
create table orderss (
order_id int primary key,
customer_id int,
order_date date,
amount decimal(10,2),
foreign key (customer_id) references customers(customer_id));

--insert the data in order table
insert into orderss VALUES
(1001, 1, '2025-01-05', 70000),
(1002, 2, '2025-01-10', 20000),
(1003, 1, '2025-02-02', 50000),
(1004, 3, '2025-02-15', 23000),
(1005, 4, '2025-03-01', 7000);

select * from orderss;

--create order_item table
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orderss(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

--insert the date into order_item table
insert into order_items values
(1001, 101, 1),   -- Laptop
(1001, 102, 1),   -- Mobile
(1002, 102, 1),   -- Mobile
(1003, 101, 1),   -- Laptop
(1004, 102, 1),   -- Mobile
(1004, 103, 1),   -- Headphones
(1005, 104, 1);   -- Smart Watch

select * from order_items;

--total orders per customer
select c.customer_id, c.name, count(o.order_id) as total_orders
from customers c left join orderss o 
on c.customer_id = o.customer_id
group by c.customer_id, c.name;

--customers who never placed an order
select c.customer_id , c.name
from customers c left join orderss o
on c.customer_id = o.customer_id
where o.order_id is null;

--highest selling product
select top 1 p.product_name, sum(oi.quantity) as total_sold
from order_items oi join products p
on oi.product_id = p.product_id
group by p.product_name
order by total_sold desc;

--monthly sales report
select 
    year(order_date) as year, month(order_date) as month, sum(amount) as total_sales
from orderss
group by year(order_date), month(order_date)
order by year, month;

--customers with total purchase > 50,000
select c.customer_id, c.name, sum(o.amount) as total_purchase
from customers c join orderss o
on c.customer_id = o.customer_id
group by c.customer_id, c.name
having sum(o.amount) > 50000;

--top 3 cities by revenue
select top 3 c.city, sum(o.amount) as total_revenue
from customers c join orderss o
on c.customer_id = o.customer_id
group by c.city
order by total_revenue desc;
