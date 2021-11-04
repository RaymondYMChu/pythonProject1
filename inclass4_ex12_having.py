import pandas as pd
from sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/"
CSV_DATA = "retailerDB.csv"
df       = pd.read_csv(PATH + CSV_DATA)

# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'Inventory'.
    engine     = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Inventory', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult

# Read all rows from the table.
SQL     = "SELECT vendor, SUM(price*quantity) as revenueValue FROM Inventory GROUP BY vendor HAVING vendor " \
          "IN ('Silverware Inc.','Waterford Corp.')"
results = showQueryResult(SQL)
print(results)