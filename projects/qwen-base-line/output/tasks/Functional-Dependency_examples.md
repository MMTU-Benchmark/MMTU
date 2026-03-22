# Functional-Dependency: All Questions (9 total)

**Model:** Qwen2.5-7B-Instruct

---

## Question 1: case_311 (Auto-Relate)

**Dataset:** Auto-Relate  
**Test case:** case_311  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Order ID   | Product ID   | Location ID   | Sales Person ID   | Customer ID   | Purchase Date           |   Quantity |   Line Sales | Sales Date              | Customer Name       | Customer Address   | Longitude   | Latitude   |
|:-----------|:-------------|:--------------|:------------------|:--------------|:------------------------|-----------:|-------------:|:------------------------|:--------------------|:-------------------|:------------|:-----------|
| AX15456    | ENX2090      | A105          | EMP1006           | C1667         | 2016-11-25 00:00:00.000 |          2 |         2676 | 2019-11-25 00:00:00.000 | Kevin Lopez         |                    |             |            |
| AX14817    | ENX2035      | A177          | EMP1014           | C1584         | 2017-12-26 00:00:00.000 |          1 |          458 | 2020-12-26 00:00:00.000 | Howard Harrison     |                    |             |            |
| AX24882    | ENX2029      | A188          | EMP1011           | C1395         | 2015-09-06 00:00:00.000 |          2 |         3696 | 2018-09-06 00:00:00.000 | Billy Reid          |                    |             |            |
| AX18918    | ENX2079      | A139          | EMP1003           | C1775         | 2017-05-11 00:00:00.000 |          1 |         1725 | 2020-05-11 00:00:00.000 | Kenneth Marshall    |                    |             |            |
| AX10196    | ENX2083      | A110          | EMP1008           | C1141         | 2015-06-22 00:00:00.000 |          1 |         2141 | 2018-06-22 00:00:00.000 | Phillip Harvey      |                    |             |            |
| AX22160    | ENX2068      | A167          | EMP1037           | C1543         | 2016-11-26 00:00:00.000 |          1 |         1500 | 2019-11-26 00:00:00.000 | Brian Kim           |                    |             |            |
| AX24319    | ENX2092      | A166          | EMP1044           | C1406         | 2016-06-26 00:00:00.000 |          1 |         1639 | 2019-06-26 00:00:00.000 | Paul Richardson     |                    |             |            |
| AX17585    | ENX2057      | A142          | EMP1030           | C1246         | 2016-08-25 00:00:00.000 |          1 |          181 | 2019-08-25 00:00:00.000 | Ronald Bradley      |                    |             |            |
| AX11899    | ENX2064      | A173          | EMP1012           | C1205         | 2017-05-13 00:00:00.000 |          1 |         1414 | 2020-05-13 00:00:00.000 | Eric Shaw           |                    |             |            |
| AX16925    | ENX2057      | A126          | EMP1002           | C1047         | 2015-04-19 00:00:00.000 |          1 |          181 | 2018-04-19 00:00:00.000 | Patrick Graham      |                    |             |            |
| AX23507    | ENX2082      | A154          | EMP1023           | C1140         | 2016-01-20 00:00:00.000 |          1 |         1103 | 2019-01-20 00:00:00.000 | Henry Reyes         |                    |             |            |
| AX23444    | ENX2056      | A118          | EMP1000           | C1216         | 2016-06-11 00:00:00.000 |          1 |         1635 | 2019-06-11 00:00:00.000 | Jimmy Harper        |                    |             |            |
| AX21334    | ENX2032      | A168          | EMP1014           | C1326         | 2016-04-22 00:00:00.000 |          2 |         3934 | 2019-04-22 00:00:00.000 | Matthew Duncan      |                    |             |            |
| AX14838    | ENX2025      | A119          | EMP1037           | C1463         | 2015-10-05 00:00:00.000 |          1 |          667 | 2018-10-05 00:00:00.000 | Christopher Nguyen  |                    |             |            |
| AX21981    | ENX2093      | A123          | EMP1037           | C1317         | 2015-07-20 00:00:00.000 |          1 |          112 | 2018-07-20 00:00:00.000 | Mark Morales        |                    |             |            |
| AX19383    | ENX2061      | A180          | EMP1001           | C1125         | 2016-05-13 00:00:00.000 |          1 |          913 | 2019-05-13 00:00:00.000 | Nicholas Williamson |                    |             |            |
| AX19147    | ENX2021      | A105          | EMP1028           | C1191         | 2015-03-26 00:00:00.000 |          1 |          217 | 2018-03-26 00:00:00.000 | Sean Vasquez        |                    |             |            |
| AX18266    | ENX2094      | A196          | EMP1009           | C1638         | 2016-04-13 00:00:00.000 |          2 |         1542 | 2019-04-13 00:00:00.000 | Jack Lynch          |                    |             |            |
| AX20023    | ENX2093      | A173          | EMP1037           | C1662         | 2015-11-27 00:00:00.000 |          2 |          224 | 2018-11-27 00:00:00.000 | Jose Ellis          |                    |             |            |
| AX22388    | ENX2074      | A126          | EMP1038           | C1644         | 2015-08-25 00:00:00.000 |          1 |          504 | 2018-08-25 00:00:00.000 | Terry Watson        |                    |             |            |
| AX23089    | ENX2065      | A125          | EMP1002           | C1232         | 2015-07-11 00:00:00.000 |          1 |         2396 | 2018-07-11 00:00:00.000 | Justin Butler       |                    |             |            |
| AX11496    | ENX2085      | A144          | EMP1032           | C1622         | 2015-08-30 00:00:00.000 |          1 |         1862 | 2018-08-30 00:00:00.000 | Joseph Warren       |                    |             |            |
| AX15912    | ENX2011      | A170          | EMP1005           | C1617         | 2017-02-24 00:00:00.000 |          1 |          530 | 2020-02-24 00:00:00.000 | Albert Rice         |                    |             |            |
| AX16013    | ENX2060      | A152          | EMP1016           | C1250         | 2016-05-08 00:00:00.000 |          3 |         4401 | 2019-05-08 00:00:00.000 | Christopher Ramos   |                    |             |            |
| AX23943    | ENX2079      | A103          | EMP1017           | C1584         | 2017-10-15 00:00:00.000 |          1 |         1725 | 2020-10-15 00:00:00.000 | Howard Harrison     |                    |             |            |
| AX22644    | ENX2091      | A182          | EMP1021           | C1492         | 2016-04-18 00:00:00.000 |          1 |          368 | 2019-04-18 00:00:00.000 | David Wilson        |                    |             |            |
| AX19054    | ENX2043      | A157          | EMP1012           | C1633         | 2016-08-22 00:00:00.000 |          1 |          545 | 2019-08-22 00:00:00.000 | Ryan Ruiz           |                    |             |            |
| AX19428    | ENX2017      | A126          | EMP1010           | C1512         | 2017-06-17 00:00:00.000 |          1 |           35 | 2020-06-17 00:00:00.000 | Shawn Ray           |                    |             |            |
| AX14442    | ENX2099      | A123          | EMP1014           | C1517         | 2015-03-08 00:00:00.000 |          3 |         4101 | 2018-03-08 00:00:00.000 | Eric Alvarez        |                    |             |            |
| AX11261    | ENX2077      | A125          | EMP1036           | C1274         | 2017-03-04 00:00:00.000 |          2 |         1060 | 2020-03-04 00:00:00.000 | Paul Henderson      |                    |             |            |
| AX17870    | ENX2036      | A151          | EMP1039           | C1400         | 2016-06-12 00:00:00.000 |          1 |         1582 | 2019-06-12 00:00:00.000 | Ralph Elliott       |                    |             |            |
| AX23715    | ENX2051      | A112          | EMP1035           | C1768         | 2015-07-29 00:00:00.000 |          1 |         1077 | 2018-07-29 00:00:00.000 | Stephen Greene      |                    |             |            |
| AX10169    | ENX2020      | A180          | EMP1018           | C1215         | 2017-09-17 00:00:00.000 |          1 |         2005 | 2020-09-17 00:00:00.000 | Jonathan Freeman    |                    |             |            |
| AX22115    | ENX2054      | A149          | EMP1009           | C1540         | 2017-08-02 00:00:00.000 |          3 |          381 | 2020-08-02 00:00:00.000 | Victor Hughes       |                    |             |            |
| AX12361    | ENX2044      | A141          | EMP1040           | C1014         | 2015-04-22 00:00:00.000 |          3 |         2658 | 2018-04-22 00:00:00.000 | Jason Duncan        |                    |             |            |
| AX15107    | ENX2002      | A162          | EMP1009           | C1179         | 2016-01-03 00:00:00.000 |          3 |         2541 | 2019-01-03 00:00:00.000 | Juan Scott          |                    |             |            |
| AX11250    | ENX2071      | A137          | EMP1003           | C1459         | 2017-07-28 00:00:00.000 |          1 |          136 | 2020-07-28 00:00:00.000 | Charles Sims        |                    |             |            |
| AX20655    | ENX2092      | A164          | EMP1031           | C1789         | 2015-10-12 00:00:00.000 |          1 |         1639 | 2018-10-12 00:00:00.000 | Steven Nichols      |                    |             |            |
| AX18635    | ENX2038      | A181          | EMP1005           | C1426         | 2016-01-07 00:00:00.000 |          4 |         1568 | 2019-01-07 00:00:00.000 | Steven Hayes        |                    |             |            |
| AX15771    | ENX2047      | A195          | EMP1025           | C1383         | 2017-04-22 00:00:00.000 |          1 |          290 | 2020-04-22 00:00:00.000 | Gary Jones          |                    |             |            |
| AX22232    | ENX2067      | A154          | EMP1036           | C1438         | 2017-04-05 00:00:00.000 |          3 |         3357 | 2020-04-05 00:00:00.000 | George Thompson     |                    |             |            |
| AX24507    | ENX2075      | A153          | EMP1019           | C1286         | 2017-07-16 00:00:00.000 |          1 |          400 | 2020-07-16 00:00:00.000 | Alan Sims           |                    |             |            |
| AX17939    | ENX2072      | A187          | EMP1031           | C1767         | 2015-12-15 00:00:00.000 |          2 |         3774 | 2018-12-15 00:00:00.000 | Donald Andrews      |                    |             |            |
| AX18238    | ENX2025      | A107          | EMP1027           | C1796         | 2017-12-09 00:00:00.000 |          1 |          667 | 2020-12-09 00:00:00.000 | Patrick Hall        |                    |             |            |
| AX22651    | ENX2066      | A142          | EMP1029           | C1289         | 2015-10-05 00:00:00.000 |          2 |         4182 | 2018-10-05 00:00:00.000 | Ronald Anderson     |                    |             |            |
| AX20784    | ENX2050      | A129          | EMP1000           | C1697         | 2016-08-24 00:00:00.000 |          4 |         9564 | 2019-08-24 00:00:00.000 | Justin Miller       |                    |             |            |
| AX22410    | ENX2077      | A177          | EMP1017           | C1738         | 2016-01-06 00:00:00.000 |          1 |          530 | 2019-01-06 00:00:00.000 | Shawn Owens         |                    |             |            |
| AX10625    | ENX2003      | A102          | EMP1035           | C1435         | 2015-01-10 00:00:00.000 |          2 |         3566 | 2018-01-10 00:00:00.000 | Kevin Campbell      |                    |             |            |
| AX10838    | ENX2100      | A132          | EMP1023           | C1229         | 2015-01-11 00:00:00.000 |          1 |          799 | 2018-01-11 00:00:00.000 | Larry Ray           |                    |             |            |
| AX16514    | ENX2098      | A150          | EMP1012           | C1408         | 2016-12-29 00:00:00.000 |          1 |         1178 | 2019-12-29 00:00:00.000 | Carl Reid           |                    |             |            |


````

### Model Response

```
```json
{
  "Functional-Dependency": [
    ["Order ID", "Product ID"],
    ["Order ID", "Location ID"],
    ["Order ID", "Sales Person ID"],
    ["Order ID", "Customer ID"],
    ["Order ID", "Purchase Date"],
    ["Order ID", "Quantity"],
    ["Order ID", "Line Sales"],
    ["Order ID", "Sales Date"],
    ["Order ID", "Customer Name"],
    ["Order ID", "Customer Address"]
  ]
}
```
```

### Correct Answer

```
{
  "Functional-Dependency": [
    [
      "Customer ID",
      "Customer Name"
    ]
  ]
}
```


---

## Question 2: case_221 (Auto-Relate)

