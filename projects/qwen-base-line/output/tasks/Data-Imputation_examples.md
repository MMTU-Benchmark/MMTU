# Data-Imputation: All Questions (9 total)

**Model:** Qwen2.5-7B-Instruct

---

## Question 1: case_207 (WebTable)

**Dataset:** WebTable  
**Test case:** case_207  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

Input Table:
|   Year | Date        | Winning Team                  |   Score | Losing Team                   | Location             |
|-------:|:------------|:------------------------------|--------:|:------------------------------|:---------------------|
|   1946 | December 14 | Compton College               |       0 | Kilgore College, TX           | Pasadena, California |
|   1947 | December 13 | Chaffey College               |      26 | 'Cameron College, OK          | Pasadena, California |
|   1948 | December 11 | Compton College               |      14 | Duluth Junior College, MN     | Pasadena, California |
|   1949 | December 10 | Little Rock Jr. College, AR   |      19 | Santa Ana College             | Pasadena, California |
|   1950 | December 9  | Long Beach City College       |      13 | Boise Junior College, ID      | Pasadena, California |
|   1951 | December 8  | Pasadena City College         |      26 | Tyler Junior College, TX      | Pasadena, California |
|   1952 | December 13 | Hartnell College, CA          |      20 | Bacone Junior College, OK     | Pasadena, California |
|   1953 | December 12 | Bakersfield College           |       6 | Northeastern Oklahoma A&M     | Pasadena, California |
|   1954 | December 11 | Hinds Junior College, MS      |       7 | El Camino College             | Pasadena, California |
|   1955 | December 10 | Compton College               |      13 | Jones Co. Jr. College, MS     | Pasadena, California |
|   1956 | December 8  | Arlington Junior College, TX  |      13 | Compton College               | Pasadena, California |
|   1957 | December 14 | Arlington Junior College, TX  |      12 | Cerritos College              | Pasadena, California |
|   1958 | December 13 | Santa Monica College          |      12 | Northeastern Oklahoma A&M     | Pasadena, California |
|   1959 | December 12 | Bakersfield College           |      14 | Del Mar College, TX           | Pasadena, California |
|   1960 | December 10 | Long Beach City College       |      16 | Tyler Junior College, TX      | Pasadena, California |
|   1961 | December 9  | Cameron College, OK           |      20 | Bakersfield College           | Pasadena, California |
|   1962 | December 8  | Santa Ana College             |       0 | Columbia Basin College, WA    | Pasadena, California |
|   1963 | December 14 | Orange Coast College          |       0 | Northeastern Oklahoma A&M     | Pasadena, California |
|   1964 | December 12 | Long Beach City College       |       6 | Cameron College, OK           | Pasadena, California |
|   1965 | December 11 | Fullerton College             |      15 | Henderson Co. Jr. College, TX | Pasadena, California |
|   1966 | December 10 | Henderson Co. Jr. College, TX |      13 | Pasadena City College         | Pasadena, California |
|   1967 | [MISSING]   | West Texas State              |      13 | San Fernando Valley State     | Pasadena, California |
|   1968 | December 7  | Grambling                     |       7 | Sacramento State              | Pasadena, California |
|   1969 | December 6  | San Diego State               |       7 | Boston University             | Pasadena, California |
|   1970 | December 19 | Louisville (tie)              |      24 | Long Beach State (tie)        | Pasadena, California |
|   1971 | December 18 | Memphis State                 |       9 | San Jose State                | Pasadena, California |
|   1976 | December 11 | Bakersfield College           |      14 | Ellsworth CC, IA              | Pasadena, California |
|   1977 | December 10 | Pasadena City College         |       9 | Jones County JC, MS           | Pasadena, California |


````

### Model Response

```
{"value": "December 9"}
```

### Correct Answer

```
{
  "value": "December 2"
}
```


---

## Question 2: case_414 (tablib)

**Dataset:** tablib  
**Test case:** case_414  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

