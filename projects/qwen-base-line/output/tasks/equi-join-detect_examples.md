# equi-join-detect: All Questions (9 total)

**Model:** Qwen2.5-7B-Instruct

---

## Question 1: 215780883 (Auto-BI)

**Dataset:** Auto-BI  
**Test case:** 215780883  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Your are given a database with related tables used for business intelligence analysis. Your task is to identify all key/foreign-key join relationships between the tables for this database. Recall that a join is a relationship between two tables, that allows rows from one table to be combined with rows from another, based on a set of common join columns.
 
 
No explanation needed. Please return all join relationships in the following JSON format:
{
  "joins": [
    {
      "from_table": "table-1",
      "from_column": "column-1",
      "to_table": "table-2",
      "to_column": "column-3"
    }, 
	...
  ]
}

Tables:

Table: DimCustomer
|   Customer Key |   WWI Customer ID | Customer                           | Bill To Customer            | Category     | Buying Group   | Primary Contact    |   Postal Code |  Credit Limit    |   Lineage Key |
|---------------:|------------------:|:-----------------------------------|:----------------------------|:-------------|:---------------|:-------------------|--------------:|:-----------------|--------------:|
|              1 |                 1 | Tailspin Toys (Head Office)        | Tailspin Toys (Head Office) | Novelty Shop | Tailspin Toys  | Waldemar Fisar     |         90410 | ? 100,000.000000 |             2 |
|              2 |                 2 | Tailspin Toys (Sylvanite, MT)      | Tailspin Toys (Head Office) | Novelty Shop | Tailspin Toys  | Lorena Cindric     |         90216 | ? 100,000.000000 |             2 |
|              3 |                 3 | Tailspin Toys (Peeples Valley, AZ) | Tailspin Toys (Head Office) | Novelty Shop | Tailspin Toys  | Bhaargav Rambhatla |         90205 | ? 100,000.000000 |             2 |
|              4 |                 4 | Tailspin Toys (Medicine Lodge, KS) | Tailspin Toys (Head Office) | Novelty Shop | Tailspin Toys  | Daniel Roman       |         90152 | ? 100,000.000000 |             2 |
|              5 |                 5 | Tailspin Toys (Gasport, NY)        | Tailspin Toys (Head Office) | Novelty Shop | Tailspin Toys  | Johanna Huiting    |         90261 | ? 100,000.000000 |             2 |
|              7 |                 7 | Tailspin Toys (Frankewing, TN)     | Tailspin Toys (Head Office) | Novelty Shop | Tailspin Toys  | Kalidas Nadar      |         90761 | ? 100,000.000000 |             2 |
|              8 |                 8 | Tailspin Toys (Bow Mar, CO)        | Tailspin Toys (Head Office) | Novelty Shop | Tailspin Toys  | Kanti Kotadia      |         90484 | ? 100,000.000000 |             2 |
|              9 |                 9 | Tailspin Toys (Netcong, NJ)        | Tailspin Toys (Head Office) | Novelty Shop | Tailspin Toys  | Sointu Aalto       |         90129 | ? 100,000.000000 |             2 |
|             10 |                10 | Tailspin Toys (Wimbledon, ND)      | Tailspin Toys (Head Office) | Novelty Shop | Tailspin Toys  | Siddhartha Parkar  |         90061 | ? 100,000.000000 |             2 |
|             11 |                11 | Tailspin Toys (Devault, PA)        | Tailspin Toys (Head Office) | Novelty Shop | Tailspin Toys  | Elnaz Javan        |         90185 | ? 100,000.000000 |             2 |


Table: DimDate
| Date                    |   Day Number |   Day | Month   | Short Month   |   Calendar Month Number | Calendar Month Label   |   Calendar Year | Calendar Year Label   |   Fiscal Month Number | Fiscal Month Label   |   Fiscal Year | Fiscal Year Label   |   ISO Week Number |
|:------------------------|-------------:|------:|:--------|:--------------|------------------------:|:-----------------------|----------------:|:----------------------|----------------------:|:---------------------|--------------:|:--------------------|------------------:|
| 2016-01-01 00:00:00.000 |            1 |     1 | January | Jan           |                       1 | CY2016-Jan             |            2016 | CY2016                |                     3 | FY2016-Jan           |          2016 | FY2016              |                53 |
| 2016-01-02 00:00:00.000 |            2 |     2 | January | Jan           |                       1 | CY2016-Jan             |            2016 | CY2016                |                     3 | FY2016-Jan           |          2016 | FY2016              |                53 |
| 2016-01-03 00:00:00.000 |            3 |     3 | January | Jan           |                       1 | CY2016-Jan             |            2016 | CY2016                |                     3 | FY2016-Jan           |          2016 | FY2016              |                53 |
| 2016-01-04 00:00:00.000 |            4 |     4 | January | Jan           |                       1 | CY2016-Jan             |            2016 | CY2016                |                     3 | FY2016-Jan           |          2016 | FY2016              |                 1 |
| 2016-01-05 00:00:00.000 |            5 |     5 | January | Jan           |                       1 | CY2016-Jan             |            2016 | CY2016                |                     3 | FY2016-Jan           |          2016 | FY2016              |                 1 |
| 2016-01-06 00:00:00.000 |            6 |     6 | January | Jan           |                       1 | CY2016-Jan             |            2016 | CY2016                |                     3 | FY2016-Jan           |          2016 | FY2016              |                 1 |
| 2016-01-07 00:00:00.000 |            7 |     7 | January | Jan           |                       1 | CY2016-Jan             |            2016 | CY2016                |                     3 | FY2016-Jan           |          2016 | FY2016              |                 1 |
| 2016-01-08 00:00:00.000 |            8 |     8 | January | Jan           |                       1 | CY2016-Jan             |            2016 | CY2016                |                     3 | FY2016-Jan           |          2016 | FY2016              |                 1 |
| 2016-01-09 00:00:00.000 |            9 |     9 | January | Jan           |                       1 | CY2016-Jan             |            2016 | CY2016                |                     3 | FY2016-Jan           |          2016 | FY2016              |                 1 |
| 2016-01-10 00:00:00.000 |           10 |    10 | January | Jan           |                       1 | CY2016-Jan             |            2016 | CY2016                |                     3 | FY2016-Jan           |          2016 | FY2016              |                 1 |


Table: DimEmployee
|   Employee Key |   WWI Employee ID | Employee           | Preferred Name   |   Is Salesperson | Photo   | Valid From              | Valid To             |   Lineage Key |
|---------------:|------------------:|:-------------------|:-----------------|-----------------:|:--------|:------------------------|:---------------------|--------------:|
|              1 |                14 | Lily Code          | Lily             |                1 | NULL    | 2013-01-01 00:00:00.000 | 1/1/2013 8:00:00 AM  |             3 |
|              2 |                 4 | Isabella Rupp      | Isabella         |                0 | NULL    | 2013-01-01 00:00:00.000 | 1/1/2013 8:00:00 AM  |             3 |
|              3 |                11 | Ethan Onslow       | Ethan            |                0 | NULL    | 2013-01-01 00:00:00.000 | 1/4/2013 8:00:00 AM  |             3 |
|              4 |                 7 | Amy Trefl          | Amy              |                1 | NULL    | 2013-01-01 00:00:00.000 | 1/5/2013 8:00:00 AM  |             3 |
|              5 |                19 | Jai Shand          | Jai              |                0 | NULL    | 2013-01-01 00:00:00.000 | 1/6/2013 8:00:00 AM  |             3 |
|              6 |                 8 | Anthony Grosse     | Anthony          |                1 | NULL    | 2013-01-01 00:00:00.000 | 1/9/2013 8:00:00 AM  |             3 |
|              7 |                15 | Taj Shand          | Taj              |                1 | NULL    | 2013-01-01 00:00:00.000 | 1/11/2013 8:00:00 AM |             3 |
|              8 |                13 | Hudson Hollinworth | Hudson           |                1 | NULL    | 2013-01-01 00:00:00.000 | 1/11/2013 8:00:00 AM |             3 |
|              9 |                20 | Jack Potter        | Jack             |                1 | NULL    | 2013-01-01 00:00:00.000 | 1/14/2013 8:00:00 AM |             3 |
|             10 |                17 | Piper Koch         | Piper            |                0 | NULL    | 2013-01-01 00:00:00.000 | 1/19/2013 8:00:00 AM |             3 |