**Dataset:** Auto-Relate  
**Test case:** case_221  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Opportunity Number   |   Fulfillment Practice | % Participation   |   Est. Revenue by Practice |   Est. Win %_many |   Wt. Revenue by Practice |   Daily Revenue | Primary Practice   | Est. Project Start Date (Org)   |   Est. Project Duration (Months) |   Est. Revenue |   Est. Win % |   Wt. Revenue | Est. Project End Date   |   Est. Project Duraction (Days) |
|:---------------------|-----------------------:|:------------------|---------------------------:|------------------:|--------------------------:|----------------:|:-------------------|:--------------------------------|---------------------------------:|---------------:|-------------:|--------------:|:------------------------|--------------------------------:|
| OP100-0893-00        |                      3 | 100.0             |                      50000 |                10 |                      5000 |         6.83995 | 3.0                | 2020-01-01 00:00:00.000         |                               24 |   50000        |         0.1  |        5000   | 2022-01-01 00:00:00.000 |                             731 |
| OP100-5652-00        |                      6 |                   |                          0 |                90 |                         0 |         0       | 4.0                | 2019-07-29 00:00:00.000         |                                1 |    1750        |         0.9  |        1575   | 2019-08-29 00:00:00.000 |                              31 |
| OP100-4408-00        |                      1 |                   |                          0 |                10 |                         0 |         0       | 7.0                | 2020-01-01 00:00:00.000         |                               12 |  100000        |         0.1  |       10000   | 2021-01-01 00:00:00.000 |                             366 |
| OP100-3158-00        |                      5 |                   |                          0 |                25 |                         0 |         0       | 6.0                | 2019-08-05 00:00:00.000         |                                2 |   15440        |         0.25 |        3860   | 2019-10-05 00:00:00.000 |                              61 |
| OP100-5577-00        |                      4 |                   |                          0 |                75 |                         0 |         0       | 2.0                | 2021-03-01 00:00:00.000         |                               14 |  212000        |         0.75 |      159000   | 2022-05-01 00:00:00.000 |                             426 |
| OP100-4359-00        |                      2 |                   |                          0 |                10 |                         0 |         0       | 6.0                | 2020-03-23 00:00:00.000         |                                8 |  494000        |         0.1  |       49400   | 2020-11-23 00:00:00.000 |                             245 |
| OP100-4350-00        |                      1 |                   |                          0 |                10 |                         0 |         0       | 7.0                | 2020-01-01 00:00:00.000         |                               24 |  200000        |         0.1  |       20000   | 2022-01-01 00:00:00.000 |                             731 |
| OP100-4217-00        |                      1 |                   |                          0 |                10 |                         0 |         0       | 6.0                | 2019-12-01 00:00:00.000         |                               12 |  520000        |         0.1  |       52000   | 2020-12-01 00:00:00.000 |                             366 |
| OP100-3434-00        |                      5 |                   |                          0 |                50 |                         0 |         0       | 4.0                | 2019-08-05 00:00:00.000         |                                6 |   50000        |         0.5  |       25000   | 2020-02-05 00:00:00.000 |                             184 |
| OP100-4052-00        |                      7 |                   |                          0 |                50 |                         0 |         0       | 2.0                | 2021-01-01 00:00:00.000         |                               12 |   97000        |         0.5  |       48500   | 2022-01-01 00:00:00.000 |                             365 |
| OP100-4247-00        |                      7 |                   |                          0 |                50 |                         0 |         0       | 4.0                | 2019-08-26 00:00:00.000         |                                6 |   50000        |         0.5  |       25000   | 2020-02-26 00:00:00.000 |                             184 |
| OP100-2173-00        |                      6 |                   |                          0 |                25 |                         0 |         0       | 2.0                | 2020-01-01 00:00:00.000         |                               18 |  500000        |         0.25 |      125000   | 2021-07-01 00:00:00.000 |                             547 |
| OP100-4346-00        |                      5 |                   |                          0 |                90 |                         0 |         0       | 7.0                | 2020-01-01 00:00:00.000         |                               12 |   50000        |         0.9  |       45000   | 2021-01-01 00:00:00.000 |                             366 |
| OP100-5133-00        |                      7 |                   |                          0 |                75 |                         0 |         0       |                    | 2019-07-29 00:00:00.000         |                               12 |   97025        |         0.75 |       72768.8 | 2020-07-29 00:00:00.000 |                             366 |
| OP100-5245-00        |                      1 |                   |                          0 |                50 |                         0 |         0       | 2.0                | 2019-09-30 00:00:00.000         |                               18 |    7500        |         0.5  |        3750   | 2021-03-30 00:00:00.000 |                             547 |
| OP100-5507-00        |                      4 | 100.0             |                      65000 |                50 |                     32500 |       178.571   | 4.0                | 2019-09-01 00:00:00.000         |                                6 |   65000        |         0.5  |       32500   | 2020-03-01 00:00:00.000 |                             182 |
| OP100-1787-00        |                      1 |                   |                          0 |                50 |                         0 |         0       | 7.0                | 2019-09-01 00:00:00.000         |                                9 |  750000        |         0.5  |      375000   | 2020-06-01 00:00:00.000 |                             274 |
| OP100-2788-00        |                      3 |                   |                          0 |                25 |                         0 |         0       | 7.0                | 2019-10-07 00:00:00.000         |                               12 |   45000        |         0.25 |       11250   | 2020-10-07 00:00:00.000 |                             366 |
| OP100-4651-00        |                      7 |                   |                          0 |                90 |                         0 |         0       | 3.0                | 2019-08-26 00:00:00.000         |                               24 |  204000        |         0.9  |      183600   | 2021-08-26 00:00:00.000 |                             731 |
| OP100-5172-00        |                      5 |                   |                          0 |                50 |                         0 |         0       | 4.0                | 2019-11-04 00:00:00.000         |                                7 |   32500        |         0.5  |       16250   | 2020-06-04 00:00:00.000 |                             213 |
| OP100-4657-00        |                      1 | 100.0             |                      41000 |                25 |                     10250 |       111.413   | 1.0                | 2019-10-01 00:00:00.000         |                                3 |   41000        |         0.25 |       10250   | 2020-01-01 00:00:00.000 |                              92 |
| OP100-4053-00        |                      1 |                   |                          0 |                25 |                         0 |         0       | 2.0                | 2022-01-01 00:00:00.000         |                               12 |  105000        |         0.25 |       26250   | 2023-01-01 00:00:00.000 |                             365 |
| OP100-3073-00        |                      6 |                   |                          0 |                25 |                         0 |         0       | 2.0                | 2020-03-31 00:00:00.000         |                                3 |    5000        |         0.25 |        1250   | 2020-06-30 00:00:00.000 |                              91 |
| OP100-4917-00        |                      2 |                   |                          0 |                10 |                         0 |         0       | 3.0                | 2019-10-20 00:00:00.000         |                                6 |   40000        |         0.1  |        4000   | 2020-04-20 00:00:00.000 |                             183 |
| OP100-0499-00        |                      5 | 15.0              |                      16350 |                10 |                      1635 |         4.47945 | 3.0                | 2020-03-06 00:00:00.000         |                               12 |  109000        |         0.1  |       10900   | 2021-03-06 00:00:00.000 |                             365 |
| OP100-3988-00        |                      1 |                   |                          0 |                50 |                         0 |         0       | 3.0                | 2022-01-15 00:00:00.000         |                               15 |   90000        |         0.5  |       45000   | 2023-04-15 00:00:00.000 |                             455 |
| OP100-0888-00        |                      4 |                   |                          0 |                10 |                         0 |         0       | 3.0                | 2020-01-01 00:00:00.000         |                                6 |    5000        |         0.1  |         500   | 2020-07-01 00:00:00.000 |                             182 |
| OP100-4790-00        |                      1 | 100.0             |                     150000 |                10 |                     15000 |        40.9836  | 1.0                | 2019-10-15 00:00:00.000         |                               12 |  150000        |         0.1  |       15000   | 2020-10-15 00:00:00.000 |                             366 |
| OP100-5652-00        |                      7 |                   |                          0 |                90 |                         0 |         0       | 4.0                | 2019-07-29 00:00:00.000         |                                1 |    1750        |         0.9  |        1575   | 2019-08-29 00:00:00.000 |                              31 |
| OP100-5612-00        |                      5 |                   |                          0 |                90 |                         0 |         0       | 4.0                | 2019-08-19 00:00:00.000         |                                2 |   15000        |         0.9  |       13500   | 2019-10-19 00:00:00.000 |                              61 |
| OP100-5580-00        |                      2 | 100.0             |                     351000 |                75 |                    263250 |       721.233   | 2.0                | 2020-09-01 00:00:00.000         |                               12 |  351000        |         0.75 |      263250   | 2021-09-01 00:00:00.000 |                             365 |
| OP100-2892-00        |                      4 |                   |                          0 |                25 |                         0 |         0       | 3.0                | 2020-08-01 00:00:00.000         |                               18 |  234000        |         0.25 |       58500   | 2022-02-01 00:00:00.000 |                             549 |
| OP100-5575-00        |                      7 |                   |                          0 |                25 |                         0 |         0       | 1.0                | 2019-09-03 00:00:00.000         |                                3 |   17500        |         0.25 |        4375   | 2019-12-03 00:00:00.000 |                              91 |
| OP100-5387-00        |                      5 | 100.0             |                      11000 |                50 |                      5500 |        90.1639  | 5.0                | 2019-06-20 00:00:00.000         |                                2 |   11000        |         0.5  |        5500   | 2019-08-20 00:00:00.000 |                              61 |
| OP100-0470-00        |                      7 |                   |                          0 |                50 |                         0 |         0       | 3.0                | 2020-01-10 00:00:00.000         |                               12 |  250000        |         0.5  |      125000   | 2021-01-10 00:00:00.000 |                             366 |
| OP100-2840-00        |                      1 |                   |                          0 |                10 |                         0 |         0       | 7.0                | 2020-04-01 00:00:00.000         |                               24 |  405000        |         0.1  |       40500   | 2022-04-01 00:00:00.000 |                             730 |
| OP100-0893-00        |                      2 |                   |                          0 |                10 |                         0 |         0       | 3.0                | 2020-01-01 00:00:00.000         |                               24 |   50000        |         0.1  |        5000   | 2022-01-01 00:00:00.000 |                             731 |
| OP100-5623-00        |                      5 |                   |                          0 |                90 |                         0 |         0       | 6.0                | 2019-08-19 00:00:00.000         |                               12 |  200000        |         0.9  |      180000   | 2020-08-19 00:00:00.000 |                             366 |
| OP100-4801-00        |                      4 |                   |                          0 |                10 |                         0 |         0       | 3.0                | 2019-11-01 00:00:00.000         |                               24 |   20000        |         0.1  |        2000   | 2021-11-01 00:00:00.000 |                             731 |
| OP100-5245-00        |                      4 |                   |                          0 |                50 |                         0 |         0       | 2.0                | 2019-09-30 00:00:00.000         |                               18 |    7500        |         0.5  |        3750   | 2021-03-30 00:00:00.000 |                             547 |
| OP100-3986-00        |                      3 | 0.0               |                          0 |                50 |                         0 |         0       | 3.0                | 2019-10-04 00:00:00.000         |                               15 |  235000        |         0.5  |      117500   | 2021-01-04 00:00:00.000 |                             458 |
| OP100-4687-00        |                      1 |                   |                          0 |                50 |                         0 |         0       | 7.0                | 2022-06-01 00:00:00.000         |                               12 |   90000        |         0.5  |       45000   | 2023-06-01 00:00:00.000 |                             365 |
| OP100-0956-00        |                      5 |                   |                          0 |                75 |                         0 |         0       | 7.0                | 2022-10-07 00:00:00.000         |                               24 |       1.05e+06 |         0.75 |      787500   | 2024-10-07 00:00:00.000 |                             731 |
| OP100-1597-00        |                      4 | 100.0             |                      20000 |                50 |                     10000 |        54.9451  | 4.0                | 2020-01-02 00:00:00.000         |                                6 |   20000        |         0.5  |       10000   | 2020-07-02 00:00:00.000 |                             182 |
| OP100-5387-00        |                      2 |                   |                          0 |                50 |                         0 |         0       | 5.0                | 2019-06-20 00:00:00.000         |                                2 |   11000        |         0.5  |        5500   | 2019-08-20 00:00:00.000 |                              61 |
| OP100-5154-00        |                      3 |                   |                          0 |                50 |                         0 |         0       | 2.0                | 2019-09-09 00:00:00.000         |                                8 |  591000        |         0.5  |      295500   | 2020-05-09 00:00:00.000 |                             243 |
| OP100-5211-00        |                      5 |                   |                          0 |                10 |                         0 |         0       | 7.0                | 2020-01-27 00:00:00.000         |                               24 |  250000        |         0.1  |       25000   | 2022-01-27 00:00:00.000 |                             731 |
| OP100-3369-00        |                      6 |                   |                          0 |                90 |                         0 |         0       | 7.0                | 2019-07-01 00:00:00.000         |                                2 |    3000        |         0.9  |        2700   | 2019-09-01 00:00:00.000 |                              62 |
| OP100-2642-00        |                      2 |                   |                          0 |                90 |                         0 |         0       | 3.0                | 2019-09-11 00:00:00.000         |                               12 |   65000        |         0.9  |       58500   | 2020-09-11 00:00:00.000 |                             366 |
| OP100-4417-00        |                      4 | 32.0              |                      54400 |                50 |                     27200 |        63.7002  | 4.0                | 2019-09-01 00:00:00.000         |                               14 |  170000        |         0.5  |       85000   | 2020-11-01 00:00:00.000 |                             427 |


````

### Model Response

```
```json
{
  "Functional-Dependency": [
    ["Opportunity Number", "Fulfillment Practice"],
    ["Opportunity Number", "% Participation"],
    ["Opportunity Number", "Est. Revenue by Practice"],
    ["Opportunity Number", "Est. Win %_many"],
    ["Opportunity Number", "Wt. Revenue by Practice"],
    ["Opportunity Number", "Daily Revenue"],
    ["Opportunity Number", "Primary Practice"],
    ["Opportunity Number", "Est. Project Start Date (Org)"],
    ["Opportunity Number", "Est. Project Duration (Months)"],
    ["Opportunity Number", "Est. Revenue"],
    ["Opportunity Number", "Est. Win %"],
    ["Opportunity Number", "Wt. Revenue"],
    ["Opportunity Number", "Est. Project End Date"],
    ["Opportunity Number", "Est. Project Duraction (Days)"]
  ]
}
```
```

### Correct Answer

```
{
  "Functional-Dependency": [
    [
      "Opportunity Number",
      "Primary Practice"
    ],
    [
      "Opportunity Number",
      "Est. Project Start Date (Org)"
    ],
    [
      "Opportunity Number",
      "Est. Project Duration (Months)"
    ],
    [
      "Opportunity Number",
      "Est. Revenue"
    ],
    [
      "Opportunity Number",
      "Est. Win %"
    ],
    [
      "Opportunity Number",
      "Wt. Revenue"
    ],
    [
      "Opportunity Number",
      "Est. Project End Date"
    ],
    [
      "Opportunity Number",
      "Est. Project Duraction (Days)"
    ]
  ]
}
```


---

## Question 3: case_33 (Auto-Relate)