Input Table:
| Name                | Position                      | Office        | Age       | Start date   | Salary     |
|:--------------------|:------------------------------|:--------------|:----------|:-------------|:-----------|
| Tiger Nixon         | System Architect              | Edinburgh     | 61        | 2011/04/25   | $320,800   |
| Garrett Winters     | Accountant                    | Tokyo         | 63        | 2011/07/25   | $170,750   |
| Ashton Cox          | Junior Technical Author       | San Francisco | 66        | 2009/01/12   | $86,000    |
| Cedric Kelly        | Senior Javascript Developer   | Edinburgh     | 22        | 2012/03/29   | $433,060   |
| Airi Satou          | Accountant                    | Tokyo         | 33        | 2008/11/28   | $162,700   |
| Brielle Williamson  | Integration Specialist        | New York      | 61        | 2012/12/02   | $372,000   |
| Herrod Chandler     | Sales Assistant               | San Francisco | 59        | 2012/08/06   | $137,500   |
| Rhona Davidson      | Integration Specialist        | Tokyo         | 55        | 2010/10/14   | $327,900   |
| Colleen Hurst       | Javascript Developer          | San Francisco | 39        | 2009/09/15   | $205,500   |
| Sonya Frost         | Software Engineer             | Edinburgh     | 23        | 2008/12/13   | $103,600   |
| Jena Gaines         | Office Manager                | London        | 30        | 2008/12/19   | $90,560    |
| Quinn Flynn         | Support Lead                  | Edinburgh     | 22        | 2013/03/03   | $342,000   |
| Charde Marshall     | Regional Director             | San Francisco | 36        | 2008/10/16   | $470,600   |
| Haley Kennedy       | Senior Marketing Designer     | London        | 43        | 2012/12/18   | $313,500   |
| Tatyana Fitzpatrick | Regional Director             | London        | 19        | 2010/03/17   | $385,750   |
| Michael Silva       | Marketing Designer            | London        | 66        | 2012/11/27   | $198,500   |
| Paul Byrd           | Chief Financial Officer (CFO) | New York      | 64        | 2010/06/09   | $725,000   |
| Gloria Little       | Systems Administrator         | New York      | 59        | 2009/04/10   | $237,500   |
| Bradley Greer       | Software Engineer             | London        | 41        | 2012/10/13   | $132,000   |
| Dai Rios            | Personnel Lead                | Edinburgh     | 35        | 2012/09/26   | $217,500   |
| Jenette Caldwell    | Development Lead              | New York      | 30        | 2011/09/03   | $345,000   |
| Yuri Berry          | Chief Marketing Officer (CMO) | New York      | 40        | 2009/06/25   | $675,000   |
| Caesar Vance        | Pre-Sales Support             | New York      | 21        | 2011/12/12   | $106,450   |
| Doris Wilder        | Sales Assistant               | Sidney        | 23        | 2010/09/20   | $85,600    |
| Angelica Ramos      | Chief Executive Officer (CEO) | London        | 47        | 2009/10/09   | $1,200,000 |
| Gavin Joyce         | Developer                     | Edinburgh     | 42        | 2010/12/22   | $92,575    |
| Jennifer Chang      | Regional Director             | Singapore     | 28        | 2010/11/14   | $357,650   |
| Brenden Wagner      | Software Engineer             | San Francisco | 28        | 2011/06/07   | $206,850   |
| Fiona Green         | Chief Operating Officer (COO) | San Francisco | 48        | 2010/03/11   | $850,000   |
| Shou Itou           | Regional Marketing            | Tokyo         | 20        | 2011/08/14   | $163,000   |
| Michelle House      | Integration Specialist        | Sidney        | 37        | 2011/06/02   | $95,400    |
| Suki Burks          | Developer                     | London        | 53        | 2009/10/22   | $114,500   |
| Prescott Bartlett   | Technical Author              | London        | 27        | 2011/05/07   | $145,000   |
| Gavin Cortez        | Team Leader                   | San Francisco | 22        | 2008/10/26   | $235,500   |
| Martena Mccray      | Post-Sales support            | Edinburgh     | 46        | 2011/03/09   | $324,050   |
| Unity Butler        | Marketing Designer            | San Francisco | 47        | 2009/12/09   | $85,675    |
| Howard Hatfield     | Office Manager                | San Francisco | 51        | 2008/12/16   | $164,500   |
| Hope Fuentes        | Secretary                     | San Francisco | 41        | 2010/02/12   | $109,850   |
| Vivian Harrell      | Financial Controller          | San Francisco | 62        | 2009/02/14   | $452,500   |
| Timothy Mooney      | Office Manager                | London        | 37        | 2008/12/11   | $136,200   |
| Jackson Bradshaw    | Director                      | New York      | 65        | 2008/09/26   | $645,750   |
| Olivia Liang        | Support Engineer              | Singapore     | 64        | 2011/02/03   | $234,500   |
| Bruno Nash          | Software Engineer             | London        | 38        | 2011/05/03   | $163,500   |
| Sakura Yamamoto     | Support Engineer              | Tokyo         | 37        | 2009/08/19   | $139,575   |
| Thor Walton         | Developer                     | New York      | 61        | 2013/08/11   | $98,540    |
| Finn Camacho        | Support Engineer              | San Francisco | 47        | 2009/07/07   | $87,500    |
| Serge Baldwin       | Data Coordinator              | Singapore     | 64        | 2012/04/09   | $138,575   |
| Zenaida Frank       | Software Engineer             | New York      | 63        | 2010/01/04   | $125,250   |
| Zorita Serrano      | Software Engineer             | San Francisco | [MISSING] | 2012/06/01   | $115,000   |
| Jennifer Acosta     | Junior Javascript Developer   | Edinburgh     | 43        | 2013/02/01   | $75,650    |
| Cara Stevens        | Sales Assistant               | New York      | 46        | 2011/12/06   | $145,600   |
| Hermione Butler     | Regional Director             | London        | 47        | 2011/03/21   | $356,250   |
| Lael Greer          | Systems Administrator         | London        | 21        | 2009/02/27   | $103,500   |
| Jonas Alexander     | Developer                     | San Francisco | 30        | 2010/07/14   | $86,500    |
| Shad Decker         | Regional Director             | Edinburgh     | 51        | 2008/11/13   | $183,000   |
| Michael Bruce       | Javascript Developer          | Singapore     | 29        | 2011/06/27   | $183,000   |
| Donna Snider        | Customer Support              | New York      | 27        | 2011/01/25   | $112,000   |
| Name                | Position                      | Office        | Age       | Start date   | Salary     |


````

### Model Response

```
{"value": 25}
```

### Correct Answer

```
{
  "value": "56"
}
```


---

## Question 3: case_518 (tablib)

**Dataset:** tablib  
**Test case:** case_518  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

