CREATE TABLE dbo.CUST_MSTR (
    CustomerID NVARCHAR(50),
    FirstName NVARCHAR(100),
    LastName NVARCHAR(100),
    Email NVARCHAR(255),
    City NVARCHAR(100),
    State NVARCHAR(50),
    LoadDate DATE  
);

CREATE TABLE dbo.master_child (
    MasterAccountID NVARCHAR(50),
    ChildAccountID NVARCHAR(50),
    RelationshipType NVARCHAR(100),
    Status NVARCHAR(50),
    [date] DATE,     
    DateKey INT      
);

CREATE TABLE dbo.H_ECOM_Orders (
    OrderID NVARCHAR(50),
    CustomerID NVARCHAR(50),
    OrderDate DATETIME2,
    ProductID NVARCHAR(50),
    Quantity INT,
    UnitPrice DECIMAL(18, 2),
    TotalAmount DECIMAL(18, 2)
);