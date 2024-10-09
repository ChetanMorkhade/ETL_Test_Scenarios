import pandas as pd
from sqlalchemy import create_engine

mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')

# extracation process from employees.csv
df = pd.read_csv('employees.csv')


# Transformation process
# 1 . filter the data based on deptno = 10
df_filter = df[df['deptno'] == 10].copy()

# 2 . convert the ename to lower case
df_filter['ename']=df_filter['ename'].str.lower()

# 3 . derive a new colum for total_sal ( sal + comm )

df_filter['total_sal'] = df_filter['sal']+df_filter['comm'].fillna(0)


# Loading into Target ( mysql database )
df_filter.to_sql('target_employees',mysql_engine,if_exists ='replace',index = False )