--odps sql 
--********************************************************************--
--author:qiyangduan
--create time:2020-04-01 19:42:04
--********************************************************************--


create table online_retail (
invoiceno	 String,
stockcode	String,
description	String,
quantity	int,
invoicedate	String,
unitprice	string,
customerid	string,
country string
);

select max(invoicedate), min(invoicedate) from online_retail;




select * from online_retail;

select customerid, count(*) from online_retail group by customerid;

drop table IF EXISTS online_retail_aggr ;
create table online_retail_aggr as
select  
  customerid as user_id,
  stockcode as item_id,
  1 as active_type,
  max(invoicedate)  as active_date
from online_retail  
where length(customerid) > 1 and substr(invoicedate, 4, 2)  <= '10'
group by customerid, stockcode
order by customerid limit 1000000;


select * from online_retail_aggr;

select max(user_id), min(user_id) from online_retail_aggr;

create table cf_data_result as select * from online_retail_aggr where user_id > '16287';
create table cf_data_train as select * from online_retail_aggr where user_id <= '16287';


select substr('30/01/11 11', 3, 2), substr('30/01/11 11', 4, 2);

drop table IF EXISTS cf_data_train ;
create table cf_data_train as
select  
  customerid as user_id,
  stockcode as item_id,
  1 as active_type,
  max(invoicedate)  as active_date
from online_retail  
where length(customerid) > 1 and substr(invoicedate, 4, 2)  <= '10'
group by customerid, stockcode
order by customerid limit 1000000;



drop table IF EXISTS cf_data_result ;
create table cf_data_result as
select  
  customerid as user_id,
  stockcode as item_id,
  1 as active_type,
  max(invoicedate)  as active_date
from online_retail  
where length(customerid) > 1 and substr(invoicedate, 4, 2)  > '10'
group by customerid, stockcode
order by customerid limit 1000000;

select * from cf_similar_item ;