Input Table:
| Unnamed: 0   |   연도 (년) |   추계인구(명) |   출생자수(명) |   사망자수(명) |   자연증가수(명) |   조출생률(%) |   조사망률(%) |   자연증가율(%) |   합계출산율(%) |
|:-------------|------------:|---------------:|---------------:|---------------:|-----------------:|--------------:|--------------:|----------------:|----------------:|
| 0            |        1925 |    1.29976e+07 |         558897 |         359042 |           199855 |          43   |          27.6 |            15.4 |            6.59 |
| 1            |        1926 |    1.30527e+07 |         511667 |         337948 |           173719 |          39.2 |          25.9 |            13.3 |          nan    |
| [MISSING]    |        1927 |    1.30372e+07 |         534524 |         353818 |           180706 |          41   |          27.1 |            13.9 |          nan    |
| 3            |        1928 |    1.31051e+07 |         566142 |         357701 |           208441 |          43.2 |          27.3 |            15.9 |          nan    |
| 4            |        1929 |    1.31243e+07 |         566969 |         414366 |           152603 |          43.2 |          31.6 |            11.6 |          nan    |
| 5            |        1930 |    1.38805e+07 |         587144 |         322611 |           264533 |          42.3 |          23.2 |            19.1 |            6.41 |
| 6            |        1931 |    1.38951e+07 |         589428 |         346800 |           242628 |          42.4 |          25   |            17.4 |          nan    |
| 7            |        1932 |    1.41172e+07 |         600545 |         384287 |           216258 |          42.5 |          27.2 |            15.3 |          nan    |
| 8            |        1933 |    1.42293e+07 |         607021 |         336232 |           270789 |          42.7 |          23.6 |            19.1 |          nan    |
| 9            |        1934 |    1.44492e+07 |         618135 |         356515 |           261620 |          42.8 |          24.7 |            18.1 |          nan    |
| 10           |        1935 |    1.5062e+07  |         646158 |         377454 |           268704 |          42.9 |          25.1 |            17.8 |            6.6  |
| 11           |        1936 |    1.51148e+07 |         639355 |         381806 |           257549 |          42.3 |          25.3 |            17   |          nan    |
| 12           |        1937 |    1.52354e+07 |         636839 |         342575 |           294264 |          41.8 |          22.5 |            19.3 |          nan    |
| 13           |        1938 |    1.53582e+07 |         569299 |         347025 |           222274 |          37.1 |          22.6 |            14.5 |          nan    |
| 14           |        1939 |    1.5486e+07  |         585482 |         353391 |           232091 |          37.8 |          22.8 |            15   |          nan    |
| 15           |        1940 |    1.55597e+07 |         527964 |         358496 |           169468 |          33.9 |          23   |            10.9 |            6.56 |
| 16           |        1941 |    1.57455e+07 |         553690 |         366239 |           187451 |          35.2 |          23.3 |            11.9 |          nan    |
| 17           |        1942 |    1.60137e+07 |         533768 |         376003 |           157765 |          33.3 |          23.5 |             9.8 |          nan    |
| 18           |        1943 |    1.62397e+07 |         513846 |         384881 |           128965 |          31.6 |          23.7 |             7.9 |          nan    |
| 19           |        1944 |    1.65992e+07 |         533215 |         380121 |           153094 |          32.1 |          22.9 |             9.2 |            6.78 |
| 20           |        1945 |    1.66958e+07 |         544786 |         367308 |           177478 |          32.6 |          22   |            10.6 |          nan    |
| 21           |        1946 |    1.93693e+07 |         590763 |         410629 |           180134 |          30.5 |          21.2 |             9.3 |          nan    |
| 22           |        1947 |    1.98362e+07 |         686334 |         361019 |           325315 |          35   |          18.2 |            16.8 |          nan    |
| 23           |        1948 |    2.00274e+07 |         692948 |         374512 |           318436 |          34.6 |          18.7 |            15.9 |          nan    |
| 24           |        1949 |    2.01886e+07 |         696508 |         341188 |           355320 |          34.5 |          16.9 |            17.6 |          nan    |
| 25           |        1950 |    1.92114e+07 |         633976 |         597474 |            36502 |          33   |          31.1 |             1.9 |            5.05 |
| 26           |        1951 |    1.93047e+07 |         675666 |         579142 |            96524 |          35   |          30   |             5   |          nan    |
| 27           |        1952 |    1.95669e+07 |         722018 |         457865 |           264153 |          36.9 |          23.4 |            13.5 |          nan    |
| 28           |        1953 |    1.99791e+07 |         777186 |         363619 |           413567 |          38.9 |          18.2 |            20.7 |          nan    |
| 29           |        1954 |    2.05206e+07 |         839293 |         348850 |           490433 |          40.9 |          17   |            23.9 |          nan    |
| 30           |        1955 |    2.11686e+07 |         908134 |         295302 |           612832 |          42.9 |          14   |            28.9 |            6.33 |
| 31           |        1956 |    2.18979e+07 |         945990 |         294344 |           651646 |          43.2 |          13.4 |            29.8 |          nan    |
| 32           |        1957 |    2.26812e+07 |         963952 |         293344 |           670608 |          42.5 |          12.9 |            29.6 |          nan    |

... (44 rows omitted) ...

| 77           |        2002 |    4.76447e+07 |         492111 |         245317 |           246794 |          10.2 |           5.1 |             5.1 |            1.17 |
| 78           |        2003 |    4.78923e+07 |         490543 |         244506 |           246037 |          10.2 |           5.1 |             5.1 |            1.18 |
| 79           |        2004 |    4.80825e+07 |         472761 |         244217 |           228544 |           9.8 |           5   |             4.7 |            1.15 |
| 80           |        2005 |    4.81846e+07 |         435031 |         243883 |           191148 |           8.9 |           5   |             3.9 |            1.08 |
| 81           |        2006 |    4.84383e+07 |         448153 |         242266 |           205887 |           9.2 |           5   |             4.2 |            1.12 |
| 82           |        2007 |    4.86836e+07 |         493189 |         244874 |           248315 |          10   |           5   |             5.1 |            1.25 |
| 83           |        2008 |    4.90547e+07 |         465892 |         246113 |           219779 |           9.4 |           5   |             4.4 |            1.19 |
| 84           |        2009 |    4.93078e+07 |         444849 |         246942 |           197907 |           9   |           5   |             4   |            1.15 |
| 85           |        2010 |    4.95541e+07 |         470171 |         255405 |           214766 |           9.4 |           5.1 |             4.3 |            1.23 |
| 86           |        2011 |    4.99366e+07 |         471265 |         257396 |           213869 |           9.4 |           5.1 |             4.3 |            1.24 |
| 87           |        2012 |    5.01999e+07 |         484550 |         267300 |           217000 |           9.6 |           5.3 |             4.3 |            1.3  |
| 88           |        2013 |    5.04289e+07 |         436455 |         266257 |           170198 |           8.6 |           5.3 |             3.4 |            1.19 |
| 89           |        2014 |    5.07467e+07 |         435435 |         267692 |           167743 |           8.6 |           5.3 |             3.3 |            1.21 |
| 90           |        2015 |    5.10149e+07 |         438420 |         275895 |           162925 |           8.6 |           5.4 |             3.2 |            1.24 |
| 91           |        2016 |    5.12457e+07 |         406243 |         280827 |           125416 |           7.9 |           5.5 |             2.4 |            1.17 |
| 92           |        2017 |    5.14462e+07 |         357771 |         285534 |            72237 |           7   |           5.5 |             1.5 |            1.05 |
| 93           |        2018 |    5.16353e+07 |         326822 |         298820 |            28002 |           6.4 |           5.8 |             0.6 |            0.98 |
| 94           |        2019 |  nan           |         303054 |         295132 |             7922 |           5.9 |           5.7 |             0.2 |            0.92 |


````

### Model Response

```
{"value": 3}
```

### Correct Answer

```
{
  "value": "2"
}
```


---

## Question 4: case_851 (tablib)

**Dataset:** tablib  
**Test case:** case_851  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