**Dataset:** Auto-Relate  
**Test case:** case_33  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Date                    | StockName   |      open |      high |       low |     close |   volume |      Returns |   Year |   MonthNr |   Day | Month     | Month short   |   DayInWeek | DayOfWeekName   | WeekStart               | WeekEnding              |   WeekofYear |   YearMonth |
|:------------------------|:------------|----------:|----------:|----------:|----------:|---------:|-------------:|-------:|----------:|------:|:----------|:--------------|------------:|:----------------|:------------------------|:------------------------|-------------:|------------:|
| 2019-01-24 00:00:00.000 | Amazon      | 1641.07   | 1657.26   | 1631.78   | 1654.93   |  4089943 |  0.00909135  |   2019 |         1 |    24 | January   | Jan           |           4 | Thursday        | 2019-01-21 00:00:00.000 | 2019-01-27 00:00:00.000 |            4 |      201901 |
| 2019-02-06 00:00:00.000 | Apple       |  173.237  |  174.149  |  171.455  |  172.83   | 28239591 |  0.000344387 |   2019 |         2 |     6 | February  | Feb           |           3 | Wednesday       | 2019-02-04 00:00:00.000 | 2019-02-10 00:00:00.000 |            6 |      201902 |
| 2018-03-26 00:00:00.000 | Microsoft   |   88.7773 |   92.0987 |   88.5715 |   91.8832 | 56396780 |  0.0757053   |   2018 |         3 |    26 | March     | Mar           |           1 | Monday          | 2018-03-26 00:00:00.000 | 2018-04-01 00:00:00.000 |           13 |      201803 |
| 2019-01-07 00:00:00.000 | Amazon      | 1602.31   | 1634.56   | 1589.18   | 1629.51   |  7993213 |  0.0343534   |   2019 |         1 |     7 | January   | Jan           |           1 | Monday          | 2019-01-07 00:00:00.000 | 2019-01-13 00:00:00.000 |            2 |      201901 |
| 2018-08-27 00:00:00.000 | Microsoft   |  107.938  |  108.303  |  107.187  |  108.264  | 19662331 |  0.0110695   |   2018 |         8 |    27 | August    | Aug           |           1 | Monday          | 2018-08-27 00:00:00.000 | 2018-09-02 00:00:00.000 |           35 |      201808 |
| 2018-10-03 00:00:00.000 | Facebook    |  160      |  163.66   |  159.53   |  162.43   | 23109456 |  0.0194565   |   2018 |        10 |     3 | October   | Oct           |           3 | Wednesday       | 2018-10-01 00:00:00.000 | 2018-10-07 00:00:00.000 |           40 |      201810 |
| 2018-02-05 00:00:00.000 | Facebook    |  186.93   |  190.61   |  180.61   |  181.26   | 33128206 | -0.0474038   |   2018 |         2 |     5 | February  | Feb           |           1 | Monday          | 2018-02-05 00:00:00.000 | 2018-02-11 00:00:00.000 |            6 |      201802 |
| 2019-05-16 00:00:00.000 | Apple       |  189.91   |  192.469  |  188.84   |  190.08   | 33031364 | -0.00439975  |   2019 |         5 |    16 | May       | May           |           4 | Thursday        | 2019-05-13 00:00:00.000 | 2019-05-19 00:00:00.000 |           20 |      201905 |
| 2019-05-14 00:00:00.000 | Amazon      | 1839.5    | 1852.44   | 1815.75   | 1840.12   |  4629107 |  0.00956833  |   2019 |         5 |    14 | May       | May           |           2 | Tuesday         | 2019-05-13 00:00:00.000 | 2019-05-19 00:00:00.000 |           20 |      201905 |
| 2018-03-02 00:00:00.000 | Google      | 1053.08   | 1082      | 1048.12   | 1078.92   |  2271551 |  0.00878899  |   2018 |         3 |     2 | March     | Mar           |           5 | Friday          | 2018-02-26 00:00:00.000 | 2018-03-04 00:00:00.000 |            9 |      201803 |
| 2018-09-24 00:00:00.000 | Facebook    |  161.03   |  165.7    |  160.88   |  165.41   | 19222775 |  0.0152213   |   2018 |         9 |    24 | September | Sep           |           1 | Monday          | 2018-09-24 00:00:00.000 | 2018-09-30 00:00:00.000 |           39 |      201809 |
| 2019-02-06 00:00:00.000 | Microsoft   |  106.152  |  106.152  |  104.694  |  105.19   | 20609759 | -0.011098    |   2019 |         2 |     6 | February  | Feb           |           3 | Wednesday       | 2019-02-04 00:00:00.000 | 2019-02-10 00:00:00.000 |            6 |      201902 |
| 2018-06-11 00:00:00.000 | Facebook    |  188.81   |  192.6    |  188.8    |  191.54   | 12928907 |  0.0129032   |   2018 |         6 |    11 | June      | Jun           |           1 | Monday          | 2018-06-11 00:00:00.000 | 2018-06-17 00:00:00.000 |           24 |      201806 |
| 2018-11-16 00:00:00.000 | Facebook    |  141.07   |  141.77   |  137.77   |  139.53   | 37250560 | -0.0300313   |   2018 |        11 |    16 | November  | Nov           |           5 | Friday          | 2018-11-12 00:00:00.000 | 2018-11-18 00:00:00.000 |           46 |      201811 |
| 2018-07-06 00:00:00.000 | Google      | 1123.58   | 1140.93   | 1120.74   | 1140.17   |   996079 |  0.0141425   |   2018 |         7 |     6 | July      | Jul           |           5 | Friday          | 2018-07-02 00:00:00.000 | 2018-07-08 00:00:00.000 |           27 |      201807 |
| 2019-04-16 00:00:00.000 | Facebook    |  179      |  180.17   |  178.3    |  178.87   | 11215193 | -0.00434178  |   2019 |         4 |    16 | April     | Apr           |           2 | Tuesday         | 2019-04-15 00:00:00.000 | 2019-04-21 00:00:00.000 |           16 |      201904 |
| 2018-01-30 00:00:00.000 | Amazon      | 1403.17   | 1439.25   | 1392      | 1437.82   |  5871942 |  0.0142063   |   2018 |         1 |    30 | January   | Jan           |           2 | Tuesday         | 2018-01-29 00:00:00.000 | 2018-02-04 00:00:00.000 |            5 |      201801 |
| 2019-03-11 00:00:00.000 | Facebook    |  171.6    |  174.3    |  171.58   |  172.07   | 18883983 |  0.0145637   |   2019 |         3 |    11 | March     | Mar           |           1 | Monday          | 2019-03-11 00:00:00.000 | 2019-03-17 00:00:00.000 |           11 |      201903 |
| 2018-03-16 00:00:00.000 | Amazon      | 1583.45   | 1589.44   | 1567.5    | 1571.68   |  5425012 | -0.0067243   |   2018 |         3 |    16 | March     | Mar           |           5 | Friday          | 2018-03-12 00:00:00.000 | 2018-03-18 00:00:00.000 |           11 |      201803 |
| 2018-04-06 00:00:00.000 | Apple       |  167.76   |  169.241  |  165.042  |  165.218  | 35005290 | -0.0255787   |   2018 |         4 |     6 | April     | Apr           |           5 | Friday          | 2018-04-02 00:00:00.000 | 2018-04-08 00:00:00.000 |           14 |      201804 |
| 2018-11-07 00:00:00.000 | Amazon      | 1673      | 1759.23   | 1664.08   | 1755.49   |  8192234 |  0.0685898   |   2018 |        11 |     7 | November  | Nov           |           3 | Wednesday       | 2018-11-05 00:00:00.000 | 2018-11-11 00:00:00.000 |           45 |      201811 |
| 2018-07-12 00:00:00.000 | Microsoft   |  101.128  |  102.742  |  101.088  |  102.525  | 24335929 |  0.0216711   |   2018 |         7 |    12 | July      | Jul           |           4 | Thursday        | 2018-07-09 00:00:00.000 | 2018-07-15 00:00:00.000 |           28 |      201807 |
| 2018-08-15 00:00:00.000 | Amazon      | 1909.55   | 1916.21   | 1869.79   | 1882.62   |  7700682 | -0.01929     |   2018 |         8 |    15 | August    | Aug           |           3 | Wednesday       | 2018-08-13 00:00:00.000 | 2018-08-19 00:00:00.000 |           33 |      201808 |
| 2019-02-04 00:00:00.000 | Google      | 1112.66   | 1132.8    | 1109.02   | 1132.8    |  2576470 |  0.0198515   |   2019 |         2 |     4 | February  | Feb           |           1 | Monday          | 2019-02-04 00:00:00.000 | 2019-02-10 00:00:00.000 |            6 |      201902 |
| 2018-07-30 00:00:00.000 | Facebook    |  175.3    |  175.3    |  166.56   |  171.06   | 65280787 | -0.0218995   |   2018 |         7 |    30 | July      | Jul           |           1 | Monday          | 2018-07-30 00:00:00.000 | 2018-08-05 00:00:00.000 |           31 |      201807 |
| 2018-06-19 00:00:00.000 | Amazon      | 1709.04   | 1736.11   | 1700.39   | 1734.78   |  4290117 |  0.00637549  |   2018 |         6 |    19 | June      | Jun           |           2 | Tuesday         | 2018-06-18 00:00:00.000 | 2018-06-24 00:00:00.000 |           25 |      201806 |
| 2018-04-13 00:00:00.000 | Apple       |  171.498  |  172.538  |  170.585  |  171.449  | 25124255 |  0.00338795  |   2018 |         4 |    13 | April     | Apr           |           5 | Friday          | 2018-04-09 00:00:00.000 | 2018-04-15 00:00:00.000 |           15 |      201804 |
| 2018-10-15 00:00:00.000 | Microsoft   |  107.582  |  108.145  |  105.643  |  106.288  | 32068103 | -0.0179795   |   2018 |        10 |    15 | October   | Oct           |           1 | Monday          | 2018-10-15 00:00:00.000 | 2018-10-21 00:00:00.000 |           42 |      201810 |
| 2019-05-28 00:00:00.000 | Microsoft   |  126.98   |  128      |  126.05   |  126.16   | 23128359 | -0.000633714 |   2019 |         5 |    28 | May       | May           |           2 | Tuesday         | 2019-05-27 00:00:00.000 | 2019-06-02 00:00:00.000 |           22 |      201905 |
| 2018-11-08 00:00:00.000 | Google      | 1091.38   | 1093.27   | 1072.2    | 1082.4    |  1488182 | -0.0100513   |   2018 |        11 |     8 | November  | Nov           |           4 | Thursday        | 2018-11-05 00:00:00.000 | 2018-11-11 00:00:00.000 |           45 |      201811 |
| 2018-09-10 00:00:00.000 | Microsoft   |  107.513  |  108.303  |  107.039  |  108.046  | 20727906 |  0.010812    |   2018 |         9 |    10 | September | Sep           |           1 | Monday          | 2018-09-10 00:00:00.000 | 2018-09-16 00:00:00.000 |           37 |      201809 |
| 2018-07-09 00:00:00.000 | Google      | 1148.48   | 1154.67   | 1143.42   | 1154.05   |   908969 |  0.0121736   |   2018 |         7 |     9 | July      | Jul           |           1 | Monday          | 2018-07-09 00:00:00.000 | 2018-07-15 00:00:00.000 |           28 |      201807 |
| 2018-05-24 00:00:00.000 | Microsoft   |   97.1474 |   97.359  |   95.263  |   96.7391 | 26649287 | -0.00354746  |   2018 |         5 |    24 | May       | May           |           4 | Thursday        | 2018-05-21 00:00:00.000 | 2018-05-27 00:00:00.000 |           21 |      201805 |
| 2018-08-29 00:00:00.000 | Facebook    |  176.295  |  176.79   |  174.75   |  175.9    | 18678301 | -0.00204244  |   2018 |         8 |    29 | August    | Aug           |           3 | Wednesday       | 2018-08-27 00:00:00.000 | 2018-09-02 00:00:00.000 |           35 |      201808 |
| 2018-11-29 00:00:00.000 | Microsoft   |  109.456  |  110.234  |  108.166  |  109.317  | 28123195 | -0.00836907  |   2018 |        11 |    29 | November  | Nov           |           4 | Thursday        | 2018-11-26 00:00:00.000 | 2018-12-02 00:00:00.000 |           48 |      201811 |
| 2018-06-08 00:00:00.000 | Apple       |  188.304  |  189.121  |  186.925  |  188.826  | 26656799 | -0.00909744  |   2018 |         6 |     8 | June      | Jun           |           5 | Friday          | 2018-06-04 00:00:00.000 | 2018-06-10 00:00:00.000 |           23 |      201806 |
| 2018-12-11 00:00:00.000 | Apple       |  170.271  |  170.4    |  165.649  |  167.266  | 47281665 | -0.00571903  |   2018 |        12 |    11 | December  | Dec           |           2 | Tuesday         | 2018-12-10 00:00:00.000 | 2018-12-16 00:00:00.000 |           50 |      201812 |
| 2018-02-13 00:00:00.000 | Apple       |  158.909  |  161.656  |  158.615  |  161.254  | 32549163 |  0.0100179   |   2018 |         2 |    13 | February  | Feb           |           2 | Tuesday         | 2018-02-12 00:00:00.000 | 2018-02-18 00:00:00.000 |            7 |      201802 |
| 2018-08-21 00:00:00.000 | Microsoft   |  105.616  |  106.041  |  104.559  |  104.688  | 22881861 | -0.00832741  |   2018 |         8 |    21 | August    | Aug           |           2 | Tuesday         | 2018-08-20 00:00:00.000 | 2018-08-26 00:00:00.000 |           34 |      201808 |
| 2018-04-11 00:00:00.000 | Microsoft   |   90.149  |   91.4031 |   89.6297 |   90.002  | 24872110 | -0.0109822   |   2018 |         4 |    11 | April     | Apr           |           3 | Wednesday       | 2018-04-09 00:00:00.000 | 2018-04-15 00:00:00.000 |           15 |      201804 |
| 2018-12-04 00:00:00.000 | Amazon      | 1756      | 1770.34   | 1665      | 1668.4    |  8694455 | -0.0586563   |   2018 |        12 |     4 | December  | Dec           |           2 | Tuesday         | 2018-12-03 00:00:00.000 | 2018-12-09 00:00:00.000 |           49 |      201812 |
| 2018-04-16 00:00:00.000 | Microsoft   |   92.1673 |   92.7454 |   91.5304 |   92.2653 | 20288083 |  0.0117109   |   2018 |         4 |    16 | April     | Apr           |           1 | Monday          | 2018-04-16 00:00:00.000 | 2018-04-22 00:00:00.000 |           16 |      201804 |
| 2018-11-05 00:00:00.000 | Microsoft   |  105.073  |  106.426  |  104.609  |  106.199  | 27922144 |  0.0127163   |   2018 |        11 |     5 | November  | Nov           |           1 | Monday          | 2018-11-05 00:00:00.000 | 2018-11-11 00:00:00.000 |           45 |      201811 |
| 2019-04-05 00:00:00.000 | Apple       |  195.696  |  196.344  |  195.178  |  196.244  | 18526644 |  0.00669439  |   2019 |         4 |     5 | April     | Apr           |           5 | Friday          | 2019-04-01 00:00:00.000 | 2019-04-07 00:00:00.000 |           14 |      201904 |
| 2019-03-11 00:00:00.000 | Apple       |  174.817  |  178.433  |  174.677  |  178.214  | 32011034 |  0.0346422   |   2019 |         3 |    11 | March     | Mar           |           1 | Monday          | 2019-03-11 00:00:00.000 | 2019-03-17 00:00:00.000 |           11 |      201903 |
| 2018-06-18 00:00:00.000 | Apple       |  185.063  |  186.383  |  184.393  |  185.91   | 18484865 | -0.000529546 |   2018 |         6 |    18 | June      | Jun           |           1 | Monday          | 2018-06-18 00:00:00.000 | 2018-06-24 00:00:00.000 |           25 |      201806 |
| 2018-07-02 00:00:00.000 | Facebook    |  193.37   |  197.45   |  192.22   |  197.36   | 13961578 |  0.0156443   |   2018 |         7 |     2 | July      | Jul           |           1 | Monday          | 2018-07-02 00:00:00.000 | 2018-07-08 00:00:00.000 |           27 |      201807 |
| 2019-04-12 00:00:00.000 | Amazon      | 1848.4    | 1851.5    | 1841.3    | 1843.06   |  3114413 | -0.000547702 |   2019 |         4 |    12 | April     | Apr           |           5 | Friday          | 2019-04-08 00:00:00.000 | 2019-04-14 00:00:00.000 |           15 |      201904 |
| 2018-02-09 00:00:00.000 | Facebook    |  174.76   |  176.9    |  167.18   |  176.11   | 39887626 |  0.0264017   |   2018 |         2 |     9 | February  | Feb           |           5 | Friday          | 2018-02-05 00:00:00.000 | 2018-02-11 00:00:00.000 |            6 |      201802 |
| 2018-07-31 00:00:00.000 | Google      | 1220.01   | 1227.59   | 1205.6    | 1217.26   |  1644722 | -0.00203322  |   2018 |         7 |    31 | July      | Jul           |           2 | Tuesday         | 2018-07-30 00:00:00.000 | 2018-08-05 00:00:00.000 |           31 |      201807 |


````

### Model Response

```
```json
{
  "Functional-Dependency": [
    ["Date", "StockName"],
    ["Date", "open"],
    ["Date", "high"],
    ["Date", "low"],
    ["Date", "close"],
    ["Date", "volume"],
    ["Date", "Returns"],
    ["Date", "Year"],
    ["Date", "MonthNr"],
    ["Date", "Day"],
    ["Date", "Month"],
    ["Date", "Month short"],
    ["Date", "DayInWeek"],
    ["Date", "DayOfWeekName"],
    ["Date", "WeekStart"],
    ["Date", "WeekEnding"],
    ["Date", "WeekofYear"],
    ["Date", "YearMonth"],
    ["StockName", "Year"],
    ["StockName", "MonthNr"],
    ["StockName", "Day"],
    ["StockName", "Month"],
    ["StockName", "Month short"],
    ["StockName", "DayInWeek"],
    ["StockName", "DayOfWeekName"],
    ["StockName", "WeekStart"],
    ["StockName", "WeekEnding"],
    ["StockName", "WeekofYear"],
    ["StockName", "YearMonth"]
  ]
}
```
```

### Correct Answer

```
{
  "Functional-Dependency": [
    [
      "Date",
      "Year"
    ],
    [
      "Date",
      "MonthNr"
    ],
    [
      "Date",
      "Day"
    ],
    [
      "Date",
      "Month"
    ],
    [
      "Date",
      "Month short"
    ],
    [
      "Date",
      "DayInWeek"
    ],
    [
      "Date",
      "DayOfWeekName"
    ],
    [
      "Date",
      "WeekStart"
    ],
    [
      "Date",
      "WeekEnding"
    ],
    [
      "Date",
      "WeekofYear"
    ],
    [
      "Date",
      "YearMonth"
    ]
  ]
}
```


---

## Question 4: case_136 (Auto-Relate)