Table: FactSale
|   Sale Key |   City Key |   Customer Key |   Bill To Customer Key |   Stock Item Key | Invoice Date Key        | Delivery Date Key       |   Salesperson Key |   WWI Invoice ID | Description                                                                           | Package   |   Quantity |   Unit Price |   Tax Rate |   Total Excluding Tax |   Tax Amount |   Profit |   Total Including Tax |   Total Dry Items |   Total Chiller Items |   Lineage Key |
|-----------:|-----------:|---------------:|-----------------------:|-----------------:|:------------------------|:------------------------|------------------:|-----------------:|:--------------------------------------------------------------------------------------|:----------|-----------:|-------------:|-----------:|----------------------:|-------------:|---------:|----------------------:|------------------:|----------------------:|--------------:|
|      49374 |      69332 |              0 |                      0 |              186 | 2013-10-22 00:00:00.000 | 2013-10-23 00:00:00.000 |                19 |            15219 | Developer joke mug - fun was unexpected at this time (White)                          | Each      |          1 |           13 |         15 |                    13 |         1.95 |      8.5 |                 14.95 |                 1 |                     0 |            11 |
|      56882 |      56111 |              0 |                      0 |              198 | 2013-12-05 00:00:00.000 | 2013-12-06 00:00:00.000 |                19 |            17512 | DBA joke mug - it depends (White)                                                     | Each      |          1 |           13 |         15 |                    13 |         1.95 |      8.5 |                 14.95 |                 1 |                     0 |            11 |
|      57068 |      82826 |              0 |                      0 |              167 | 2013-12-06 00:00:00.000 | 2013-12-07 00:00:00.000 |                19 |            17572 | IT joke mug - keyboard not found … press F1 to continue (Black)                       | Each      |          1 |           13 |         15 |                    13 |         1.95 |      8.5 |                 14.95 |                 1 |                     0 |            11 |
|      57429 |      42598 |              0 |                      0 |              172 | 2013-12-09 00:00:00.000 | 2013-12-10 00:00:00.000 |                19 |            17684 | Developer joke mug - this code was generated by a tool (White)                        | Each      |          1 |           13 |         15 |                    13 |         1.95 |      8.5 |                 14.95 |                 1 |                     0 |            11 |
|      57669 |      84888 |              0 |                      0 |              173 | 2013-12-10 00:00:00.000 | 2013-12-11 00:00:00.000 |                19 |            17757 | Developer joke mug - a foo walks into a bar (Black)                                   | Each      |          1 |           13 |         15 |                    13 |         1.95 |      8.5 |                 14.95 |                 1 |                     0 |            11 |
|      58705 |      42573 |              0 |                      0 |              201 | 2013-12-18 00:00:00.000 | 2013-12-19 00:00:00.000 |                19 |            18085 | DBA joke mug - daaaaaa-ta (Black)                                                     | Each      |          1 |           13 |         15 |                    13 |         1.95 |      8.5 |                 14.95 |                 1 |                     0 |            11 |
|      59359 |      43854 |              0 |                      0 |              165 | 2013-12-23 00:00:00.000 | 2013-12-24 00:00:00.000 |                19 |            18288 | IT joke mug - that behavior is by design (Black)                                      | Each      |          1 |           13 |         15 |                    13 |         1.95 |      8.5 |                 14.95 |                 1 |                     0 |            11 |
|       1022 |      50625 |              0 |                      0 |              178 | 2013-01-07 00:00:00.000 | 2013-01-08 00:00:00.000 |                19 |              394 | Developer joke mug - understanding recursion requires understanding recursion (White) | Each      |          1 |           13 |         15 |                    13 |         1.95 |      8.5 |                 14.95 |                 1 |                     0 |            11 |
|       2974 |      43529 |              0 |                      0 |              177 | 2013-01-18 00:00:00.000 | 2013-01-19 00:00:00.000 |                19 |              971 | Developer joke mug - understanding recursion requires understanding recursion (Black) | Each      |          1 |           13 |         15 |                    13 |         1.95 |      8.5 |                 14.95 |                 1 |                     0 |            11 |
|       3661 |      49849 |              0 |                      0 |              177 | 2013-01-23 00:00:00.000 | 2013-01-24 00:00:00.000 |                19 |             1178 | Developer joke mug - understanding recursion requires understanding recursion (Black) | Each      |          1 |           13 |         15 |                    13 |         1.95 |      8.5 |                 14.95 |                 1 |                     0 |            11 |

 

````

### Model Response

```
```json
{
  "joins": [
    {
      "from_table": "DimCustomer",
      "from_column": "Customer Key",
      "to_table": "FactSale",
      "to_column": "Customer Key"
    },
    {
      "from_table": "DimCustomer",
      "from_column": "WWI Customer ID",
      "to_table": "FactSale",
      "to_column": "Bill To Customer Key"
    },
    {
      "from_table": "DimDate",
      "from_column": "Date",
      "to_table": "FactSale",
      "to_column": "Invoice Date Key"
    },
    {
      "from_table": "DimDate",
      "from_column": "Date",
      "to_table": "FactSale",
      "to_column": "Delivery Date Key"
    },
    {
      "from_table": "DimEmployee",
      "from_column": "Employee Key",
      "to_table": "FactSale",
      "to_column": "Salesperson Key"
    }
  ]
}
```
```

### Correct Answer

```
{
  "joins": [
    {
      "from_table": "FactSale",
      "from_column": "Invoice Date Key",
      "to_table": "DimDate",
      "to_column": "Date"
    },
    {
      "from_table": "FactSale",
      "from_column": "Salesperson Key",
      "to_table": "DimEmployee",
      "to_column": "Employee Key"
    },
    {
      "from_table": "FactSale",
      "from_column": "Customer Key",
      "to_table": "DimCustomer",
      "to_column": "Customer Key"
    }
  ]
}
```


---

## Question 2: 312175967 (Auto-BI)

**Dataset:** Auto-BI  
**Test case:** 312175967  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Your are given a database with related tables used for business intelligence analysis. Your task is to identify all key/foreign-key join relationships between the tables for this database. Recall that a join is a relationship between two tables, that allows rows from one table to be combined with rows from another, based on a set of common join columns.
 
 
No explanation needed. Please return all join relationships in the following JSON format:
{
  "joins": [
    {
      "from_table": "table-1",
      "from_column": "column-1",
      "to_table": "table-2",
      "to_column": "column-3"
    }, 
	...
  ]
}

Tables:

Table: SalesLT Address
|   AddressID | AddressLine1                | AddressLine2   | City          | StateProvince   | CountryRegion   |   PostalCode |
|------------:|:----------------------------|:---------------|:--------------|:----------------|:----------------|-------------:|
|         988 | 482505 Warm Springs Blvd.   |                | Fremont       | California      | United States   |        94536 |
|         989 | 39933 Mission Oaks Blvd     |                | Camarillo     | California      | United States   |        93010 |
|         991 | 60025 Bollinger Canyon Road |                | San Ramon     | California      | United States   |        94583 |
|         992 | 9992 Whipple Rd             |                | Union City    | California      | United States   |        94587 |
|         993 | Corporate Office            |                | El Segundo    | California      | United States   |        90245 |
|         994 | 25001 Montague Expressway   |                | Milpitas      | California      | United States   |        95035 |
|         995 | 4460 Newport Center Drive   |                | Newport Beach | California      | United States   |        92625 |
|         997 | 70259 West Sunnyview Ave    |                | Visalia       | California      | United States   |        93291 |
|         998 | 60750 San Clemente          |                | Hayward       | California      | United States   |        94541 |
|         999 | Receiving                   |                | Fullerton     | California      | United States   |        92831 |


Table: SalesLT Customer
|   CustomerID | NameStyle   | Title   | FirstName   | MiddleName   | LastName   | Suffix   | CompanyName                        | SalesPerson              | EmailAddress                | Phone        | CustomerName     |
|-------------:|:------------|:--------|:------------|:-------------|:-----------|:---------|:-----------------------------------|:-------------------------|:----------------------------|:-------------|:-----------------|
|            2 | False       | Mr.     | Keith       |              | Harris     |          | Progressive Sports                 | adventure-works\david8   | keith0@adventure-works.com  | 170-555-0127 | Harris, Keith    |
|            5 | False       | Mr.     | Lucy        |              | Harrington |          | Metropolitan Sports Supply         | adventure-works\shu0     | lucy0@adventure-works.com   | 828-555-0186 | Harrington, Lucy |
|           23 | False       | Mr.     | Kerim       |              | Hanif      |          | Bike World                         | adventure-works\shu0     | kerim0@adventure-works.com  | 216-555-0122 | Hanif, Kerim     |
|           24 | False       | Mr.     | Kevin       |              | Liu        |          | Eastside Department Store          | adventure-works\linda3   | kevin5@adventure-works.com  | 926-555-0164 | Liu, Kevin       |

... (109 rows omitted) ...

|          71780 |               110622 |          1 |         743 |     809.76  |                   0 |               809.76  |
|          71780 |               110623 |          4 |         782 |    1376.99  |                   0 |              5507.98  |