Input Table:
| First name   | Last name   | Position                      | Office        |   Age | Start date   | Salary     | Extn.     | E-mail                       |
|:-------------|:------------|:------------------------------|:--------------|------:|:-------------|:-----------|:----------|:-----------------------------|
| Tiger        | Nixon       | System Architect              | Edinburgh     |    61 | 2011/04/25   | $320,800   | 5421      | t.nixon@datatables.net       |
| Garrett      | Winters     | Accountant                    | Tokyo         |    63 | 2011/07/25   | $170,750   | 8422      | g.winters@datatables.net     |
| Ashton       | Cox         | Junior Technical Author       | San Francisco |    66 | 2009/01/12   | $86,000    | 1562      | a.cox@datatables.net         |
| Cedric       | Kelly       | Senior Javascript Developer   | Edinburgh     |    22 | 2012/03/29   | $433,060   | 6224      | c.kelly@datatables.net       |
| Airi         | Satou       | Accountant                    | Tokyo         |    33 | 2008/11/28   | $162,700   | 5407      | a.satou@datatables.net       |
| Brielle      | Williamson  | Integration Specialist        | New York      |    61 | 2012/12/02   | $372,000   | 4804      | b.williamson@datatables.net  |
| Herrod       | Chandler    | Sales Assistant               | San Francisco |    59 | 2012/08/06   | $137,500   | 9608      | h.chandler@datatables.net    |
| Rhona        | Davidson    | Integration Specialist        | Tokyo         |    55 | 2010/10/14   | $327,900   | 6200      | r.davidson@datatables.net    |
| Colleen      | Hurst       | Javascript Developer          | San Francisco |    39 | 2009/09/15   | $205,500   | 2360      | c.hurst@datatables.net       |
| Sonya        | Frost       | Software Engineer             | Edinburgh     |    23 | 2008/12/13   | $103,600   | 1667      | s.frost@datatables.net       |
| Jena         | Gaines      | Office Manager                | London        |    30 | 2008/12/19   | $90,560    | 3814      | j.gaines@datatables.net      |
| Quinn        | Flynn       | Support Lead                  | Edinburgh     |    22 | 2013/03/03   | $342,000   | 9497      | q.flynn@datatables.net       |
| Charde       | Marshall    | Regional Director             | San Francisco |    36 | 2008/10/16   | $470,600   | [MISSING] | c.marshall@datatables.net    |
| Haley        | Kennedy     | Senior Marketing Designer     | London        |    43 | 2012/12/18   | $313,500   | 3597      | h.kennedy@datatables.net     |
| Tatyana      | Fitzpatrick | Regional Director             | London        |    19 | 2010/03/17   | $385,750   | 1965      | t.fitzpatrick@datatables.net |
| Michael      | Silva       | Marketing Designer            | London        |    66 | 2012/11/27   | $198,500   | 1581      | m.silva@datatables.net       |
| Paul         | Byrd        | Chief Financial Officer (CFO) | New York      |    64 | 2010/06/09   | $725,000   | 3059      | p.byrd@datatables.net        |
| Gloria       | Little      | Systems Administrator         | New York      |    59 | 2009/04/10   | $237,500   | 1721      | g.little@datatables.net      |
| Bradley      | Greer       | Software Engineer             | London        |    41 | 2012/10/13   | $132,000   | 2558      | b.greer@datatables.net       |
| Dai          | Rios        | Personnel Lead                | Edinburgh     |    35 | 2012/09/26   | $217,500   | 2290      | d.rios@datatables.net        |
| Jenette      | Caldwell    | Development Lead              | New York      |    30 | 2011/09/03   | $345,000   | 1937      | j.caldwell@datatables.net    |
| Yuri         | Berry       | Chief Marketing Officer (CMO) | New York      |    40 | 2009/06/25   | $675,000   | 6154      | y.berry@datatables.net       |
| Caesar       | Vance       | Pre-Sales Support             | New York      |    21 | 2011/12/12   | $106,450   | 8330      | c.vance@datatables.net       |
| Doris        | Wilder      | Sales Assistant               | Sidney        |    23 | 2010/09/20   | $85,600    | 3023      | d.wilder@datatables.net      |
| Angelica     | Ramos       | Chief Executive Officer (CEO) | London        |    47 | 2009/10/09   | $1,200,000 | 5797      | a.ramos@datatables.net       |
| Gavin        | Joyce       | Developer                     | Edinburgh     |    42 | 2010/12/22   | $92,575    | 8822      | g.joyce@datatables.net       |
| Jennifer     | Chang       | Regional Director             | Singapore     |    28 | 2010/11/14   | $357,650   | 9239      | j.chang@datatables.net       |
| Brenden      | Wagner      | Software Engineer             | San Francisco |    28 | 2011/06/07   | $206,850   | 1314      | b.wagner@datatables.net      |
| Fiona        | Green       | Chief Operating Officer (COO) | San Francisco |    48 | 2010/03/11   | $850,000   | 2947      | f.green@datatables.net       |
| Shou         | Itou        | Regional Marketing            | Tokyo         |    20 | 2011/08/14   | $163,000   | 8899      | s.itou@datatables.net        |
| Michelle     | House       | Integration Specialist        | Sidney        |    37 | 2011/06/02   | $95,400    | 2769      | m.house@datatables.net       |
| Suki         | Burks       | Developer                     | London        |    53 | 2009/10/22   | $114,500   | 6832      | s.burks@datatables.net       |
| Prescott     | Bartlett    | Technical Author              | London        |    27 | 2011/05/07   | $145,000   | 3606      | p.bartlett@datatables.net    |
| Gavin        | Cortez      | Team Leader                   | San Francisco |    22 | 2008/10/26   | $235,500   | 2860      | g.cortez@datatables.net      |
| Martena      | Mccray      | Post-Sales support            | Edinburgh     |    46 | 2011/03/09   | $324,050   | 8240      | m.mccray@datatables.net      |
| Unity        | Butler      | Marketing Designer            | San Francisco |    47 | 2009/12/09   | $85,675    | 5384      | u.butler@datatables.net      |
| Howard       | Hatfield    | Office Manager                | San Francisco |    51 | 2008/12/16   | $164,500   | 7031      | h.hatfield@datatables.net    |
| Hope         | Fuentes     | Secretary                     | San Francisco |    41 | 2010/02/12   | $109,850   | 6318      | h.fuentes@datatables.net     |
| Vivian       | Harrell     | Financial Controller          | San Francisco |    62 | 2009/02/14   | $452,500   | 9422      | v.harrell@datatables.net     |
| Timothy      | Mooney      | Office Manager                | London        |    37 | 2008/12/11   | $136,200   | 7580      | t.mooney@datatables.net      |
| Jackson      | Bradshaw    | Director                      | New York      |    65 | 2008/09/26   | $645,750   | 1042      | j.bradshaw@datatables.net    |
| Olivia       | Liang       | Support Engineer              | Singapore     |    64 | 2011/02/03   | $234,500   | 2120      | o.liang@datatables.net       |
| Bruno        | Nash        | Software Engineer             | London        |    38 | 2011/05/03   | $163,500   | 6222      | b.nash@datatables.net        |
| Sakura       | Yamamoto    | Support Engineer              | Tokyo         |    37 | 2009/08/19   | $139,575   | 9383      | s.yamamoto@datatables.net    |
| Thor         | Walton      | Developer                     | New York      |    61 | 2013/08/11   | $98,540    | 8327      | t.walton@datatables.net      |
| Finn         | Camacho     | Support Engineer              | San Francisco |    47 | 2009/07/07   | $87,500    | 2927      | f.camacho@datatables.net     |
| Serge        | Baldwin     | Data Coordinator              | Singapore     |    64 | 2012/04/09   | $138,575   | 8352      | s.baldwin@datatables.net     |
| Zenaida      | Frank       | Software Engineer             | New York      |    63 | 2010/01/04   | $125,250   | 7439      | z.frank@datatables.net       |
| Zorita       | Serrano     | Software Engineer             | San Francisco |    56 | 2012/06/01   | $115,000   | 4389      | z.serrano@datatables.net     |
| Jennifer     | Acosta      | Junior Javascript Developer   | Edinburgh     |    43 | 2013/02/01   | $75,650    | 3431      | j.acosta@datatables.net      |
| Cara         | Stevens     | Sales Assistant               | New York      |    46 | 2011/12/06   | $145,600   | 3990      | c.stevens@datatables.net     |
| Hermione     | Butler      | Regional Director             | London        |    47 | 2011/03/21   | $356,250   | 1016      | h.butler@datatables.net      |
| Lael         | Greer       | Systems Administrator         | London        |    21 | 2009/02/27   | $103,500   | 6733      | l.greer@datatables.net       |
| Jonas        | Alexander   | Developer                     | San Francisco |    30 | 2010/07/14   | $86,500    | 8196      | j.alexander@datatables.net   |
| Shad         | Decker      | Regional Director             | Edinburgh     |    51 | 2008/11/13   | $183,000   | 6373      | s.decker@datatables.net      |
| Michael      | Bruce       | Javascript Developer          | Singapore     |    29 | 2011/06/27   | $183,000   | 5384      | m.bruce@datatables.net       |
| Donna        | Snider      | Customer Support              | New York      |    27 | 2011/01/25   | $112,000   | 4226      | d.snider@datatables.net      |