**Dataset:** Auto-Relate  
**Test case:** case_136  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| CountryRegion   | Brand                | Month     | Sale 2013   | Sale 2014   | Sale 2015   |   Budget |       x1 |       x2 |        x3 |
|:----------------|:---------------------|:----------|:------------|:------------|:------------|---------:|---------:|---------:|----------:|
| G               | Southridge Video     | October   | 5296.42     | 396.0       | 124.32      | 1375     | 20646.3  |  4599.41 |  19124.3  |
| G               | Fabrikam             | February  | 3573.93     |             | 3249.0      | 3750     | 90969.2  | 27137    | 128885    |
| C               | Wide World Importers | March     |             | 3127.7      | 3012.0      | 3750     | 48359.7  | 59935.2  |  65355.5  |
| United States   | Contoso              | September | 6232.99     | 3786.22     | 10863.67    | 7916.67  | 84152    | 40952    |  78616.9  |
| G               | A. Datum             | July      | 8778        | 1800.0      |             | 1125     | 21397    | 18774.8  |   8869.4  |
| United States   | Tailspin Toys        | July      | 258         | 280.52      | 792.87      |  708.333 |  2811.78 |  2772.85 |   3140.53 |
| C               | Proseware            | May       |             | 1749.0      |             | 1666.67  | 29281.5  | 26190.1  |  41645.8  |
| United States   | Fabrikam             | December  | 11872       |             |             | 2916.67  | 90969.2  | 27137    | 128885    |
| United States   | The Phone Company    | July      |             | 2680.0      | 1602.0      | 2083.33  | 29733    | 13890    |  21834    |
| G               | Contoso              | January   | 8172.92     | 93.78       | 6800.52     | 4166.67  | 84152    | 40952    |  78616.9  |
| United States   | Southridge Video     | May       | 4897.73     | 4841.85     | 1838.5      | 1875     | 20646.3  |  4599.41 |  19124.3  |
| United States   | Northwind Traders    | March     | 154.14      |             |             | 1250     | 13092    |   341.55 |  11201.1  |
| C               | Proseware            | August    | 1399.93     |             | 1831.5      | 1666.67  | 29281.5  | 26190.1  |  41645.8  |
| G               | Tailspin Toys        | June      |             |             | 608.0       | 1041.67  |  2811.78 |  2772.85 |   3140.53 |
| United States   | Contoso              | November  | 8218.2      | 15254.44    |             | 7916.67  | 84152    | 40952    |  78616.9  |
| C               | Fabrikam             | June      | 2820        | 28407.99    | 6223.31     | 7566.67  | 90969.2  | 27137    | 128885    |
| C               | A. Datum             | January   | ，          |             | 1935.0      |  416.667 | 21397    | 18774.8  |   8869.4  |
| United States   | Proseware            | September | 21903       | 9739.84     | 2219.0      | 2916.67  | 29281.5  | 26190.1  |  41645.8  |
| United States   | Southridge Video     | September | 1395.9      | 4718.87     | 10774.9     | 1875     | 20646.3  |  4599.41 |  19124.3  |
| G               | Contoso              | September | 13894.28    | 9406.25     | 5011.4      | 4166.67  | 84152    | 40952    |  78616.9  |
| C               | Tailspin Toys        | August    | 272.89      |             |             |  666.667 |  2811.78 |  2772.85 |   3140.53 |
| C               | Southridge Video     | November  | 1439.64     |             |             | 1875     | 20646.3  |  4599.41 |  19124.3  |
| C               | Adventure Works      | July      | 9938.12     | 2819.82     |             | 3041.67  | 56990.4  | 18042.7  |  29649.6  |
| G               | The Phone Company    | June      |             | 1400.0      |             | 2083.33  | 29733    | 13890    |  21834    |
| C               | Fabrikam             | January   | 5794.38     | 9244.97     |             | 7566.67  | 90969.2  | 27137    | 128885    |
| G               | A. Datum             | May       | 10520.5     | 3325.5      |             | 1125     | 21397    | 18774.8  |   8869.4  |
| United States   | Wide World Importers | February  | 2299        | 10971.9     |             | 4166.67  | 48359.7  | 59935.2  |  65355.5  |
| G               | Adventure Works      | May       | 3289.79     | 2583.0      | 7461.79     | 1250     | 56990.4  | 18042.7  |  29649.6  |
| C               | A. Datum             | February  | 6270        | 7059.0      |             |  416.667 | 21397    | 18774.8  |   8869.4  |
| G               | Contoso              | June      | 2743.85     | 373.52      | 3598.86     | 4166.67  | 84152    | 40952    |  78616.9  |
| United States   | Adventure Works      | November  | 4699.7      |             |             | 1300     | 56990.4  | 18042.7  |  29649.6  |
| C               | Northwind Traders    | January   | 34616.15    | 359.66      |             | 1000     | 13092    |   341.55 |  11201.1  |
| United States   | Contoso              | May       | 7133.14     | 921.35      | 7049.65     | 7916.67  | 84152    | 40952    |  78616.9  |
| G               | Northwind Traders    | February  | 5508.08     |             |             | 5416.67  | 13092    |   341.55 |  11201.1  |
| United States   | Tailspin Toys        | October   | 834.91      |             |             |  708.333 |  2811.78 |  2772.85 |   3140.53 |
| United States   | Tailspin Toys        | February  |             |             | 499.86      |  708.333 |  2811.78 |  2772.85 |   3140.53 |
| C               | Litware              | May       |             | 11186.0     | 2087.73     | 5416.67  | 74853.2  | 31861.8  | 122433    |
| C               | The Phone Company    | February  | 2408        |             |             | 2500     | 29733    | 13890    |  21834    |
| United States   | Proseware            | February  |             |             | 3669.97     | 2916.67  | 29281.5  | 26190.1  |  41645.8  |
| G               | The Phone Company    | July      |             |             | 2152.0      | 2083.33  | 29733    | 13890    |  21834    |
| G               | Northwind Traders    | December  | 18570.3     |             |             | 5416.67  | 13092    |   341.55 |  11201.1  |
| United States   | Fabrikam             | November  | 3038        | 17404.6     |             | 2916.67  | 90969.2  | 27137    | 128885    |
| United States   | Litware              | November  | 19229.82    | 9065.85     |             | 5416.67  | 74853.2  | 31861.8  | 122433    |
| C               | Adventure Works      | March     | 3689.85     | 5489.23     | 11163.94    | 3041.67  | 56990.4  | 18042.7  |  29649.6  |
| United States   | Tailspin Toys        | December  | 927.56      | 56.0        |             |  708.333 |  2811.78 |  2772.85 |   3140.53 |
| C               | Litware              | April     | 599.9       |             |             | 5416.67  | 74853.2  | 31861.8  | 122433    |
| C               | Proseware            | January   |             | 735.0       |             | 1666.67  | 29281.5  | 26190.1  |  41645.8  |
| G               | Northwind Traders    | January   | 77.07       |             |             | 5416.67  | 13092    |   341.55 |  11201.1  |
| G               | Tailspin Toys        | December  | 301         | 161.0       |             | 1041.67  |  2811.78 |  2772.85 |   3140.53 |
| G               | A. Datum             | September | 3762        | 3072.3      |             | 1125     | 21397    | 18774.8  |   8869.4  |


````

### Model Response

```
```json
{
  "Functional-Dependency": [
    ["CountryRegion", "Brand"],
    ["CountryRegion", "Month"],
    ["CountryRegion", "Sale 2013"],
    ["CountryRegion", "Sale 2014"],
    ["CountryRegion", "Sale 2015"],
    ["CountryRegion", "Budget"],
    ["CountryRegion", "x1"],
    ["CountryRegion", "x2"],
    ["CountryRegion", "x3"],
    ["Brand", "Month"],
    ["Brand", "Sale 2013"],
    ["Brand", "Sale 2014"],
    ["Brand", "Sale 2015"],
    ["Brand", "Budget"],
    ["Brand", "x1"],
    ["Brand", "x2"],
    ["Brand", "x3"]
  ]
}
```
```

### Correct Answer

```
{
  "Functional-Dependency": [
    [
      "Brand",
      "x1"
    ],
    [
      "Brand",
      "x2"
    ],
    [
      "Brand",
      "x3"
    ]
  ]
}
```


---

## Question 5: case_313 (Auto-Relate)

**Dataset:** Auto-Relate  
**Test case:** case_313  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|   FactID |   Hrs | Days   | Weeks   | Time             | Room   | CourseCode   |   InstructorID |   Section Code |   Semester Code |   Current/Actual enrollment |   Registered/Original enrollment |   Cap enrollment | Title                          | Subject   |   Course Number |   Hours | Level1    | Level2     |
|---------:|------:|:-------|:--------|:-----------------|:-------|:-------------|---------------:|---------------:|----------------:|----------------------------:|---------------------------------:|-----------------:|:-------------------------------|:----------|----------------:|--------:|:----------|:-----------|
|       57 |   3   | ONLINE | 16      | ONLINE           |        | CS3243       |              3 |            900 |          201108 |                           8 |                                8 |                0 | Operating Systems              | CS        |            3243 |       3 | Undergrad | Junior     |
|       59 |   3   | ONLINE | 8E      | ONLINE           |        | CS3243       |              3 |            900 |          201205 |                          10 |                               12 |               20 | Operating Systems              | CS        |            3243 |       3 | Undergrad | Junior     |
|      371 |   3   | W      | 8E      | 5:00PM - 7:30PM  | J 210  | IT4723       |              5 |            850 |          201205 |                           6 |                                6 |               20 | IT Policy and Law              | IT        |            4723 |       3 | Undergrad | Senior     |
|      207 |   3   | M W    | 16      | 3:00PM - 4:15PM  | J 217  | CS6263       |             18 |            001 |          201202 |                          10 |                               11 |               10 | Computer Networks              | CS        |            6263 |       3 | Grad      | Grad       |
|      356 |   3   | ONLINE | 16      | ONLINE           |        | IT4513       |             44 |            900 |          201108 |                           3 |                                3 |               20 | Elec Health Record Systems     | IT        |            4513 |       3 | Undergrad | Senior     |
|      638 |   4   | T R    | 16      | 7:30PM - 9:10PM  | J 201L | SWE4724      |             33 |            001 |          201108 |                           8 |                                8 |               20 | Software Engineering Project   | SWE       |            4724 |       3 | Undergrad | Senior     |
|      501 |   3   | M W    | 16      | 7:30PM - 8:45PM  | J 110  | IT6533       |              5 |            001 |          201202 |                           7 |                                8 |               20 | Health Info Sec & Privacy      | IT        |            6533 |       3 | Grad      | Grad       |
|      120 |   3   | T R    | 16      | 4:30PM - 5:45PM  | J 131  | CS4903       |             19 |            001 |          201202 |                          10 |                               11 |                0 | SpTp-                          | CS        |            4903 |       3 | Undergrad | Senior     |
|      526 |   3   | R      | 16      | 7:30PM - 8:45PM  | J 210  | IT6753       |             14 |            850 |          201202 |                          12 |                               12 |               20 | Adv Web Concepts & Apps        | IT        |            6753 |       3 | Grad      | Grad       |
|      385 |   3   | ONLINE | 4L      | ONLINE           |        | IT4823       |             32 |            901 |          201205 |                           1 |                                1 |                0 | Info Security Admin.           | IT        |            4823 |       3 | Undergrad | Senior     |
|      302 |   3   | ONLINE | 16      | ONLINE           |        | IT3223       |             25 |            900 |          201008 |                          20 |                               20 |               19 | SoftwareAcq&ProjManagement     | IT        |            3223 |       3 | Undergrad | Junior     |
|      601 |   3   | M W    | 16      | 3:00PM - 4:15PM  | J 131  | SWE3623      |              9 |            001 |          201108 |                          27 |                               27 |               35 | Software Systems Requiremnts   | SWE       |            3623 |       3 | Undergrad | Junior     |
|      485 |   3   | ONLINE | 16      | ONLINE           |        | IT6423       |             14 |            900 |          201102 |                          15 |                               18 |               20 | ITSysAcquisition&Integ         | IT        |            6423 |       3 | Grad      | Grad       |
|      394 |   3   | M W    | 16      | 7:30PM - 8:45PM  | J 210  | IT4853       |              1 |            001 |          201202 |                          19 |                               19 |               20 | Computer Forensics             | IT        |            4853 |       3 | Undergrad | Senior     |
|       65 |   4   | T R    | 16      | 1:00PM - 2:15PM  | J 201L | CS3424       |             19 |            001 |          201202 |                          16 |                               25 |               25 | Data Structures                | CS        |            3424 |       3 | Undergrad | Junior     |
|      498 |   3   | ONLINE | 16      | ONLINE           |        | IT6513       |             44 |            900 |          201108 |                          15 |                               15 |               20 | EHR Systems                    | IT        |            6513 |       3 | Grad      | Grad       |
|      618 |   3   | ONLINE | 16      | ONLINE           |        | SWE3843      |              3 |            900 |          201008 |                           2 |                                3 |                5 | EmbSysSoftwareCNST&Testing     | SWE       |            3843 |       3 | Undergrad | Junior     |
|      616 |   3   | ONLINE | 16      | ONLINE           |        | SWE3683      |             30 |            900 |          201202 |                           0 |                                0 |               10 | Embedded Sys Analy & Design    | SWE       |            3683 |       3 | Undergrad | Junior     |
|      569 |   3   | TBA    | 16      | TBA              |        | IT7803       |             40 |            001 |          201008 |                           0 |                                0 |                0 | Master's Thesis                | IT        |            7803 |       3 | Grad      | Grad       |
|      454 |   1.5 | T R    | 4L      | 7:40PM - 10:10PM | J 210  | IT5302       |              5 |            001 |          201105 |                           8 |                                9 |               20 | Intro to Web Development       | IT        |            5302 |       3 | Grad      | Transition |
|       85 |   3   | T R    | 16      | 1:00PM - 2:15PM  | J 251  | CS4243       |             30 |            001 |          201008 |                           8 |                                8 |               15 | Systems Programming            | CS        |            4243 |       3 | Undergrad | Senior     |
|      256 |   3   | M W    | 16      | 2:30PM - 3:45PM  | J 265  | IT1113       |             10 |            001 |          201202 |                          18 |                               18 |               35 | Programming Principles         | IT        |            1113 |       3 | Undergrad | Freshman   |
|      472 |   3   | ONLINE | 16      | ONLINE           |        | IT6203       |             26 |            900 |          201108 |                          15 |                               16 |               20 | IT Design Studio               | IT        |            6203 |       3 | Grad      | Grad       |
|      663 |   3   | M W    | 16      | 6:00PM - 7:15PM  | J 159  | SWE6633      |             37 |            001 |          201008 |                           5 |                                7 |               25 | Software Project Management    | SWE       |            6633 |       3 | Grad      | Grad       |
|      640 |   3   | M W    | 16      | 4:30PM - 5:45PM  | J 201  | SWE4743      |              9 |            001 |          201102 |                           9 |                               13 |               35 | Object-Oriented Development    | SWE       |            4743 |       3 | Undergrad | Senior     |
|      684 |   3   | ONLINE | 16      | ONLINE           |        | SWE6743      |              9 |            900 |          201008 |                           7 |                                8 |               25 | Object-Oriented Analy & Design | SWE       |            6743 |       3 | Grad      | Grad       |
|      434 |   1.5 | T R    | 7       | 4:30PM - 5:45PM  | J 210  | IT5201       |             25 |            001 |          201008 |                          12 |                               12 |               15 | Intro to Computer Networks     | IT        |            5201 |       3 | Grad      | Transition |
|      669 |   3   | ONLINE | 8E      | ONLINE           |        | SWE6633      |             28 |            900 |          201205 |                           8 |                                8 |               20 | Software Project Management    | SWE       |            6633 |       3 | Grad      | Grad       |
|      222 |   3   | T R    | 16      | 7:30PM - 8:45PM  | J 201  | CS6523       |             19 |            002 |          201108 |                           0 |                                0 |               15 | Artifical Intelligence         | CS        |            6523 |       3 | Grad      | Grad       |
|       94 |   3   | M W    | 16      | 3:00PM - 4:15PM  | J 217  | CS4263       |             18 |            001 |          201202 |                           8 |                                8 |               20 | Computer Networks              | CS        |            4263 |       3 | Undergrad | Senior     |
|      340 |   3   | M W    | 16      | 7:30PM - 8:45PM  | J 266  | IT4203       |              5 |            001 |          201108 |                          12 |                               16 |               30 | Advanced Web Development       | IT        |            4203 |       3 | Undergrad | Senior     |
|      642 |   3   | M W    | 16      | 4:30PM - 5:45PM  | J 201L | SWE4783      |              2 |            001 |          201202 |                          26 |                               26 |               35 | User Interaction Engg          | SWE       |            4783 |       3 | Undergrad | Senior     |
|      461 |   3   | W      | 16      | 6:00PM - 7:15PM  | J 266  | IT6103       |             32 |            850 |          201202 |                          10 |                               10 |               20 | IT and the Law                 | IT        |            6103 |       3 | Grad      | Grad       |
|      475 |   3   | M      | 16      | 4:30PM - 5:45PM  | J 210  | IT6413       |             44 |            850 |          201008 |                          15 |                               15 |               20 | IT Service Delivery            | IT        |            6413 |       3 | Grad      | Grad       |
|      636 |   4   | M W    | 16      | 7:30PM - 9:15PM  | J 159  | SWE4724      |             37 |            001 |          201008 |                           8 |                                8 |               15 | Software Engineering Project   | SWE       |            4724 |       3 | Undergrad | Senior     |
|       34 |   3   | ONLINE | 16      | ONLINE           |        | CS3153       |             19 |            901 |          201102 |                           7 |                                7 |               25 | Database Systems               | CS        |            3153 |       3 | Undergrad | Junior     |
|      520 |   3   | ONLINE | 8E      | ONLINE           |        | IT6723       |             26 |            900 |          201105 |                          11 |                               11 |               20 | Managing Oper & Network Sys    | IT        |            6723 |       3 | Grad      | Grad       |
|      717 |   3   | TBA    | 16      | TBA              |        | SWE7803      |              9 |            001 |          201102 |                           1 |                                1 |                0 | SWE Master's Thesis            | SWE       |            7803 |       3 | Grad      | Grad       |
|      158 |   3   | ONLINE | 16      | ONLINE           |        | CS5153       |             36 |            900 |          201102 |                           2 |                                2 |                5 | Database Systems               | CS        |            5153 |       3 | Grad      | Transition |
|      659 |   3   | ONLINE | 8E      | ONLINE           |        | SWE6623      |              9 |            900 |          201105 |                           4 |                                6 |               15 | Software Engineering I         | SWE       |            6623 |       3 | Grad      | Grad       |
|      127 |   3   | ONLINE | 16      | ONLINE           |        | CS5003       |             24 |            900 |          201108 |                           5 |                                9 |               15 | Acc Intro to Programming       | CS        |            5003 |       3 | Grad      | Transition |
|      598 |   3   | T R    | 16      | 6:00PM - 7:15PM  | J 201L | SWE3613      |             33 |            001 |          201108 |                          35 |                               35 |               35 | Software Systems Engineering   | SWE       |            3613 |       3 | Undergrad | Junior     |
|      654 |   3   | T R    | 16      | 7:30PM - 8:45PM  | J 131  | SWE6623      |             37 |            001 |          201108 |                           6 |                                9 |               15 | Software Engineering I         | SWE       |            6623 |       3 | Grad      | Grad       |
|      420 |   1.5 | T R    | 7       | 7:30PM - 8:45PM  | J 210  | IT5102       |             25 |            001 |          201008 |                          11 |                               12 |               15 | Intro Computer Security        | IT        |            5102 |       3 | Grad      | Transition |
|      411 |   3   | R      | 16      | 4:30PM - 5:45PM  | J 211  | IT4983       |             40 |            850 |          201202 |                          22 |                               22 |               20 | IT Capstone                    | IT        |            4983 |       3 | Undergrad | Senior     |
|      269 |   0   | T      | 8E      | 3:00PM - 4:30PM  | J 266  | IT1324       |             39 |            051 |          201205 |                          13 |                               13 |               30 | Adv Programming Principles     | IT        |            1324 |       3 | Undergrad | Freshman   |
|      190 |   3   | ONLINE | 16      | ONLINE           |        | CS5423       |             36 |            900 |          201108 |                           4 |                               10 |               15 | Math Structures for CS         | CS        |            5423 |       3 | Grad      | Transition |
|      440 |   1.5 | ONLINE | 7       | ONLINE           |        | IT5201       |             25 |            900 |          201102 |                          13 |                               13 |               15 | Intro to Computer Networks     | IT        |            5201 |       3 | Grad      | Transition |
|      685 |   3   | ONLINE | 16      | ONLINE           |        | SWE6743      |              9 |            900 |          201108 |                           5 |                                7 |               15 | Object-Oriented Analy & Design | SWE       |            6743 |       3 | Grad      | Grad       |
|      382 |   3   | ONLINE | 8E      | ONLINE           |        | IT4823       |              5 |            900 |          201105 |                          15 |                               21 |               20 | Info Security Admin.           | IT        |            4823 |       3 | Undergrad | Senior     |