Table: SalesLT SalesOrderHeader
|   SalesOrderID |   RevisionNumber | OrderDate               | DueDate                 | ShipDate                |   Status | OnlineOrderFlag   | SalesOrderNumber   | PurchaseOrderNumber   | AccountNumber   |   CustomerID |   ShipToAddressID |   BillToAddressID | ShipMethod        | CreditCardApprovalCode   |   SOH_SubTotal_$ales |    TaxAmt |   Freight |    TotalDue | Comment   |
|---------------:|-----------------:|:------------------------|:------------------------|:------------------------|---------:|:------------------|:-------------------|:----------------------|:----------------|-------------:|------------------:|------------------:|:------------------|:-------------------------|---------------------:|----------:|----------:|------------:|:----------|
|          71774 |                2 | 2008-06-01 00:00:00.000 | 2008-06-13 00:00:00.000 | 2008-06-08 00:00:00.000 |        5 | False             | SO71774            | PO348186287           | 10-4020-000609  |        29847 |              1092 |              1092 | CARGO TRANSPORT 5 |                          |              880.348 |   70.4279 |   22.0087 |    972.785  |           |
|          71776 |                2 | 2008-06-01 00:00:00.000 | 2008-06-13 00:00:00.000 | 2008-06-08 00:00:00.000 |        5 | False             | SO71776            | PO19952192051         | 10-4020-000106  |        30072 |               640 |               640 | CARGO TRANSPORT 5 |                          |               78.81  |    6.3048 |    1.9703 |     87.0851 |           |
|          71780 |                2 | 2008-06-01 00:00:00.000 | 2008-06-13 00:00:00.000 | 2008-06-08 00:00:00.000 |        5 | False             | SO71780            | PO19604173239         | 10-4020-000340  |        30113 |               653 |               653 | CARGO TRANSPORT 5 |                          |            38418.7   | 3073.5    |  960.467  |  42452.7    |           |
|          71782 |                2 | 2008-06-01 00:00:00.000 | 2008-06-13 00:00:00.000 | 2008-06-08 00:00:00.000 |        5 | False             | SO71782            | PO19372114749         | 10-4020-000582  |        29485 |              1086 |              1086 | CARGO TRANSPORT 5 |                          |            39785.3   | 3182.83   |  994.633  |  43962.8    |           |
|          71783 |                2 | 2008-06-01 00:00:00.000 | 2008-06-13 00:00:00.000 | 2008-06-08 00:00:00.000 |        5 | False             | SO71783            | PO19343113609         | 10-4020-000024  |        29957 |               992 |               992 | CARGO TRANSPORT 5 |                          |            83858.4   | 6708.67   | 2096.46   |  92663.6    |           |
|          71784 |                2 | 2008-06-01 00:00:00.000 | 2008-06-13 00:00:00.000 | 2008-06-08 00:00:00.000 |        5 | False             | SO71784            | PO19285135919         | 10-4020-000448  |        29736 |               659 |               659 | CARGO TRANSPORT 5 |                          |           108562     | 8684.95   | 2714.05   | 119961      |           |
|          71796 |                2 | 2008-06-01 00:00:00.000 | 2008-06-13 00:00:00.000 | 2008-06-08 00:00:00.000 |        5 | False             | SO71796            | PO17052159664         | 10-4020-000420  |        29660 |              1058 |              1058 | CARGO TRANSPORT 5 |                          |            57634.6   | 4610.77   | 1440.87   |  63686.3    |           |
|          71797 |                2 | 2008-06-01 00:00:00.000 | 2008-06-13 00:00:00.000 | 2008-06-08 00:00:00.000 |        5 | False             | SO71797            | PO16501134889         | 10-4020-000142  |        29796 |               642 |               642 | CARGO TRANSPORT 5 |                          |            78029.7   | 6242.38   | 1950.74   |  86222.8    |           |
|          71815 |                2 | 2008-06-01 00:00:00.000 | 2008-06-13 00:00:00.000 | 2008-06-08 00:00:00.000 |        5 | False             | SO71815            | PO13021155785         | 10-4020-000276  |        30089 |              1034 |              1034 | CARGO TRANSPORT 5 |                          |             1141.58  |   91.3263 |   28.5395 |   1261.44   |           |
|          71816 |                2 | 2008-06-01 00:00:00.000 | 2008-06-13 00:00:00.000 | 2008-06-08 00:00:00.000 |        5 | False             | SO71816            | PO12992180445         | 10-4020-000295  |        30027 |              1038 |              1038 | CARGO TRANSPORT 5 |                          |             3398.17  |  271.853  |   84.9541 |   3754.97   |           |

 

````

### Model Response

```
```json
{
  "joins": [
    {
      "from_table": "SalesLT CustomerAddress",
      "from_column": "CustomerID",
      "to_table": "SalesLT Customer",
      "to_column": "CustomerID"
    },
    {
      "from_table": "SalesLT CustomerAddress",
      "from_column": "AddressID",
      "to_table": "SalesLT Address",
      "to_column": "AddressID"
    }
  ]
}
```
```

### Correct Answer

```
{
  "joins": [
    {
      "from_table": "SalesLT CustomerAddress",
      "from_column": "AddressID",
      "to_table": "SalesLT Address",
      "to_column": "AddressID"
    },
    {
      "from_table": "SalesLT SalesOrderHeader",
      "from_column": "BillToAddressID",
      "to_table": "SalesLT Address",
      "to_column": "AddressID"
    },
    {
      "from_table": "SalesLT CustomerAddress",
      "from_column": "CustomerID",
      "to_table": "SalesLT Customer",
      "to_column": "CustomerID"
    },
    {
      "from_table": "SalesLT Product",
      "from_column": "ProductCategoryID",
      "to_table": "SalesLT ProductCategory",
      "to_column": "ProductCategoryID"
    },
    {
      "from_table": "SalesLT Product",
      "from_column": "ProductModelID",
      "to_table": "SalesLT ProductModel",
      "to_column": "ProductModelID"
    },
    {
      "from_table": "SalesLT SalesOrderDetail",
      "from_column": "ProductID",
      "to_table": "SalesLT Product",
      "to_column": "ProductID"
    },
    {
      "from_table": "SalesLT ProductModelProductDescription",
      "from_column": "ProductDescriptionID",
      "to_table": "SalesLT ProductDescription",
      "to_column": "ProductDescriptionID"
    },
    {
      "from_table": "SalesLT ProductModelProductDescription",
      "from_column": "ProductModelID",
      "to_table": "SalesLT ProductModel",
      "to_column": "ProductModelID"
    },
    {
      "from_table": "SalesLT SalesOrderDetail",
      "from_column": "SalesOrderID",
      "to_table": "SalesLT SalesOrderHeader",
      "to_column": "SalesOrderID"
    }
  ]
}
```


---

## Question 3: 655206294 (Auto-BI)

**Dataset:** Auto-BI  
**Test case:** 655206294  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Your are given a database with related tables used for business intelligence analysis. Your task is to identify all key/foreign-key join relationships between the tables for this database. Recall that a join is a relationship between two tables, that allows rows from one table to be combined with rows from another, based on a set of common join columns.
 
 
No explanation needed. Please return all join relationships in the following JSON format:
{
  "joins": [
    {
      "from_table": "table-1",
      "from_column": "column-1",
      "to_table": "table-2",
      "to_column": "column-3"
    }, 
	...
  ]
}

Tables:

Table: All measures
| Column1   |
|:----------|
| d         |


Table: Calendar
| DateKey                 |   YearNumber |   MonthNumber | MonthName   |   DayNumber | DayName   | Quarter   |
|:------------------------|-------------:|--------------:|:------------|------------:|:----------|:----------|
| 2015-07-01 00:00:00.000 |         2015 |             7 | July        |           1 | Wednesday | Q3        |
| 2015-07-02 00:00:00.000 |         2015 |             7 | July        |           2 | Thursday  | Q3        |
| 2015-07-03 00:00:00.000 |         2015 |             7 | July        |           3 | Friday    | Q3        |
| 2015-07-04 00:00:00.000 |         2015 |             7 | July        |           4 | Saturday  | Q3        |
| 2015-07-05 00:00:00.000 |         2015 |             7 | July        |           5 | Sunday    | Q3        |
| 2015-07-06 00:00:00.000 |         2015 |             7 | July        |           6 | Monday    | Q3        |
| 2015-07-07 00:00:00.000 |         2015 |             7 | July        |           7 | Tuesday   | Q3        |
| 2015-07-08 00:00:00.000 |         2015 |             7 | July        |           8 | Wednesday | Q3        |
| 2015-07-09 00:00:00.000 |         2015 |             7 | July        |           9 | Thursday  | Q3        |
| 2015-07-10 00:00:00.000 |         2015 |             7 | July        |          10 | Friday    | Q3        |


Table: Centre

... (94 rows omitted) ...

|          8 | West Midlands          |
|          9 | Yorkshire & Humberside |


Table: Town
|   TownId | TownName          |   RegionId |
|---------:|:------------------|-----------:|
|        1 | Aintree           |          5 |
|        2 | Aldershot         |          6 |
|        3 | Altrincham        |          5 |
|        4 | Andover           |          6 |
|        5 | Ashford           |          6 |
|        6 | Ashton Under Lyne |          5 |
|        7 | Aylesbury         |          6 |
|        8 | Banbury           |          6 |
|        9 | Barhill           |          1 |
|       10 | Barking           |          3 |

 

````

### Model Response

