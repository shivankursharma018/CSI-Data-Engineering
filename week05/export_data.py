import pandas as pd
from sqlalchemy import create_engine
import pyarrow as pa
import pyarrow.parquet as pq
from fastavro import writer, parse_schema

# Create a connection to the MySQL database
engine = create_engine('mysql+pymysql://root:sspace@localhost:3306/shiv33')

# Query to select data
query = "SELECT * FROM your_table"

# Read data into a pandas DataFrame
df = pd.read_sql_query(query, engine)

# Export to CSV
df.to_csv('output.csv', index=False)

# Export to Parquet
table = pa.Table.from_pandas(df)
pq.write_table(table, 'output.parquet')

# Define Avro schema
avro_schema = {
    "type": "record",
    "name": "YourRecord",
    "fields": [{"name": col, "type": "string"} for col in df.columns]
}
parsed_schema = parse_schema(avro_schema)

# Export to Avro
with open('output.avro', 'wb') as out:
    writer(out, parsed_schema, df.to_dict('records'))
