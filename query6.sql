--assessment6-transaction and safety
--create accounts table
create table accounts (
account_id int primary key,
account_name varchar(50),
balance decimal(10,2));

--insert records into accounts table
insert into accounts values 
(1, 'Cheriti', 10000.00),
(2, 'Riya', 8000.00);

select * from accounts;

--start a transaction
begin transaction;

--rollback changes
begin transaction;
	
	--debit cheriti
	update accounts 
	set balance = balance - 2000
	where account_id = 1;

	--debit riya
	update accounts 
	set balance = balance + 2000
	where account_id = 2;

	--cancel the transaction
	rollback;

--demonstrate transfer of money using transaction
--commit valid transaction
begin transaction;

	--debit cheriti
	update accounts 
	set balance = balance - 2000
	where account_id = 1;

	--debit riya
	update accounts 
	set balance = balance + 2000
	where account_id = 2;

	--save changes
	commit;