```
```json
{
  "joins": [
    {
      "from_table": "Centre",
      "from_column": "TownId",
      "to_table": "Town",
      "to_column": "TownId"
    },
    {
      "from_table": "Centre",
      "from_column": "CentreTypeId",
      "to_table": "CentreType",
      "to_column": "CentreTypeId"
    },
    {
      "from_table": "Product",
      "from_column": "FamilyId",
      "to_table": "Family",
      "to_column": "FamilyId"
    },
    {
      "from_table": "Product",
      "from_column": "HabitatId",
      "to_table": "Habitat",
      "to_column": "HabitatId"
    },
    {
      "from_table": "Purchase",
      "from_column": "ProductId",
      "to_table": "Product",
      "to_column": "ProductId"
    },
    {
      "from_table": "Purchase",
      "from_column": "CentreId",
      "to_table": "Centre",
      "to_column": "CentreId"
    }
  ]
}
```
```

### Correct Answer

```
{
  "joins": [
    {
      "from_table": "Centre",
      "from_column": "CentreTypeId",
      "to_table": "CentreType",
      "to_column": "CentreTypeId"
    },
    {
      "from_table": "Purchase",
      "from_column": "CentreId",
      "to_table": "Centre",
      "to_column": "CentreId"
    },
    {
      "from_table": "Centre",
      "from_column": "TownId",
      "to_table": "Town",
      "to_column": "TownId"
    },
    {
      "from_table": "Habitat",
      "from_column": "EnvironmentId",
      "to_table": "Environment",
      "to_column": "EnviromentId"
    },
    {
      "from_table": "Product",
      "from_column": "FamilyId",
      "to_table": "Family",
      "to_column": "FamilyId"
    },
    {
      "from_table": "Product",
      "from_column": "HabitatId",
      "to_table": "Habitat",
      "to_column": "HabitatId"
    },
    {
      "from_table": "Purchase",
      "from_column": "ProductId",
      "to_table": "Product",
      "to_column": "ProductId"
    },
    {
      "from_table": "Town",
      "from_column": "RegionId",
      "to_table": "Region",
      "to_column": "RegionId"
    },
    {
      "from_table": "Purchase",
      "from_column": "PurchaseDate",
      "to_table": "Calendar",
      "to_column": "DateKey"
    }
  ]
}
```


---

## Question 4: 228684154 (Auto-BI)

**Dataset:** Auto-BI  
**Test case:** 228684154  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Your are given a database with related tables used for business intelligence analysis. Your task is to identify all key/foreign-key join relationships between the tables for this database. Recall that a join is a relationship between two tables, that allows rows from one table to be combined with rows from another, based on a set of common join columns.
 
 
No explanation needed. Please return all join relationships in the following JSON format:
{
  "joins": [
    {
      "from_table": "table-1",
      "from_column": "column-1",
      "to_table": "table-2",
      "to_column": "column-3"
    }, 
	...
  ]
}

Tables:

Table: All measures
| Column1   |
|:----------|
| d         |


Table: Calendar
| DateKey                 |   YearNumber |   MonthNumber | MonthName   |   DayNumber | DayName   | Quarter   |
|:------------------------|-------------:|--------------:|:------------|------------:|:----------|:----------|
| 2015-07-01 00:00:00.000 |         2015 |             7 | July        |           1 | Wednesday | Q3        |
| 2015-07-02 00:00:00.000 |         2015 |             7 | July        |           2 | Thursday  | Q3        |
| 2015-07-03 00:00:00.000 |         2015 |             7 | July        |           3 | Friday    | Q3        |
| 2015-07-04 00:00:00.000 |         2015 |             7 | July        |           4 | Saturday  | Q3        |
| 2015-07-05 00:00:00.000 |         2015 |             7 | July        |           5 | Sunday    | Q3        |
| 2015-07-06 00:00:00.000 |         2015 |             7 | July        |           6 | Monday    | Q3        |
| 2015-07-07 00:00:00.000 |         2015 |             7 | July        |           7 | Tuesday   | Q3        |
| 2015-07-08 00:00:00.000 |         2015 |             7 | July        |           8 | Wednesday | Q3        |
| 2015-07-09 00:00:00.000 |         2015 |             7 | July        |           9 | Thursday  | Q3        |
| 2015-07-10 00:00:00.000 |         2015 |             7 | July        |          10 | Friday    | Q3        |


Table: Centre

... (94 rows omitted) ...

|          8 | West Midlands          |
|          9 | Yorkshire & Humberside |


Table: Town
|   TownId | TownName          |   RegionId |
|---------:|:------------------|-----------:|
|        1 | Aintree           |          5 |
|        2 | Aldershot         |          6 |
|        3 | Altrincham        |          5 |
|        4 | Andover           |          6 |
|        5 | Ashford           |          6 |
|        6 | Ashton Under Lyne |          5 |
|        7 | Aylesbury         |          6 |
|        8 | Banbury           |          6 |
|        9 | Barhill           |          1 |
|       10 | Barking           |          3 |

 

````

### Model Response

```
```json
{
  "joins": [
    {
      "from_table": "Centre",
      "from_column": "TownId",
      "to_table": "Town",
      "to_column": "TownId"
    },
    {
      "from_table": "Centre",
      "from_column": "CentreTypeId",
      "to_table": "CentreType",
      "to_column": "CentreTypeId"
    },
    {
      "from_table": "Product",
      "from_column": "HabitatId",
      "to_table": "Habitat",
      "to_column": "HabitatId"
    },
    {
      "from_table": "Purchase",
      "from_column": "CentreId",
      "to_table": "Centre",
      "to_column": "CentreId"
    },
    {
      "from_table": "Purchase",
      "from_column": "ProductId",
      "to_table": "Product",
      "to_column": "ProductId"
    }
  ]
}
```
```

### Correct Answer

```
{
  "joins": [
    {
      "from_table": "Centre",
      "from_column": "CentreTypeId",
      "to_table": "CentreType",
      "to_column": "CentreTypeId"
    },
    {
      "from_table": "Purchase",
      "from_column": "CentreId",
      "to_table": "Centre",
      "to_column": "CentreId"
    },
    {
      "from_table": "Centre",
      "from_column": "TownId",
      "to_table": "Town",
      "to_column": "TownId"
    },
    {
      "from_table": "Habitat",
      "from_column": "EnvironmentId",
      "to_table": "Environment",
      "to_column": "EnviromentId"
    },
    {
      "from_table": "Product",
      "from_column": "FamilyId",
      "to_table": "Family",
      "to_column": "FamilyId"
    },
    {
      "from_table": "Product",
      "from_column": "HabitatId",
      "to_table": "Habitat",
      "to_column": "HabitatId"
    },
    {
      "from_table": "Purchase",
      "from_column": "ProductId",
      "to_table": "Product",
      "to_column": "ProductId"
    },
    {
      "from_table": "Town",
      "from_column": "RegionId",
      "to_table": "Region",
      "to_column": "RegionId"
    },
    {
      "from_table": "Purchase",
      "from_column": "PurchaseDate",
      "to_table": "Calendar",
      "to_column": "DateKey"
    }
  ]
}
```


---

## Question 5: 121666661 (Auto-BI)

**Dataset:** Auto-BI  
**Test case:** 121666661  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Your are given a database with related tables used for business intelligence analysis. Your task is to identify all key/foreign-key join relationships between the tables for this database. Recall that a join is a relationship between two tables, that allows rows from one table to be combined with rows from another, based on a set of common join columns.
 
 
No explanation needed. Please return all join relationships in the following JSON format:
{
  "joins": [
    {
      "from_table": "table-1",
      "from_column": "column-1",
      "to_table": "table-2",
      "to_column": "column-3"
    }, 
	...
  ]
}

Tables:

Table: Age Charachteristics Median
| Postal Code   | Topic               | Characteristics                                                            |   Total |   Male |   Female |   Age_Popu |
|:--------------|:--------------------|:---------------------------------------------------------------------------|--------:|-------:|---------:|-----------:|
| H8R           | Age characteristics | Total - Distribution (%) of the population by broad age groups - 100% data |     100 |    100 |      100 |    2991300 |
| H3C           | Age characteristics | Total - Distribution (%) of the population by broad age groups - 100% data |     100 |    100 |      100 |    1087700 |
| H3Z           | Age characteristics | Total - Distribution (%) of the population by broad age groups - 100% data |     100 |    100 |      100 |    1181300 |
| H3Y           | Age characteristics | Total - Distribution (%) of the population by broad age groups - 100% data |     100 |    100 |      100 |     974700 |
| H2P           | Age characteristics | Total - Distribution (%) of the population by broad age groups - 100% data |     100 |    100 |      100 |    1469300 |
| H2R           | Age characteristics | Total - Distribution (%) of the population by broad age groups - 100% data |     100 |    100 |      100 |    2243600 |
| H2E           | Age characteristics | Total - Distribution (%) of the population by broad age groups - 100% data |     100 |    100 |      100 |    2429700 |
| H4E           | Age characteristics | Total - Distribution (%) of the population by broad age groups - 100% data |     100 |    100 |      100 |    3051300 |
| H4H           | Age characteristics | Total - Distribution (%) of the population by broad age groups - 100% data |     100 |    100 |      100 |    1926800 |
| H4G           | Age characteristics | Total - Distribution (%) of the population by broad age groups - 100% data |     100 |    100 |      100 |    2948800 |


