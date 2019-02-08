from odps import ODPS
import os
import sqlalchemy
import pandas as pd

access_id= os.environ['access_id']
secret_access_key= os.environ['secret_access_key']

o = ODPS(access_id = access_id, 
 secret_access_key= secret_access_key,
 project='qiyangduanproj1',
 endpoint='http://service.eu-west-1.maxcompute.aliyun.com/api')

#d = o.get_table('bank_data')
#from odps.df import DataFrame
#df = DataFrame(o.get_table('bank_data'))
#pd_df = df.head(300).to_pandas() 




# https://github.com/aliyun/aliyun-odps-python-sdk/issues/31

with o.execute_sql('''select '2019-02-01' apply_day, job,  avg(age) as age_avg, avg(duration) as duration_avg, count(1) as cust_count
        from bank_card_apply
        where apply_date between  cast('2019-02-01 00:00:00' as datetime) and cast('2019-02-02 00:00:00' as datetime)
        group by job''').open_reader() as reader:
    pd_df = reader.to_pandas()


database_ip = os.environ['MYSQL_HOST']
database_username = os.environ['MYSQL_USER']
database_password = os.environ['MYSQL_PASS']
database_name  = os.environ['MYSQL_DB']


str_conn = "mysql://{0}:{1}@{2}/{3}".format(database_username, database_password, database_ip, database_name)
str_conn


engine = sqlalchemy.create_engine(str_conn)

pd_df.to_sql(con=engine.connect(),  name='apply_stat',  index=False,  if_exists='append')



with o.execute_sql('''select '2019-02-02' apply_day, job,  avg(age) as age_avg, avg(duration) as duration_avg, count(1) as cust_count
        from bank_card_apply
        where apply_date between  cast('2019-02-02 00:00:00' as datetime) and cast('2019-02-03 00:00:00' as datetime)
        group by job''').open_reader() as reader:
    pd_df = reader.to_pandas()


pd_df.to_sql(con=engine.connect(),  name='apply_stat',  index=False,  if_exists='append')