````

### Model Response

```
```json
{
  "Functional-Dependency": [
    ["CourseCode", "InstructorID"],
    ["CourseCode", "Section Code"],
    ["CourseCode", "Semester Code"],
    ["CourseCode", "Current/Actual enrollment"],
    ["CourseCode", "Registered/Original enrollment"],
    ["CourseCode", "Cap enrollment"],
    ["CourseCode", "Title"],
    ["CourseCode", "Subject"],
    ["CourseCode", "Course Number"],
    ["CourseCode", "Hours"],
    ["CourseCode", "Level1"],
    ["CourseCode", "Level2"]
  ]
}
```
```

### Correct Answer

```
{
  "Functional-Dependency": [
    [
      "CourseCode",
      "Title"
    ],
    [
      "CourseCode",
      "Subject"
    ],
    [
      "CourseCode",
      "Course Number"
    ],
    [
      "CourseCode",
      "Hours"
    ],
    [
      "CourseCode",
      "Level1"
    ],
    [
      "CourseCode",
      "Level2"
    ]
  ]
}
```


---

## Question 6: case_259 (Auto-Relate)

**Dataset:** Auto-Relate  
**Test case:** case_259  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Merged        |   Client# | ModoPag   | Date                    | Doc# Origin   | Receipt#    |   Receipt Val | Receipt# - Copy   | Nº Doc.   | Data                    | Nº Cliente   | Valor   |
|:--------------|----------:|:----------|:------------------------|:--------------|:------------|--------------:|:------------------|:----------|:------------------------|:-------------|:--------|
| RE 531 - 1067 |      1067 | RTB       | 2020-06-25 00:00:00.000 | FA 2020/732   | RE 2020/531 |          2306 | RE 531            | RE 531    | 2020-06-25 00:00:00.000 | 1067.0       | 2306.25 |
| RE 65 - 159   |       159 | RTB       | 2020-01-28 00:00:00.000 | FA 2020/87    | RE 2020/65  |           308 | RE 65             |           |                         |              |         |
| RE 802 - 1590 |      1590 | RTB       | 2020-09-25 00:00:00.000 | FA 2020/975   | RE 2020/802 |          2460 | RE 802            |           |                         |              |         |
| RE 412 - 614  |       614 | RTB       | 2020-05-13 00:00:00.000 | FA 2020/368   | RE 2020/412 |          2460 | RE 412            | RE 412    | 2020-05-13 00:00:00.000 | 614.0        | 14760.0 |
| RE 507 - 97   |        97 | RTB       | 2020-08-11 00:00:00.000 | FA 2020/433   | RE 2020/507 |            31 | RE 507            |           |                         |              |         |
| RE 285 - 145  |       145 | RTB       | 2020-05-05 00:00:00.000 | FA 2019/1173  | RE 2020/285 |           271 | RE 285            |           |                         |              |         |
| RE 379 - 1829 |      1829 | RTB       | 2020-04-30 00:00:00.000 | FA 2020/379   | RE 2020/379 |          6273 | RE 379            | RE 379    | 2020-04-30 00:00:00.000 | 1829.0       | 6273.0  |
| RE 228 - 344  |       344 | RTB       | 2020-03-12 00:00:00.000 | FA 2018/1468  | RE 2020/228 |           236 | RE 228            | RE 228    | 2020-03-12 00:00:00.000 | 344.0        | 708.48  |
| RE 396 - 59   |        59 | RTB       | 2020-06-26 00:00:00.000 | FA 2020/367   | RE 2020/396 |           185 | RE 396            |           |                         |              |         |
| RE 492 - 149  |       149 | RTB       | 2020-08-04 00:00:00.000 | FA 2020/657   | RE 2020/492 |           176 | RE 492            |           |                         |              |         |
| RE 95 - 156   |       156 | RTB       | 2020-02-12 00:00:00.000 | FA 2019/1180  | RE 2020/95  |           185 | RE 95             |           |                         |              |         |
| RE 191 - 1767 |      1767 | RTB       | 2020-03-02 00:00:00.000 | FA 2020/15    | RE 2020/191 |          1107 | RE 191            | RE 191    | 2020-03-02 00:00:00.000 | 1767.0       | 1107.0  |
| RE 201 - 1731 |      1731 | RTB       | 2020-03-03 00:00:00.000 | FA 2019/1364  | RE 2020/201 |            77 | RE 201            | RE 201    | 2020-03-03 00:00:00.000 | 1731.0       | 153.76  |
| RE 203 - 1729 |      1729 | RTB       | 2020-03-03 00:00:00.000 | FA 2019/1362  | RE 2020/203 |           461 | RE 203            | RE 203    | 2020-03-03 00:00:00.000 | 1729.0       | 922.5   |
| RE 370 - 1683 |      1683 | RTB       | 2020-04-28 00:00:00.000 | FA 2020/308   | RE 2020/370 |           308 | RE 370            | RE 370    | 2020-04-28 00:00:00.000 | 1683.0       | 922.5   |
| RE 149 - 76   |        76 | RTB       | 2020-02-21 00:00:00.000 | FA 2019/1288  | RE 2020/149 |           492 | RE 149            | RE 149    | 2020-02-21 00:00:00.000 | 76.0         | 3936.0  |
| RE 14 - 67    |        67 | RTB       | 2020-01-10 00:00:00.000 | FA 2019/1349  | RE 2020/14  |           554 | RE 14             |           |                         |              |         |
| RE 334 - 1404 |      1404 | RTB       | 2020-04-17 00:00:00.000 | FA 2020/403   | RE 2020/334 |           615 | RE 334            | RE 334    | 2020-04-17 00:00:00.000 | 1404.0       | 615.0   |
| RE 537 - 7    |         7 | RTB       | 2020-08-27 00:00:00.000 | FA 2020/697   | RE 2020/537 |           123 | RE 537            |           |                         |              |         |
| RE 381 - 1    |         1 | RTB       | 2020-06-16 00:00:00.000 | FA 2020/523   | RE 2020/381 |          2829 | RE 381            |           |                         |              |         |
| RE 509 - 250  |       250 | RTB       | 2020-06-18 00:00:00.000 | FA 2020/258   | RE 2020/509 |           517 | RE 509            | RE 509    | 2020-06-18 00:00:00.000 | 250.0        | 1549.8  |
| RE 459 - 619  |       619 | RTB       | 2020-05-26 00:00:00.000 | FA 2020/579   | RE 2020/459 |          3383 | RE 459            | RE 459    | 2020-05-26 00:00:00.000 | 619.0        | 3382.5  |
| RE 642 - 1753 |      1753 | RTB       | 2020-07-30 00:00:00.000 | FA 2019/1013  | RE 2020/642 |          3321 | RE 642            | RE 642    | 2020-07-30 00:00:00.000 | 1753.0       | 3321.0  |
| RE 244 - 1575 |      1575 | RTB       | 2020-03-17 00:00:00.000 | FA 2018/1132  | RE 2020/244 |          1464 | RE 244            | RE 244    | 2020-03-17 00:00:00.000 | 1575.0       | 5856.0  |
| RE 508 - 1105 |      1105 | RTB       | 2020-06-18 00:00:00.000 | FA 2020/718   | RE 2020/508 |          1107 | RE 508            | RE 508    | 2020-06-18 00:00:00.000 | 1105.0       | 1107.0  |
| RE 583 - 9    |         9 | RTB       | 2020-09-24 00:00:00.000 | FA 2020/699   | RE 2020/583 |           185 | RE 583            |           |                         |              |         |
| RE 145 - 205  |       205 | RTB       | 2020-03-05 00:00:00.000 | FA 2020/220   | RE 2020/145 |           369 | RE 145            |           |                         |              |         |
| RE 11 - 1718  |      1718 | RTB       | 2020-01-03 00:00:00.000 | FA 2019/443   | RE 2020/11  |           923 | RE 11             | RE 11     | 2020-01-03 00:00:00.000 | 1718.0       | 9505.36 |
| RE 220 - 732  |       732 | RTB       | 2020-03-09 00:00:00.000 | FA 2020/216   | RE 2020/220 |          2857 | RE 220            | RE 220    | 2020-03-09 00:00:00.000 | 732.0        | 2856.68 |
| RE 542 - 166  |       166 | RTB       | 2020-08-28 00:00:00.000 | FA 2020/742   | RE 2020/542 |           185 | RE 542            |           |                         |              |         |
| RE 145 - 1349 |      1349 | RTB       | 2020-02-21 00:00:00.000 | FA 2020/72    | RE 2020/145 |           461 | RE 145            | RE 145    | 2020-02-21 00:00:00.000 | 1349.0       | 461.25  |
| RE 653 - 460  |       460 | RTB       | 2020-08-04 00:00:00.000 | FA 2020/794   | RE 2020/653 |           695 | RE 653            | RE 653    | 2020-08-04 00:00:00.000 | 460.0        | 694.95  |
| RE 219 - 35   |        35 | RTB       | 2020-04-07 00:00:00.000 | FA 2020/351   | RE 2020/219 |           246 | RE 219            |           |                         |              |         |
| RE 619 - 1730 |      1730 | RTB       | 2020-07-22 00:00:00.000 | FA 2020/842   | RE 2020/619 |            77 | RE 619            | RE 619    | 2020-07-22 00:00:00.000 | 1730.0       | 76.88   |
| RE 495 - 212  |       212 | RTB       | 2020-08-05 00:00:00.000 | FA 2020/680   | RE 2020/495 |           923 | RE 495            |           |                         |              |         |
| RE 454 - 148  |       148 | RTB       | 2020-07-16 00:00:00.000 | FA 2020/570   | RE 2020/454 |          1845 | RE 454            |           |                         |              |         |
| RE 384 - 663  |       663 | RTB       | 2020-04-30 00:00:00.000 | FA 2020/390   | RE 2020/384 |           923 | RE 384            | RE 384    | 2020-04-30 00:00:00.000 | 663.0        | 1230.0  |
| RE 756 - 865  |       865 | RTB       | 2020-09-14 00:00:00.000 | FA 2020/753   | RE 2020/756 |           984 | RE 756            |           |                         |              |         |
| RE 148 - 1781 |      1781 | RTB       | 2020-02-21 00:00:00.000 | FA 2019/1368  | RE 2020/148 |           677 | RE 148            | RE 148    | 2020-02-21 00:00:00.000 | 1781.0       | 2029.5  |
| RE 186 - 1042 |      1042 | RTB       | 2020-03-02 00:00:00.000 | FA 2020/161   | RE 2020/186 |           492 | RE 186            | RE 186    | 2020-03-02 00:00:00.000 | 1042.0       | 492.0   |
| RE 502 - 445  |       445 | RTB       | 2020-06-16 00:00:00.000 | FA 2020/654   | RE 2020/502 |           615 | RE 502            | RE 502    | 2020-06-16 00:00:00.000 | 445.0        | 615.0   |
| RE 10 - 343   |       343 | DEP       | 2020-01-02 00:00:00.000 | FA 2018/1467  | RE 2020/10  |           412 | RE 10             | RE 10     | 2020-01-02 00:00:00.000 | 343.0        | 3000.0  |
| RE 41 - 13    |        13 | RTB       | 2020-07-01 00:00:00.000 | FA 2017/68    | RE 2020/41  |           492 | RE 41             |           |                         |              |         |
| RE 203 - 1729 |      1729 | RTB       | 2020-03-03 00:00:00.000 | FA 2020/194   | RE 2020/203 |           461 | RE 203            | RE 203    | 2020-03-03 00:00:00.000 | 1729.0       | 922.5   |
| RE 392 - 44   |        44 | RTB       | 2020-05-05 00:00:00.000 | FA 2020/409   | RE 2020/392 |           861 | RE 392            | RE 392    | 2020-05-05 00:00:00.000 | 44.0         | 1722.0  |
| RE 211 - 776  |       776 | RTB       | 2020-03-06 00:00:00.000 | FA 2020/208   | RE 2020/211 |          2755 | RE 211            | RE 211    | 2020-03-06 00:00:00.000 | 776.0        | 2755.2  |
| RE 688 - 145  |       145 | RTB       | 2020-08-20 00:00:00.000 | FA 2019/1465  | RE 2020/688 |          1845 | RE 688            | RE 688    | 2020-08-20 00:00:00.000 | 145.0        | 7380.0  |
| RE 58 - 135   |       135 | DEP       | 2020-01-24 00:00:00.000 | NC 2019/48    | RE 2020/58  |           -28 | RE 58             |           |                         |              |         |
| RE 333 - 161  |       161 | RTB       | 2020-05-26 00:00:00.000 | FA 2020/491   | RE 2020/333 |           185 | RE 333            |           |                         |              |         |
| RE 27 - 3     |         3 | RTB       | 2020-01-15 00:00:00.000 | FA 2020/5     | RE 2020/27  |            62 | RE 27             |           |                         |              |         |


````

### Model Response

