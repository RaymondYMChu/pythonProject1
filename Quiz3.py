import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# The data file path and file name need to be configured.
PATH = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/"
CSV_DATA = "fruit.csv"
df       = pd.read_csv(PATH + CSV_DATA)
# Placed query in this function to enable code re-usuability.
def showQueryResult(sql):
    # This code creates an in-memory table called 'RetailInventory'.
    engine     = create_engine('sqlite://', echo=False)
    connection = engine.connect()
    df.to_sql(name='Fruit', con=connection, if_exists='replace', index=False)

    # This code performs the query.
    queryResult = pd.read_sql(sql, connection)
    return queryResult

SQL = "SELECT Region, Product, SUM(Quantity) As TotalSold FROM Fruit WHERE Product = 'apples' GROUP BY Region, Product"
results = showQueryResult(SQL)
print(results)

plt.bar(results.Region, results.TotalSold, color='green')
plt.title("Total Amounts Sold Apples")

plt.xticks(results.Region, results.Region)
plt.show()