Table: Age Characteristics
| Postal Code   | Topic               | Characteristics                                                  | Total   | Male   | Female   | age goup           |
|:--------------|:--------------------|:-----------------------------------------------------------------|:--------|:-------|:---------|:-------------------|
| H4Z           | Age characteristics | Total - Age groups and average age of the population - 100% data |         |        |          |                    |
| H4Z           | Age characteristics | 0 to 14 years                                                    |         |        |          | Age 0 to 14 years  |
| H4Z           | Age characteristics | 0 to 4 years                                                     |         |        |          |                    |
| H4Z           | Age characteristics | 5 to 9 years                                                     |         |        |          |                    |

... (429 rows omitted) ...

| Charlemagne                      |              10   |                1 | Montréal                  | French     | Private       | H9K          | H9K 1G4               | 45.4604 | -73.9184 |
| Chomedey-De-Maisonneuve          |               1.3 |              467 | Montréal                  | French     | Public        | H1V          | H1V 2R2               | 45.5527 | -73.5385 |


Table: WalkscoreZipcode
| Postal Code   | ZIP_CIDE   |   Walk_Score |   Score List |
|:--------------|:-----------|-------------:|-------------:|
| H1E           | H1E 0A1    |           50 |           50 |
| H1E           | H1E 0A2    |           44 |           44 |
| H1E           | H1E 0A3    |           24 |           24 |
| H1E           | H1E 0A5    |           28 |           28 |
| H1E           | H1E 0A6    |           32 |           32 |
| H1E           | H1E 0A7    |           21 |           21 |
| H1E           | H1E 0A8    |           25 |           25 |
| H1E           | H1E 0A9    |           28 |           28 |
| H1E           | H1E 0B1    |           23 |           23 |
| H1E           | H1E 0B2    |           50 |           50 |

 

````

### Model Response

