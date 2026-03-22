# Data-Imputation: 3 Example Questions

## Example 1: Junior Rose Bowl Game Date (WebTable)

**Question:** Fill in the `[MISSING]` value in the table below.

| Year | Date | Winning Team | Score | Losing Team | Location |
|---:|:--|:--|---:|:--|:--|
| 1946 | December 14 | Compton College | 0 | Kilgore College, TX | Pasadena, California |
| 1947 | December 13 | Chaffey College | 26 | 'Cameron College, OK | Pasadena, California |
| 1948 | December 11 | Compton College | 14 | Duluth Junior College, MN | Pasadena, California |
| 1949 | December 10 | Little Rock Jr. College, AR | 19 | Santa Ana College | Pasadena, California |
| 1950 | December 9 | Long Beach City College | 13 | Boise Junior College, ID | Pasadena, California |
| 1951 | December 8 | Pasadena City College | 26 | Tyler Junior College, TX | Pasadena, California |
| 1952 | December 13 | Hartnell College, CA | 20 | Bacone Junior College, OK | Pasadena, California |
| 1953 | December 12 | Bakersfield College | 6 | Northeastern Oklahoma A&M | Pasadena, California |
| 1954 | December 11 | Hinds Junior College, MS | 7 | El Camino College | Pasadena, California |
| 1955 | December 10 | Compton College | 13 | Jones Co. Jr. College, MS | Pasadena, California |
| 1956 | December 8 | Arlington Junior College, TX | 13 | Compton College | Pasadena, California |
| 1957 | December 14 | Arlington Junior College, TX | 12 | Cerritos College | Pasadena, California |
| 1958 | December 13 | Santa Monica College | 12 | Northeastern Oklahoma A&M | Pasadena, California |
| 1959 | December 12 | Bakersfield College | 14 | Del Mar College, TX | Pasadena, California |
| 1960 | December 10 | Long Beach City College | 16 | Tyler Junior College, TX | Pasadena, California |
| 1961 | December 9 | Cameron College, OK | 20 | Bakersfield College | Pasadena, California |
| 1962 | December 8 | Santa Ana College | 0 | Columbia Basin College, WA | Pasadena, California |
| 1963 | December 14 | Orange Coast College | 0 | Northeastern Oklahoma A&M | Pasadena, California |
| 1964 | December 12 | Long Beach City College | 6 | Cameron College, OK | Pasadena, California |
| 1965 | December 11 | Fullerton College | 15 | Henderson Co. Jr. College, TX | Pasadena, California |
| 1966 | December 10 | Henderson Co. Jr. College, TX | 13 | Pasadena City College | Pasadena, California |
| **1967** | **[MISSING]** | West Texas State | 13 | San Fernando Valley State | Pasadena, California |
| 1968 | December 7 | Grambling | 7 | Sacramento State | Pasadena, California |
| 1969 | December 6 | San Diego State | 7 | Boston University | Pasadena, California |
| 1970 | December 19 | Louisville (tie) | 24 | Long Beach State (tie) | Pasadena, California |
| 1971 | December 18 | Memphis State | 9 | San Jose State | Pasadena, California |
| 1976 | December 11 | Bakersfield College | 14 | Ellsworth CC, IA | Pasadena, California |
| 1977 | December 10 | Pasadena City College | 9 | Jones County JC, MS | Pasadena, California |

**Model answer:** `December 9`
**Correct answer:** `December 2`

> The model picked a plausible December date that fits the pattern, but the actual
> historical date was December 2, 1967. This requires factual recall, not just
> pattern matching.

---

## Example 2: Employee Age (tablib)

**Question:** Fill in the `[MISSING]` value in the table below.

| Name | Position | Office | Age | Start date | Salary |
|:--|:--|:--|:--|:--|:--|
| Tiger Nixon | System Architect | Edinburgh | 61 | 2011/04/25 | $320,800 |
| Garrett Winters | Accountant | Tokyo | 63 | 2011/07/25 | $170,750 |
| Ashton Cox | Junior Technical Author | San Francisco | 66 | 2009/01/12 | $86,000 |
| Cedric Kelly | Senior Javascript Developer | Edinburgh | 22 | 2012/03/29 | $433,060 |
| Airi Satou | Accountant | Tokyo | 33 | 2008/11/28 | $162,700 |
| ... | ... | ... | ... | ... | ... |
| **Zorita Serrano** | **Software Engineer** | **San Francisco** | **[MISSING]** | **2012/06/01** | **$115,000** |
| ... | ... | ... | ... | ... | ... |
| Donna Snider | Customer Support | New York | 27 | 2011/01/25 | $112,000 |

*(56 rows total)*

**Model answer:** `25`
**Correct answer:** `56`

> The table is a well-known sample dataset (DataTables). The model guessed a
> young age, but the actual value is 56. There are no in-table clues that
> uniquely determine the age — this requires knowing the specific dataset.

---

## Example 3: Row Index in Korean Demographics Table (tablib)

**Question:** Fill in the `[MISSING]` value in the table below.

| Unnamed: 0 | Year | Est. Population | Births | Deaths | Natural Increase | CBR (%) | CDR (%) | NI Rate (%) | TFR (%) |
|:--|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 1925 | 12,997,600 | 558,897 | 359,042 | 199,855 | 43.0 | 27.6 | 15.4 | 6.59 |
| 1 | 1926 | 13,052,700 | 511,667 | 337,948 | 173,719 | 39.2 | 25.9 | 13.3 | nan |
| **[MISSING]** | **1927** | 13,037,200 | 534,524 | 353,818 | 180,706 | 41.0 | 27.1 | 13.9 | nan |
| 3 | 1928 | 13,105,100 | 566,142 | 357,701 | 208,441 | 43.2 | 27.3 | 15.9 | nan |
| 4 | 1929 | 13,124,300 | 566,969 | 414,366 | 152,603 | 43.2 | 31.6 | 11.6 | nan |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 94 | 2019 | nan | 303,054 | 295,132 | 7,922 | 5.9 | 5.7 | 0.2 | 0.92 |

*(95 rows, row 0 through row 94)*

**Model answer:** `3`
**Correct answer:** `2`

> The `Unnamed: 0` column is a simple 0-based row index (0, 1, ?, 3, 4, ...).
> The model answered `3` instead of the obvious `2`. A trivial pattern that even
> a 7B model should get — likely confused by the column header being "Unnamed: 0"
> or the Korean-language column names.
