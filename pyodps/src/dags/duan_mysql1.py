
from __future__ import print_function


import datetime
import MySQLdb
import time
from builtins import range
from pprint import pprint

import airflow
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(6),
}

dag = DAG(
    dag_id='duan_mysql1',
    default_args=args,
    schedule_interval='0 0 * * *',
)


# [START howto_operator_python]
def print_context(ds, **kwargs):
    # pprint(kwargs)
    # print(ds)
    ed = kwargs.get("execution_date")
    # print('started run qiyang:' + ds['execution_date'].strftime("%I:%M%p on %B %d, %Y"))
    print(ed)
    import os
    mysql_host = os.environ['MYSQL_HOST']
    mysql_user = os.environ['MYSQL_USER']
    mysql_passwd = os.environ['MYSQL_PASS']
    mysql_db  = os.environ['MYSQL_DB']
    print(mysql_host )
    print(mysql_passwd )

    import MySQLdb
    conn = MySQLdb.connect(host=mysql_host,
                    user=mysql_user,
                    passwd=mysql_passwd,
                    db=mysql_db)

    x = conn.cursor()

    try:
        x.execute("""INSERT INTO people VALUES (%s,%s)""",("mysql1:"  + ed.strftime("%I:%M%p on %B %d, %Y") ,20))
        # x.execute("""INSERT INTO people VALUES (%s,%s)""",("mysql1:"  + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y") ,20))
        conn.commit()
    except:
        conn.rollback()
        print('failed')

    conn.close()

    return 'new version with insert qiyang ------------- you return gets printed in the logs'


run_this = PythonOperator(
    task_id='print_the_context',
    provide_context=True,
    python_callable=print_context,
    dag=dag,
)
# [END howto_operator_python]


