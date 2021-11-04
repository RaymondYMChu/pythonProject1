import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH     = "C:\\datasets\\"
CSV_DATA = "brazil_forestFires.csv"


 # Create the database at the specified path.
DB_FILE    = 'forestFire.db'
engine     = create_engine('sqlite:///' + PATH + DB_FILE, echo=False)
connection = engine.connect()

# Store data in database in a table named 'brazilForest'.
df.to_sql(name='brazilForest', con=connection, if_exists='replace', index=False)


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