````

### Model Response

```
{"value": "5797"}
```

### Correct Answer

```
{
  "value": "6741"
}
```


---

## Question 5: case_136 (tablib)

**Dataset:** tablib  
**Test case:** case_136  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

Input Table:
|   Participating Data Bits | ECC0   | ECC1   | ECC2   | ECC3      | ECC4   | ECC5   | ECC6   |
|--------------------------:|:-------|:-------|:-------|:----------|:-------|:-------|:-------|
|                         0 | *      | *      |        |           |        |        | *      |
|                         1 | *      |        | *      |           |        |        | *      |
|                         2 |        | *      | *      |           |        |        | *      |
|                         3 | *      | *      | *      |           |        |        |        |
|                         4 | *      |        |        | *         |        |        | *      |
|                         5 |        | *      |        | *         |        |        | *      |
|                         6 | *      | *      |        | *         |        |        |        |
|                         7 |        |        | *      | *         |        |        | *      |
|                         8 | *      |        | *      | *         |        |        |        |
|                         9 |        | *      | *      | *         |        |        |        |
|                        10 | *      | *      | *      | *         |        |        | *      |
|                        11 | *      |        |        |           | *      |        | *      |
|                        12 |        | *      |        |           | *      |        | *      |
|                        13 | *      | *      |        |           | *      |        |        |
|                        14 |        |        | *      |           | *      |        | *      |
|                        15 | *      |        | *      |           | *      |        |        |
|                        16 |        | *      | *      |           | *      |        |        |
|                        17 | *      | *      | *      | [MISSING] | *      |        | *      |
|                        18 |        |        |        | *         | *      |        | *      |
|                        19 | *      |        |        | *         | *      |        |        |
|                        20 |        | *      |        | *         | *      |        |        |
|                        21 | *      | *      |        | *         | *      |        | *      |
|                        22 |        |        | *      | *         | *      |        |        |
|                        23 | *      |        | *      | *         | *      |        | *      |
|                        24 |        | *      | *      | *         | *      |        | *      |
|                        25 | *      | *      | *      | *         | *      |        |        |
|                        26 | *      |        |        |           |        | *      | *      |
|                        27 |        | *      |        |           |        | *      | *      |
|                        28 | *      | *      |        |           |        | *      |        |
|                        29 |        |        | *      |           |        | *      | *      |
|                        30 | *      |        | *      |           |        | *      |        |
|                        31 |        | *      | *      |           |        | *      |        |


````

### Model Response

```
{"value": "*"}
```

### Correct Answer

```
{
  "value": ""
}
```


---

## Question 6: case_170 (WebTable)

**Dataset:** WebTable  
**Test case:** case_170  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

