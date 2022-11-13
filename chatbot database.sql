create database chatbot
use chatbot

ALTER DATABASE chatbot
SET MULTI_USER; -- set database to multi-user so everyone can see the same result 

CREATE LOGIN corp  
    WITH PASSWORD = '123';  
CREATE USER corp FOR LOGIN corp;  -- admin is one who created them


drop table [order]


create table [order](
id int primary key identity(1,1),
email varchar(60), 
Item_code varchar(50),
CreatedOn date,
Quantity int,
[Status] varchar(50)
)

select * from [order]
delete from [order]
insert into [order](email,Item_code,CreatedOn,Quantity,[Status]) values ('j','a',getdate(),10,'pending')