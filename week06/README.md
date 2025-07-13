# Task 1: Configure SHIR to Extract from Local SQL Server and Load into Azure SQL Database

This guide provides step-by-step instructions to set up a Self-hosted Integration Runtime (SHIR) in Azure Data Factory (ADF) to securely transfer data from an on-premises SQL Server to an Azure SQL Database.

---

## Step 1: Create a Self-hosted Integration Runtime in ADF

1. **Navigate to Azure Portal**: Open your browser and go to the [Azure Portal](https://portal.azure.com).
2. **Open Data Factory**: Locate and open your Data Factory resource.
3. **Launch ADF Studio**: Click on "Launch Studio" to open the Azure Data Factory interface.
4. **Create Integration Runtime**:
   - Go to the "Manage" section (represented by a gear icon).
   - Select "Integration Runtimes" and click on "+ New".
   - Choose the option for a "Self-hosted" integration runtime.
   - Name your integration runtime as `SHIR_LocalServer`.
   - Click "Create" to generate the integration runtime.
5. **Download Installer**: After creation, click on your new integration runtime and download the installer.
6. **Copy Authentication Key**: Copy the authentication key provided; you will need it during the installation process on your local machine.

![task1.2](/week06/screenshots/selfhostednode.png)

---

## Step 2: Install SHIR on Local Machine

1. **Run Installer**: Execute the downloaded SHIR installer (.exe file) on your local machine.
2. **Register with ADF**: During installation, choose the option to register with Azure Data Factory.
3. **Paste Authentication Key**: When prompted, paste the authentication key you copied earlier.
4. **Complete Setup**: Follow the on-screen instructions to complete the installation.

Your local machine is now registered as the SHIR host, allowing secure data transfer between your on-premises environment and Azure.

---

![task1.4](/week06/screenshots/1_4.png)
![task1.7](/week06/screenshots/1_7.png)

## Step 3: Create Linked Services in Azure Data Factory

Linked services are connections that link your data stores to Azure Data Factory.

### For On-Premises SQL Server

1. In ADF Studio, go to the "Manage" tab and select "Linked Services".
2. Click on "+ New" to create a new linked service.
3. Choose "SQL Server" as the data store.
4. Select the integration runtime you created (`SHIR_LocalServer`).
5. Configure the authentication method (SQL Authentication or Windows Authentication).
6. Enter your local SQL Server name and database details.
7. Test the connection and click "Create".

### For Azure SQL Database

1. Create another linked service by clicking on "+ New".
2. Choose "Azure SQL Database" as the data store.
3. Use SQL Authentication and enter the server, database, username, and password.
4. Test the connection and click "Create".

---

## Step 4: Create Datasets

Datasets represent the data structures within your data stores.

### For Source (On-Premises SQL Server)

1. Go to the "Author" tab and select "Datasets".
2. Click on "+ New Dataset" and choose "SQL Server" as the data store.
3. Use the linked service for your local SQL Server.
4. Select the table you want to extract data from.

### For Sink (Azure SQL Database)

1. Create a second dataset by clicking on "+ New Dataset" and choosing "Azure SQL Database".
2. Use the linked service for your Azure SQL Database.
3. Choose or create the destination table where data will be loaded.

---

## Step 5: Create Copy Data Pipeline

Pipelines define the workflow for data movement and transformation.

1. **Create Pipeline**:
   - In the "Author" tab, go to "Pipelines" and click on "+ New Pipeline".
   - Add a "Copy Data" activity to your pipeline.
2. **Configure Source and Sink**:
   - Set the Source to the On-premises SQL Server dataset.
   - Set the Sink to the Azure SQL Database dataset.

---

## Step 6: Run and Verify

1. **Validate and Publish**:
   - Validate your pipeline to ensure there are no errors.
   - Publish all changes to deploy the pipeline.
2. **Trigger Pipeline**:
   - Click on "Add Trigger" and select "Trigger Now" to run the pipeline immediately.
3. **Monitor Pipeline**:
   - Go to the "Monitor" tab to check the status of your pipeline run.
4. **Verify Data Load**:
   - Navigate to your Azure SQL Database and confirm that the data has been successfully loaded into the destination table.

![task1.1](/week06/screenshots/1_1.png)
![task1.6](/week06/screenshots/1_6.png)
![task1.5](/week06/screenshots/1_5.png)

By following these steps, you have configured a Self-hosted Integration Runtime to securely extract data from a local SQL Server and load it into an Azure SQL Database.


# Task 2: Configure FTP/SFTP Server and Create an ADF Pipeline for Data Extraction

This guide provides step-by-step instructions to set up an Azure Data Factory (ADF) pipeline to extract files from an FTP/SFTP server. This setup is useful for integrating partner files or legacy systems into your Azure data workflows.

---

## Step 1: Gather FTP/SFTP Credentials

Ensure you have the following credentials:

- Hostname (e.g., `ftp.example.com` or `sftp.mydomain.net`).
- Port (default: 21 for FTP, 22 for SFTP).
- Username and password (or private key if using SFTP key-based authentication).
- Directory path where files are stored.

---

## Step 2: Create Linked Services in Azure Data Factory

### a. FTP/SFTP Linked Service

1. **Open ADF Studio**: Navigate to the [Azure Portal](https://portal.azure.com) and open your Data Factory.
2. **Create Linked Service**:
   - Go to the "Manage" section (represented by a gear icon).
   - Select "Linked Services" and click on "+ New".
   - Choose "FTP" for basic FTP servers or "SFTP" for Secure FTP servers.
3. **Configure Linked Service**:
   - Fill in the hostname and port.
   - Select the authentication type: Basic (Username + Password) or SSH Key.
   - Specify the root directory or subdirectory path.
   - Integration Runtime: Use `AutoResolveIntegrationRuntime` or select SHIR if required.
4. **Test and Create**: Test the connection and click "Create".

### b. Azure Blob Storage Linked Service

1. **Create Linked Service**:
   - Click on "+ New" and choose "Azure Blob Storage".
   - Use account key authentication.
   - Select your storage account.
2. **Test and Create**: Test the connection and click "Create".


![task2.1](/week06/screenshots/2_1.png)

---

## Step 3: Create Datasets

### a. Source Dataset (FTP/SFTP)

1. **Create Dataset**:
   - Go to the "Author" tab and select "Datasets".
   - Click on "+ New Dataset" and choose "FTP" or "SFTP".
   - Select your FTP/SFTP linked service.
2. **Configure Dataset**:
   - Specify the file path: Use a specific filename or a wildcard (e.g., `data.csv` or `*.csv`).
   - Set the file format: DelimitedText, JSON, Excel, etc.

### b. Sink Dataset (Blob Storage)

1. **Create Dataset**:
   - Click on "+ New Dataset" and choose "DelimitedText" or the appropriate file format.
   - Select your Azure Blob Storage linked service.
2. **Configure Dataset**:
   - Specify the file path: Target location in the container.
   - Configure the file name, format, etc.

---

## Step 4: Create Copy Data Pipeline

1. **Create Pipeline**:
   - In ADF Studio, go to the "Author" tab and select "Pipelines".
   - Click on "+ New Pipeline".
2. **Add Copy Data Activity**:
   - Add a "Copy Data" activity to your pipeline.
   - Set the Source to your FTP/SFTP dataset.
   - Set the Sink to your Blob Storage dataset.
3. **Optional Configurations**:
   - Enable Wildcard file processing.
   - Set skip/overwrite options as needed.


![task2.2](/week06/screenshots/2_2.png)
![task2.3](/week06/screenshots/2_3.png)

---

## Step 5: Validate and Run Pipeline

1. **Validate**: Click "Validate All" and fix any issues.
2. **Publish**: Click "Publish All" to deploy the pipeline.
3. **Trigger Pipeline**: Manually trigger the pipeline by clicking "Add Trigger" and selecting "Trigger Now".
4. **Monitor**: Go to the "Monitor" tab to confirm the pipeline's success.

![task2.4](/week06/screenshots/2_4.png)

---

## Step 6: Verify Output

1. **Check Storage Account**: Navigate to your Azure Storage Account and open the specified container.
2. **Verify Files**: Ensure the file(s) downloaded from the FTP/SFTP server exist and are correct.

By following these steps, you have configured an ADF pipeline to extract files from an FTP/SFTP server and store them in Azure Blob Storage.


# Task 3: Create Incremental Load Pipeline and Automate It Daily using Azure Data Factory

Design a pipeline that loads only new or updated records from a source (e.g., SQL Server) into a target (e.g., Azure SQL DB) using a watermark column like LastUpdatedDate. This improves efficiency and enables automated daily refreshes.

---

## Step 1: Add a Watermark Column to Source Table
Ensure your source table (e.g., Customers) has a datetime column to track changes.

```sql
ALTER TABLE Customers ADD UpdatedAt DATETIME DEFAULT GETDATE();
```

Make sure the column updates when records are inserted or modified.

---

## Step 2: Create Watermark Table in ADF Sink (Optional)
In your destination database, create a table to store the last loaded timestamp:

```sql
CREATE TABLE WatermarkTracking (
    TableName VARCHAR(100),
    LastLoadedTime DATETIME
);
```

Initialize with current date:

```sql
INSERT INTO WatermarkTracking VALUES ('Customers', '2023-01-01 00:00:00');
```

---

## Step 3: Create Linked Services
Ensure you’ve created Linked Services for:
- Source SQL Server / On-prem SQL (via SHIR)
- Azure SQL Database (destination)

Test and save both connections.

![task3.1](/week06/screenshots/3_1.png)
![task3.2](/week06/screenshots/3_2.png)

---

## Step 4: Create Datasets with Parameters
Create parameterized datasets for dynamic SQL queries.

**Source Dataset (SQL):**
- Add parameter: watermarkValue
- Use query like:

```sql
SELECT * FROM Customers WHERE UpdatedAt > '@{dataset().watermarkValue}'
```

**Sink Dataset:**
- Configure for Azure SQL Database
- Allow insert/upsert as required

![task3.3](/week06/screenshots/3_3.png)

---

## Step 5: Create Pipeline Logic
1. Add Lookup activity to read last watermark:

```sql
SELECT LastLoadedTime FROM WatermarkTracking WHERE TableName = 'Customers';
```

2. Add a Set Variable activity:
- Save output of Lookup to variable `watermarkValue`

3. Add Copy Data activity:
- Source: parameterized dataset using `watermarkValue`
- Sink: Azure SQL Database

4. Add Stored Procedure or Script activity (optional):
- Update the WatermarkTracking table with the current timestamp

```sql
UPDATE WatermarkTracking
SET LastLoadedTime = GETDATE()
WHERE TableName = 'Customers';
```

---

## Step 6: Schedule Daily Execution
1. Go to “Triggers” → + New
2. Choose “Schedule”
   - Name: DailyIncrementalLoad
   - Recurrence: Every 24 hours (or your desired frequency)
3. Attach this trigger to the pipeline
4. Publish all changes


![task3.4](/week06/screenshots/3_4.png)
![task3.5](/week06/screenshots/3_5.png)

---

# Task 4: Automate a Pipeline to Trigger Every Last Saturday of the Month in Azure Data Factory

Create a time-based custom trigger in Azure Data Factory that automatically executes a pipeline on the last Saturday of each month. This supports monthly batch processing and compliance reporting without manual scheduling.

---

## Step 1: Understand the Limitation
Azure Data Factory's native scheduler does not directly support "Last Saturday of the Month." You must:

- Use a Tumbling Window or Scheduled Trigger
- Apply logic inside the pipeline to skip execution unless the current day is the last Saturday

---

## Step 2: Create the Scheduled Trigger (Weekly on Saturdays)
1. Go to Azure Data Factory Studio → Manage → Triggers → + New
2. Trigger Name: LastSaturdayTrigger
3. Type: Schedule
4. Recurrence:
   - Frequency: Week
   - Interval: 1
   - Select Saturday only
5. Start Date: Choose upcoming Saturday (e.g., 2024-07-13T00:00Z)
6. Time Zone: Your local zone or UTC
7. Click Next → Attach to your target pipeline (e.g., MonthlyReportPipeline)
8. Click Finish → Publish All

---

## Step 3: Add Date Check Logic Inside Pipeline
To restrict execution to only the last Saturday of the month:

1. Inside your pipeline, add a Get Metadata activity or Set Variable activity with this logic:
2. Since there is no built-in function like lastSaturdayOfMonth(), simulate it using a stored procedure, Azure Function, or script (SQL, Python, etc.) that:
   - Calculates if today is the last Saturday of the month
   - Returns True/False
3. Use If Condition activity:
   - If today is the last Saturday → Run downstream activities
   - Else → End pipeline or log a skip

Example Implementation:
- Use Azure Function / Web Activity / SQL script to return True only if today is last Saturday
- If-Condition proceeds only if result = True

---

## Step 4: Deploy and Monitor
1. Publish All
2. Monitor the Trigger tab to confirm scheduled trigger runs
3. Monitor pipeline logic and log success/skips

---

## Result
Your pipeline will run every Saturday, but only execute core logic if it is the last Saturday of the month.

This approach ensures fully automated monthly processing without false triggers.


# Task 5: Handle Data Retrieval Failures Gracefully Using Retry and Wait Logic in Azure Data Factory

Design your Azure Data Factory (ADF) pipeline to handle transient data access failures (like "Retrieving data. Wait a few seconds and try to cut or copy again") by implementing retry policies and conditional wait logic. This improves resilience and stability.

---

## Step 1: Set Built-in Retry Policies for Activities
ADF supports built-in retry configurations on most activities like Copy, Lookup, Web, etc.

Select your activity (e.g., Copy Data)

In the Settings tab:

- Retry: Set to a number like 3 (default is 0)
- Retry interval (seconds): e.g., 30

Example:
```yaml
Retry: 3
Retry interval: 30 seconds
```
This tells ADF to retry the activity up to 3 times, with a 30-second delay between each try.

---

## Step 2: Add Wait Activity for Controlled Delay
To simulate a "wait and try again" logic manually:

- Add a Wait activity before retrying
- Set Wait time in seconds (e.g., 10)
- Chain it to retryable activity using dependency conditions

Example use case: Add Wait before retrying REST API or file read if failure is likely.

------

## Step 3: Use If Condition or Switch for Recovery Logic
- Add an If Condition activity after a potentially failing activity
- Evaluate the output status using:

```expression
@equals(activity('CopyFromFTP').Status,'Failed')
```
- If True → Execute Wait + Retry block
- If False → Continue as normal

---

## Step 4: Implement Custom Retry Using Until Activity (Advanced)
For scenarios requiring more advanced retry logic:

- Add Until activity
- Inside it: Call the Copy, Lookup, or Web Activity
- Set condition to:

```expression
@equals(activity('CopyFromAPI').Status, 'Succeeded')
```
- Add a Wait activity to prevent tight looping (e.g., wait 10 seconds per loop)
- Set timeout (e.g., 5 minutes) and max iterations

---

## Step 5: Test and Monitor
- Simulate failure (disconnect FTP, delay API)
- Observe retry behavior in ADF Monitor tab
- Check logs and alerts to verify retry and wait

![task4.1](/week06/screenshots/4_1.png)

---

## Result
Your pipeline will gracefully handle data retrieval errors by waiting and retrying — reducing the chance of failures due to transient issues and ensuring more stable data workflows.

