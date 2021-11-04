import pandas as pd
from   sqlalchemy import create_engine

# The data file path and file name need to be configured.
PATH = "/Users/rchuy/OneDrive/Desktop/BCIT/COMP2454 Python/Dataset/"
CSV_DATA = "brazil_forestFires.csv"

# Note this has a comma separator.
df = pd.read_csv(PATH + CSV_DATA, skiprows=1,  encoding = "ISO-8859-1", sep=',',
                 names=('year', 'state',  'month', 'number','date', ))
print(df.tail(2))

 # Create the database at the specified path.
DB_FILE    = 'forestFire.db'
engine     = create_engine('sqlite:///' + PATH + DB_FILE, echo=False)
connection = engine.connect()

# Store data in database in a table named 'brazilForest'.
df.to_sql(name='brazilForest', con=connection, if_exists='replace', index=False)
