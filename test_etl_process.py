import pandas as pd
import pytest
from sqlalchemy import create_engine

mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')
query = """select * from target_employees"""
df = pd.read_sql(query,mysql_engine)

# 1. Data completeness check
@pytest.mark.smoke
@pytest.mark.regression
def test_dataCompltenessCheck():
    assert not df.empty,"Please check why target is not populated"

# 2. Filter check
@pytest.mark.smoke
def test_dataTransfromationFilterCheck():
   assert all(df['deptno'] == 10),"Check why other deptno data is there in target"

@pytest.mark.smoke
# 3. ename is conerted to lower case
def test_dataTransfromationEmpnameLowerConversionCheck():
    assert all(df['ename'] == df['ename'].str.lower()), "Check why ename is having upper case letter"



# 4. Data qaulaity NUll values check
@pytest.mark.skip
def test_dataQualityCheck():
   assert df.isnull().sum().sum() == 0,"Please check why there is null values in target"