Input Table:
| Year            | Music                                           | Editing                                                    | Cinematography                                        | Sound Design                                | Art Direction                                                   | Visual Effects                                                                  |
|:----------------|:------------------------------------------------|:-----------------------------------------------------------|:------------------------------------------------------|:--------------------------------------------|:----------------------------------------------------------------|:--------------------------------------------------------------------------------|
| 1998            | nan                                             | nan                                                        | nan                                                   | nan                                         | Huang Wen-ying for Flowers of Shanghai                          | nan                                                                             |
| 1999            | nan                                             | nan                                                        | nan                                                   | nan                                         | nan                                                             | nan                                                                             |
| [MISSING]       | nan                                             | nan                                                        | nan                                                   | nan                                         | nan                                                             | nan                                                                             |
| 2001 (not held) | nan                                             | nan                                                        | nan                                                   | nan                                         | nan                                                             | nan                                                                             |
| 2002            | nan                                             | nan                                                        | nan                                                   | nan                                         | Tang Shu-fen, Jyu Zih and Jiang Wun-cih for A Garden in the Sky | nan                                                                             |
| 2003            | nan                                             | nan                                                        | nan                                                   | Nail                                        | nan                                                             | Dreams Are Floating                                                             |
| 2004            | nan                                             | nan                                                        | nan                                                   | nan                                         | nan                                                             | nan                                                                             |
| 2005            | nan                                             | nan                                                        | nan                                                   | nan                                         | nan                                                             | nan                                                                             |
| 2006            | nan                                             | nan                                                        | nan                                                   | nan                                         | nan                                                             | nan                                                                             |
| 2007            | nan                                             | nan                                                        | nan                                                   | nan                                         | nan                                                             | nan                                                                             |
| 2008            | Lu Sheng-fei and Luo Chii for Cape No. 7        | nan                                                        | Chin Ding-Chang for Cape No.7                         | nan                                         | Weng Kuei-pang for Orz Boyz                                     | nan                                                                             |
| 2009            | Lim Giong for Yang Yang                         | William Chang for Miao Miao                                | Kwan Pun Leung for Miao Miao                          | nan                                         | Huang Mei-chin for A Place of One's Own                         | nan                                                                             |
| 2010            | Summer Lei and Ho Zhi-jian for Taipei Exchanges | Kwan Pun-leung and Hsu Hung-yuan for Let The Wind Carry Me | Liao Peng-jung for Face                               | nan                                         | Huang Mei-chin and Chen Po-jen for Monga                        | nan                                                                             |
| 2011            | Chang Wu-wu for Honey Pupu                      | Lin Wei-chih and Ko Meng-rong for My Buddies               | Fisher Yu for Honey Pupu                              | nan                                         | Tseng Chia-chi for Libangbang                                   | nan                                                                             |
| 2012            | Soler for Young Dudes                           | Adong Chen for Cha Cha for Twins                           | Patrick Chow for Young Dudes                          | nan                                         | nan                                                             | Xiao Yang, Chang Song, A Law, Li Ming-hsung, Li Jin-hui for Starry Starry Night |
| 2013            | Tseng Si-ming for Soul                          | Huang Kuan-Chun for A Rolling Stone                        | Nagao Nakashima for Soul                              | nan                                         | nan                                                             | nan                                                                             |
| 2014            | nan                                             | Hung Chun-hsiu for The Lost Sea                            | Yao Hung-i for Pusu Qhuni                             | nan                                         | Huang Mei-ching for Zone Pro Site                               | Chen Ming-ho for Rock Rabbit                                                    |
| 2015            | nan                                             | Xu Wei-yao for A Life That Sings                           | Chen Hyin-gen and Chang Hao-jan for A Life That Sings | nan                                         | Huang Mei-ching for Paradise in Service                         | nan                                                                             |
| 2016            | Lim Giong for City of Jade                      | Kenji Chen for Hang in There, Kids!                        | Zhao Fei for The Left Ear                             | Huang Ya-li and Yannick Dauby for Le Moulin | nan                                                             | nan                                                                             |
| 2017            | Lin Sheng-xiang for The Great Buddha +          | Lai Hsiu-hsiung for The Great Buddha +                     | Yao Hung-i for Missing Johnny                         | nan                                         | Chao Shih-hao for The Great Buddha +                            | nan                                                                             |


````

### Model Response

```
{"value": 2000}
```

### Correct Answer

```
{
  "value": "2000"
}
```


---

## Question 7: case_241 (tablib)

**Dataset:** tablib  
**Test case:** case_241  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

