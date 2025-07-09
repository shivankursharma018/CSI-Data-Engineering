#  Task 1: Copy Data from Azure SQL Database to CSV, Parquet, and Avro using Azure Data Factory

Export relational database data to multiple file formats (CSV, Parquet, and Avro) stored in Azure Blob Storage using Azure Data Factory.

---

##  Prerequisites

- Azure for Students subscription
- Azure SQL Database with sample table and data
- Azure Storage Account (StorageV2, LRS)
- Azure Data Factory resource created
- Basic familiarity with Azure Portal

---

##  Step 1: Create Azure SQL Database

1. Go to Azure Portal  Create a resource  Search SQL Database
2. Fill the form:
   - Choose SQL Authentication
   - Set admin login/password (remember it)
   - Set backup redundancy to Locally-redundant
   - Select Development for workload
   - Do not use elastic pool
3. Click Review + Create  then Create

![task1.1](/week05/screenshots/1_1.png)
![task1.2](/week05/screenshots/1_2.png)
![task1.3](/week05/screenshots/1_3.png)

---

##  Step 2: Add Sample Data to SQL Database

1. Go to the SQL Database  Query editor (preview)
2. Sign in using your SQL admin login
3. Run the following to create and populate a table:

```sql
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Age INT,
    Email NVARCHAR(100)
);

INSERT INTO Students (StudentID, FirstName, LastName, Age, Email)
VALUES 
(1, 'Alice', 'Johnson', 20, 'alice.johnson@example.com'),
(2, 'Bob', 'Smith', 22, 'bob.smith@example.com'),
(3, 'Charlie', 'Lee', 19, 'charlie.lee@example.com');
```

---

##  Step 3: Create Azure Blob Storage

1. Go to Azure Portal  Create a resource  Search Storage account
2. Select StorageV2 (general purpose v2)
3. Set Redundancy: Locally-redundant (LRS)
4. Click Review + Create  then Create

---

##  Step 4: Create Linked Services in Azure Data Factory

1. Open your Data Factory  Click Launch Studio
2. Go to Manage ()  Linked Services  + New

### a. For Azure SQL Database
- Choose Azure SQL Database
- Use SQL authentication
- Test connection and create

### b. For Azure Blob Storage
- Choose Azure Blob Storage
- Use Account Key authentication
- Test connection and create

![task1.4](/week05/screenshots/1_4.png)
![task1.5](/week05/screenshots/1_5.png)
![task1.6](/week05/screenshots/1_6.png)
![task1.7](/week05/screenshots/1_7.png)
![task1.8](/week05/screenshots/1_8.png)
![task1.9](/week05/screenshots/1_9.png)

---

##  Step 5: Create Copy Pipelines for Each File Format

### 1. In Data Factory Studio:
- Go to Author ()  Pipelines  + New Pipeline
- Name it (e.g., `CopySQLtoCSV`)

### 2. Add a Copy Data activity:
- Drag it to canvas

### 3. Configure Source:
- Click Source tab  + New Dataset  Azure SQL Database
- Choose the Students table

![task2.1](/week05/screenshots/2_1.png)
![task2.2](/week05/screenshots/2_2.png)
![task2.3](/week05/screenshots/2_3.png)

---

### Format-Specific Instructions

####  Export to CSV:
- Sink  + New Dataset  DelimitedText
- Linked service: Azure Blob Storage
- File name: e.g., students.csv
- Format settings: UTF-8, comma-delimited, \n row delimiter

####  Export to Parquet:
- Sink  + New Dataset  Parquet
- Linked service: Azure Blob Storage
- File name: e.g., students.parquet

####  Export to Avro:
- Sink  + New Dataset  Avro
- Linked service: Azure Blob Storage
- File name: e.g., students.avro

![task2.10](/week05/screenshots/2_10.png)
![task2.11](/week05/screenshots/2_11.png)
![task2.12](/week05/screenshots/2_12.png)
![task2.13](/week05/screenshots/2_13.png)

---

##  Step 6: Validate and Run

1. Click Validate all  Fix if needed
2. Click Publish all
3. Click Add Trigger  Trigger now  OK

![task2.4](/week05/screenshots/2_4.png)
![task2.5](/week05/screenshots/2_5.png)

---

##  Step 7: Verify in Blob Storage

1. Go to your Storage Account  Containers
2. Open the container you selected
3. Youll see:
   - students.csv
   - students.parquet
   - students.avro

---

#  Task 2: Configure Schedule and Event Triggers in Azure Data Factory

