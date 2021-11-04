import pandas as pd
from sqlalchemy import create_engine

PATH = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/ramenReviews.db"
df = PATH
engine     = create_engine('sqlite:///' + PATH, echo=False)
connection = engine.connect()

# Store data in database in a table named 'ramenReviews'.
df.to_sql(name='ramenReviews', con=connection, if_exists='replace', index=False)

def showQueryResult(sql, connection):
    print("\n*** Showing SQL statement")
    print(sql)

    # Perform query
    subDf = pd.read_sql(sql, connection)
    print("\n*** Showing dataframe summary")
    return subDf

sql = "SELECT * FROM ramenReviews"
newDf = showQueryResult(sql, connection)
print(newDf)