```
```json
{
  "Functional-Dependency": [
    ["Client#", "ModoPag"],
    ["Client#", "Date"],
    ["Client#", "Doc# Origin"],
    ["Client#", "Receipt#"],
    ["Client#", "Receipt Val"],
    ["Client#", "Receipt# - Copy"],
    ["Client#", "Nº Doc."],
    ["Client#", "Data"],
    ["Client#", "Nº Cliente"],
    ["Client#", "Valor"]
  ]
}
```
```

### Correct Answer

```
{
  "Functional-Dependency": [
    [
      "Merged",
      "N\u00ba Doc."
    ],
    [
      "Merged",
      "Data"
    ],
    [
      "Merged",
      "N\u00ba Cliente"
    ],
    [
      "Merged",
      "Valor"
    ]
  ]
}
```


---

## Question 7: case_133 (Auto-Relate)

**Dataset:** Auto-Relate  
**Test case:** case_133  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|   판매ID | 날짜                    |   거래처코드 |   제품코드 |    단가 |   수량 |   할인율 |         매출금액 |   매출원가 |   원가 |         매출이익 | 거래처명             |   우편코드 | 시도           | 구군시   | 기타   | 지역       | 상태   |
|---------:|:------------------------|-------------:|-----------:|--------:|-------:|---------:|-----------------:|-----------:|-------:|-----------------:|:---------------------|-----------:|:---------------|:---------|:-------|:-----------|:-------|
|      573 | 2019-12-26 00:00:00.000 |           48 |         13 |   93216 |     83 |      0   |      7.73693e+06 |    3557712 |  42864 |      4.17922e+06 | (유)드림테크         |      58247 | 전라남도       | 나주시   | 나주   | 전남       | ON     |
|     2016 | 2021-12-10 00:00:00.000 |            4 |         68 |   11988 |     22 |      0   | 263736           |     134376 |   6108 | 129360           | 동광통상             |       7224 | 서울특별시     | 영등포구 | 서울   | 서울시     | ON     |
|      576 | 2019-12-27 00:00:00.000 |           23 |         14 |  115140 |     59 |      0   |      6.79326e+06 |    3463536 |  58704 |      3.32972e+06 | 알프스무역           |      62207 | 광주광역시     | 광산구   | 광주   | 광주시     | ON     |
|      561 | 2019-12-18 00:00:00.000 |           29 |         43 | 1027200 |     41 |      0   |      4.21152e+07 |   19367088 | 472368 |      2.27481e+07 | 태성무역             |      21945 | 인천광역시     | 연수구   | 인천   | 인천시     | ON     |
|       52 | 2019-02-02 00:00:00.000 |           51 |          8 | 1479988 |     10 |      0.1 |      1.33199e+07 |    8529840 | 852984 |      4.79005e+06 | (유)타오스           |      63563 | 제주특별자치도 | 서귀포시 | 제주   | 제주       | ON     |
|      687 | 2020-02-27 00:00:00.000 |            1 |         11 |  278400 |     69 |      0   |      1.92096e+07 |    8833932 | 128028 |      1.03757e+07 | 한미전자             |       6309 | 서울특별시     | 강남구   | 서울   | 서울시     | ON     |
|     1330 | 2021-01-08 00:00:00.000 |           51 |         69 |  274800 |      6 |      0   |      1.6488e+06  |     758232 | 126372 | 890568           | (유)타오스           |      63563 | 제주특별자치도 | 서귀포시 | 제주   | 제주       | ON     |
|     1883 | 2021-10-06 00:00:00.000 |            3 |         49 |  429600 |      7 |      0.1 |      2.70648e+06 |    1377600 | 196800 |      1.32888e+06 | 태화상사             |       8804 | 서울특별시     | 관악구   | 서울   | 서울시     | ON     |
|     1172 | 2020-10-26 00:00:00.000 |           16 |          4 |  599988 |     38 |      0.1 |      2.05196e+07 |   10484808 | 275916 |      1.00348e+07 | 대진상사             |      31220 | 충청남도       | 천안시   | 천안   | 충남       | ON     |
|     1460 | 2021-03-16 00:00:00.000 |           25 |         65 |  369600 |     67 |      0.1 |      2.22869e+07 |   11387856 | 169968 |      1.0899e+07  | 삼양상사             |      61421 | 광주광역시     | 동구     | 광주   | 광주시     | ON     |
|      305 | 2019-07-17 00:00:00.000 |           31 |         33 |  131988 |     45 |      0   |      5.93946e+06 |    3028320 |  67296 |      2.91114e+06 | 한진무역             |      44915 | 울산광역시     | 울주군   | 울산   | 울산광역시 | ON     |
|     1958 | 2021-11-16 00:00:00.000 |           41 |         37 |   47988 |      4 |      0.1 | 172757           |      97872 |  24468 |  74884.8         | (주)비젼웨이브       |      38125 | 경상북도       | 경주시   | 경주   | 경북       | ON     |
|     1015 | 2020-08-11 00:00:00.000 |            9 |         78 |  309600 |     78 |      0.1 |      2.17339e+07 |   11105640 | 142380 |      1.06283e+07 | 월드링크             |      16454 | 경기도         | 수원시   | 수원   | 경기       | ON     |
|      675 | 2020-02-20 00:00:00.000 |            3 |         56 |   22896 |     94 |      0.1 |      1.937e+06   |     914808 |   9732 |      1.02219e+06 | 태화상사             |       8804 | 서울특별시     | 관악구   | 서울   | 서울시     | ON     |
|      204 | 2019-05-10 00:00:00.000 |           43 |          6 | 1421964 |     45 |      0   |      6.39884e+07 |   21200400 | 471120 |      4.2788e+07  | 동원특수음향         |      50594 | 경상남도       | 양산시   | 양산   | 경남       | ON     |
|     1203 | 2020-11-09 00:00:00.000 |            5 |         59 |  843840 |     58 |      0   |      4.89427e+07 |   18755808 | 323376 |      3.01869e+07 | 오성통상             |      31220 | 충청남도       | 천안시   | 천안   | 충남       | ON     |
|      130 | 2019-03-23 00:00:00.000 |           28 |         44 | 1027200 |      8 |      0.1 |      7.39584e+06 |    3778944 | 472368 |      3.6169e+06  | 언더우드상사         |      21329 | 인천광역시     | 부평구   | 인천   | 인천시     | ON     |
|     1991 | 2021-12-02 00:00:00.000 |            1 |         75 |  321600 |     64 |      0   |      2.05824e+07 |    9464832 | 147888 |      1.11176e+07 | 한미전자             |       6309 | 서울특별시     | 강남구   | 서울   | 서울시     | ON     |
|      239 | 2019-06-04 00:00:00.000 |           28 |         44 | 1027200 |     51 |      0.1 |      4.71485e+07 |   24090768 | 472368 |      2.30577e+07 | 언더우드상사         |      21329 | 인천광역시     | 부평구   | 인천   | 인천시     | ON     |
|     1677 | 2021-07-06 00:00:00.000 |           21 |         14 |  115140 |     86 |      0   |      9.90204e+06 |    5048544 |  58704 |      4.8535e+06  | 글로리아 백화점      |      42260 | 대구광역시     | 수성구   | 대구   | 대구시     | ON     |
|      101 | 2019-03-07 00:00:00.000 |           41 |         71 |  286800 |     20 |      0.1 |      5.1624e+06  |    2637840 | 131892 |      2.52456e+06 | (주)비젼웨이브       |      38125 | 경상북도       | 경주시   | 경주   | 경북       | ON     |
|      350 | 2019-08-14 00:00:00.000 |           37 |         42 | 1032000 |      9 |      0   |      9.288e+06   |    4271184 | 474576 |      5.01682e+06 | J마켓                |       1129 | 서울특별시     | 강북구   | 서울   | 서울시     | ON     |
|       65 | 2019-02-13 00:00:00.000 |           32 |         38 |   33600 |     60 |      0   |      2.016e+06   |    1028160 |  17136 | 987840           | 대한상사             |      44468 | 울산광역시     | 중구     | 울산   | 울산광역시 | ON     |
|     1373 | 2021-02-03 00:00:00.000 |           51 |          8 | 1479988 |     57 |      0.1 |      7.59234e+07 |   48620088 | 852984 |      2.73033e+07 | (유)타오스           |      63563 | 제주특별자치도 | 서귀포시 | 제주   | 제주       | ON     |
|      500 | 2019-11-14 00:00:00.000 |            8 |         32 |   27468 |     82 |      0   |      2.25238e+06 |     745872 |   9096 |      1.5065e+06  | 태강교역             |      18126 | 경기도         | 오산시   | 오산   | 경기       | ON     |
|      463 | 2019-10-19 00:00:00.000 |           14 |         73 |  154800 |     20 |      0   |      3.096e+06   |    1578480 |  78924 |      1.51752e+06 | 베네디스             |      47385 | 부산광역시     | 부산진구 | 부산   | 부산시     | ON     |
|      906 | 2020-06-19 00:00:00.000 |           38 |         13 |   93216 |     92 |      0.1 |      7.71828e+06 |    3943488 |  42864 |      3.7748e+06  | k마켓                |      47880 | 부산광역시     | 동래구   | 부산   | 부산시     | ON     |
|     1874 | 2021-10-02 00:00:00.000 |           36 |         23 |  179988 |     69 |      0.1 |      1.11773e+07 |    4114332 |  59628 |      7.06292e+06 | 투프린트             |      18387 | 경기도         | 화성시   | 화성   | 경기       | ON     |
|     2050 | 2021-12-22 00:00:00.000 |           25 |         42 | 1032000 |      7 |      0.1 |      6.5016e+06  |    3322032 | 474576 |      3.17957e+06 | 삼양상사             |      61421 | 광주광역시     | 동구     | 광주   | 광주시     | ON     |
|      575 | 2019-12-27 00:00:00.000 |           24 |         65 |  369600 |     14 |      0.1 |      4.65696e+06 |    2379552 | 169968 |      2.27741e+06 | 유미백화점           |      61636 | 광주광역시     | 남구     | 광주   | 광주시     | ON     |
|      464 | 2019-10-19 00:00:00.000 |           25 |         78 |  309600 |     13 |      0   |      4.0248e+06  |    1850940 | 142380 |      2.17386e+06 | 삼양상사             |      61421 | 광주광역시     | 동구     | 광주   | 광주시     | ON     |
|     1070 | 2020-09-08 00:00:00.000 |           46 |         77 |  307200 |     51 |      0.1 |      1.41005e+07 |    7205076 | 141276 |      6.8954e+06  | (유)탑월드           |      54600 | 전라북도       | 익산시   | 익산   | 전북       | ON     |
|     1559 | 2021-05-04 00:00:00.000 |           38 |          7 |  916212 |     85 |      0.1 |      7.00902e+07 |   39704520 | 467112 |      3.03857e+07 | k마켓                |      47880 | 부산광역시     | 동래구   | 부산   | 부산시     | ON     |
|     1875 | 2021-10-05 00:00:00.000 |           14 |         62 |  502560 |     74 |      0   |      3.71894e+07 |   14251512 | 192588 |      2.29379e+07 | 베네디스             |      47385 | 부산광역시     | 부산진구 | 부산   | 부산시     | ON     |
|      992 | 2020-07-31 00:00:00.000 |           24 |         77 |  307200 |     60 |      0   |      1.8432e+07  |    8476560 | 141276 |      9.95544e+06 | 유미백화점           |      61636 | 광주광역시     | 남구     | 광주   | 광주시     | ON     |
|      512 | 2019-11-22 00:00:00.000 |           49 |         48 |  576600 |     63 |      0   |      3.63258e+07 |   12035520 | 191040 |      2.42903e+07 | (유)서원정보통신     |      59766 | 전라남도       | 여수시   | 여수   | 전남       | ON     |
|      803 | 2020-04-27 00:00:00.000 |           47 |         35 |   59952 |     12 |      0.1 | 647482           |     366768 |  30564 | 280714           | (유)누리미르정보통신 |      54800 | 전라북도       | 전주시   | 전주   | 전북       | ON     |
|      614 | 2020-01-20 00:00:00.000 |           48 |         36 |  246000 |      8 |      0   |      1.968e+06   |     904992 | 113124 |      1.06301e+06 | (유)드림테크         |      58247 | 전라남도       | 나주시   | 나주   | 전남       | ON     |
|     1960 | 2021-11-16 00:00:00.000 |           10 |         17 |  131940 |     29 |      0   |      3.82626e+06 |    1759488 |  60672 |      2.06677e+06 | 신영상사             |      13976 | 경기도         | 안양시   | 안양   | 경기       | ON     |
|      442 | 2019-10-08 00:00:00.000 |            7 |         39 |  714000 |     34 |      0.1 |      2.18484e+07 |    8043312 | 236568 |      1.38051e+07 | 삼화상사             |      28204 | 충청북도       | 청주시   | 청주   | 충북       | ON     |
|      433 | 2019-10-02 00:00:00.000 |           45 |         52 |   18720 |     33 |      0   | 617760           |     262548 |   7956 | 355212           | 인터비타             |      51403 | 경상남도       | 창원시   | 창원   | 경남       | ON     |
|     1544 | 2021-04-27 00:00:00.000 |           29 |         54 |   24336 |    127 |      0   |      3.09067e+06 |    1313688 |  10344 |      1.77698e+06 | 태성무역             |      21945 | 인천광역시     | 연수구   | 인천   | 인천시     | ON     |
|     1550 | 2021-04-30 00:00:00.000 |            3 |         45 | 1032000 |     49 |      0.2 |      4.04544e+07 |   23254224 | 474576 |      1.72002e+07 | 태화상사             |       8804 | 서울특별시     | 관악구   | 서울   | 서울시     | ON     |
|     1687 | 2021-07-09 00:00:00.000 |           17 |         31 |   16668 |     27 |      0   | 450036           |     207036 |   7668 | 243000           | 금강                 |      31511 | 충청남도       | 아산시   | 아산   | 충남       | ON     |
|      390 | 2019-09-07 00:00:00.000 |           45 |         40 |   71988 |      9 |      0.1 | 583103           |     330264 |  36696 | 252839           | 인터비타             |      51403 | 경상남도       | 창원시   | 창원   | 경남       | ON     |
|      892 | 2020-06-11 00:00:00.000 |           13 |         38 |   33600 |     22 |      0.1 | 665280           |     376992 |  17136 | 288288           | 미림상사             |      48551 | 부산광역시     | 남구     | 부산   | 부산시     | ON     |
|      208 | 2019-05-14 00:00:00.000 |           13 |         39 |  714000 |     59 |      0.1 |      3.79134e+07 |   13957512 | 236568 |      2.39559e+07 | 미림상사             |      48551 | 부산광역시     | 남구     | 부산   | 부산시     | ON     |
|      475 | 2019-10-26 00:00:00.000 |           31 |         69 |  274800 |     41 |      0.1 |      1.01401e+07 |    5181252 | 126372 |      4.95887e+06 | 한진무역             |      44915 | 울산광역시     | 울주군   | 울산   | 울산광역시 | ON     |
|     2031 | 2021-12-14 00:00:00.000 |           36 |          9 | 1910640 |     84 |      0.1 |      1.44444e+08 |   53175024 | 633036 |      9.12694e+07 | 투프린트             |      18387 | 경기도         | 화성시   | 화성   | 경기       | ON     |
|      171 | 2019-04-19 00:00:00.000 |            9 |         31 |   16668 |     45 |      0   | 750060           |     345060 |   7668 | 405000           | 월드링크             |      16454 | 경기도         | 수원시   | 수원   | 경기       | ON     |


````

### Model Response

```
```json
{
  "Functional-Dependency": [
    ["판매ID", "날짜"],
    ["판매ID", "거래처코드"],
    ["판매ID", "제품코드"],
    ["판매ID", "단가"],
    ["판매ID", "수량"],
    ["판매ID", "할인율"],
    ["판매ID", "매출금액"],
    ["판매ID", "매출원가"],
    ["판매ID", "원가"],
    ["판매ID", "매출이익"],
    ["판매ID", "거래처명"],
    ["판매ID", "우편코드"],
    ["판매ID", "시도"],
    ["판매ID", "구군시"],
    ["판매ID", "기타"],
    ["판매ID", "지역"],
    ["판매ID", "상태"]
  ]
}
```
```

### Correct Answer