Input Table:
| Unnamed: 0   | First name   | Last name   | Position                      | Office        | Age   | Start date   | Salary     | Extn.   |
|:-------------|:-------------|:------------|:------------------------------|:--------------|:------|:-------------|:-----------|:--------|
| nan          | Tiger        | Nixon       | System Architect              | Edinburgh     | 61    | 2011/04/25   | $320,800   | 5421    |
| nan          | Garrett      | Winters     | Accountant                    | Tokyo         | 63    | 2011/07/25   | $170,750   | 8422    |
| nan          | Ashton       | Cox         | Junior Technical Author       | San Francisco | 66    | 2009/01/12   | $86,000    | 1562    |
| nan          | Cedric       | Kelly       | Senior Javascript Developer   | Edinburgh     | 22    | 2012/03/29   | $433,060   | 6224    |
| nan          | Airi         | Satou       | Accountant                    | Tokyo         | 33    | 2008/11/28   | $162,700   | 5407    |
| nan          | Brielle      | Williamson  | Integration Specialist        | New York      | 61    | 2012/12/02   | $372,000   | 4804    |
| nan          | Herrod       | Chandler    | Sales Assistant               | San Francisco | 59    | 2012/08/06   | $137,500   | 9608    |
| nan          | Rhona        | Davidson    | Integration Specialist        | Tokyo         | 55    | 2010/10/14   | $327,900   | 6200    |
| nan          | Colleen      | Hurst       | Javascript Developer          | San Francisco | 39    | 2009/09/15   | $205,500   | 2360    |
| nan          | Sonya        | Frost       | Software Engineer             | Edinburgh     | 23    | 2008/12/13   | $103,600   | 1667    |
| nan          | Jena         | Gaines      | Office Manager                | London        | 30    | 2008/12/19   | $90,560    | 3814    |
| nan          | Quinn        | Flynn       | Support Lead                  | Edinburgh     | 22    | 2013/03/03   | $342,000   | 9497    |
| nan          | Charde       | Marshall    | Regional Director             | San Francisco | 36    | 2008/10/16   | $470,600   | 6741    |
| nan          | Haley        | Kennedy     | Senior Marketing Designer     | London        | 43    | 2012/12/18   | $313,500   | 3597    |
| nan          | Tatyana      | Fitzpatrick | Regional Director             | London        | 19    | 2010/03/17   | $385,750   | 1965    |
| nan          | Michael      | Silva       | Marketing Designer            | London        | 66    | 2012/11/27   | $198,500   | 1581    |
| nan          | Paul         | Byrd        | Chief Financial Officer (CFO) | New York      | 64    | 2010/06/09   | $725,000   | 3059    |
| nan          | Gloria       | Little      | Systems Administrator         | New York      | 59    | 2009/04/10   | $237,500   | 1721    |
| nan          | Bradley      | Greer       | Software Engineer             | London        | 41    | 2012/10/13   | $132,000   | 2558    |
| nan          | Dai          | Rios        | Personnel Lead                | Edinburgh     | 35    | 2012/09/26   | $217,500   | 2290    |
| nan          | Jenette      | Caldwell    | Development Lead              | New York      | 30    | 2011/09/03   | $345,000   | 1937    |
| nan          | Yuri         | Berry       | Chief Marketing Officer (CMO) | New York      | 40    | 2009/06/25   | $675,000   | 6154    |
| nan          | Caesar       | Vance       | Pre-Sales Support             | New York      | 21    | 2011/12/12   | $106,450   | 8330    |
| nan          | Doris        | Wilder      | Sales Assistant               | Sidney        | 23    | 2010/09/20   | $85,600    | 3023    |
| nan          | Angelica     | Ramos       | Chief Executive Officer (CEO) | London        | 47    | 2009/10/09   | $1,200,000 | 5797    |
| nan          | Gavin        | Joyce       | Developer                     | Edinburgh     | 42    | 2010/12/22   | $92,575    | 8822    |
| nan          | Jennifer     | Chang       | Regional Director             | Singapore     | 28    | 2010/11/14   | $357,650   | 9239    |
| nan          | Brenden      | Wagner      | Software Engineer             | San Francisco | 28    | 2011/06/07   | $206,850   | 1314    |
| nan          | Fiona        | Green       | Chief Operating Officer (COO) | San Francisco | 48    | 2010/03/11   | $850,000   | 2947    |
| nan          | Shou         | Itou        | Regional Marketing            | Tokyo         | 20    | 2011/08/14   | $163,000   | 8899    |
| nan          | Michelle     | House       | Integration Specialist        | Sidney        | 37    | 2011/06/02   | $95,400    | 2769    |
| nan          | Suki         | Burks       | Developer                     | London        | 53    | 2009/10/22   | $114,500   | 6832    |
| nan          | Prescott     | Bartlett    | Technical Author              | London        | 27    | 2011/05/07   | $145,000   | 3606    |
| nan          | Gavin        | Cortez      | Team Leader                   | San Francisco | 22    | 2008/10/26   | $235,500   | 2860    |
| nan          | Martena      | Mccray      | Post-Sales support            | Edinburgh     | 46    | 2011/03/09   | $324,050   | 8240    |
| nan          | Unity        | Butler      | Marketing Designer            | San Francisco | 47    | 2009/12/09   | $85,675    | 5384    |
| nan          | Howard       | Hatfield    | Office Manager                | San Francisco | 51    | 2008/12/16   | $164,500   | 7031    |
| nan          | Hope         | Fuentes     | Secretary                     | San Francisco | 41    | 2010/02/12   | $109,850   | 6318    |
| nan          | Vivian       | Harrell     | Financial Controller          | San Francisco | 62    | 2009/02/14   | $452,500   | 9422    |
| nan          | Timothy      | Mooney      | Office Manager                | London        | 37    | 2008/12/11   | $136,200   | 7580    |
| nan          | Jackson      | Bradshaw    | Director                      | New York      | 65    | 2008/09/26   | $645,750   | 1042    |
| nan          | Olivia       | Liang       | Support Engineer              | Singapore     | 64    | 2011/02/03   | $234,500   | 2120    |
| nan          | Bruno        | Nash        | Software Engineer             | London        | 38    | 2011/05/03   | $163,500   | 6222    |
| nan          | Sakura       | Yamamoto    | Support Engineer              | Tokyo         | 37    | 2009/08/19   | $139,575   | 9383    |
| nan          | Thor         | Walton      | Developer                     | New York      | 61    | 2013/08/11   | $98,540    | 8327    |
| nan          | Finn         | Camacho     | Support Engineer              | San Francisco | 47    | 2009/07/07   | $87,500    | 2927    |
| nan          | Serge        | Baldwin     | Data Coordinator              | Singapore     | 64    | 2012/04/09   | $138,575   | 8352    |
| nan          | Zenaida      | Frank       | Software Engineer             | New York      | 63    | 2010/01/04   | $125,250   | 7439    |
| [MISSING]    | Zorita       | Serrano     | Software Engineer             | San Francisco | 56    | 2012/06/01   | $115,000   | 4389    |
| nan          | Jennifer     | Acosta      | Junior Javascript Developer   | Edinburgh     | 43    | 2013/02/01   | $75,650    | 3431    |
| nan          | Cara         | Stevens     | Sales Assistant               | New York      | 46    | 2011/12/06   | $145,600   | 3990    |
| nan          | Hermione     | Butler      | Regional Director             | London        | 47    | 2011/03/21   | $356,250   | 1016    |
| nan          | Lael         | Greer       | Systems Administrator         | London        | 21    | 2009/02/27   | $103,500   | 6733    |
| nan          | Jonas        | Alexander   | Developer                     | San Francisco | 30    | 2010/07/14   | $86,500    | 8196    |
| nan          | Shad         | Decker      | Regional Director             | Edinburgh     | 51    | 2008/11/13   | $183,000   | 6373    |
| nan          | Michael      | Bruce       | Javascript Developer          | Singapore     | 29    | 2011/06/27   | $183,000   | 5384    |
| nan          | Donna        | Snider      | Customer Support              | New York      | 27    | 2011/01/25   | $112,000   | 4226    |
| nan          | First name   | Last name   | Position                      | Office        | Age   | Start date   | Salary     | Extn.   |


````

### Model Response

```
{"value": "Zorita"}
```

### Correct Answer

```
{
  "value": "nan"
}
```


---

## Question 8: case_888 (WebTable)

**Dataset:** WebTable  
**Test case:** case_888  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

Input Table:
| Academic Unit                              |   Undergrad. Rank |   Grad. Rank |
|:-------------------------------------------|------------------:|-------------:|
| College of Engineering (overall)           |                 9 |            9 |
| Aeronautical and Astronautical Engineering |                 4 |            6 |
| Agricultural and Biological Engineering    |                 1 |            1 |
| Biomedical Engineering                     |                18 |           22 |
| [MISSING]                                  |                13 |           15 |
| Civil Engineering                          |                 6 |            6 |
| Computer Engineering                       |                11 |            9 |
| Electrical Engineering                     |                 8 |            8 |
| Environmental Engineering                  |                13 |           18 |
| Industrial Engineering                     |                 3 |            9 |
| Materials Engineering                      |                11 |           15 |
| Mechanical Engineering                     |                 7 |            8 |
| Nuclear Engineering                        |                 4 |           10 |