Automate pipeline execution using schedule-based triggers for regular intervals and event-based triggers that respond to dynamic actions like blob creation. This ensures timely and hands-free data movement in both real-time and batch scenarios.

---

##  Prerequisites

- Azure Data Factory pipeline that is already working (e.g., CopySQLtoCSV)
- Linked services and datasets are already configured (from Task 1)
- Azure Storage Account with a container (for event trigger)

---

##  Part 1: Create a Schedule Trigger

This will run the pipeline automatically at defined time intervals.

### Step 1: Go to Data Factory Studio

1. Open Azure Data Factory Studio
2. Click the Author tab () > Select your pipeline (e.g., `CopySQLtoCSV`)

### Step 2: Add Trigger

1. Click Add Trigger > New/Edit
2. In the trigger configuration panel:
   - Name: `EveryHourTrigger`
   - Type: Schedule
   - Start Date & Time: Set a time in the future (UTC)
   - Recurrence: Choose interval (e.g., Every 1 Hour)
   - Time Zone: Select your local time zone
   - Enabled:  Yes
3. Click OK

![task3.1](/week05/screenshots/3_1.png)
![task3.2](/week05/screenshots/3_2.png)

### Step 3: Associate Trigger with Pipeline

1. After creating the trigger, click Publish All
2. Now the pipeline will run automatically based on the schedule

![task3.3](/week05/screenshots/3_3.png)
![task3.4](/week05/screenshots/3_4.png)
![task3.5](/week05/screenshots/3_5.png)
![task3.6](/week05/screenshots/3_6.png)
![task3.7](/week05/screenshots/3_7.png)
![task3.8](/week05/screenshots/3_8.png)
![task3.9](/week05/screenshots/3_9.png)
![task3.10](/week05/screenshots/3_10.png)

---

##  Part 2: Create an Event-Based Trigger (Blob Arrival)

This will run the pipeline automatically when a new file arrives in a blob container.

### Step 1: Ensure Storage Events Are Enabled

1. Go to your Azure Storage Account in the portal
2. Under Settings > Event Grid > Enable system events

### Step 2: Create Event Trigger in Data Factory

1. Go back to Azure Data Factory Studio
2. Click Manage () > Triggers > + New

![task3.11](/week05/screenshots/3_11.png)
![task3.12](/week05/screenshots/3_12.png)

### Step 3: Configure the Trigger

- Name: `BlobArrivalTrigger`
- Type: Event
- Linked Service: Select your Azure Blob Storage linked service
- Event Type: Blob Created
- Container: Select the container to monitor
- Blob Path Begins With: (optional, e.g., input/)
- Blob Path Ends With: (optional, e.g., .csv)
- Ignore Empty Blobs: Yes

Click Continue > Review > Finish

### Step 4: Attach Event Trigger to Pipeline

1. Go back to your pipeline
2. Click Add Trigger > New/Edit > Choose `BlobArrivalTrigger`
3. Click OK > Publish All

Now the pipeline runs when a file lands in the monitored container.

![task3.13](/week05/screenshots/3_13.png)
![task3.14](/week05/screenshots/3_14.png)

---

#  Task 3: Copy All Tables from One Azure SQL Database to Another

Perform full database replication by dynamically copying all tables and their data from a source Azure SQL Database to a destination Azure SQL Database using Azure Data Factory.

---

##  Prerequisites

- Two Azure SQL Databases (Source & Destination)
- Azure Data Factory created
- SQL authentication enabled for both databases
- Sample tables exist in the source database

---

##  Step 1: Create Linked Services

1. In Azure Data Factory Studio  Manage ()  Linked Services  + New
2. Create two linked services:
   - One for the Source SQL Database
   - One for the Destination SQL Database
3. Use SQL authentication for both
4. Test and save the connections

![task4.1](/week05/screenshots/4_1.png)
![task4.2](/week05/screenshots/4_2.png)
![task4.3](/week05/screenshots/4_3.png)
![task4.4](/week05/screenshots/4_4.png)
![task4.5](/week05/screenshots/4_5.png)

---

##  Step 2: Create Datasets

Since tables will be dynamic, datasets will be parameterized.

### Step 2.1: Create Source Dataset

1. Go to Author  Datasets  + New Dataset  Azure SQL Database
2. Name it: `SourceSQLDataset`
3. Linked service: Source SQL DB
4. Check "Parameterized" option for Table Name
5. In Parameters tab:
   - Add parameter: tableName (type: String)
6. In Connection tab  Table: set as `@dataset().tableName`

![task4.6](/week05/screenshots/4_6.png)

### Step 2.2: Create Sink Dataset

