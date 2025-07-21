# File Processing Pipeline with Azure Data Factory

This guide provides instructions for setting up Azure Data Factory (ADF) pipelines to process three different types of files from an Azure Data Lake container and load them into respective database tables with specific transformations.

## Prerequisites

- Azure Data Factory instance
- Azure Data Lake Storage Gen2 account linked to ADF
- Azure SQL Database or another target database
- Appropriate linked services for Azure Data Lake Storage and your database

## File Types and Requirements

1. **CUST_MSTR_YYYYMMDD.csv**
   - Extract the date from the filename.
   - Add an additional column for the date in the format `YYYY-MM-DD`.
   - Load into the `CUST_MSTR` table.

2. **master_child_export-YYYYMMDD.csv**
   - Extract the date from the filename.
   - Add two additional columns: date in the format `YYYY-MM-DD` and date key in the format `YYYYMMDD`.
   - Load into the `master_child` table.

3. **H_ECOM_ORDER.csv**
   - Load the file into the database as-is.
   - Load into the `H_ECOM_Orders` table.

## Setup Instructions

### Step 1: Set Up Linked Services

1. **Azure Data Lake Storage Linked Service**
   - Create a linked service for your Azure Data Lake Storage account in ADF.

![Image 1](/week07/screenshots/7_1.png)
![Image 2](/week07/screenshots/7_2.png)


2. **Database Linked Service**
   - Create a linked service for your target database.

![Image 3](/week07/screenshots/7_3.png)
![Image 1](/week07/screenshots/7_4.png)
![Image 5](/week07/screenshots/7_5.png)


### Step 2: Create Datasets

1. **Source Datasets**
   - Create a dataset for each file type using the DelimitedText format.
   - Use wildcards to capture all files:
     - `CUST_MSTR_*.csv`
     - `master_child_export-*.csv`
     - `H_ECOM_ORDER.csv`

![Image 6](/week07/screenshots/7_6.png)
![Image 7](/week07/screenshots/7_7.png)
![Image 8](/week07/screenshots/7_8.png)

2. **Sink Datasets**
   - Create sink datasets for each target table in your database:
     - `CUST_MSTR`
     - `master_child`
     - `H_ECOM_Orders`

![Image 9](/week07/screenshots/7_9.png)
![Image 10](/week07/screenshots/7_10.png)
![Image 11](/week07/screenshots/7_11.png)

### Step 3: Create Pipelines

#### Pipeline for "CUST_MSTR" Files

1. **Get Metadata Activity**
   - Retrieve the list of "CUST_MSTR" files.

2. **ForEach Activity**
   - Iterate over each file using `@activity('GetMetadataActivity').output.childItems`.

3. **Data Flow Activity**
   - **Source Transformation**: Read the CSV file.
   - **Derived Column Transformation**: Add a new column for the date extracted from the filename.
     ```plaintext
     toDate(concat(substring(item().name, 11, 4), '-', substring(item().name, 15, 2), '-', substring(item().name, 17, 2)), 'yyyy-MM-dd')
     ```
   - **Sink Transformation**: Write the data to the `CUST_MSTR` table.

#### Pipeline for "master_child_export" Files

1. **Get Metadata Activity**
   - Retrieve the list of "master_child_export" files.

2. **ForEach Activity**
   - Iterate over each file using `@activity('GetMetadataActivity').output.childItems`.

3. **Data Flow Activity**
   - **Source Transformation**: Read the CSV file.
   - **Derived Column Transformation**: Add two new columns for the date and date key.
     ```plaintext
     toDate(concat(substring(item().name, 20, 4), '-', substring(item().name, 24, 2), '-', substring(item().name, 26, 2)), 'yyyy-MM-dd')
     ```
     ```plaintext
     concat(substring(item().name, 20, 4), substring(item().name, 24, 2), substring(item().name, 26, 2))
     ```
   - **Sink Transformation**: Write the data to the `master_child` table.

#### Pipeline for "H_ECOM_ORDER" Files

1. **Copy Data Activity**
   - Load the `H_ECOM_ORDER.csv` file directly into the `H_ECOM_Orders` table.

### Step 4: Schedule and Truncate Load

1. **Truncate Tables**
   - Use a Stored Procedure activity to truncate the target tables before loading data.

2. **Schedule Pipelines**
   - Use ADF triggers to schedule these pipelines to run daily.

![Image 12](/week07/screenshots/7_12.jpeg)
![Image 13](/week07/screenshots/7_13.jpeg)
![Image 14](/week07/screenshots/7_14.jpeg)

## Conclusion

By following these steps, you will create three separate pipelines in Azure Data Factory to handle different file types, apply necessary transformations, and load the data into respective database tables on a daily basis.