````

### Model Response

```
{"value": "Chemical and Biological Engineering"}
```

### Correct Answer

```
{
  "value": "Chemical Engineering"
}
```


---

## Question 9: case_30 (WebTable)

**Dataset:** WebTable  
**Test case:** case_30  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Please fill in the missing value in the input table. The missing value is denoted by '[MISSING]'. Please only return the value filled in. Do not return the whole table.

No explanation, return the value filled in JSON format: {"value": "filled_value"}. 

Input Table:
| Year        | Program (Less Than One Hour)        | Episode                            | Network                | Program (One Hour or More)                   |
|:------------|:------------------------------------|:-----------------------------------|:-----------------------|:---------------------------------------------|
| 2000 (52nd) | The Simpsons                        | Special                            | Discovery Channel      | Walking With Dinosaurs                       |
| 2000 (52nd) | Downtown                            | Special                            | Fox                    | Olive, the Other Reindeer                    |
| 2000 (52nd) | Family Guy                          | nan                                | nan                    | nan                                          |
| 2000 (52nd) | The Powerpuff Girls                 | nan                                | nan                    | nan                                          |
| 2000 (52nd) | South Park                          | nan                                | nan                    | nan                                          |
| 2001 (53rd) | The Simpsons                        | Special                            | Discovery Channel      | Allosaurus: A Walking With Dinosaurs Special |
| 2001 (53rd) | As Told by Ginger                   | nan                                | nan                    | nan                                          |
| 2001 (53rd) | Futurama                            | nan                                | nan                    | nan                                          |
| 2001 (53rd) | King of the Hill                    | nan                                | nan                    | nan                                          |
| 2001 (53rd) | The Powerpuff Girls                 | nan                                | nan                    | nan                                          |
| 2002 (54th) | Futurama                            | Special                            | Discovery Channel      | Walking With Prehistoric Beasts              |
| 2002 (54th) | As Told by Ginger                   | The Trilogy                        | Cartoon Network        | Samurai Jack                                 |
| 2002 (54th) | King of the Hill                    | Special                            | Discovery Channel      | When Dinosaurs Roamed America                |
| 2002 (54th) | The Simpsons                        | nan                                | nan                    | nan                                          |
| 2002 (54th) | South Park                          | nan                                | nan                    | nan                                          |
| 2003 (55th) | The Simpsons                        | Special                            | Discovery Channel      | Chased by Dinosaurs                          |
| 2003 (55th) | As Told by Ginger                   | nan                                | nan                    | nan                                          |
| 2003 (55th) | Futurama                            | nan                                | nan                    | nan                                          |
| 2003 (55th) | Kim Possible                        | nan                                | nan                    | nan                                          |
| 2003 (55th) | SpongeBob SquarePants               | nan                                | nan                    | nan                                          |
| 2004 (56th) | Samurai Jack                        | Volume 1 (Chapters 1-20)           | Cartoon Network        | Star Wars: Clone Wars                        |
| 2004 (56th) | Futurama                            | "'Twas the Fight Before Christmas" | Cartoon Network        | The Powerpuff Girls                          |
| 2004 (56th) | The Simpsons                        | nan                                | nan                    | nan                                          |
| 2004 (56th) | South Park                          | nan                                | nan                    | nan                                          |
| 2004 (56th) | SpongeBob SquarePants               | nan                                | nan                    | nan                                          |
| 2005 (57th) | South Park                          | Volume 2 (Chapters 21-25)          | Cartoon Network        | Star Wars: Clone Wars                        |
| 2005 (57th) | Family Guy                          | Special                            | Animal Planet          | Dragons: A Fantasy Made Real                 |
| 2005 (57th) | Samurai Jack                        | nan                                | nan                    | nan                                          |
| 2005 (57th) | The Simpsons                        | nan                                | nan                    | nan                                          |
| 2005 (57th) | SpongeBob SquarePants               | nan                                | nan                    | nan                                          |
| 2006 (58th) | The Simpsons                        | Special                            | Discovery Channel      | Before the Dinosaurs                         |
| 2006 (58th) | Camp Lazlo                          | "Escape from Cluster Prime"        | Nickelodeon            | My Life as a Teenage Robot                   |
| 2006 (58th) | Family Guy                          | nan                                | nan                    | nan                                          |
| 2006 (58th) | Foster's Home for Imaginary Friends | nan                                | nan                    | nan                                          |
| 2006 (58th) | South Park                          | nan                                | nan                    | nan                                          |
| 2007 (59th) | South Park                          | "Where's Lazlo?"                   | Cartoon Network        | Camp Lazlo                                   |
| 2007 (59th) | Avatar: The Last Airbender          | "Good Wilt Hunting"                | Cartoon Network        | Foster's Home for Imaginary Friends          |
| 2007 (59th) | Robot Chicken                       | Movie                              | Cartoon Network        | Hellboy: Sword of Storms                     |
| 2007 (59th) | The Simpsons                        | Special                            | Discovery Channel      | Secrets of the Deep                          |
| 2007 (59th) | SpongeBob SquarePants               | nan                                | nan                    | nan                                          |
| 2008 (60th) | The Simpsons                        | Imaginationland: The Movie         | Comedy Central         | South Park                                   |
| 2008 (60th) | Creature Comforts                   | "Blue Harvest"                     | Fox                    | Family Guy                                   |
| 2008 (60th) | [MISSING]                           | Movie                              | Warner Bros. on Demand | Justice League: The New Frontier             |
| 2008 (60th) | Robot Chicken                       | nan                                | nan                    | nan                                          |
| 2008 (60th) | SpongeBob SquarePants               | nan                                | nan                    | nan                                          |
| 2009 (61st) | South Park                          | "Destination: Imagination"         | Cartoon Network        | Foster's Home for Imaginary Friends          |
| 2009 (61st) | American Dad!                       | Movie                              | Spike                  | Afro Samurai: Resurrection                   |
| 2009 (61st) | Robot Chicken                       | nan                                | nan                    | nan                                          |
| 2009 (61st) | The Simpsons                        | nan                                | nan                    | nan                                          |


````

### Model Response

```
{"value": "American Dad!"}
```

### Correct Answer

```
{
  "value": "King of the Hill"
}
```