1. Repeat the above steps for Destination database
2. Name it: `DestinationSQLDataset`
3. Use the destination linked service
4. Use the same `tableName` parameter
5. Table: `@dataset().tableName`

![task4.9](/week05/screenshots/4_9.png)
![task4.10](/week05/screenshots/4_10.png)

---

##  Step 3: Create a Pipeline to Copy All Tables

![task4.11](/week05/screenshots/4_11.png)
![task4.12](/week05/screenshots/4_12.png)

### Step 3.1: Use Get Metadata Activity

1. Add "Get Metadata" activity to pipeline
2. Configure it to use the Source SQL linked service
3. Set the dataset to any existing table temporarily
4. Field list: Add "schema"
5. Select option: "List of Tables" (use stored procedure or query if needed)

### Step 3.2: Add ForEach Activity

1. Connect it to "Get Metadata"
2. Items: `@activity('Get Metadata1').output.tableNames`

### Step 3.3: Inside ForEach

1. Add "Copy Data" activity inside ForEach
2. Source:
   - Use SourceSQLDataset
   - Set tableName: `@item().name`
3. Sink:
   - Use DestinationSQLDataset
   - Set tableName: `@item().name`

![task4.13](/week05/screenshots/4_13.png)

---

##  Step 4: Publish and Run

1. Click Validate All and resolve errors
2. Click Publish All
3. Trigger pipeline  Monitor tab for progress

![task5.1](/week05/screenshots/5_1.png)

---

##  Result

All tables from the source database will be copied into the destination database with the same schema and data.

---

#  Task 4: Copy Selective Tables with Selective Columns from One Azure SQL Database to Another

Copy only specific tables and selected columns from a source Azure SQL Database to a destination Azure SQL Database using Azure Data Factory. This supports targeted data migration for compliance or business-specific needs.

---

##  Prerequisites

- Two Azure SQL Databases (Source & Destination)
- Azure Data Factory created
- SQL authentication enabled for both databases
- A list of selected tables and required columns is defined

---

##  Step 1: Create Linked Services

1. In Azure Data Factory Studio  Manage ()  Linked Services  + New
2. Create two linked services:
   - One for Source SQL Database
   - One for Destination SQL Database
3. Use SQL authentication for both
4. Test and save connections

![task5.2](/week05/screenshots/5_2.png)

---

##  Step 2: Create Datasets

We will use parameterized datasets for dynamic table names.

### Step 2.1: Source Dataset

1. Go to Author  Datasets  + New  Azure SQL Database
2. Name: `SourceSelectiveDataset`
3. Linked Service: Source DB
4. Add Parameter: tableName (String)
5. Query  Use parameterized query:
   ```sql
   SELECT column1, column2 FROM @{dataset().tableName}
   ```
   Replace column1, column2 with actual column names (this can be passed dynamically via pipeline too)

![task5.3](/week05/screenshots/5_3.png)

### Step 2.2: Sink Dataset

1. Repeat the above for Destination DB
2. Name: `DestinationSelectiveDataset`
3. Use parameter for tableName
4. Table: `@dataset().tableName`

---

##  Step 3: Create Pipeline for Selective Copy

![task5.5](/week05/screenshots/5_5.png)

### Step 3.1: Define Table & Column Mapping List

1. Use a pipeline parameter or a Lookup activity to define a table of mappings, e.g.:
   ```json
   [
     { "table": "Students", "columns": "StudentID, FirstName" },
     { "table": "Courses", "columns": "CourseID, CourseName" }
   ]
   ```

### Step 3.2: Add ForEach Activity

1. For each item in the mapping list:
   - Set table name and columns as variables

### Step 3.3: Add Copy Data Activity Inside ForEach

1. Source:
   - Dataset: SourceSelectiveDataset
   - Pass tableName parameter: `@item().table`
   - Use dynamic query: `SELECT @{item().columns} FROM @{item().table}`
2. Sink:
   - Dataset: DestinationSelectiveDataset
   - Pass tableName parameter: `@item().table`

![task5.6](/week05/screenshots/5_6.png)
![task5.7](/week05/screenshots/5_7.png)
![task5.8](/week05/screenshots/5_8.png)

---

##  Step 4: Validate and Run

1. Validate All  Fix errors
2. Publish All
3. Trigger pipeline and monitor

![task5.9](/week05/screenshots/5_9.png)
![task5.10](/week05/screenshots/5_10.png)
![task5.11](/week05/screenshots/5_11.png)

---

##  Result

Only selected tables with specific columns are copied to the destination database.