```
{
  "Functional-Dependency": [
    [
      "\uac70\ub798\ucc98\ucf54\ub4dc",
      "\uac70\ub798\ucc98\uba85"
    ],
    [
      "\uac70\ub798\ucc98\ucf54\ub4dc",
      "\uc6b0\ud3b8\ucf54\ub4dc"
    ],
    [
      "\uac70\ub798\ucc98\ucf54\ub4dc",
      "\uc2dc\ub3c4"
    ],
    [
      "\uac70\ub798\ucc98\ucf54\ub4dc",
      "\uad6c\uad70\uc2dc"
    ],
    [
      "\uac70\ub798\ucc98\ucf54\ub4dc",
      "\uae30\ud0c0"
    ],
    [
      "\uac70\ub798\ucc98\ucf54\ub4dc",
      "\uc9c0\uc5ed"
    ],
    [
      "\uac70\ub798\ucc98\ucf54\ub4dc",
      "\uc0c1\ud0dc"
    ]
  ]
}
```


---

## Question 8: case_181 (Auto-Relate)

**Dataset:** Auto-Relate  
**Test case:** case_181  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| InvoiceDate             |   InvoiceID |   InvoiceNumber |   ProfileNumber | ProfileName   |   InvoiceAmount | DueDate                 |   CreditDays | StatementGroup   |   CreditDays+1 |
|:------------------------|------------:|----------------:|----------------:|:--------------|----------------:|:------------------------|-------------:|:-----------------|---------------:|
| 2020-07-09 00:00:00.000 |      835286 |          748216 |          801500 | HSML          |          2075   | 2020-08-31 00:00:00.000 |           30 | M                |             31 |
| 2020-01-31 00:00:00.000 |      835051 |          748039 |        13000316 | KayeT         |           370   | 2020-03-03 00:00:00.000 |           30 | F                |             31 |
| 2020-03-01 00:00:00.000 |      835062 |          748055 |          104500 | Loyalty       |          3115   | 2020-05-01 00:00:00.000 |           30 | M                |             31 |
| 2020-04-13 00:00:00.000 |      835319 |          748252 |         1802500 | Pipeline      |           835   | 2020-05-31 00:00:00.000 |           30 | M                |             31 |
| 2020-02-13 00:00:00.000 |      835283 |          748212 |          104500 | Loyalty       |          2185   | 2020-03-31 00:00:00.000 |           30 | M                |             31 |
| 2020-08-18 00:00:00.000 |      835237 |          748161 |          104500 | Loyalty       |          2435   | 2020-10-01 00:00:00.000 |           30 | M                |             31 |
| 2020-05-18 00:00:00.000 |      835183 |          748135 |          102501 | Construction3 |          1625   | 2020-07-17 00:00:00.000 |           45 | F                |             46 |
| 2020-05-07 00:00:00.000 |      835305 |          748241 |          402800 | SMEF          |          6640   | 2020-06-16 00:00:00.000 |           30 | F                |             31 |
| 2020-05-15 00:00:00.000 |      835316 |          748248 |         1903300 | STINTINCINP   |          3625   | 2020-06-01 00:00:00.000 |           15 | F                |             16 |
| 2020-03-31 00:00:00.000 |      835083 |          748030 |         1903700 | SSTech        |           833   | 2020-05-02 00:00:00.000 |           30 | F                |             31 |
| 2020-05-12 00:00:00.000 |      835307 |          748244 |          102506 | Construction2 |             0   | 2020-07-01 00:00:00.000 |           45 | F                |             46 |
| 2020-05-31 00:00:00.000 |      835321 |          748255 |          102500 | Construct1    |          5150   | 2020-07-17 00:00:00.000 |           45 | F                |             46 |
| 2020-04-27 00:00:00.000 |      835264 |          748187 |         1905100 | SAMESAAAS     |           370   | 2020-05-31 00:00:00.000 |           30 | M                |             31 |
| 2020-06-05 00:00:00.000 |      835328 |          748266 |          403900 | DBMC          |          2450   | 2020-08-30 00:00:00.000 |           60 | M                |             61 |
| 2020-06-08 00:00:00.000 |      827597 |          741027 |          201200 | Cream         |           447.5 | 2020-08-16 00:00:00.000 |           60 | F                |             61 |
| 2020-05-21 00:00:00.000 |      835224 |          748152 |          102502 | Construction2 |          1485   | 2020-07-17 00:00:00.000 |           45 | F                |             46 |
| 2020-04-22 00:00:00.000 |      835222 |          748150 |         1301500 | CBM           |          6426   | 2020-06-16 00:00:00.000 |           45 | F                |             46 |
| 2020-04-01 00:00:00.000 |      835206 |          748142 |          106200 | NIGAMJ        |           720   | 2020-05-31 00:00:00.000 |           30 | M                |             31 |
| 2020-06-13 00:00:00.000 |      835251 |          748174 |          502200 | ESMESC        |         11735   | 2020-07-31 00:00:00.000 |           30 | M                |             31 |
| 2020-05-16 00:00:00.000 |      835309 |          748246 |          102506 | Construction2 |          1095   | 2020-07-17 00:00:00.000 |           45 | F                |             46 |
| 2020-02-05 00:00:00.000 |      835263 |          748186 |          104500 | Loyalty       |          3935   | 2020-03-31 00:00:00.000 |           30 | M                |             31 |
| 2020-02-02 00:00:00.000 |      835122 |          748047 |          202500 | LINKKARDO     |           962   | 2020-03-18 00:00:00.000 |           30 | F                |             31 |
| 2020-03-24 00:00:00.000 |      835158 |          748126 |         1303400 | MILDB         |          2410   | 2020-05-01 00:00:00.000 |           30 | M                |             31 |
| 2020-07-05 00:00:00.000 |      835256 |          748162 |          702200 | GMETC         |          2035   | 2020-09-30 00:00:00.000 |           60 | M                |             61 |
| 2020-05-10 00:00:00.000 |      835306 |          748243 |          102506 | Construction2 |          1120   | 2020-07-01 00:00:00.000 |           45 | F                |             46 |
| 2020-04-30 00:00:00.000 |      835302 |          748236 |         1301500 | CBM           |           605   | 2020-06-16 00:00:00.000 |           45 | F                |             46 |
| 2020-06-17 00:00:00.000 |      835312 |          748185 |          501900 | EVLEML        |          1585   | 2020-07-31 00:00:00.000 |           30 | M                |             31 |
| 2020-05-14 00:00:00.000 |      835308 |          748245 |          102506 | Construction2 |         14365   | 2020-07-01 00:00:00.000 |           45 | F                |             46 |
| 2020-02-07 00:00:00.000 |      835273 |          748199 |          104500 | Loyalty       |           890   | 2020-03-31 00:00:00.000 |           30 | M                |             31 |
| 2020-02-21 00:00:00.000 |      835320 |          748253 |          104500 | Loyalty       |          2240   | 2020-03-31 00:00:00.000 |           30 | M                |             31 |
| 2020-01-19 00:00:00.000 |      835189 |          748083 |         1301500 | CBM           |          5425   | 2020-03-18 00:00:00.000 |           45 | F                |             46 |
| 2020-02-06 00:00:00.000 |      835046 |          748035 |          104500 | Loyalty       |          1915   | 2020-03-31 00:00:00.000 |           30 | M                |             31 |
| 2020-04-20 00:00:00.000 |      835268 |          748193 |          107300 | ASABLLL       |          3070   | 2020-06-30 00:00:00.000 |           60 | M                |             61 |
| 2020-05-30 00:00:00.000 |      835210 |          748144 |          201201 | Cream1        |         -6500   | 2020-08-01 00:00:00.000 |           60 | F                |             61 |
| 2020-03-28 00:00:00.000 |      835293 |          748225 |         1303400 | MILDB         |           240   | 2020-05-01 00:00:00.000 |           30 | M                |             31 |
| 2020-07-27 00:00:00.000 |      835069 |          748091 |          104500 | Loyalty       |          2265   | 2020-08-31 00:00:00.000 |           30 | M                |             31 |
| 2020-02-27 00:00:00.000 |      835235 |          748159 |         1303300 | DAGDU         |          9525   | 2020-04-30 00:00:00.000 |           60 | M                |             61 |
| 2020-03-02 00:00:00.000 |      835269 |          748195 |         1303300 | DAGDU         |         26125   | 2020-05-31 00:00:00.000 |           60 | M                |             61 |
| 2020-04-25 00:00:00.000 |      835260 |          748181 |         1905100 | SAMESAAAS     |          1210   | 2020-05-31 00:00:00.000 |           30 | M                |             31 |
| 2020-06-01 00:00:00.000 |      835278 |          748201 |          201201 | Cream1        |          7970   | 2020-08-16 00:00:00.000 |           60 | F                |             61 |
| 2020-06-07 00:00:00.000 |      835304 |          748238 |          502000 | ESCB          |          4970   | 2020-07-17 00:00:00.000 |           30 | F                |             31 |
| 2020-06-30 00:00:00.000 |      825250 |          736144 |         1300109 | FAMJ          |           527   | 2020-08-16 00:00:00.000 |           45 | F                |             46 |
| 2020-03-17 00:00:00.000 |      835145 |          748087 |         1300900 | Malik         |          2795   | 2020-05-01 00:00:00.000 |           30 | M                |             31 |
| 2020-02-18 00:00:00.000 |      835056 |          748043 |          104500 | Loyalty       |          7250   | 2020-03-31 00:00:00.000 |           30 | M                |             31 |
| 2020-02-01 00:00:00.000 |      835255 |          748178 |          104500 | Loyalty       |          8725   | 2020-03-31 00:00:00.000 |           30 | M                |             31 |
| 2020-06-26 00:00:00.000 |      815934 |          730051 |          302100 | CME           |           560   | 2020-07-31 00:00:00.000 |           30 | M                |             31 |
| 2020-02-28 00:00:00.000 |      835061 |          748054 |          104500 | Loyalty       |          3280   | 2020-03-31 00:00:00.000 |           30 | M                |             31 |
| 2020-02-08 00:00:00.000 |      835047 |          748036 |          104500 | Loyalty       |          4720   | 2020-03-31 00:00:00.000 |           30 | M                |             31 |
| 2020-03-14 00:00:00.000 |      835266 |          748191 |         1300108 | MGFSH         |           240   | 2020-05-01 00:00:00.000 |           45 | F                |             46 |
| 2020-06-21 00:00:00.000 |      835314 |          748223 |          501900 | EVLEML        |          3860   | 2020-07-31 00:00:00.000 |           30 | M                |             31 |


````

### Model Response

```
```json
{
  "Functional-Dependency": [
    ["InvoiceDate", "InvoiceID"],
    ["InvoiceDate", "InvoiceNumber"],
    ["InvoiceDate", "ProfileNumber"],
    ["InvoiceDate", "ProfileName"],
    ["InvoiceDate", "InvoiceAmount"],
    ["InvoiceDate", "DueDate"],
    ["InvoiceDate", "CreditDays"],
    ["InvoiceDate", "StatementGroup"],
    ["InvoiceDate", "CreditDays+1"]
  ]
}
```
```

### Correct Answer

```
{
  "Functional-Dependency": [
    [
      "ProfileNumber",
      "CreditDays"
    ],
    [
      "ProfileNumber",
      "StatementGroup"
    ],
    [
      "ProfileNumber",
      "CreditDays+1"
    ]
  ]
}
```


---

## Question 9: case_257 (Auto-Relate)