```
```json
{
  "joins": [
    {
      "from_table": "Age Characteristics",
      "from_column": "Postal Code",
      "to_table": "Age Charachteristics Median",
      "to_column": "Postal Code"
    },
    {
      "from_table": "Cod_Area_Montreal",
      "from_column": "POSTAL_CODES",
      "to_table": "Montreal_KIJIJI_Rent",
      "to_column": "Postal Code"
    },
    {
      "from_table": "Cod_Area_Montreal",
      "from_column": "POSTAL_CODES",
      "to_table": "Montreal_Choice-Area",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "Cod_Area_Montreal",
      "from_column": "POSTAL_CODES",
      "to_table": "Population_dwellings",
      "to_column": "Postal Code"
    },
    {
      "from_table": "Cod_Area_Montreal",
      "from_column": "POSTAL_CODES",
      "to_table": "WalkscoreZipcode",
      "to_column": "Postal Code"
    },
    {
      "from_table": "Continent_Country",
      "from_column": "Place",
      "to_table": "Immigrant Measure",
      "to_column": "Region"
    },
    {
      "from_table": "Continent_Country",
      "from_column": "Place",
      "to_table": "Immigrants_Regions",
      "to_column": "Regions"
    },
    {
      "from_table": "Continent_Country",
      "from_column": "Place",
      "to_table": "region immigrant",
      "to_column": "Region"
    },
    {
      "from_table": "Factor_Immigrant",
      "from_column": "Grade",
      "to_table": "Immigrant Measure",
      "to_column": "Grade"
    },
    {
      "from_table": "Factor_Infraction",
      "from_column": "Grade",
      "to_table": "InterventionsCitoyendo",
      "to_column": "Grade"
    },
    {
      "from_table": "Factor_Price",
      "from_column": "Grade",
      "to_table": "Montreal_KIJIJI_Rent",
      "to_column": "Grade"
    },
    {
      "from_table": "Factor_SchoolScore",
      "from_column": "Grade",
      "to_table": "secondary_schools_2019",
      "to_column": "Grade"
    },
    {
      "from_table": "Factor_WalkScore",
      "from_column": "Grade",
    

... (truncated) ...
```

### Correct Answer

```
{
  "joins": [
    {
      "from_table": "Montreal_neighborhood",
      "from_column": "POSTAL CODES",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "secondary_schools_2019",
      "from_column": "Posta Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "interventionscitoyendo",
      "from_column": "POSTAL_CODES",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "Population_dwellings",
      "from_column": "Postal Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "Age Characteristics",
      "from_column": "Postal Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "Immigrants by Place",
      "from_column": "Postal Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "Immigrants by Place",
      "from_column": "Region",
      "to_table": "Immigrants_Regions",
      "to_column": "Regions"
    },
    {
      "from_table": "Language Spoken",
      "from_column": "Postal Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "Age Charachteristics Median",
      "from_column": "Postal Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "Income Censu",
      "from_column": "Postal Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "Language at Work",
      "from_column": "Postal Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "Language official knowledge",
      "from_column": "Postal Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "Language Spoken at Home",
      "from_column": "Postal Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "RentalPricesKijij",
      "from_column": "Postal Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "WalkscoreZipcode",
      "from_column": "Postal Code",
      "to_table": "Cod_Area_Montreal",
      "to_column": "POSTAL_CODES"
    },
    {
      "from_table": "Cod_Area_Montreal",
      "from_column": "POSTAL_CODES",
      "to_table": "Montreal_Choice-Area",
      "to_column": "POSTAL_CODES"
    }
  ]
}
```


---

## Question 6: 229954750 (Auto-BI)

**Dataset:** Auto-BI  
**Test case:** 229954750  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Your are given a database with related tables used for business intelligence analysis. Your task is to identify all key/foreign-key join relationships between the tables for this database. Recall that a join is a relationship between two tables, that allows rows from one table to be combined with rows from another, based on a set of common join columns.
 
 
No explanation needed. Please return all join relationships in the following JSON format:
{
  "joins": [
    {
      "from_table": "table-1",
      "from_column": "column-1",
      "to_table": "table-2",
      "to_column": "column-3"
    }, 
	...
  ]
}

Tables:

Table: Airports
| Airports   | Type        |
|:-----------|:------------|
| Columbus   | Origin      |
| Atlanta    | Destination |
| Dallas     | Origin      |
| Fort Worth | Destination |
| Columbus   | Destination |
| Cleveland  | Origin      |
| Cincinatti | Destination |


Table: BadgeID
|   BadgeID |
|----------:|
|       456 |
|       321 |
|       765 |


Table: Calendar
| Date                    |   Weeknum |

... (411 rows omitted) ...

| 2017-07-19 00:00:00.000 |       4 |        29 |
| 2017-07-20 00:00:00.000 |       5 |        29 |
| 2017-07-21 00:00:00.000 |       6 |        29 |
| 2017-07-22 00:00:00.000 |       7 |        29 |
| 2017-07-23 00:00:00.000 |       8 |        30 |
| 2017-07-24 00:00:00.000 |       9 |        30 |
| 2017-07-25 00:00:00.000 |      10 |        30 |


Table: WorkOrders
|   WorkOrder | MaterialType   |   Amount |
|------------:|:---------------|---------:|
|     1000001 | XYZ789         |       10 |
|     1000002 | ABC123         |        9 |
|     1000003 | XYZ789         |       20 |
|     1000004 | ABC123         |        3 |
|     1000005 | PGN561         |       20 |

 

````

### Model Response

```
```json
{
  "joins": [
    {
      "from_table": "Airports",
      "from_column": "Origin",
      "to_table": "Calendar",
      "to_column": "Date"
    },
    {
      "from_table": "Airports",
      "from_column": "Destination",
      "to_table": "Calendar",
      "to_column": "Date"
    },
    {
      "from_table": "Changes Contracts",
      "from_column": "Contract Number",
      "to_table": "Contract Management",
      "to_column": "Contract Number"
    },
    {
      "from_table": "Columns",
      "from_column": "Date",
      "to_table": "Calendar",
      "to_column": "Date"
    },
    {
      "from_table": "Customers",
      "from_column": "Customer",
      "to_table": "CustomersTable",
      "to_column": "Customer"
    },
    {
      "from_table": "Dates",
      "from_column": "Dates",
      "to_table": "Calendar",
      "to_column": "Date"
    },
    {
      "from_table": "Distinct",
      "from_column": "Date",
      "to_table": "Calendar",
      "to_column": "Date"
    },
    {
      "from_table": "Examinations",
      "from_column": "Req_id",
      "to_table": "Names",
      "to_column": "BadgeID"
    },
    {
      "from_table": "Failures",
      "from_column": "Location",
      "to_table": "Inventory",
      "to_column": "Stock Out"
    },
    {
      "from_table": "Materials",
      "from_column": "Materials",
      "to_table": "MaterialTypes",
      "to_column": "Materials"
    },
    {
      "from_table": "MatrixFun",
      "from_column": "Year",
      "to_table": "Numbers",
      "to_column": "Number"
    },
    {
      "from_table": "Opportunities",
      "from_column": "Company",
      "to_table": "Projects",
      "to_column": "ProjectNO"
    },
    {
      "from_table": "ProductsCustomers",
      "from_column": "ProductNo",
      "to_table": "Products",
      "to_column": "Product"
    },
    {
      "from_table": "Sales",
      "from_column": "ORDERID",
      "to_table": "OrderIDs",
      "to_column": "ORDERID"
    },
    {
      "from_table": "

... (truncated) ...
```

### Correct Answer

```
{
  "joins": [
    {
      "from_table": "Sales",
      "from_column": "ORDERID",
      "to_table": "OrderIDs",
      "to_column": "ORDERID"
    },
    {
      "from_table": "Sales",
      "from_column": "ItemDesc",
      "to_table": "Shirts",
      "to_column": "ItemDesc"
    },
    {
      "from_table": "Calendar",
      "from_column": "Date",
      "to_table": "Values",
      "to_column": "Date"
    },
    {
      "from_table": "Changes Contracts",
      "from_column": "Contract Number",
      "to_table": "Contract Management",
      "to_column": "Contract Number"
    },
    {
      "from_table": "MaterialTypes",
      "from_column": "MaterialType",
      "to_table": "Materials",
      "to_column": "Materials"
    },
    {
      "from_table": "WorkOrders",
      "from_column": "MaterialType",
      "to_table": "Materials",
      "to_column": "Materials"
    },
    {
      "from_table": "JournalDetailView",
      "from_column": "ProjectNO",
      "to_table": "Projects",
      "to_column": "ProjectNO"
    },
    {
      "from_table": "Names",
      "from_column": "BadgeID",
      "to_table": "BadgeID",
      "to_column": "BadgeID"
    },
    {
      "from_table": "Customers",
      "from_column": "Product",
      "to_table": "Products",
      "to_column": "Product"
    },
    {
      "from_table": "Customers",
      "from_column": "Customer",
      "to_table": "CustomersTable",
      "to_column": "Customer"
    }
  ]
}
```


---

## Question 7: 222763042 (Auto-BI)

**Dataset:** Auto-BI  
**Test case:** 222763042  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Your are given a database with related tables used for business intelligence analysis. Your task is to identify all key/foreign-key join relationships between the tables for this database. Recall that a join is a relationship between two tables, that allows rows from one table to be combined with rows from another, based on a set of common join columns.
 
 
No explanation needed. Please return all join relationships in the following JSON format:
{
  "joins": [
    {
      "from_table": "table-1",
      "from_column": "column-1",
      "to_table": "table-2",
      "to_column": "column-3"
    }, 
	...
  ]
}

Tables:

Table: aeropuerto (2)
|   id | sigla   | nombre                |   gcd_municipio | iata   |   categoria |   latitud |   longitud |   longitud_pista |   ancho_pista |   pbmo |   elevacion |   tipo |   clase |   explotador |   propietario |
|-----:|:--------|:----------------------|----------------:|:-------|------------:|----------:|-----------:|-----------------:|--------------:|-------:|------------:|-------:|--------:|-------------:|--------------:|
|    1 | 7FU     | LA ESCONDIDA          |           50568 |        |           1 |    4.6108 |   -71.1935 |             1300 |            18 |   5000 |         564 |      2 |       2 |           33 |           104 |
|    2 | 7FW     | MORICHITO             |           85125 |        |           1 |    5.9188 |   -71.7932 |              800 |            15 |   3500 |         720 |      3 |       2 |           87 |            27 |
|    3 | 7FX     | CAROLINA DEL PRINCIPE |            5150 |        |           1 |    6.7248 |   -75.2909 |              400 |            16 |   1000 |        6004 |      4 |       2 |           79 |            95 |
|    4 | 7FY     | DUBAI                 |           23068 |        |           1 |    8.296  |   -75.0307 |              350 |            10 |    500 |          82 |      3 |       2 |           18 |            16 |
|    5 | 7GA     | BARU - HIDROPUERTO    |           13001 |        |           1 |   10.2321 |   -75.5877 |              450 |            20 |    500 |           0 |      3 |       2 |           40 |            89 |
|    6 | 7GB     | LA CAROLINA           |           20250 |        |           1 |    9.528  |   -73.7866 |              350 |            10 |    500 |         690 |      3 |      15 |           64 |            69 |
|    7 | 7GC     | SAN FELIPE DEL PAUTO  |           85430 |        |           1 |    5.2032 |   -70.8951 |              720 |            10 |   3000 |        3125 |      3 |       2 |            8 |             5 |
|    8 | 7GD     | VELASQUEZ             |           15572 |        |           1 |    5.9482 |   -74.4575 |             1500 |            18 |  10000 |         617 |      3 |      10 |           73 |            46 |
|    9 | 7GF     | LA UNION              |           85250 |        |           1 |    5.6283 |   -70.7032 |              640 |            18 |   3500 |         335 |      3 |       2 |           52 |            87 |
|   10 | 7GG     | LA ILUSION            |           85139 |        |           1 |    4.5805 |   -72.4282 |              890 |            18 |   3500 |         574 |      3 |       2 |           93 |           115 |


Table: aeropuerto
|   id | sigla   | nombre                |   gcd_municipio | iata   |   categoria |   latitud |   longitud |   longitud_pista |   ancho_pista |   pbmo |   elevacion |   tipo |   clase |   explotador |   propietario |
|-----:|:--------|:----------------------|----------------:|:-------|------------:|----------:|-----------:|-----------------:|--------------:|-------:|------------:|-------:|--------:|-------------:|--------------:|
|    1 | 7FU     | LA ESCONDIDA          |           50568 |        |           1 |    4.6108 |   -71.1935 |             1300 |            18 |   5000 |         564 |      2 |       2 |           33 |           104 |
|    2 | 7FW     | MORICHITO             |           85125 |        |           1 |    5.9188 |   -71.7932 |              800 |            15 |   3500 |         720 |      3 |       2 |           87 |            27 |
|    3 | 7FX     | CAROLINA DEL PRINCIPE |            5150 |        |           1 |    6.7248 |   -75.2909 |              400 |            16 |   1000 |        6004 |      4 |       2 |           79 |            95 |
|    4 | 7FY     | DUBAI                 |           23068 |        |           1 |    8.296  |   -75.0307 |              350 |            10 |    500 |          82 |      3 |       2 |           18 |            16 |

... (196 rows omitted) ...

|    3 | R      |
|    4 | T      |


Table: vuelo
|    id |   mes |   ano |   origen |   destino |   tipo_equipo |   tipo_vuelo | trafico   |   sillas |   carga_ofrecida |   carga_bordo |   vuelos |   empresa | fecha                   |   pasajeros |
|------:|------:|------:|---------:|----------:|--------------:|-------------:|:----------|---------:|-----------------:|--------------:|---------:|----------:|:------------------------|------------:|
|  2933 |     3 |  2010 |      178 |       207 |            91 |            4 | N         |        0 |                0 |             0 |        1 |        54 | 2010-03-01 00:00:00.000 |           2 |
|  4308 |     4 |  2010 |      201 |       207 |            91 |            4 | N         |        0 |                0 |             0 |        1 |        54 | 2010-04-01 00:00:00.000 |           2 |
|  5346 |     5 |  2010 |      176 |       207 |            91 |            4 | N         |        0 |                0 |             0 |        1 |        54 | 2010-05-01 00:00:00.000 |           2 |
|  6627 |     6 |  2010 |      165 |       207 |            91 |            4 | N         |        0 |                0 |             0 |        1 |        54 | 2010-06-01 00:00:00.000 |           2 |
|  9403 |     8 |  2010 |      183 |       207 |            91 |            4 | N         |        0 |                0 |             0 |        1 |        54 | 2010-08-01 00:00:00.000 |           2 |
| 10644 |     9 |  2010 |      182 |       207 |            91 |            4 | N         |        0 |                0 |             0 |        1 |        54 | 2010-09-01 00:00:00.000 |           2 |
| 11811 |    10 |  2010 |      165 |       207 |            91 |            4 | N         |        0 |                0 |             0 |        1 |        54 | 2010-10-01 00:00:00.000 |           2 |
| 11933 |    10 |  2010 |      178 |       207 |            91 |            4 | N         |        0 |                0 |             0 |        1 |        54 | 2010-10-01 00:00:00.000 |           2 |
| 11941 |    10 |  2010 |      182 |       207 |            91 |            4 | N         |        0 |                0 |             0 |        1 |        54 | 2010-10-01 00:00:00.000 |           2 |
| 11944 |    10 |  2010 |      182 |       207 |            91 |            4 | N         |        0 |                0 |             0 |        1 |        54 | 2010-10-01 00:00:00.000 |           2 |

 

````

### Model Response

```
```json
{
  "joins": [
    {
      "from_table": "aeropuerto",
      "from_column": "gcd_municipio",
      "to_table": "municipio",
      "to_column": "gcd_municipio"
    },
    {
      "from_table": "aeropuerto",
      "from_column": "categoria",
      "to_table": "categoria_aeropuerto",
      "to_column": "id"
    },
    {
      "from_table": "aeropuerto",
      "from_column": "clase",
      "to_table": "clase_aeropuerto",
      "to_column": "id"
    },
    {
      "from_table": "aeropuerto",
      "from_column": "explotador",
      "to_table": "explotador_aeropuerto",
      "to_column": "explotador"
    },
    {
      "from_table": "aeropuerto",
      "from_column": "propietario",
      "to_table": "propietario_aeropuerto",
      "to_column": "propietario"
    },
    {
      "from_table": "aeropuerto",
      "from_column": "iata",
      "to_table": "iata",
      "to_column": "iata"
    }
  ]
}
```
```

### Correct Answer

```
{
  "joins": [
    {
      "from_table": "aeropuerto",
      "from_column": "gcd_municipio",
      "to_table": "municipio",
      "to_column": "gcd_municipio"
    },
    {
      "from_table": "municipio",
      "from_column": "gcd_departamento",
      "to_table": "departamento",
      "to_column": "gcd_departamento"
    },
    {
      "from_table": "aeropuerto",
      "from_column": "clase",
      "to_table": "clase_aeropuerto",
      "to_column": "id"
    },
    {
      "from_table": "aeropuerto",
      "from_column": "categoria",
      "to_table": "categoria_aeropuerto",
      "to_column": "categoria"
    },
    {
      "from_table": "aeropuerto",
      "from_column": "propietario",
      "to_table": "propietario_aeropuerto",
      "to_column": "id"
    },
    {
      "from_table": "aeropuerto",
      "from_column": "explotador",
      "to_table": "explotador_aeropuerto",
      "to_column": "explotador"
    },
    {
      "from_table": "aeropuerto",
      "from_column": "tipo",
      "to_table": "tipo_aeropuerto",
      "to_column": "id"
    },
    {
      "from_table": "resolucion",
      "from_column": "aeropuerto",
      "to_table": "aeropuerto",
      "to_column": "id"
    },
    {
      "from_table": "aeropuerto",
      "from_column": "iata",
      "to_table": "iata",
      "to_column": "id"
    },
    {
      "from_table": "vuelo",
      "from_column": "empresa",
      "to_table": "empresa",
      "to_column": "empresa"
    },
    {
      "from_table": "vuelo",
      "from_column": "tipo_equipo",
      "to_table": "tipo_equipo",
      "to_column": "id"
    },
    {
      "from_table": "vuelo",
      "from_column": "tipo_vuelo",
      "to_table": "tipo_vuelo",
      "to_column": "id"
    },
    {
      "from_table": "vuelo",
      "from_column": "origen",
      "to_table": "aeropuerto",
      "to_column": "id"
    },
    {
      "from_table": "municipio (2)",
      "from_column": "gcd_departamento",
      "to_table": "departamento (2)",
      "to_column": "gcd_departamento"
    },
    {
      "from_table": "aeropuerto (2)",
      "from_column": "gcd_municipio",
      "to_table": "municipio (2)",
      "to_column": "gcd_municipio"
    },
    {
      "from_table": "vuelo",
      "from_column": "destino",
      "to_table": "aeropuerto (2)",
      "to_column": "id"
    }
  ]
}
```


---

## Question 8: 184974692 (Auto-BI)

**Dataset:** Auto-BI  
**Test case:** 184974692  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Your are given a database with related tables used for business intelligence analysis. Your task is to identify all key/foreign-key join relationships between the tables for this database. Recall that a join is a relationship between two tables, that allows rows from one table to be combined with rows from another, based on a set of common join columns.
 
 
No explanation needed. Please return all join relationships in the following JSON format:
{
  "joins": [
    {
      "from_table": "table-1",
      "from_column": "column-1",
      "to_table": "table-2",
      "to_column": "column-3"
    }, 
	...
  ]
}

Tables:

Table: DIM_CANDIDATO
|   SK_CANDIDATO |   NK_CANDIDDATO | NM_CANDIDATO    |
|---------------:|----------------:|:----------------|
|              0 |              -1 | NA              |
|              1 |             100 | Candidato 100   |
|              2 |            1000 | Candidato 1000  |
|              3 |           10000 | Candidato 10000 |
|              4 |           10001 | Candidato 10001 |
|              5 |           10002 | Candidato 10002 |
|              6 |           10003 | Candidato 10003 |
|              7 |           10004 | Candidato 10004 |
|              8 |           10005 | Candidato 10005 |
|              9 |           10006 | Candidato 10006 |


Table: DIM_CURSO
|   SK_CURSO |   NK_CURSO | NM_CURSO   |
|-----------:|-----------:|:-----------|
|          0 |         -1 | NA         |
|          1 |         55 | Curso 55   |
|          2 |         26 | Curso 26   |
|          3 |         41 | Curso 41   |

... (92 rows omitted) ...

Table: FATO_PRE_INSCRICOES
|   SK_CANDIDATO |   SK_PROCESSO |   SK_CURSO |     SK_DATA |   SK_HORA |
|---------------:|--------------:|-----------:|------------:|----------:|
|             91 |             2 |         21 | 2.01902e+07 |      2048 |
|            123 |             2 |         21 | 2.01902e+07 |      1503 |
|            171 |             2 |         21 | 2.01902e+07 |      1754 |
|            242 |             2 |         21 | 2.01902e+07 |      1321 |
|            369 |             2 |         21 | 2.01902e+07 |      2343 |
|            529 |             2 |         21 | 2.01902e+07 |       816 |
|            592 |             2 |         21 | 2.01902e+07 |      1946 |
|            642 |             2 |         21 | 2.01902e+07 |      1758 |
|            643 |             2 |         21 | 2.01902e+07 |      1759 |
|            681 |             2 |         21 | 2.01902e+07 |      1916 |


Table: Metricas


 

````

### Model Response

```
```json
{
  "joins": [
    {
      "from_table": "DIM_CANDIDATO",
      "from_column": "SK_CANDIDATO",
      "to_table": "FATO_INSCRICOES",
      "to_column": "SK_CANDIDATO"
    },
    {
      "from_table": "DIM_CURSO",
      "from_column": "SK_CURSO",
      "to_table": "FATO_INSCRICOES",
      "to_column": "SK_CURSO"
    },
    {
      "from_table": "DIM_PROCESSO",
      "from_column": "SK_PROCESSO",
      "to_table": "FATO_INSCRICOES",
      "to_column": "SK_PROCESSO"
    },
    {
      "from_table": "DIM_DATA",
      "from_column": "SK_DATA",
      "to_table": "FATO_INSCRICOES",
      "to_column": "SK_DATA"
    },
    {
      "from_table": "DIM_HORA",
      "from_column": "SK_HORA",
      "to_table": "FATO_INSCRICOES",
      "to_column": "SK_HORA"
    },
    {
      "from_table": "DIM_CANDIDATO",
      "from_column": "SK_CANDIDATO",
      "to_table": "FATO_INSCRICOES_PAGA",
      "to_column": "SK_CANDIDATO"
    },
    {
      "from_table": "DIM_CURSO",
      "from_column": "SK_CURSO",
      "to_table": "FATO_INSCRICOES_PAGA",
      "to_column": "SK_CURSO"
    },
    {
      "from_table": "DIM_PROCESSO",
      "from_column": "SK_PROCESSO",
      "to_table": "FATO_INSCRICOES_PAGA",
      "to_column": "SK_PROCESSO"
    },
    {
      "from_table": "DIM_DATA",
      "from_column": "SK_DATA",
      "to_table": "FATO_INSCRICOES_PAGA",
      "to_column": "SK_DATA"
    },
    {
      "from_table": "DIM_HORA",
      "from_column": "SK_HORA",
      "to_table": "FATO_INSCRICOES_PAGA",
      "to_column": "SK_HORA"
    },
    {
      "from_table": "DIM_FORMA_PAG",
      "from_column": "SK_FORMA_PAG",
      "to_table": "FATO_INSCRICOES_PAGA",
      "to_column": "SK_FORMA_PAG"
    },
    {
      "from_table": "DIM_CANDIDATO",
      "from_column": "SK_CANDIDATO",
      "to_table": "FATO_PRE_INSCRICOES",
      "to_column": "SK_CANDIDATO"
    },
    {
      "from_table": "DIM_PROCESSO",
      "from_column": "SK_PROCESSO",
      "to_table": "FATO_PRE_INSCRICOES",
      "to_column":

... (truncated) ...
```

### Correct Answer

```
{
  "joins": [
    {
      "from_table": "FATO_INSCRICOES",
      "from_column": "SK_CANDIDATO",
      "to_table": "DIM_CANDIDATO",
      "to_column": "SK_CANDIDATO"
    },
    {
      "from_table": "FATO_INSCRICOES_PAGA",
      "from_column": "SK_CANDIDATO",
      "to_table": "DIM_CANDIDATO",
      "to_column": "SK_CANDIDATO"
    },
    {
      "from_table": "FATO_PRE_INSCRICOES",
      "from_column": "SK_CANDIDATO",
      "to_table": "DIM_CANDIDATO",
      "to_column": "SK_CANDIDATO"
    },
    {
      "from_table": "FATO_INSCRICOES",
      "from_column": "SK_CURSO",
      "to_table": "DIM_CURSO",
      "to_column": "SK_CURSO"
    },
    {
      "from_table": "FATO_INSCRICOES_PAGA",
      "from_column": "SK_CURSO",
      "to_table": "DIM_CURSO",
      "to_column": "SK_CURSO"
    },
    {
      "from_table": "FATO_PRE_INSCRICOES",
      "from_column": "SK_CURSO",
      "to_table": "DIM_CURSO",
      "to_column": "SK_CURSO"
    },
    {
      "from_table": "FATO_INSCRICOES",
      "from_column": "SK_DATA",
      "to_table": "DIM_DATA",
      "to_column": "SK_DATA"
    },
    {
      "from_table": "FATO_INSCRICOES_PAGA",
      "from_column": "SK_DATA",
      "to_table": "DIM_DATA",
      "to_column": "SK_DATA"
    },
    {
      "from_table": "FATO_PRE_INSCRICOES",
      "from_column": "SK_DATA",
      "to_table": "DIM_DATA",
      "to_column": "SK_DATA"
    },
    {
      "from_table": "FATO_INSCRICOES_PAGA",
      "from_column": "SK_FORMA_PAG",
      "to_table": "DIM_FORMA_PAG",
      "to_column": "SK_FORMA_PAG"
    },
    {
      "from_table": "FATO_INSCRICOES",
      "from_column": "SK_HORA",
      "to_table": "DIM_HORA",
      "to_column": "SK_HORA"
    },
    {
      "from_table": "FATO_INSCRICOES_PAGA",
      "from_column": "SK_HORA",
      "to_table": "DIM_HORA",
      "to_column": "SK_HORA"
    },
    {
      "from_table": "FATO_PRE_INSCRICOES",
      "from_column": "SK_HORA",
      "to_table": "DIM_HORA",
      "to_column": "SK_HORA"
    },
    {
      "from_table": "FATO_INSCRICOES",
      "from_column": "SK_PROCESSO",
      "to_table": "DIM_PROCESSO",
      "to_column": "SK_PROCESSO"
    },
    {
      "from_table": "FATO_INSCRICOES_PAGA",
      "from_column": "SK_PROCESSO",
      "to_table": "DIM_PROCESSO",
      "to_column": "SK_PROCESSO"
    },
    {
      "from_table": "FATO_PRE_INSCRICOES",
      "from_column": "SK_PROCESSO",
      "to_table": "DIM_PROCESSO",
      "to_column": "SK_PROCESSO"
    }
  ]
}
```


---

## Question 9: 324475578 (Auto-BI)

**Dataset:** Auto-BI  
**Test case:** 324475578  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Your are given a database with related tables used for business intelligence analysis. Your task is to identify all key/foreign-key join relationships between the tables for this database. Recall that a join is a relationship between two tables, that allows rows from one table to be combined with rows from another, based on a set of common join columns.
 
 
No explanation needed. Please return all join relationships in the following JSON format:
{
  "joins": [
    {
      "from_table": "table-1",
      "from_column": "column-1",
      "to_table": "table-2",
      "to_column": "column-3"
    }, 
	...
  ]
}

Tables:

Table: Account
| Account ID   | Account                    |
|:-------------|:---------------------------|
| B70100       | Produits Finis             |
| B70210       | Produits Semi Finis        |
| B70220       | Autres Produits Semi Finis |
| B70300       | Produits intermédiaires    |
| B70400       | Prestations de services    |
| B70500       | Ventes de marchandises     |
| B70600       | Autres activités           |
| B70700       | RRR                        |


Table: Activity_Product
| Activity ID   | Activity                          |
|:--------------|:----------------------------------|
| B1000         | Technologiques                    |
| B9000         | Autres                            |
| BC000         | Activités destinées à être cédées |
| BNA           | Non Applicable                    |
| E10000        | Futaille                          |
| E10ORM        | Fûts                              |

... (174 rows omitted) ...

| M30         | SM3030         | VS Pietec   |
| M40         | SM4010         | Autres      |


Table: Subpole
| Subpole ID   | Subpole                           | Pole ID   |
|:-------------|:----------------------------------|:----------|
| SPV1010      | Innerstaves                       | PV10      |
| SPV1020      | Copeaux                           | PV10      |
| SPV2010      | Pôle Vigne                        | PV20      |
| SPV2020      | Pôle Cave                         | PV20      |
| SPV2030      | Pôle Microbio                     | PV20      |
| SPV2040      | Pôle Sensoriel                    | PV20      |
| SPV3010      | Réparation & Maintenance          | PV30      |
| SPV3015      | Mise à dispo personnel facturé Tx | PV30      |
| SPV3020      | Autres prestations                | PV30      |
| SPV3025      | Fûts d'occasion                   | PV30      |

 

````

### Model Response

```
```json
{
  "joins": [
    {
      "from_table": "Account",
      "from_column": "Account ID",
      "to_table": "Sales Budget VS Actual",
      "to_column": "Account ID"
    },
    {
      "from_table": "Account",
      "from_column": "Account ID",
      "to_table": "Sales",
      "to_column": "Account ID"
    },
    {
      "from_table": "Activity_Product",
      "from_column": "Activity ID",
      "to_table": "Control gap",
      "to_column": "Type"
    },
    {
      "from_table": "Category",
      "from_column": "Activity ID",
      "to_table": "Activity_Product",
      "to_column": "Activity ID"
    },
    {
      "from_table": "Country_Fact",
      "from_column": "Country ID",
      "to_table": "Sales",
      "to_column": "Country ID"
    },
    {
      "from_table": "Date",
      "from_column": "Date",
      "to_table": "Sales Budget VS Actual",
      "to_column": "Date"
    },
    {
      "from_table": "Family",
      "from_column": "Process ID",
      "to_table": "Process",
      "to_column": "Process ID"
    },
    {
      "from_table": "Market",
      "from_column": "Market ID",
      "to_table": "Submarket",
      "to_column": "Market ID"
    },
    {
      "from_table": "Pole",
      "from_column": "Pole ID",
      "to_table": "Subpole",
      "to_column": "Pole ID"
    },
    {
      "from_table": "Product Grouping",
      "from_column": "Family ID",
      "to_table": "Family",
      "to_column": "Family ID"
    },
    {
      "from_table": "Product Grouping",
      "from_column": "Submarket ID",
      "to_table": "Market",
      "to_column": "Market ID"
    },
    {
      "from_table": "Product Grouping",
      "from_column": "Subpole ID",
      "to_table": "Pole",
      "to_column": "Pole ID"
    },
    {
      "from_table": "Product",
      "from_column": "Product Grouping ID",
      "to_table": "Product Grouping",
      "to_column": "Product Grouping ID"
    }
  ]
}
```
```

### Correct Answer

```
{
  "joins": [
    {
      "from_table": "Product Grouping",
      "from_column": "Subpole ID",
      "to_table": "Subpole",
      "to_column": "Subpole ID"
    },
    {
      "from_table": "Subpole",
      "from_column": "Pole ID",
      "to_table": "Pole",
      "to_column": "Pole ID"
    },
    {
      "from_table": "Product Grouping",
      "from_column": "Submarket ID",
      "to_table": "Submarket",
      "to_column": "Submarket ID"
    },
    {
      "from_table": "Product",
      "from_column": "Product Grouping ID",
      "to_table": "Product Grouping",
      "to_column": "Product Grouping ID"
    },
    {
      "from_table": "Product Grouping",
      "from_column": "Family ID",
      "to_table": "Family",
      "to_column": "Family ID"
    },
    {
      "from_table": "Family",
      "from_column": "Process ID",
      "to_table": "Process",
      "to_column": "Process ID"
    },
    {
      "from_table": "Product Grouping",
      "from_column": "Category ID",
      "to_table": "Category",
      "to_column": "Category ID"
    },
    {
      "from_table": "Category",
      "from_column": "Activity ID",
      "to_table": "Activity_Product",
      "to_column": "Activity ID"
    },
    {
      "from_table": "Submarket",
      "from_column": "Market ID",
      "to_table": "Market",
      "to_column": "Market ID"
    },
    {
      "from_table": "Sales",
      "from_column": "Country ID",
      "to_table": "Country_Fact",
      "to_column": "Country ID"
    },
    {
      "from_table": "Sales",
      "from_column": "Account ID",
      "to_table": "Account",
      "to_column": "Account ID"
    },
    {
      "from_table": "Sales",
      "from_column": "Product ID",
      "to_table": "Product",
      "to_column": "Product ID"
    },
    {
      "from_table": "Sales",
      "from_column": "Date",
      "to_table": "Date",
      "to_column": "Date"
    },
    {
      "from_table": "Sales Budget VS Actual",
      "from_column": "Account ID",
      "to_table": "Account",
      "to_column": "Account ID"
    },
    {
      "from_table": "Sales Budget VS Actual",
      "from_column": "Date",
      "to_table": "Date",
      "to_column": "Date"
    },
    {
      "from_table": "Sales Budget VS Actual",
      "from_column": "Product ID",
      "to_table": "Product",
      "to_column": "Product ID"
    }
  ]
}
```

