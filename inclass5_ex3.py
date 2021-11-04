import pandas as pd
from sqlalchemy import create_engine

PATH = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/"
DB_FILE = 'forestFire.db'
engine = create_engine('sqlite:///' + PATH + DB_FILE, echo=False)
connection = engine.connect()

def showQueryResult(sql, connection):
    print("\n*** Showing SQL statement")
    print(sql)

# Perform query
    subDf = pd.read_sql(sql, connection)
    print("\n*** Showing dataframe summary")
    return subDf

# Get DataFrame contents for 'Rio' and 'Sao Paulo' only.
sql = "SELECT * FROM brazilForest WHERE state = 'Rio' OR state='Sao Paulo' ORDER BY date"
newDf = showQueryResult(sql, connection)
print(newDf.tail())