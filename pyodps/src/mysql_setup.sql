
-- mysql -u duan -p -h ???.mysql.singapore.rds.aliyuncs.com  db1
-- docker run -it --name mysql1 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=xyz mysql:5.7 
-- mysqldump --add-drop-table  -u duan -p -h rm-gs5za51i7trp7x83aio.mysql.singapore.rds.aliyuncs.com  db1 > db1.sql
-- mysql   -u root -p -h 8.208.10.9  db1 < db1.sql




drop table apply_stat;
create table apply_stat (
  apply_day varchar(100),
  job varchar(500),
  age_avg float,
  duration_avg float,
  cust_count int
)
;


