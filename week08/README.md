
# NYC Taxi Data Analysis with PySpark

This project involves loading NYC taxi trip data into a Data Lake/Blob Storage/DataBricks environment, processing it using PySpark, and performing various analytical queries.

## Problem Statement

![problem statement](/week08/screenshots/problem_statement.png)

## Dataset

The dataset used in this project is the NYC Taxi Trip Record Data. Specifically, we use the Yellow Taxi Trip Records for January 2020.

- **Dataset URL**: [NYC Taxi Trip Data](http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml)
- **Direct Download Link**: [yellow_tripdata_2020-01.csv](https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv)

## Prerequisites

- Access to a DataBricks environment or similar big data platform.
- Basic knowledge of PySpark and SQL.
- Access to Blob Storage or Data Lake Storage for storing datasets.

## Setup

1. **DataBricks Environment**: Ensure you have access to a DataBricks workspace.
2. **Cluster Configuration**: Set up a cluster with appropriate configurations to run PySpark jobs.
3. **Libraries**: Ensure necessary libraries are installed in your DataBricks environment.

## Loading Data

1. **Download the Dataset**: Download the dataset from the provided URL.
2. **Upload to DBFS**: Upload the dataset to the Databricks File System (DBFS).

```python
# Example code to load data from DBFS
file_location = "/FileStore/tables/yellow_tripdata_2020_01.csv"
file_type = "csv"

df = spark.read.format(file_type) \n  .option("inferSchema", "true") \n  .option("header", "true") \n  .option("sep", ",") \n  .load(file_location)
```

## Processing and Flattening JSON Fields

If your dataset contains JSON fields, you will need to flatten them for easier processing.

```python
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Define schema for JSON fields
json_schema = StructType([
    StructField("field1", StringType(), True),
    StructField("field2", DoubleType(), True)
    # Add more fields as necessary
])

# Flatten JSON fields
df = df.withColumn("flattened_data", from_json(col("json_column"), json_schema))
df = df.select("*", "flattened_data.*").drop("flattened_data", "json_column")
```

## Writing Flattened Data as External Parquet Table

Once the data is processed and flattened, write it as an external Parquet table for efficient querying.

```python
# Write DataFrame to Parquet format
df.write.format("parquet").saveAsTable("yellow_taxi_data")
```

## Performing Queries

Below are the queries to be performed on the dataset:

### Query 1: Add a Revenue Column
```python
df = df.withColumn("Revenue", col('Fare_amount') + col('Extra') + col('MTA_tax') +
                   col('Improvement_surcharge') + col('Tip_amount') +
                   col('Tolls_amount') + col('Total_amount'))
```

### Query 2: Increasing Count of Total Passengers by Area
```python
passenger_count_by_area = df.groupBy("PULocationID").sum("passenger_count")
```

### Query 3: Realtime Average Fare/Total Earning Amount by Vendors
```python
average_fare_by_vendor = df.groupBy("VendorID").avg("Total_amount")
```

### Query 4: Moving Count of Payments by Payment Mode
```python
from pyspark.sql.window import Window
from pyspark.sql.functions import count

payment_mode_counts = df.groupBy("payment_type").count()
```

### Query 5: Highest Two Gaining Vendors on a Particular Date
```python
from pyspark.sql.functions import rank
from pyspark.sql.window import Window

windowSpec = Window.partitionBy("pickup_date").orderBy(col("Revenue").desc())

highest_gaining_vendors = df.withColumn("rank", rank().over(windowSpec)) \
                            .filter(col("rank") <= 2) \
                            .filter(col("pickup_date") == "2020-01-01")
```

### Query 6: Most Number of Passengers Between a Route of Two Locations
```python
most_passengers_route = df.groupBy("PULocationID", "DOLocationID").sum("passenger_count") \n                          .orderBy(col("sum(passenger_count)").desc()) \n                          .first()
```

### Query 7: Top Pickup Locations with Most Passengers in Last 5/10 Seconds
```python
from pyspark.sql.functions import window, current_timestamp

top_pickup_locations = df.filter(col("pickup_datetime") > current_timestamp() - 10) \n                         .groupBy("PULocationID").sum("passenger_count") \n                         .orderBy(col("sum(passenger_count)").desc())
```

## Conclusion

This project demonstrates how to load, process, and analyze NYC taxi trip data using PySpark in a DataBricks environment. By following the steps outlined in this README, you can perform various analytical queries to gain insights from the dataset.
