--assessment8-query optimization

--add index to improve search on orderss.customer_id
create index idx_orderss_customer_id
on orderss(customer_id);

--use explain to analyze query
--EXPLAIN
select * 
from orderss
where customer_id = 1;

--drop index idx_orderss_customer_id on orderss;

--optimize a slow join query
create index idx_orders_customer_id on orderss(customer_id);
create index idx_customers_customer_id on customers(customer_id);

--explain when index should not be used
select * from orderss
where year(order_date) = 2024;  --index not used