**Dataset:** Auto-Relate  
**Test case:** case_257  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|   InvoiceID | InvoiceNumber                        |   ClientID | InvoiceDate             |   TotalDiscount |   DeliveryCharge |   InvoiceDateKey | ClientName                  | Address1                 | Address2   | Town          | County       | PostCode   | Region                   | OuterPostode   |   CountryID | ClientType   | ClientSize   | ClientSince             |   IsCreditWorthy |   IsDealer |
|------------:|:-------------------------------------|-----------:|:------------------------|----------------:|-----------------:|-----------------:|:----------------------------|:-------------------------|:-----------|:--------------|:-------------|:-----------|:-------------------------|:---------------|------------:|:-------------|:-------------|:------------------------|-----------------:|-----------:|
|         125 | F7131994-57EE-42F2-A5DC-54E520AD0D1E |          2 | 2013-03-02 00:00:00.000 |          150    |               50 |         20130302 | Honest John                 | 99a Baker Street         |            | London        |              | NSW1 1A    | Greater London Authority | EC             |           1 | Dealer       | Large        | 2000-01-01 00:00:00.000 |                0 |          0 |
|          31 | 8BE305D6-8553-4CCB-8689-AEF1D9E1F89D |          3 | 2013-05-02 00:00:00.000 |            0.01 |              500 |         20130502 | Bright Orange               | 17, Arcadia Way          |            | Birmingham    |              | B1 50AZ    | West Midlands            | B              |           1 | Dealer       | Large        | 2005-04-01 00:00:00.000 |                0 |          0 |
|         200 | 9A778E61-3ED5-4D05-8494-171CC7FE8DA2 |          8 | 2014-09-01 00:00:00.000 |          800    |             1725 |         20140901 | Rocky Riding                | 5205 108th Ave           |            | New York      | New York     |            |                          | NY             |           3 | Dealer       | Large        | 2009-10-15 00:00:00.000 |                1 |          0 |
|         439 | 373ECB78-9EAA-40F4-A7C9-09817F5CFF52 |         31 | 2015-11-02 00:00:00.000 |          200    |              -50 |         20151102 | Classy Car Sales            | 30 Isabella St           |            | Pittsburgh    | Pennsylvania |            |                          | PA             |           3 | Wholesaler   | Small        | 2013-04-01 00:00:00.000 |                1 |          0 |
|         155 | A98E92AE-9623-4606-9665-D00866DA877A |          2 | 2014-01-01 00:00:00.000 |           50    |             1475 |         20140101 | Honest John                 | 99a Baker Street         |            | London        |              | NSW1 1A    | Greater London Authority | EC             |           1 | Dealer       | Large        | 2000-01-01 00:00:00.000 |                0 |          0 |
|         226 | 839EA745-F223-4CD0-AE70-F4D22688C30E |          1 | 2014-11-01 00:00:00.000 |          550    |              425 |         20141101 | Aldo Motors                 | 4, Scale Street          |            | Uttoxeter     | Staffs       | ST17 99RZ  | East Midlands            | ST             |           1 | Wholesaler   | Large        | 1998-01-04 00:00:00.000 |                1 |          1 |
|         406 | 3023EF50-B10B-41B3-BFE7-27082B10CB8C |         25 | 2015-02-02 00:00:00.000 |          200    |              -50 |         20150202 | BritWheels                  | 1414 NW Northrup Street  |            | Portland      | Oregon       |            |                          | OR             |           3 | Dealer       | Large        | 2013-04-01 00:00:00.000 |                0 |          1 |
|         297 | FAA72EBE-53A8-4502-9CC0-55B8EFA77D66 |         21 | 2015-05-18 00:00:00.000 |          550    |              950 |         20150518 | Jungfrau                    |                          |            | Zurich        |              |            |                          |                |           6 | Wholesaler   | Small        | 2012-01-01 00:00:00.000 |                1 |          1 |
|         223 | 4A11F947-E46D-4E1B-9E4C-8A8E97021641 |          9 | 2014-08-01 00:00:00.000 |          550    |              750 |         20140801 | Voitures Diplomatiques S.A. |                          |            | Geneva        |              |            |                          |                |           6 | Wholesaler   | Large        | 2009-10-15 00:00:00.000 |                1 |          0 |
|          76 | CF1DD826-C7F9-4E11-8E56-35C074CEE57A |          4 | 2013-02-02 00:00:00.000 |          500    |              500 |         20130202 | Cut'n'Shut                  | Grange Avenue            |            | Manchester    |              | M1 5AZ     | North West               | M              |           1 | Dealer       | Small        | 2010-01-01 00:00:00.000 |                1 |          0 |
|         451 | 458CEC75-D3D4-4DB9-8B33-00E24B05DB44 |         23 | 2015-05-19 00:00:00.000 |         1050    |              -75 |         20150519 | Embassy Motors              | 57595 Technology Way     |            | Denver        | Colorado     |            |                          | CO             |           3 | Dealer       | Small        | 2013-04-01 00:00:00.000 |                1 |          0 |
|         343 | B317DC9A-3D76-4533-A377-BED059566C45 |         26 | 2015-11-02 00:00:00.000 |           50    |             1650 |         20151102 | Sporty Types Corp           | 13550 Market Street      |            | San Francisco | California   |            |                          | CA             |           3 | Wholesaler   | Large        | 2013-04-01 00:00:00.000 |                0 |          0 |
|          79 | 3581958A-F3F5-4F21-8EB0-F7A30748715D |          7 | 2013-05-02 00:00:00.000 |          500    |              775 |         20130502 | Crippen & Co                | 1012 Princess Street     |            | Glasgow       |              | G1 8GH     |                          |                |           1 | Dealer       | Large        | 2009-10-15 00:00:00.000 |                1 |          0 |
|         333 | CF2E265F-BAF9-480E-B7F8-A5F874EA2134 |         26 | 2015-01-02 00:00:00.000 |           50    |              400 |         20150102 | Sporty Types Corp           | 13550 Market Street      |            | San Francisco | California   |            |                          | CA             |           3 | Wholesaler   | Large        | 2013-04-01 00:00:00.000 |                0 |          0 |
|         246 | 161441E2-080A-425E-86A4-12A6117792BC |          2 | 2015-07-02 00:00:00.000 |          200    |               25 |         20150702 | Honest John                 | 99a Baker Street         |            | London        |              | NSW1 1A    | Greater London Authority | EC             |           1 | Dealer       | Large        | 2000-01-01 00:00:00.000 |                0 |          0 |
|         417 | E180BB34-8C21-4BAB-AA1F-B6666515897A |         26 | 2015-01-02 00:00:00.000 |          150    |              -50 |         20150102 | Sporty Types Corp           | 13550 Market Street      |            | San Francisco | California   |            |                          | CA             |           3 | Wholesaler   | Large        | 2013-04-01 00:00:00.000 |                0 |          0 |
|         211 | AFCE8828-C9DA-4A4E-9783-1B8F9660F6A9 |          7 | 2015-08-02 00:00:00.000 |          550    |              425 |         20150802 | Crippen & Co                | 1012 Princess Street     |            | Glasgow       |              | G1 8GH     |                          |                |           1 | Dealer       | Large        | 2009-10-15 00:00:00.000 |                1 |          0 |
|         249 | 426289C9-45ED-4418-AF35-7C7310277651 |          8 | 2015-10-02 00:00:00.000 |          200    |               25 |         20151002 | Rocky Riding                | 5205 108th Ave           |            | New York      | New York     |            |                          | NY             |           3 | Dealer       | Large        | 2009-10-15 00:00:00.000 |                1 |          0 |
|         447 | 8C5BCF50-E0AF-4044-9434-D353C6189DDC |         24 | 2015-04-15 00:00:00.000 |         2550    |              250 |         20150415 | Style ‘N Ride               | 5404 Wisconsin Ave       |            | Chevy Chase   | Maryland     |            |                          | MA             |           3 | Dealer       | Large        | 2013-04-01 00:00:00.000 |                1 |          0 |
|           1 | 8B3D7F83-F42C-4523-A737-CDCBF7705B77 |          1 | 2012-10-04 00:00:00.000 |          500    |              750 |         20121004 | Aldo Motors                 | 4, Scale Street          |            | Uttoxeter     | Staffs       | ST17 99RZ  | East Midlands            | ST             |           1 | Wholesaler   | Large        | 1998-01-04 00:00:00.000 |                1 |          1 |
|          71 | 876F8F73-BF6B-496B-A022-9DA0D622DBC6 |          8 | 2012-09-01 00:00:00.000 |          500    |              775 |         20120901 | Rocky Riding                | 5205 108th Ave           |            | New York      | New York     |            |                          | NY             |           3 | Dealer       | Large        | 2009-10-15 00:00:00.000 |                1 |          0 |
|         263 | 108244C3-96AB-4EFE-A3C0-93AB8CB60DA2 |          4 | 2015-12-02 00:00:00.000 |          200    |               25 |         20151202 | Cut'n'Shut                  | Grange Avenue            |            | Manchester    |              | M1 5AZ     | North West               | M              |           1 | Dealer       | Small        | 2010-01-01 00:00:00.000 |                1 |          0 |
|         458 | 54C176DE-35B7-4DB9-8BAE-0321704E1F97 |         22 | 2015-11-26 00:00:00.000 |          800    |              875 |         20151126 | Ambassador Cars             | 11 Times Square          |            | Bellevue      | Washington   |            |                          | WA             |           3 | Dealer       | Small        | 2013-04-01 00:00:00.000 |                1 |          0 |
|          40 | 13E5C30E-155B-4EAF-9246-C392C613A116 |          8 | 2012-02-01 00:00:00.000 |          500    |              450 |         20120201 | Rocky Riding                | 5205 108th Ave           |            | New York      | New York     |            |                          | NY             |           3 | Dealer       | Large        | 2009-10-15 00:00:00.000 |                1 |          0 |
|         209 | A12CAAB5-D008-475F-8BE6-FB8541077EBC |          9 | 2015-06-02 00:00:00.000 |          550    |              425 |         20150602 | Voitures Diplomatiques S.A. |                          |            | Geneva        |              |            |                          |                |           6 | Wholesaler   | Large        | 2009-10-15 00:00:00.000 |                1 |          0 |
|         306 | 45275E14-7807-4788-BD7D-1E505F8AB515 |         19 | 2015-11-27 00:00:00.000 |          550    |              950 |         20151127 | Carosse Des Papes           |                          |            | Avignon       |              | 84000      |                          |                |           2 | Wholesaler   | Large        | 2012-01-01 00:00:00.000 |                1 |          0 |
|          73 | 7C1BD830-524C-4B84-8036-32F84DC89C70 |          1 | 2012-11-01 00:00:00.000 |          500    |              450 |         20121101 | Aldo Motors                 | 4, Scale Street          |            | Uttoxeter     | Staffs       | ST17 99RZ  | East Midlands            | ST             |           1 | Wholesaler   | Large        | 1998-01-04 00:00:00.000 |                1 |          1 |
|          83 | F636F5F0-BF2A-4231-8FC5-F61DD393BBA6 |          6 | 2013-09-02 00:00:00.000 |         1250    |              450 |         20130902 | Les Arnaqueurs              | 33, Rue Des Bleus        |            | Paris         |              | 75010      |                          |                |           2 | Dealer       | Large        | 2003-02-15 00:00:00.000 |                1 |          0 |
|         127 | CA859D0B-4B26-48C0-80C6-A7416D1F51BE |          3 | 2013-05-02 00:00:00.000 |          150    |               50 |         20130502 | Bright Orange               | 17, Arcadia Way          |            | Birmingham    |              | B1 50AZ    | West Midlands            | B              |           1 | Dealer       | Large        | 2005-04-01 00:00:00.000 |                0 |          0 |
|          10 | CFC6726D-1522-4981-BC6B-766AE2C6EED0 |          1 | 2012-09-04 00:00:00.000 |            0    |             1000 |         20120904 | Aldo Motors                 | 4, Scale Street          |            | Uttoxeter     | Staffs       | ST17 99RZ  | East Midlands            | ST             |           1 | Wholesaler   | Large        | 1998-01-04 00:00:00.000 |                1 |          1 |
|          56 | 59D9B6B2-00BF-4B0F-859C-9DC53A13EDB0 |          9 | 2013-06-02 00:00:00.000 |          500    |              450 |         20130602 | Voitures Diplomatiques S.A. |                          |            | Geneva        |              |            |                          |                |           6 | Wholesaler   | Large        | 2009-10-15 00:00:00.000 |                1 |          0 |
|         232 | 3CC94853-8794-46CE-8D41-B9C45C1B4AC5 |          7 | 2015-05-02 00:00:00.000 |          550    |              750 |         20150502 | Crippen & Co                | 1012 Princess Street     |            | Glasgow       |              | G1 8GH     |                          |                |           1 | Dealer       | Large        | 2009-10-15 00:00:00.000 |                1 |          0 |
|         454 | FAE8C854-586E-49DD-8994-81C49D4D447D |         26 | 2015-07-22 00:00:00.000 |         1050    |              175 |         20150722 | Sporty Types Corp           | 13550 Market Street      |            | San Francisco | California   |            |                          | CA             |           3 | Wholesaler   | Large        | 2013-04-01 00:00:00.000 |                0 |          0 |
|         295 | 6FBA0BC3-1BA1-41F6-96DD-1D9F1C60C79C |         19 | 2015-04-16 00:00:00.000 |         1300    |              325 |         20150416 | Carosse Des Papes           |                          |            | Avignon       |              | 84000      |                          |                |           2 | Wholesaler   | Large        | 2012-01-01 00:00:00.000 |                1 |          0 |
|         380 | 02C5476A-F229-4308-8C56-C07D917C375B |         23 | 2014-12-01 00:00:00.000 |          550    |              350 |         20141201 | Embassy Motors              | 57595 Technology Way     |            | Denver        | Colorado     |            |                          | CO             |           3 | Dealer       | Small        | 2013-04-01 00:00:00.000 |                1 |          0 |
|         322 | 9CD3E1D7-C76E-4A7A-B315-56A7D9962D6E |         26 | 2015-02-02 00:00:00.000 |           50    |             1650 |         20150202 | Sporty Types Corp           | 13550 Market Street      |            | San Francisco | California   |            |                          | CA             |           3 | Wholesaler   | Large        | 2013-04-01 00:00:00.000 |                0 |          0 |
|         409 | 34E84A5D-EFF3-4AB3-B3D8-31E0EBCAB799 |         25 | 2015-05-02 00:00:00.000 |          200    |              -50 |         20150502 | BritWheels                  | 1414 NW Northrup Street  |            | Portland      | Oregon       |            |                          | OR             |           3 | Dealer       | Large        | 2013-04-01 00:00:00.000 |                0 |          1 |
|         250 | 1ACB5F7C-7FC1-4AA0-811F-1D87C53AD2DD |          5 | 2015-11-02 00:00:00.000 |          200    |               25 |         20151102 | Wheels'R'Us                 | Buckingham Drive         |            | London        |              | SE1 4YY    | Greater London Authority | NE             |           1 | Dealer       | Large        | 2007-05-31 00:00:00.000 |                1 |          1 |
|          78 | 9C4F7810-8B87-4D91-B73F-817354FCE5F5 |          6 | 2013-04-02 00:00:00.000 |          500    |              775 |         20130402 | Les Arnaqueurs              | 33, Rue Des Bleus        |            | Paris         |              | 75010      |                          |                |           2 | Dealer       | Large        | 2003-02-15 00:00:00.000 |                1 |          0 |
|         324 | 250876E8-0EC1-4E7D-9764-233FC5CA03B6 |         24 | 2015-04-02 00:00:00.000 |           50    |              400 |         20150402 | Style ‘N Ride               | 5404 Wisconsin Ave       |            | Chevy Chase   | Maryland     |            |                          | MA             |           3 | Dealer       | Large        | 2013-04-01 00:00:00.000 |                1 |          0 |
|         429 | 35EAF044-B0BA-45A4-A5F7-F2F64B84DD96 |         28 | 2015-01-02 00:00:00.000 |          150    |              -50 |         20150102 | Union Jack Sports Cars      | 9900 Corporate Campus Dr |            | Louisville    | Kentucky     |            |                          | KY             |           3 | Dealer       | Small        | 2013-04-01 00:00:00.000 |                0 |          0 |
|         390 | 09D2948D-7D1D-4EE1-9197-C76903D78D4B |         26 | 2015-10-02 00:00:00.000 |         1050    |              350 |         20151002 | Sporty Types Corp           | 13550 Market Street      |            | San Francisco | California   |            |                          | CA             |           3 | Wholesaler   | Large        | 2013-04-01 00:00:00.000 |                0 |          0 |
|         169 | C8BE0F19-9213-4CA4-9437-8B04F4045241 |          5 | 2015-02-02 00:00:00.000 |           50    |             1725 |         20150202 | Wheels'R'Us                 | Buckingham Drive         |            | London        |              | SE1 4YY    | Greater London Authority | NE             |           1 | Dealer       | Large        | 2007-05-31 00:00:00.000 |                1 |          1 |
|          80 | F481DD95-1694-4BBC-BFAC-76002D88CEF2 |          8 | 2013-06-02 00:00:00.000 |          500    |              500 |         20130602 | Rocky Riding                | 5205 108th Ave           |            | New York      | New York     |            |                          | NY             |           3 | Dealer       | Large        | 2009-10-15 00:00:00.000 |                1 |          0 |
|         275 | B7146A2D-DC47-498E-BF34-FFB95E4DFC01 |          1 | 2015-12-02 00:00:00.000 |          200    |               25 |         20151202 | Aldo Motors                 | 4, Scale Street          |            | Uttoxeter     | Staffs       | ST17 99RZ  | East Midlands            | ST             |           1 | Wholesaler   | Large        | 1998-01-04 00:00:00.000 |                1 |          1 |
|         413 | 283CA979-A592-48A0-A3AD-90FB2F6265BA |         23 | 2015-09-02 00:00:00.000 |          200    |              -50 |         20150902 | Embassy Motors              | 57595 Technology Way     |            | Denver        | Colorado     |            |                          | CO             |           3 | Dealer       | Small        | 2013-04-01 00:00:00.000 |                1 |          0 |
|          77 | 5A3DE169-4DDE-4E5D-8110-80C7207289DA |          5 | 2013-03-02 00:00:00.000 |          500    |              775 |         20130302 | Wheels'R'Us                 | Buckingham Drive         |            | London        |              | SE1 4YY    | Greater London Authority | NE             |           1 | Dealer       | Large        | 2007-05-31 00:00:00.000 |                1 |          1 |
|         238 | C91ABD7D-5247-4750-8847-72372D2A6CA6 |          2 | 2015-11-02 00:00:00.000 |         1050    |              425 |         20151102 | Honest John                 | 99a Baker Street         |            | London        |              | NSW1 1A    | Greater London Authority | EC             |           1 | Dealer       | Large        | 2000-01-01 00:00:00.000 |                0 |          0 |
|         425 | D466E36A-D90E-4552-9757-20FA06EF6A1E |         22 | 2015-09-02 00:00:00.000 |          200    |              -50 |         20150902 | Ambassador Cars             | 11 Times Square          |            | Bellevue      | Washington   |            |                          | WA             |           3 | Dealer       | Small        | 2013-04-01 00:00:00.000 |                1 |          0 |
|          74 | F297C073-09FB-4BDE-810A-A3F12137378A |          2 | 2012-12-01 00:00:00.000 |          500    |              450 |         20121201 | Honest John                 | 99a Baker Street         |            | London        |              | NSW1 1A    | Greater London Authority | EC             |           1 | Dealer       | Large        | 2000-01-01 00:00:00.000 |                0 |          0 |


````

### Model Response

```
```json
{
  "Functional-Dependency": [
    ["InvoiceID", "InvoiceNumber"],
    ["ClientID", "ClientName"],
    ["ClientID", "Address1"],
    ["ClientID", "Address2"],
    ["ClientID", "Town"],
    ["ClientID", "County"],
    ["ClientID", "PostCode"],
    ["ClientID", "Region"],
    ["ClientID", "OuterPostode"],
    ["ClientID", "CountryID"],
    ["ClientID", "ClientType"],
    ["ClientID", "ClientSize"],
    ["ClientID", "ClientSince"],
    ["ClientID", "IsCreditWorthy"],
    ["ClientID", "IsDealer"],
    ["InvoiceDate", "InvoiceDateKey"]
  ]
}
```
```

### Correct Answer

```
{
  "Functional-Dependency": [
    [
      "ClientID",
      "ClientName"
    ],
    [
      "ClientID",
      "Address1"
    ],
    [
      "ClientID",
      "Town"
    ],
    [
      "ClientID",
      "County"
    ],
    [
      "ClientID",
      "PostCode"
    ],
    [
      "ClientID",
      "Region"
    ],
    [
      "ClientID",
      "OuterPostode"
    ],
    [
      "ClientID",
      "CountryID"
    ],
    [
      "ClientID",
      "ClientType"
    ],
    [
      "ClientID",
      "ClientSize"
    ],
    [
      "ClientID",
      "ClientSince"
    ],
    [
      "ClientID",
      "IsCreditWorthy"
    ],
    [
      "ClientID",
      "IsDealer"
    ]
  ]
}
```

