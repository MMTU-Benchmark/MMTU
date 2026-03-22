# Schema-Matching: All Questions (9 total)

**Model:** Qwen2.5-7B-Instruct

---

## Question 1: assays_Semantically-Joinable_assays_both_50_1_ec_av (assays)

**Dataset:** assays  
**Test case:** assays_Semantically-Joinable_assays_both_50_1_ec_av  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to null. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or null]. Provide the mapping for each column in Table A and return all mappings in a list.

No explanation and return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

TableA:
|   assay_id |   doc_id | description                                                                                                 | assay_type   | assay_test_type   | assay_category   | assay_organism   | assay_tax_id   | assay_strain   | assay_tissue   | assay_cell_type   | assay_subcellular_fraction   |
|-----------:|---------:|:------------------------------------------------------------------------------------------------------------|:-------------|:------------------|:-----------------|:-----------------|:---------------|:---------------|:---------------|:------------------|:-----------------------------|
|          1 |    11087 | The compound was tested for the in vitro inhibition of platelet 12-lipoxygenase at a concentration of 30 uM | B            |                   |                  |                  |                |                |                |                   |                              |
|          2 |      684 | Compound was evaluated for its ability to mobilize calcium in 1321NI cells                                  | F            |                   |                  |                  |                |                |                |                   |                              |
|          3 |    15453 |                                                                                                             | B            |                   |                  |                  |                |                |                |                   |                              |
|          4 |    17841 | Binding affinity against A2 adenosine receptor in bovine striatal membranes using [3H]CGS-21680             | B            |                   |                  | Bos taurus       | 9913.0         |                |                |                   |                              |
|          5 |    17430 | In vitro cell cytotoxicity against 143-B cell lines (Human osteosarcoma cell line)                          | F            |                   |                  | Homo sapiens     | 9606.0         |                |                | 143B              |                              |
|          6 |    17430 | In vitro cell cytotoxicity against 143-B cell lines (Human osteosarcoma cell line)                          | F            |                   |                  | Homo sapiens     | 9606.0         |                |                | 143B              |                              |
|          7 |    13799 | Cytotoxic Activity was evaluated against 143B (TK-) tumor cells                                             | F            |                   |                  | Mus musculus     | 10090.0        |                |                | 143B              |                              |
|          8 |    17774 | In vitro cell cytotoxicity was determined against 143B cell line                                            | F            |                   |                  | Homo sapiens     | 9606.0         |                |                | 143B              |                              |
|          9 |     3801 | Inhibitory activity against tumor osteosarcoma cell line 143B after 72 hr continuous exposure to compound   | F            |                   |                  | Homo sapiens     | 9606.0         |                |                | 143B              |                              |
|         10 |    17430 | In vitro cell cytotoxicity against 143B-LTK cell lines expressed in HSV-1 TK                                | F            |                   |                  | Homo sapiens     | 9606.0         |                |                | 143B              |                              |

TableB:
|   assay_id |   tid | relationship_type   |   confidence_score | curated_by   |   src_id | src_assay_id   | chembl_id    | cell_id   | bao_format   | tissue_id   | variant_id   |
|-----------:|------:|:--------------------|-------------------:|:-------------|---------:|:---------------|:-------------|:----------|:-------------|:------------|:-------------|
|       7524 | 50597 | N                   |                  1 | Intermediate |        1 |                | CHEMBL618647 |           | BAO_0000218  | 2113.0      |              |
|       7525 | 50597 | N                   |                  1 | Intermediate |        1 |                | CHEMBL618648 |           | BAO_0000218  | 2113.0      |              |
|       7526 | 50597 | N                   |                  1 | Intermediate |        1 |                | CHEMBL618649 |           | BAO_0000218  | 2113.0      |              |
|       7527 | 50597 | N                   |                  1 | Intermediate |        1 |                | CHEMBL618650 |           | BAO_0000218  | 2107.0      |              |
|       7528 | 50597 | N                   |                  1 | Intermediate |        1 |                | CHEMBL618651 |           | BAO_0000218  | 2107.0      |              |
|       7529 | 50597 | N                   |                  1 | Intermediate |        1 |                | CHEMBL876497 |           | BAO_0000218  | 2107.0      |              |
|       7530 | 50597 | N                   |                  1 | Intermediate |        1 |                | CHEMBL618652 |           | BAO_0000218  | 2048.0      |              |
|       7531 | 50597 | N                   |                  1 | Intermediate |        1 |                | CHEMBL618653 |           | BAO_0000218  | 2048.0      |              |
|       7532 | 50597 | N                   |                  1 | Intermediate |        1 |                | CHEMBL618654 |           | BAO_0000218  | 2048.0      |              |
|       7533 | 50597 | N                   |                  1 | Intermediate |        1 |                | CHEMBL618655 |           | BAO_0000218  |             |              |


````

### Model Response

```
```json
{
  "column_mappings": [
    ["assay_id", "assay_id"],
    ["doc_id", null],
    ["description", null],
    ["assay_type", null],
    ["assay_test_type", null],
    ["assay_category", null],
    ["assay_organism", null],
    ["assay_tax_id", "tid"],
    ["assay_strain", null],
    ["assay_tissue", null],
    ["assay_cell_type", "cell_id"],
    ["assay_subcellular_fraction", null]
  ]
}
```
```

### Correct Answer

```
{
  "column_mappings": [
    [
      "assay_id",
      "assay_id"
    ],
    [
      "doc_id",
      null
    ],
    [
      "description",
      null
    ],
    [
      "assay_type",
      null
    ],
    [
      "assay_test_type",
      null
    ],
    [
      "assay_category",
      null
    ],
    [
      "assay_organism",
      null
    ],
    [
      "assay_tax_id",
      null
    ],
    [
      "assay_strain",
      null
    ],
    [
      "assay_tissue",
      null
    ],
    [
      "assay_cell_type",
      null
    ],
    [
      "assay_subcellular_fraction",
      null
    ]
  ]
}
```


---

## Question 2: prospect_View-Unionable_prospect_both_0_1_ac2_av (prospect)

**Dataset:** prospect  
**Test case:** prospect_View-Unionable_prospect_both_0_1_ac2_av  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to null. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or null]. Provide the mapping for each column in Table A and return all mappings in a list.

No explanation and return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

TableA:
| AgencyID   | LastName   | FirstName   | MiddleInitial   | Gender   | AddressLine1         | AddressLine2   | PostalCode   | City           | State                | Country                  |
|:-----------|:-----------|:------------|:----------------|:---------|:---------------------|:---------------|:-------------|:---------------|:---------------------|:-------------------------|
| PEL0       | PELLAND    | Netti       |                 | f        | 21847 olympia street |                | T6b 1i1      | Fairbanks      | MA                   | United States of America |
| LED1       | LEDUC      | TRUDY       |                 | F        | 245 congress court   | APT. 624       | 77281        | Quebec         | PA                   | United States of America |
| lat2       | latif      | ireland     |                 |          | 6517 frailing west   |                | 91355        | Henderson      | Alberta              | United States of America |
| RUD3       | RUDDICK    | Misti       |                 |          | 11449 blalock park   |                | 36615        | Salem          | AR                   | Canada                   |
| JAY4       | JAYAMANNE  | sarena      | M               | f        | 18354 dodd court     | Apt. 619       | t6a 1i3      | Toledo         | OR                   | Canada                   |
| tod5       | todo       | Paulette    | Z               | M        | 14117 roxboro street |                | A2b 1v3      | Corpus Christi | VA                   | United States of America |
| Kan6       | Kanno      | AMALITA     | R               | m        | 24697 FLORENCE WEST  |                | 49513        | Salt Lake City | OH                   | Canada                   |
| Din7       | Dinkel     | Ernesto     | Z               |          | 6488 applewood drive |                | M5d 1v6      | Brownsville    | Prince Edward Island | United States of America |
| Thi8       | Thibodeaux | Toby        |                 |          | 17404 gale court     |                | V6c 1q1      | Escondido      | NV                   | United States of America |
| May9       | Mayo       | evangelia   |                 |          | 15913 alexis street  |                | 99716        | Los Angeles    | Ontario              | United States of America |

TableB:
| AgeID   | Ph             |     In |   NuCa | NumChil   | MaSt   |   A |   CreRat | OOReF   | Empl                           | NumCreCa   |              NWo |
|:--------|:---------------|-------:|-------:|:----------|:-------|----:|---------:|:--------|:-------------------------------|:-----------|-----------------:|
| Iok7501 | 1-637-119-9996 |  94490 |      3 |           | U      |   7 |      580 | U       | FM Global                      |            | 321776           |
| tia7502 | 1-560-405-0048 |   7037 |      4 | 4.0       | S      |  48 |      683 | R       | MGIC Investment                | 2.0        |      2.29232e+06 |
| AOI7503 | 1-261-306-5079 | 419269 |      1 | 5.0       | M      |  14 |      411 | O       | Ross Stores                    | 2.0        | 969707           |
| PJQ7504 | 1-642-299-6655 |  76681 |      4 | 5.0       | W      |  29 |      818 | U       |                                | 9.0        |      3.89946e+06 |
| SDV7505 |                | 209116 |      2 | 4.0       | U      |  69 |      370 | R       | Alliance One International     | 7.0        |      3.74922e+06 |
| Hga7506 | 1-388-257-4273 | 212203 |      0 | 0.0       | U      |  47 |      833 | O       | Sally Beauty Holdings          | 6.0        |      3.65853e+06 |
| Beo7507 |                |  42018 |      5 | 5.0       | M      |   0 |      536 | U       | Wisconsin Energy               | 2.0        |      1.73846e+06 |
| Qum7508 | 1-632-118-1891 |  90446 |      0 | 0.0       | S      |  46 |      775 | R       | Carpenter Technology           | 0.0        |      3.3073e+06  |
| Hud7509 | 1-853-806-4986 |  16274 |      1 | 1.0       | M      |   6 |      765 | R       | Liberty Mutual Insurance Group | 3.0        |      1.81642e+06 |
| jba7510 | 1-220-687-2027 |  22215 |      5 | 2.0       | M      |  22 |      555 | O       | Black & Decker                 | 6.0        |      2.59925e+06 |


````

### Model Response

```
```json
{
  "column_mappings": [
    ["AgencyID", null],
    ["LastName", "Empl"],
    ["FirstName", null],
    ["MiddleInitial", null],
    ["Gender", null],
    ["AddressLine1", null],
    ["AddressLine2", null],
    ["PostalCode", null],
    ["City", null],
    ["State", null],
    ["Country", null]
  ]
}
```
```

### Correct Answer

```
{
  "column_mappings": [
    [
      "AgencyID",
      "AgeID"
    ],
    [
      "LastName",
      null
    ],
    [
      "FirstName",
      null
    ],
    [
      "MiddleInitial",
      null
    ],
    [
      "Gender",
      null
    ],
    [
      "AddressLine1",
      null
    ],
    [
      "AddressLine2",
      null
    ],
    [
      "PostalCode",
      null
    ],
    [
      "City",
      null
    ],
    [
      "State",
      null
    ],
    [
      "Country",
      null
    ]
  ]
}
```


---

## Question 3: pair_99 (HXD)

**Dataset:** HXD  
**Test case:** pair_99  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to null. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or null]. Provide the mapping for each column in Table A and return all mappings in a list.

No explanation and return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

TableA:
| country_name                     | country_code   | reported_date   | admin_1_code   | admin_1_label   | admin_2_code   | admin_2_label   | admin_3_code   | admin_3_label   | Date_enquete        |   hh_PDIs_presents |   ind_PDIs_presents |   hh_RETs_presents |   ind_RETs_presents |
|:---------------------------------|:---------------|:----------------|:---------------|:----------------|:---------------|:----------------|:---------------|:----------------|:--------------------|-------------------:|--------------------:|-------------------:|--------------------:|
| Democratic Republic of the Congo | COD            | Dec-31-20       | COD74          | TANGANYIKA      | COD7409        | KONGOLO         | COD7409ZS01    | KONGOLO         | 2020-12-27 00:00:00 |                  0 |                   0 |                  0 |                   0 |
| Democratic Republic of the Congo | COD            | Dec-31-20       | COD74          | TANGANYIKA      | COD7404        | MOBA            | COD7404ZS02    | MOBA            | 2020-11-09 00:00:00 |                  0 |                   0 |                  0 |                   0 |
| Democratic Republic of the Congo | COD            | Dec-31-20       | COD74          | TANGANYIKA      | COD7410        | NYUNZU          | COD7410ZS01    | NYUNZU          | 2020-11-17 00:00:00 |                  0 |                   0 |                  0 |                   0 |
| Democratic Republic of the Congo | COD            | Dec-31-20       | COD74          | TANGANYIKA      | COD7406        | MANONO          | COD7406ZS02    | KIAMBI          | 2020-12-31 00:00:00 |                  0 |                   0 |                  0 |                   0 |
| Democratic Republic of the Congo | COD            | Dec-31-20       | COD74          | TANGANYIKA      | COD7409        | KONGOLO         | COD7409ZS02    | MBULULA         | 2020-12-29 00:00:00 |                 10 |                  60 |                  0 |                   0 |
| Democratic Republic of the Congo | COD            | Dec-31-20       | COD74          | TANGANYIKA      | COD7404        | MOBA            | COD7404ZS01    | KANSIMBA        | 2020-11-14 00:00:00 |                  0 |                   0 |                  0 |                   0 |
| Democratic Republic of the Congo | COD            | Dec-31-20       | COD74          | TANGANYIKA      | COD7406        | MANONO          | COD7406ZS01    | ANKORO          | 2020-12-23 00:00:00 |                  0 |                   0 |                  0 |                   0 |
| Democratic Republic of the Congo | COD            | Dec-31-20       | COD74          | TANGANYIKA      | COD7410        | NYUNZU          | COD7410ZS01    | NYUNZU          | 2020-11-16 00:00:00 |                  6 |                  35 |                  7 |                  38 |
| Democratic Republic of the Congo | COD            | Dec-31-20       | COD74          | TANGANYIKA      | COD7404        | MOBA            | COD7404ZS01    | KANSIMBA        | 2020-11-12 00:00:00 |                  0 |                   0 |                  0 |                   0 |
| Democratic Republic of the Congo | COD            | Dec-31-20       | COD74          | TANGANYIKA      | COD7409        | KONGOLO         | COD7409ZS01    | KONGOLO         | 2020-12-22 00:00:00 |                  0 |                   0 |                  0 |                   0 |

TableB:
| Country                          | Country Code   | Reported Date   | admin_1_code   | admin_1_label   | admin_2_code   | admin_2_label   | date_enquete        |   hh_IDP_presents_36_mois |   ind_IDP_presents_36_mois |   hh_RETs_presents_36mo |   ind_RETs_presents_36mo |
|:---------------------------------|:---------------|:----------------|:---------------|:----------------|:---------------|:----------------|:--------------------|--------------------------:|---------------------------:|------------------------:|-------------------------:|
| Democratic Republic of the Congo | COD            | July-31-2022    | COD62          | SUD-KIVU        | COD6202        | KABARE          | 2022-07-14 00:00:00 |                         1 |                          5 |                       0 |                        0 |
| Democratic Republic of the Congo | COD            | July-31-2022    | COD62          | SUD-KIVU        | COD6205        | KALEHE          | 2022-07-09 00:00:00 |                       116 |                        801 |                      94 |                      565 |
| Democratic Republic of the Congo | COD            | July-31-2022    | COD62          | SUD-KIVU        | COD6203        | SHABUNDA        | 2022-07-20 00:00:00 |                         9 |                         52 |                       2 |                       11 |
| Democratic Republic of the Congo | COD            | July-31-2022    | COD62          | SUD-KIVU        | COD6212        | MWENGA          | 2022-07-14 00:00:00 |                         8 |                         49 |                       6 |                       31 |
| Democratic Republic of the Congo | COD            | July-31-2022    | COD62          | SUD-KIVU        | COD6207        | WALUNGU         | 2022-07-09 00:00:00 |                        48 |                        239 |                       0 |                        0 |
| Democratic Republic of the Congo | COD            | July-31-2022    | COD62          | SUD-KIVU        | COD6207        | WALUNGU         | 2022-07-07 00:00:00 |                        17 |                         95 |                       0 |                        0 |
| Democratic Republic of the Congo | COD            | July-31-2022    | COD62          | SUD-KIVU        | COD6207        | WALUNGU         | 2022-07-13 00:00:00 |                         0 |                          0 |                       0 |                        0 |
| Democratic Republic of the Congo | COD            | July-31-2022    | COD62          | SUD-KIVU        | COD6210        | FIZI            | 2022-07-25 00:00:00 |                        41 |                        226 |                       0 |                        0 |
| Democratic Republic of the Congo | COD            | July-31-2022    | COD62          | SUD-KIVU        | COD6207        | WALUNGU         | 2022-07-11 00:00:00 |                         0 |                          0 |                       0 |                        0 |
| Democratic Republic of the Congo | COD            | July-31-2022    | COD62          | SUD-KIVU        | COD6203        | SHABUNDA        | 2022-07-14 00:00:00 |                       137 |                        787 |                     165 |                      679 |


````

### Model Response

```
```json
{
  "column_mappings": [
    ["country_name", "Country"],
    ["country_code", "Country Code"],
    ["reported_date", "Reported Date"],
    ["admin_1_code", "admin_1_code"],
    ["admin_1_label", "admin_1_label"],
    ["admin_2_code", "admin_2_code"],
    ["admin_2_label", "admin_2_label"],
    ["Date_enquete", "date_enquete"],
    ["hh_PDIs_presents", "hh_IDP_presents_36_mois"],
    ["ind_PDIs_presents", "ind_IDP_presents_36_mois"],
    ["hh_RETs_presents", "hh_RETs_presents_36mo"],
    ["ind_RETs_presents", "ind_RETs_presents_36mo"]
  ]
}
```
```

### Correct Answer

```
{
  "column_mappings": [
    [
      "country_name",
      "Country"
    ],
    [
      "country_code",
      "Country Code"
    ],
    [
      "reported_date",
      "Reported Date"
    ],
    [
      "admin_1_code",
      "admin_1_code"
    ],
    [
      "admin_1_label",
      "admin_1_label"
    ],
    [
      "admin_2_code",
      "admin_2_code"
    ],
    [
      "admin_2_label",
      "admin_2_label"
    ],
    [
      "admin_3_code",
      null
    ],
    [
      "admin_3_label",
      null
    ],
    [
      "Date_enquete",
      "date_enquete"
    ],
    [
      "hh_PDIs_presents",
      "hh_IDP_presents_36_mois"
    ],
    [
      "ind_PDIs_presents",
      "ind_IDP_presents_36_mois"
    ],
    [
      "hh_RETs_presents",
      "hh_RETs_presents_36mo"
    ],
    [
      "ind_RETs_presents",
      "ind_RETs_presents_36mo"
    ]
  ]
}
```


---

## Question 4: assays_View-Unionable_assays_both_0_1_ac3_ev (assays)

**Dataset:** assays  
**Test case:** assays_View-Unionable_assays_both_0_1_ac3_ev  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to null. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or null]. Provide the mapping for each column in Table A and return all mappings in a list.

No explanation and return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

TableA:
|   assay_id |   doc_id | description                                                                                                 | assay_type   | assay_test_type   | assay_category   | assay_organism   | assay_tax_id   | assay_strain   | assay_tissue   | assay_cell_type   | assay_subcellular_fraction   |
|-----------:|---------:|:------------------------------------------------------------------------------------------------------------|:-------------|:------------------|:-----------------|:-----------------|:---------------|:---------------|:---------------|:------------------|:-----------------------------|
|          1 |    11087 | The compound was tested for the in vitro inhibition of platelet 12-lipoxygenase at a concentration of 30 uM | B            |                   |                  |                  |                |                |                |                   |                              |
|          2 |      684 | Compound was evaluated for its ability to mobilize calcium in 1321NI cells                                  | F            |                   |                  |                  |                |                |                |                   |                              |
|          3 |    15453 |                                                                                                             | B            |                   |                  |                  |                |                |                |                   |                              |
|          4 |    17841 | Binding affinity against A2 adenosine receptor in bovine striatal membranes using [3H]CGS-21680             | B            |                   |                  | Bos taurus       | 9913.0         |                |                |                   |                              |
|          5 |    17430 | In vitro cell cytotoxicity against 143-B cell lines (Human osteosarcoma cell line)                          | F            |                   |                  | Homo sapiens     | 9606.0         |                |                | 143B              |                              |
|          6 |    17430 | In vitro cell cytotoxicity against 143-B cell lines (Human osteosarcoma cell line)                          | F            |                   |                  | Homo sapiens     | 9606.0         |                |                | 143B              |                              |
|          7 |    13799 | Cytotoxic Activity was evaluated against 143B (TK-) tumor cells                                             | F            |                   |                  | Mus musculus     | 10090.0        |                |                | 143B              |                              |
|          8 |    17774 | In vitro cell cytotoxicity was determined against 143B cell line                                            | F            |                   |                  | Homo sapiens     | 9606.0         |                |                | 143B              |                              |
|          9 |     3801 | Inhibitory activity against tumor osteosarcoma cell line 143B after 72 hr continuous exposure to compound   | F            |                   |                  | Homo sapiens     | 9606.0         |                |                | 143B              |                              |
|         10 |    17430 | In vitro cell cytotoxicity against 143B-LTK cell lines expressed in HSV-1 TK                                | F            |                   |                  | Homo sapiens     | 9606.0         |                |                | 143B              |                              |

TableB:
|   ss_d |    td | rltnshp_tp   |   cnfdnc_scr | crtd_b       |   src_d | src_ss_d   | chmbl_d      | cll_d   | b_frmt      | tss_d   | vrnt_d   |
|-------:|------:|:-------------|-------------:|:-------------|--------:|:-----------|:-------------|:--------|:------------|:--------|:---------|
|   7524 | 50597 | N            |            1 | Intermediate |       1 |            | CHEMBL618647 |         | BAO_0000218 | 2113.0  |          |
|   7525 | 50597 | N            |            1 | Intermediate |       1 |            | CHEMBL618648 |         | BAO_0000218 | 2113.0  |          |
|   7526 | 50597 | N            |            1 | Intermediate |       1 |            | CHEMBL618649 |         | BAO_0000218 | 2113.0  |          |
|   7527 | 50597 | N            |            1 | Intermediate |       1 |            | CHEMBL618650 |         | BAO_0000218 | 2107.0  |          |
|   7528 | 50597 | N            |            1 | Intermediate |       1 |            | CHEMBL618651 |         | BAO_0000218 | 2107.0  |          |
|   7529 | 50597 | N            |            1 | Intermediate |       1 |            | CHEMBL876497 |         | BAO_0000218 | 2107.0  |          |
|   7530 | 50597 | N            |            1 | Intermediate |       1 |            | CHEMBL618652 |         | BAO_0000218 | 2048.0  |          |
|   7531 | 50597 | N            |            1 | Intermediate |       1 |            | CHEMBL618653 |         | BAO_0000218 | 2048.0  |          |
|   7532 | 50597 | N            |            1 | Intermediate |       1 |            | CHEMBL618654 |         | BAO_0000218 | 2048.0  |          |
|   7533 | 50597 | N            |            1 | Intermediate |       1 |            | CHEMBL618655 |         | BAO_0000218 |         |          |


````

### Model Response

```
```json
{
  "column_mappings": [
    ["assay_id", null],
    ["doc_id", "src_ss_d"],
    ["description", null],
    ["assay_type", "rltnshp_tp"],
    ["assay_test_type", null],
    ["assay_category", null],
    ["assay_organism", null],
    ["assay_tax_id", null],
    ["assay_strain", null],
    ["assay_tissue", null],
    ["assay_cell_type", null],
    ["assay_subcellular_fraction", null]
  ]
}
```
```

### Correct Answer

```
{
  "column_mappings": [
    [
      "assay_id",
      "ss_d"
    ],
    [
      "doc_id",
      null
    ],
    [
      "description",
      null
    ],
    [
      "assay_type",
      null
    ],
    [
      "assay_test_type",
      null
    ],
    [
      "assay_category",
      null
    ],
    [
      "assay_organism",
      null
    ],
    [
      "assay_tax_id",
      null
    ],
    [
      "assay_strain",
      null
    ],
    [
      "assay_tissue",
      null
    ],
    [
      "assay_cell_type",
      null
    ],
    [
      "assay_subcellular_fraction",
      null
    ]
  ]
}
```


---

## Question 5: prospect_Joinable_prospect_vertical_1_ac3_ev (prospect)

**Dataset:** prospect  
**Test case:** prospect_Joinable_prospect_vertical_1_ac3_ev  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to null. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or null]. Provide the mapping for each column in Table A and return all mappings in a list.

No explanation and return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

TableA:
| AgencyID   | LastName   | FirstName   | MiddleInitial   | Gender   | AddressLine1         | AddressLine2   | PostalCode   | City           | State                | Country                  |
|:-----------|:-----------|:------------|:----------------|:---------|:---------------------|:---------------|:-------------|:---------------|:---------------------|:-------------------------|
| PEL0       | PELLAND    | Netti       |                 | f        | 21847 olympia street |                | T6b 1i1      | Fairbanks      | MA                   | United States of America |
| LED1       | LEDUC      | TRUDY       |                 | F        | 245 congress court   | APT. 624       | 77281        | Quebec         | PA                   | United States of America |
| lat2       | latif      | ireland     |                 |          | 6517 frailing west   |                | 91355        | Henderson      | Alberta              | United States of America |
| RUD3       | RUDDICK    | Misti       |                 |          | 11449 blalock park   |                | 36615        | Salem          | AR                   | Canada                   |
| JAY4       | JAYAMANNE  | sarena      | M               | f        | 18354 dodd court     | Apt. 619       | t6a 1i3      | Toledo         | OR                   | Canada                   |
| tod5       | todo       | Paulette    | Z               | M        | 14117 roxboro street |                | A2b 1v3      | Corpus Christi | VA                   | United States of America |
| Kan6       | Kanno      | AMALITA     | R               | m        | 24697 FLORENCE WEST  |                | 49513        | Salt Lake City | OH                   | Canada                   |
| Din7       | Dinkel     | Ernesto     | Z               |          | 6488 applewood drive |                | M5d 1v6      | Brownsville    | Prince Edward Island | United States of America |
| Thi8       | Thibodeaux | Toby        |                 |          | 17404 gale court     |                | V6c 1q1      | Escondido      | NV                   | United States of America |
| May9       | Mayo       | evangelia   |                 |          | 15913 alexis street  |                | 99716        | Los Angeles    | Ontario              | United States of America |

TableB:
| gncd   | phn            |    ncm | nmbrcrs   | nmbrchldrn   | mrtlstts   | g    | crdtrtng   | wnrrntflg   | mplr                     | nmbrcrdtcrds   |           ntwrth |
|:-------|:---------------|-------:|:----------|:-------------|:-----------|:-----|:-----------|:------------|:-------------------------|:---------------|-----------------:|
| PEL0   | 1-712-522-6088 | 368776 |           | 3.0          | W          | 20.0 | 760.0      | O           | Brink's                  |                |      1.05887e+06 |
| LED1   | 1-626-426-4298 | 177967 | 5.0       | 1.0          | U          | 3.0  | 555.0      | U           |                          | 6.0            |      1.98818e+06 |
| lat2   | 1-524-787-8784 | 321772 | 2.0       | 1.0          | S          |      | 566.0      | O           |                          | 6.0            |      3.67313e+06 |
| RUD3   | 1-741-997-1688 |  25449 | 2.0       | 1.0          | W          | 77.0 |            | O           | Air Products & Chemicals | 3.0            |      2.0059e+06  |
| JAY4   | 1-002-194-1991 | 166567 | 0.0       | 3.0          | M          | 21.0 | 815.0      | O           | Oshkosh                  | 4.0            | 624736           |
| tod5   | 1-441-371-7651 |  43631 | 1.0       | 4.0          | M          | 77.0 | 333.0      | R           |                          | 10.0           |      3.06462e+06 |
| Kan6   | 1-957-940-5980 | 466230 | 4.0       | 0.0          |            | 23.0 | 528.0      | O           | VeraSun Energy           | 1.0            |      3.48913e+06 |
| Din7   | 1-768-633-4096 | 420243 | 2.0       | 2.0          | M          | 9.0  | 680.0      | U           | IDT                      | 7.0            |      3.43074e+06 |
| Thi8   | 1-107-689-2155 | 141862 | 3.0       |              | U          | 63.0 | 761.0      | O           | Adams Resources & Energy | 10.0           |      1.74361e+06 |
| May9   | 1-173-594-6096 | 402011 | 0.0       | 2.0          | M          | 32.0 | 416.0      | O           | MGIC Investment          |                | 216299           |


````

### Model Response

```
```json
{
  "column_mappings": [
    ["AgencyID", "gncd"],
    ["LastName", null],
    ["FirstName", null],
    ["MiddleInitial", null],
    ["Gender", "g"],
    ["AddressLine1", null],
    ["AddressLine2", null],
    ["PostalCode", null],
    ["City", null],
    ["State", "mrtlstts"],
    ["Country", null]
  ]
}
```
```

### Correct Answer

```
{
  "column_mappings": [
    [
      "AgencyID",
      "gncd"
    ],
    [
      "LastName",
      null
    ],
    [
      "FirstName",
      null
    ],
    [
      "MiddleInitial",
      null
    ],
    [
      "Gender",
      null
    ],
    [
      "AddressLine1",
      null
    ],
    [
      "AddressLine2",
      null
    ],
    [
      "PostalCode",
      null
    ],
    [
      "City",
      null
    ],
    [
      "State",
      null
    ],
    [
      "Country",
      null
    ]
  ]
}
```


---

## Question 6: assays_Semantically-Joinable_assays_both_50_70_ac2_av (assays)

**Dataset:** assays  
**Test case:** assays_Semantically-Joinable_assays_both_50_70_ac2_av  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to null. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or null]. Provide the mapping for each column in Table A and return all mappings in a list.

No explanation and return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

TableA:
|   assay_id | assay_organism   | assay_subcellular_fraction   |   confidence_score | assay_cell_type   | variant_id   | assay_test_type   | relationship_type   | assay_tissue   | assay_type   | description                                                                                 |   doc_id | curated_by   | assay_category   | bao_format   | cell_id   | assay_tax_id   | assay_strain   |    tid |
|-----------:|:-----------------|:-----------------------------|-------------------:|:------------------|:-------------|:------------------|:--------------------|:---------------|:-------------|:--------------------------------------------------------------------------------------------|---------:|:-------------|:-----------------|:-------------|:----------|:---------------|:---------------|-------:|
|          1 |                  |                              |                  8 |                   |              |                   | H                   |                | B            | Tbeckmpoundwast2etexfo3theinviyroinjibutionofplatelet12lipocufwnaseatacobc4ntratipbof30uM   |    11087 | Autocuratuin |                  | nA00000019   |           |                |                |  12052 |
|          2 |                  |                              |                  0 |                   |              |                   | U                   |                | F            | Cojpoundwasevaluatevfo4itsab9lifytomobilizesxpcouminw32qNIcelos                             |      684 | Augocurat9on |                  | BxO0000w19   |           |                |                |  22226 |
|          3 |                  |                              |                  0 |                   |              |                   | U                   |                | B            |                                                                                             |    15453 | Autocjratiog |                  | BA900000q9   |           |                |                |  22226 |
|          4 | Bostautus        |                              |                  4 |                   |              |                   | H                   |                | B            | BindjnfadeihitysgainstAwadenosobr5eceptironbovinesteiz5almembranesusing3HCGS21680           |    17841 | Autocjratiom |                  | BAOp000248   |           | 9913.0         |                | 104729 |
|          5 | Homoswpkens      |                              |                  1 | 143B              |              |                   | N                   |                | F            | Invitrocellcytotoxlc8tyayainxt143BcsollimesHuhanosteksarcomzceillijs                        |    17430 | Integmedoate |                  | BAOo000w19   | 526.0     | 9606.0         |                |  80001 |
|          6 | Homksapiejs      |                              |                  1 | 143B              |              |                   | N                   |                | F            | 8nvi6tocellcgtitoxisityagainst143BcelliinesHukanosteosa5comxceplluje                        |    17430 | Intermrdlate |                  | fqO0000219   | 868.0     | 9606.0         |                |  80001 |
|          7 | M7smksculus      |                              |                  1 | 143B              |              |                   | N                   |                | F            | vytotoxicAstivitywasevaluat4dava7nst142BTlyumorceolx                                        |    13799 | Intermevixte |                  | BAO0900e19   | 443.0     | 10090.0        |                |  80001 |
|          8 | Homosapisjs      |                              |                  1 | 143B              |              |                   | N                   |                | F            | Inviyroceplct606ox7citywasdetermunedagainst14rBcellkkne                                     |    17774 | Exlert       |                  | BAO0p00119   | 1100.0    | 9606.0         |                |  80001 |
|          9 | Hohpsapiens      |                              |                  1 | 143B              |              |                   | N                   |                | F            | 7nh9bitoryac4ivittagainsttuklrosgeossrcomaselll7new43Bafger73hrcobtinuousexpoxugetofompounv |     3801 | Intedmexiate |                  | BqO0000q19   | 608.0     | 9606.0         |                |  80001 |
|         10 | Homisapi4ns      |                              |                  1 | 143B              |              |                   | N                   |                | F            | Invitroceoicytotoxicigyagaigsh143BpTKcelllinesexpresxed8buSgqTK                             |    17430 | Intermefiafe |                  | BAk9000219   | 555.0     | 9606.0         |                |  80001 |

TableB:
|   ASSI | ASSORGA           | ASSSUBCEFRA   |   CONFSCO | ASCET   | VARII   | ASSTTY   | RELAT   | ASTIS   | ASTY   | Descr                                                                                                    |   DOI | CURAB        | ASCA   | BAFOR       | CEI   |   SRI | SRASSI   | CHI          | TII    |
|-------:|:------------------|:--------------|----------:|:--------|:--------|:---------|:--------|:--------|:-------|:---------------------------------------------------------------------------------------------------------|------:|:-------------|:-------|:------------|:------|------:|:---------|:-------------|:-------|
|   7524 | Rattus norvegicus |               |         1 |         |         | In vivo  | N       | Kidney  | A      | Biodistribution in normal rat kidney in the presence of 0.005 M Gd/0.01 M lig at 2 hr                    |  9866 | Intermediate |        | BAO_0000218 |       |     1 |          | CHEMBL618647 | 2113.0 |
|   7525 | Rattus norvegicus |               |         1 |         |         | In vivo  | N       | Kidney  | A      | Biodistribution in normal rat kidney in the presence of 0.01 M Gd/0.05 M lig                             |  9866 | Intermediate |        | BAO_0000218 |       |     1 |          | CHEMBL618648 | 2113.0 |
|   7526 | Rattus norvegicus |               |         1 |         |         | In vivo  | N       | Kidney  | A      | Biodistribution in normal rat kidney in the presence of NAC Gd 0.01 M lig at 2 hr                        |  9866 | Intermediate |        | BAO_0000218 |       |     1 |          | CHEMBL618649 | 2113.0 |
|   7527 | Rattus norvegicus |               |         1 |         |         | In vivo  | N       | Liver   | A      | Biodistribution in normal rat liver in the presence of 0.005 M Gd/0.01 M lig at 2 hr                     |  9866 | Intermediate |        | BAO_0000218 |       |     1 |          | CHEMBL618650 | 2107.0 |
|   7528 | Rattus norvegicus |               |         1 |         |         | In vivo  | N       | Liver   | A      | Biodistribution in normal rat liver in the presence of 0.01 M Gd/0.05 M lig                              |  9866 | Intermediate |        | BAO_0000218 |       |     1 |          | CHEMBL618651 | 2107.0 |
|   7529 | Rattus norvegicus |               |         1 |         |         | In vivo  | N       | Liver   | A      | Biodistribution in normal rat liver in the presence of NAC Gd 0.01 M lig at 2 hr                         |  9866 | Intermediate |        | BAO_0000218 |       |     1 |          | CHEMBL876497 | 2107.0 |
|   7530 | Rattus norvegicus |               |         1 |         |         | In vivo  | N       | Lung    | A      | Biodistribution in normal rat lung in the presence of 0.005 M Gd/0.01 M lig at 2 hr                      |  9866 | Intermediate |        | BAO_0000218 |       |     1 |          | CHEMBL618652 | 2048.0 |
|   7531 | Rattus norvegicus |               |         1 |         |         | In vivo  | N       | Lung    | A      | Biodistribution in normal rat lung in the presence of 0.01 M Gd/0.05 M lig                               |  9866 | Intermediate |        | BAO_0000218 |       |     1 |          | CHEMBL618653 | 2048.0 |
|   7532 | Rattus norvegicus |               |         1 |         |         | In vivo  | N       | Lung    | A      | Biodistribution in normal rat lung in the presence of NAC Gd 0.01 M lig at 2 hr                          |  9866 | Intermediate |        | BAO_0000218 |       |     1 |          | CHEMBL618654 | 2048.0 |
|   7533 | Rattus norvegicus |               |         1 |         |         |          | N       |         | A      | Recovery rate from urine and bile was determined after iv administration at 20 mg/kg in rats; Not tested |  6351 | Intermediate |        | BAO_0000218 |       |     1 |          | CHEMBL618655 |        |


````

### Model Response

```
```json
{
  "column_mappings": [
    ["assay_id", null],
    ["assay_organism", "ASSORGA"],
    ["assay_subcellular_fraction", "ASSSUBCEFRA"],
    ["confidence_score", "CONFSCO"],
    ["assay_cell_type", "ASCET"],
    ["variant_id", "VARII"],
    ["assay_test_type", "ASSTTY"],
    ["relationship_type", "RELAT"],
    ["assay_tissue", "ASTIS"],
    ["assay_type", "ASTY"],
    ["description", "Descr"],
    ["doc_id", "DOI"],
    ["curated_by", "CURAB"],
    ["assay_category", "ASCA"],
    ["bao_format", "BAFOR"],
    ["cell_id", "CEI"],
    ["assay_tax_id", "SRI"],
    ["assay_strain", "SRASSI"],
    ["tid", null]
  ]
}
```
```

### Correct Answer

```
{
  "column_mappings": [
    [
      "assay_id",
      "ASSI"
    ],
    [
      "assay_organism",
      "ASSORGA"
    ],
    [
      "assay_subcellular_fraction",
      "ASSSUBCEFRA"
    ],
    [
      "confidence_score",
      "CONFSCO"
    ],
    [
      "assay_cell_type",
      "ASCET"
    ],
    [
      "variant_id",
      "VARII"
    ],
    [
      "assay_test_type",
      "ASSTTY"
    ],
    [
      "relationship_type",
      "RELAT"
    ],
    [
      "assay_tissue",
      "ASTIS"
    ],
    [
      "assay_type",
      "ASTY"
    ],
    [
      "description",
      "Descr"
    ],
    [
      "doc_id",
      "DOI"
    ],
    [
      "curated_by",
      "CURAB"
    ],
    [
      "assay_category",
      "ASCA"
    ],
    [
      "bao_format",
      "BAFOR"
    ],
    [
      "cell_id",
      "CEI"
    ],
    [
      "assay_tax_id",
      null
    ],
    [
      "assay_strain",
      null
    ],
    [
      "tid",
      null
    ]
  ]
}
```


---

## Question 7: pair_207 (HXD)

**Dataset:** HXD  
**Test case:** pair_207  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to null. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or null]. Provide the mapping for each column in Table A and return all mappings in a list.

No explanation and return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

TableA:
| date reported   | Date of Assessment   |   Round Number: | 1.1.e.2 Province (Admin 1)   | Province pcode   | 1.1.e.3 District (Admin 2)   | District pcode   | 1.1.e.4 Post (Admin 3)   | Locality:              |   Latitude |   Longitude |   Total Households Affected |   Total Individuals Affected |
|:----------------|:---------------------|----------------:|:-----------------------------|:-----------------|:-----------------------------|:-----------------|:-------------------------|:-----------------------|-----------:|------------:|----------------------------:|-----------------------------:|
| 15/9/2019       | 2019-08-27 00:00:00  |               5 | Sofala                       | MZ09             | Buzi                         | MZ0901           | Sofala                   | Nova Sofala            |   -20.0872 |     34.7444 |                        3473 |                        16265 |
| 15/9/2019       | 2019-08-23 00:00:00  |               5 | Sofala                       | MZ09             | Nhamatanda                   | MZ0913           | Nhamatanda               | Siluvo                 |   -19.2459 |     34.0255 |                        7895 |                        40209 |
| 15/9/2019       | 2019-08-22 00:00:00  |               5 | Zambezia                     | MZ11             | Morrumbala                   | MZ1118           | Megaza                   | Megaza                 |   -17.1521 |     35.3735 |                        1276 |                         6380 |
| 15/9/2019       | 2019-08-27 00:00:00  |               5 | Sofala                       | MZ09             | Buzi                         | MZ0901           | Buzi                     | Chissinguana           |   -20.2041 |     34.157  |                        5101 |                        25505 |
| 15/9/2019       | 2019-08-22 00:00:00  |               5 | Zambezia                     | MZ11             | Cidade De Quelimane          | MZ1103           | Cidade De Quelimane      | Municipio De Quelimane |   -17.8798 |     36.8882 |                         728 |                         5089 |
| 15/9/2019       | 2019-08-21 00:00:00  |               5 | Sofala                       | MZ09             | Cidade da Beira              | MZ0906           | NHANGAU - URBANO 5       | Nhangau  - Sede        |   -19.7159 |     35.0022 |                        9730 |                        48650 |
| 15/9/2019       | 2019-08-21 00:00:00  |               5 | Manica                       | MZ04             | Sussundenga                  | MZ0410           | Dombe                    | Muoco                  |   -20.0703 |     33.2638 |                         184 |                         1043 |
| 15/9/2019       | 2019-08-21 00:00:00  |               5 | Manica                       | MZ04             | Macate                       | MZ0405           | Macate                   | Macate                 |   -19.4148 |     33.5146 |                        2688 |                         7036 |
| 15/9/2019       | 2019-08-21 00:00:00  |               5 | Manica                       | MZ04             | Manica                       | MZ0408           | Messica                  | Chinhambuzi            |   -19.0449 |     33.9063 |                         167 |                          835 |
| 15/9/2019       | 2019-08-27 00:00:00  |               5 | Sofala                       | MZ09             | Cidade da Beira              | MZ0906           | INHAMIZUA - URBANO 3     | Alto Da Manga          |   -19.493  |     34.5256 |                        5026 |                        25129 |

TableB:
| Date Reported       | Date of Current Survey   |   Survey Round | Country    | Country Code   | Site Name                  | SSID     | Site location (Province)   | Province PCODE   | Site location (District)   | District PCODE   | Site location (Posto)   | Posto PCODE   | Locality:   |   Latitude |   Longitude | Site status   | What is the site open date?   | Is there Site Management Agency at the site?   | IDP Province of Origin (Admin 1)   | IDP District of Origin (Admin 2)   | IDP Posto of Origin (Admin 3)   | IDP Locality of Origin:   |   Number of families/households |   Total number of IDP individuals |   Total number of families displaced due to Cyclone Idai |   Total number of individuals displaced due to Cyclone Idai |   Total number of families displaced due to flood (December 2019 - February 2020) |   Total number of individuals displaced due to flood (December 2019 - February 2020) |   Infants (less than 1 y) Male |   Infants (less than 1 y) Female |   Children (1-5 y) Male |   Children (1-5 y) Female |   Youth (6-17 y) Male |   Youth (6-17 y) Female |   Adults (18-59 y) Male |   Adults (18-59 y) Female |   Elderly (60 year up) Male |   Elderly (60 year up) Female |   Total male |   Total female |
|:--------------------|:-------------------------|---------------:|:-----------|:---------------|:---------------------------|:---------|:---------------------------|:-----------------|:---------------------------|:-----------------|:------------------------|:--------------|:------------|-----------:|------------:|:--------------|:------------------------------|:-----------------------------------------------|:-----------------------------------|:-----------------------------------|:--------------------------------|:--------------------------|--------------------------------:|----------------------------------:|---------------------------------------------------------:|------------------------------------------------------------:|----------------------------------------------------------------------------------:|-------------------------------------------------------------------------------------:|-------------------------------:|---------------------------------:|------------------------:|--------------------------:|----------------------:|------------------------:|------------------------:|--------------------------:|----------------------------:|------------------------------:|-------------:|---------------:|
| 2020-12-04 00:00:00 | 2020-11-04               |             17 | Mozambique | MOZ            | Maxiquiri alto 3           | MOZ_R093 | Sofala                     | MZ09             | Buzi                       | MZ0901           | Buzi                    | MZ090101      | Guara Guara |   -19.8664 |     33.4348 | Open          | 2020-07-14                    | Yes                                            | Sofala                             | Buzi                               | Buzi                            | Vila Do Buzi              |                             155 |                               775 |                                                        0 |                                                           0 |                                                                               155 |                                                                                  775 |                             76 |                               75 |                      65 |                        65 |                    32 |                      32 |                     161 |                       194 |                          43 |                            32 |          377 |            398 |
| 2020-12-04 00:00:00 | 2020-11-04               |             17 | Mozambique | MOZ            | Maxiquiri alto/Maxiquiri 1 | MOZ_R064 | Sofala                     | MZ09             | Buzi                       | MZ0901           | Buzi                    | MZ090101      | Guara Guara |   -19.86   |     34.454  | Open          | 2019-05-20                    | Yes                                            | Sofala                             | Buzi                               | Buzi                            | Guara Guara               |                            1863 |                              9315 |                                                     1863 |                                                        9315 |                                                                                 0 |                                                                                    0 |                            505 |                              798 |                     401 |                       701 |                  1703 |                     601 |                    2003 |                      2103 |                         300 |                           200 |         4912 |           4403 |
| 2020-12-04 00:00:00 | 2020-11-05               |             17 | Mozambique | MOZ            | Chicuaxa                   | MOZ_R004 | Sofala                     | MZ09             | Chibabava                  | MZ0905           | Goonda                  | MZ090502      | Hamamba     |   -19.8852 |     34.0438 | Open          | 2019-05-27                    | No                                             | Sofala                             | Chibabava                          | Goonda                          | Chinhica                  |                             551 |                              2755 |                                                      551 |                                                        2755 |                                                                                 0 |                                                                                    0 |                             28 |                               28 |                     227 |                       284 |                   511 |                     398 |                     568 |                       540 |                          57 |                           114 |         1391 |           1364 |
| 2020-12-04 00:00:00 | 2020-11-04               |             17 | Mozambique | MOZ            | Macarate                   | MOZ_R029 | Sofala                     | MZ09             | Chibabava                  | MZ0905           | Goonda                  | MZ090502      | Mutindiri   |   -19.838  |     33.9193 | Open          | 2019-05-01                    | No                                             | Sofala                             | Chibabava                          | Goonda                          | Mutindiri                 |                             461 |                              2305 |                                                      461 |                                                        2305 |                                                                                 0 |                                                                                    0 |                             18 |                               18 |                     145 |                       145 |                   363 |                     436 |                     472 |                       526 |                         109 |                            73 |         1107 |           1198 |
| 2020-12-04 00:00:00 | 2020-11-04               |             17 | Mozambique | MOZ            | Chibue Mateo               | MOZ_R085 | Manica                     | MZ04             | Sussundenga                | MZ0410           | Dombe                   | MZ041001      | Bunga       |   -19.959  |     33.489  | Open          | 2019-05-10                    | Yes                                            | Manica                             | Sussundenga                        | Dombe                           | Mabaia                    |                              98 |                               542 |                                                       98 |                                                         542 |                                                                                 0 |                                                                                    0 |                              0 |                                6 |                      33 |                        85 |                    99 |                      76 |                      99 |                       121 |                           6 |                            17 |          237 |            305 |
| 2020-12-04 00:00:00 | 2020-11-04               |             17 | Mozambique | MOZ            | Geromi                     | MOZ_R060 | Sofala                     | MZ09             | Chibabava                  | MZ0905           | Goonda                  | MZ090502      | Hamamba     |   -19.8731 |     33.8898 | Open          | 2019-05-13                    | No                                             | Sofala                             | Chibabava                          | Goonda                          | Hamamba                   |                             384 |                              1920 |                                                      384 |                                                        1920 |                                                                                 0 |                                                                                    0 |                             40 |                               40 |                     160 |                       180 |                   280 |                     460 |                     240 |                       340 |                          80 |                           100 |          800 |           1120 |
| 2020-12-04 00:00:00 | 2020-11-05               |             17 | Mozambique | MOZ            | Magueba                    | MOZ_R047 | Manica                     | MZ04             | Sussundenga                | MZ0410           | Dombe                   | MZ041001      | Javera      |   -20      |     33.389  | Open          | 2019-03-16                    | Yes                                            | Manica                             | Sussundenga                        | Dombe                           | Mabaia                    |                             120 |                               485 |                                                       67 |                                                         335 |                                                                                53 |                                                                                  150 |                              0 |                                0 |                      23 |                        17 |                   155 |                     152 |                      66 |                        66 |                           3 |                             3 |          247 |            238 |
| 2020-12-04 00:00:00 | 2020-11-04               |             17 | Mozambique | MOZ            | 25 de Setembro             | MOZ_R083 | Manica                     | MZ04             | Sussundenga                | MZ0410           | Dombe                   | MZ041001      | Mabaia      |   -19.964  |     33.4    | Open          | 2019-05-30                    | Yes                                            | Manica                             | Sussundenga                        | Dombe                           | Mabaia                    |                             163 |                              1050 |                                                      152 |                                                         771 |                                                                                11 |                                                                                  279 |                              0 |                                0 |                      66 |                        44 |                   153 |                     196 |                     241 |                       273 |                          33 |                            44 |          493 |            557 |
| 2020-12-04 00:00:00 | 2020-11-04               |             17 | Mozambique | MOZ            | Minas Gerais               | MOZ_R052 | Manica                     | MZ04             | Sussundenga                | MZ0410           | Muoha                   | MZ041002      | Muhoa       |   -19.4831 |     33.1915 | Open          | 2019-03-17                    | Yes                                            | Manica                             | Sussundenga                        | Muoha                           | Muhoa                     |                             142 |                               632 |                                                      142 |                                                         632 |                                                                                 0 |                                                                                    0 |                              0 |                                6 |                      57 |                        63 |                    86 |                     161 |                      98 |                       149 |                           6 |                             6 |          247 |            385 |
| 2020-12-04 00:00:00 | 2020-11-05               |             17 | Mozambique | MOZ            | Munguissa                  | MOZ_R057 | Zambezia                   | MZ11             | Namacurra                  | MZ1120           | Macuze                  | MZ112001      | Furquia     |   -17.4577 |     37.2018 | Open          | 2015-01-10                    | Yes                                            | Zambezia                           | Namacurra                          | Macuze                          | Furquia                   |                             209 |                               863 |                                                       24 |                                                          52 |                                                                               185 |                                                                                  811 |                             24 |                               16 |                      48 |                        96 |                   176 |                     112 |                     184 |                       199 |                           0 |                             8 |          432 |            431 |


````

### Model Response

```
```json
{
    "column_mappings": [
        ["date reported", "Date Reported"],
        ["Date of Assessment", "Date of Current Survey"],
        ["Round Number:", "Survey Round"],
        ["1.1.e.2 Province (Admin 1)", "Site location (Province)"],
        ["Province pcode", "Province PCODE"],
        ["1.1.e.3 District (Admin 2)", "Site location (District)"],
        ["District pcode", "District PCODE"],
        ["1.1.e.4 Post (Admin 3)", "Site location (Posto)"],
        ["Locality:", "Locality:"],
        ["Latitude", "Latitude"],
        ["Longitude", "Longitude"],
        ["Total Households Affected", "Number of families/households"],
        ["Total Individuals Affected", "Total number of IDP individuals"]
    ]
}
```
```

### Correct Answer

```
{
  "column_mappings": [
    [
      "date reported",
      "Date Reported"
    ],
    [
      "Date of Assessment",
      "Date of Current Survey"
    ],
    [
      "Round Number:",
      "Survey Round"
    ],
    [
      "1.1.e.2 Province (Admin 1)",
      "Site location (Province)"
    ],
    [
      "Province pcode",
      "Province PCODE"
    ],
    [
      "1.1.e.3 District (Admin 2)",
      "Site location (District)"
    ],
    [
      "District pcode",
      "District PCODE"
    ],
    [
      "1.1.e.4 Post (Admin 3)",
      "Site location (Posto)"
    ],
    [
      "Locality:",
      "Locality:"
    ],
    [
      "Latitude",
      "Latitude"
    ],
    [
      "Longitude",
      "Longitude"
    ],
    [
      "Total Households Affected",
      "Number of families/households"
    ],
    [
      "Total Individuals Affected",
      "Total number of IDP individuals"
    ]
  ]
}
```


---

## Question 8: miller2_View -Unionable_miller2_both_0_1_ac4_av (miller2)

**Dataset:** miller2  
**Test case:** miller2_View -Unionable_miller2_both_0_1_ac4_av  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to null. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or null]. Provide the mapping for each column in Table A and return all mappings in a list.

No explanation and return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

TableA:
| Fiscal year   | Project number   | Status   |   Maximum CIDA contribution (project-level) | Branch ID   | Branch name                         | Division ID   | Division name                      | Section ID   | Section name                            |   Regional program (marker) |   Fund centre ID | Fund centre name   |   Untied amount(Project-level budget) |   FSTC percent |   IRTC percent |   CFLI (marker) | CIDA business delivery model (old)   | Programming process (new)   |   Bilateral aid (international marker) | PBA type   |   Enviromental sustainability (marker) |   Climate change adaptation (marker) |   Climate change mitigation (marker) |   Desertification (marker) |   Participatory development and good governance |
|:--------------|:-----------------|:---------|--------------------------------------------:|:------------|:------------------------------------|:--------------|:-----------------------------------|:-------------|:----------------------------------------|----------------------------:|-----------------:|:-------------------|--------------------------------------:|---------------:|---------------:|----------------:|:-------------------------------------|:----------------------------|---------------------------------------:|:-----------|---------------------------------------:|-------------------------------------:|-------------------------------------:|---------------------------:|------------------------------------------------:|
| 2009201o      | A017716001       | Closed   |                                 8.50027e+06 | B4100       | OGM Asia Pacific                    | D4100         | OAD Asia Programming               | S4122        | Bangladesh Section                      |                           0 |             4122 | Bangladesh         |                           8.50027e+06 |              1 |              0 |               0 | Directive                            | Uncoded: Pre-APP            |                                      1 | Not PBA    |                                      0 |                                    0 |                                    0 |                          0 |                                               0 |
| 20092019      | A017716001       | Closed   |                                 8.50027e+06 | B4100       | OGM Asia Pacific                    | D4100         | OAD Asia Programming               | S4122        | Bangladesh Section                      |                           0 |             4122 | Bangladesh         |                           8.50027e+06 |              1 |              0 |               0 | Directive                            | Uncoded: Pre-APP            |                                      1 | Not PBA    |                                      0 |                                    0 |                                    0 |                          0 |                                               0 |
| 200p2010      | A017716001       | Closed   |                                 8.50027e+06 | B4100       | OGM Asia Pacific                    | D4100         | OAD Asia Programming               | S4122        | Bangladesh Section                      |                           0 |             4122 | Bangladesh         |                           8.50027e+06 |              1 |              0 |               0 | Directive                            | Uncoded: Pre-APP            |                                      1 | Not PBA    |                                      0 |                                    0 |                                    0 |                          0 |                                               0 |
| 2009e010      | A018652001       | Closed   |                            500458           | B3100       | EGM Europe, Middle East and Maghreb | D3100         | EDD Europe-Middle East Programming | S4264        | West Bank Gaza & Palestinian Refugees   |                           0 |             4265 | West Bank Gaza     |                           0           |              0 |              0 |               0 | Directive                            | Uncoded: Pre-APP            |                                      1 | Not PBA    |                                      0 |                                    0 |                                    0 |                          0 |                                               0 |
| 20093010      | A018893001       | Closed   |                                 1.44101e+07 | B4200       | WGM Sub-Saharan Africa              | D4207         | WWD West & Central Africa          | S4215        | Mali Program Section                    |                           0 |             4216 | Mali               |                           1.44101e+07 |              1 |              0 |               0 | Responsive                           | Uncoded: Pre-APP            |                                      1 | Not PBA    |                                      0 |                                    0 |                                    0 |                          0 |                                               1 |
| 20002010      | A018893001       | Closed   |                                 1.44101e+07 | B4200       | WGM Sub-Saharan Africa              | D4207         | WWD West & Central Africa          | S4215        | Mali Program Section                    |                           0 |             4216 | Mali               |                           1.44101e+07 |              1 |              0 |               0 | Responsive                           | Uncoded: Pre-APP            |                                      1 | Not PBA    |                                      0 |                                    0 |                                    0 |                          0 |                                               1 |
| 20082010      | A018893001       | Closed   |                                 1.44101e+07 | B4200       | WGM Sub-Saharan Africa              | D4207         | WWD West & Central Africa          | S4215        | Mali Program Section                    |                           0 |             4216 | Mali               |                           1.44101e+07 |              1 |              0 |               0 | Responsive                           | Uncoded: Pre-APP            |                                      1 | Not PBA    |                                      0 |                                    0 |                                    0 |                          0 |                                               1 |
| 20092019      | A019043001       | Closed   |                                 1.37432e+07 | B4100       | OGM Asia Pacific                    | D4100         | OAD Asia Programming               | S4141        | OAA Afghanistan, Pakistan and Sri Lanka |                           0 |             4124 | Pakistan           |                           1.37432e+07 |              1 |              0 |               0 | Responsive                           | Uncoded: Pre-APP            |                                      1 | Not PBA    |                                      0 |                                    0 |                                    0 |                          0 |                                               1 |
| 200i2010      | A019043001       | Closed   |                                 1.37432e+07 | B4100       | OGM Asia Pacific                    | D4100         | OAD Asia Programming               | S4141        | OAA Afghanistan, Pakistan and Sri Lanka |                           0 |             4124 | Pakistan           |                           1.37432e+07 |              1 |              0 |               0 | Responsive                           | Uncoded: Pre-APP            |                                      1 | Not PBA    |                                      0 |                                    0 |                                    0 |                          0 |                                               1 |
| e0092010      | A019043001       | Closed   |                                 1.37432e+07 | B4100       | OGM Asia Pacific                    | D4100         | OAD Asia Programming               | S4141        | OAA Afghanistan, Pakistan and Sri Lanka |                           0 |             4124 | Pakistan           |                           1.37432e+07 |              1 |              0 |               0 | Responsive                           | Uncoded: Pre-APP            |                                      1 | Not PBA    |                                      0 |                                    0 |                                    0 |                          0 |                                               1 |

TableB:
| miller2_FisY   |   miller2_TrDevel |   miller2_Bio |   miller2_UrIss |   miller2_ChiIss |   miller2_YoIss |   miller2_IndiIs |   miller2_DisabIss |   miller2_ICTAATFDeve |   miller2_KnoFDevel |   miller2_GeEq |   miller2_OrganiID | miller2_OrgNa                                                        | miller2_OrgaTy             | miller2_OrganiCla   | miller2_OrgS          |   miller2_ContiID | miller2_ContiN   | miller2_ProBroCoID   | miller2_CouRegID   | miller2_CouRegN   |   miller2_CounRegPerc |   miller2_SecID | miller2_SeN                                              |   miller2_SecPerc |   miller2_AmSpe |
|:---------------|------------------:|--------------:|----------------:|-----------------:|----------------:|-----------------:|-------------------:|----------------------:|--------------------:|---------------:|-------------------:|:---------------------------------------------------------------------|:---------------------------|:--------------------|:----------------------|------------------:|:-----------------|:---------------------|:-------------------|:------------------|----------------------:|----------------:|:---------------------------------------------------------|------------------:|----------------:|
| 2009/2010      |                 0 |             0 |               0 |                0 |               0 |                0 |                  0 |                     1 |                   1 |              0 |            1005967 | IAEA - International Atomic Energy Agency Technical Cooperation Fund | Foreign Non-Profit Making  | Multilateral        | UNITED NATIONS        |                 3 | Asia             | X3                   | X3                 | Asia MC           |                  0.22 |           33140 | Multilateral trade negotiations                          |             0.14  |     75768       |
| 2009/2010      |                 0 |             0 |               0 |                0 |               0 |                0 |                  0 |                     1 |                   1 |              0 |            1005967 | IAEA - International Atomic Energy Agency Technical Cooperation Fund | Foreign Non-Profit Making  | Multilateral        | UNITED NATIONS        |                 3 | Asia             | X3                   | X3                 | Asia MC           |                  0.22 |           99810 | Sectors not specified                                    |             0.505 |    273306       |
| 2009/2010      |                 0 |             0 |               0 |                0 |               0 |                0 |                  0 |                     1 |                   1 |              0 |            1005967 | IAEA - International Atomic Energy Agency Technical Cooperation Fund | Foreign Non-Profit Making  | Multilateral        | UNITED NATIONS        |                 5 | Europe           | X4                   | X4                 | Europe MC         |                  0.32 |           12191 | Medical services                                         |             0.268 |    210970       |
| 2009/2010      |                 0 |             0 |               0 |                0 |               0 |                0 |                  0 |                     1 |                   1 |              0 |            1005967 | IAEA - International Atomic Energy Agency Technical Cooperation Fund | Foreign Non-Profit Making  | Multilateral        | UNITED NATIONS        |                 5 | Europe           | X4                   | X4                 | Europe MC         |                  0.32 |           14015 | Water resources conservation (including data collection) |             0.047 |     36998.4     |
| 2009/2010      |                 0 |             0 |               0 |                0 |               0 |                0 |                  0 |                     1 |                   1 |              0 |            1005967 | IAEA - International Atomic Energy Agency Technical Cooperation Fund | Foreign Non-Profit Making  | Multilateral        | UNITED NATIONS        |                 5 | Europe           | X4                   | X4                 | Europe MC         |                  0.32 |           23510 | Nuclear energy electric power plants                     |             0.04  |     31488       |
| 2009/2010      |                 0 |             0 |               0 |                0 |               0 |                0 |                  0 |                     1 |                   1 |              0 |            1005967 | IAEA - International Atomic Energy Agency Technical Cooperation Fund | Foreign Non-Profit Making  | Multilateral        | UNITED NATIONS        |                 5 | Europe           | X4                   | X4                 | Europe MC         |                  0.32 |           33140 | Multilateral trade negotiations                          |             0.14  |    110208       |
| 2009/2010      |                 0 |             0 |               0 |                0 |               0 |                0 |                  0 |                     1 |                   1 |              0 |            1005967 | IAEA - International Atomic Energy Agency Technical Cooperation Fund | Foreign Non-Profit Making  | Multilateral        | UNITED NATIONS        |                 5 | Europe           | X4                   | X4                 | Europe MC         |                  0.32 |           99810 | Sectors not specified                                    |             0.505 |    397536       |
| 2009/2010      |                 0 |             0 |               0 |                0 |               0 |                0 |                  0 |                     0 |                   0 |              0 |            1001300 | PAHO - Pan American Health Organization                              | Foreign Non-Profit Making  | Multilateral        | REGIONAL ORGANIZATION |                 1 | America          | SV                   | SV                 | El Salvador       |                  1    |           72010 | Material relief assistance and services                  |             1     |    300000       |
| 2009/2010      |                 0 |             0 |               0 |                0 |               0 |                0 |                  0 |                     0 |                   0 |              1 |            1014663 | ICRC Appeals via CRCS                                                | Canadian Non-Profit Making | Civil Society       | INTERNATIONAL NGO     |                 2 | Africa           | X1                   | X1                 | Africa MC         |                  0.5  |           72010 | Material relief assistance and services                  |             1     |         1.5e+06 |
| 2009/2010      |                 0 |             0 |               0 |                0 |               0 |                0 |                  0 |                     0 |                   0 |              1 |            1014663 | ICRC Appeals via CRCS                                                | Canadian Non-Profit Making | Civil Society       | INTERNATIONAL NGO     |                 1 | America          | X2                   | X2                 | Americas MC       |                  0.15 |           72010 | Material relief assistance and services                  |             1     |    450000       |


````

### Model Response

```
```json
{
  "column_mappings": [
    ["Fiscal year", "miller2_FisY"],
    ["Project number", null],
    ["Status", null],
    ["Maximum CIDA contribution (project-level)", null],
    ["Branch ID", null],
    ["Branch name", null],
    ["Division ID", null],
    ["Division name", null],
    ["Section ID", "miller2_SecID"],
    ["Section name", "miller2_SeN"],
    ["Regional program (marker)", "miller2_CounRegPerc"],
    ["Fund centre ID", "miller2_CouRegID"],
    ["Fund centre name", "miller2_CouRegN"],
    ["Untied amount(Project-level budget)", "miller2_ContiID"],
    ["FSTC percent", null],
    ["IRTC percent", null],
    ["CFLI (marker)", null],
    ["CIDA business delivery model (old)", null],
    ["Programming process (new)", null],
    ["Bilateral aid (international marker)", null],
    ["PBA type", null],
    ["Enviromental sustainability (marker)", null],
    ["Climate change adaptation (marker)", null],
    ["Climate change mitigation (marker)", null],
    ["Desertification (marker)", null],
    ["Participatory development and good governance", "miller2_SecPerc"]
  ]
}
```
```

### Correct Answer

```
{
  "column_mappings": [
    [
      "Fiscal year",
      "miller2_FisY"
    ],
    [
      "Project number",
      null
    ],
    [
      "Status",
      null
    ],
    [
      "Maximum CIDA contribution (project-level)",
      null
    ],
    [
      "Branch ID",
      null
    ],
    [
      "Branch name",
      null
    ],
    [
      "Division ID",
      null
    ],
    [
      "Division name",
      null
    ],
    [
      "Section ID",
      null
    ],
    [
      "Section name",
      null
    ],
    [
      "Regional program (marker)",
      null
    ],
    [
      "Fund centre ID",
      null
    ],
    [
      "Fund centre name",
      null
    ],
    [
      "Untied amount(Project-level budget)",
      null
    ],
    [
      "FSTC percent",
      null
    ],
    [
      "IRTC percent",
      null
    ],
    [
      "CFLI (marker)",
      null
    ],
    [
      "CIDA business delivery model (old)",
      null
    ],
    [
      "Programming process (new)",
      null
    ],
    [
      "Bilateral aid (international marker)",
      null
    ],
    [
      "PBA type",
      null
    ],
    [
      "Enviromental sustainability (marker)",
      null
    ],
    [
      "Climate change adaptation (marker)",
      null
    ],
    [
      "Climate change mitigation (marker)",
      null
    ],
    [
      "Desertification (marker)",
      null
    ],
    [
      "Participatory development and good governance",
      null
    ]
  ]
}
```


---

## Question 9: pair_160 (HXD)

**Dataset:** HXD  
**Test case:** pair_160  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Task: 
Please identify the matching columns between Table A and Table B. For each column in Table A, specify the corresponding column in Table B. If a column in A has no corresponding column in Table B, you can map it to null. Represent each column mapping using a pair of column headers in a list, i.e., [Table A Column, Table B column or null]. Provide the mapping for each column in Table A and return all mappings in a list.

No explanation and return the matching columns in a structured JSON format: {"column_mappings": <a list of column pairs>}.

TableA:
| GHO (CODE)     | GHO (DISPLAY)                                                                                                               | GHO (URL)                                                                 | DATASOURCE (DISPLAY)   | PUBLISHSTATE (CODE)   | PUBLISHSTATE (DISPLAY)   | YEAR (DISPLAY)   | REGION (CODE)   |   STARTYEAR |   ENDYEAR | REGION (DISPLAY)   | COUNTRY (CODE)   | COUNTRY (DISPLAY)   | SEX (CODE)   | SEX (DISPLAY)   |   Numeric |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------|:-----------------------|:----------------------|:-------------------------|:-----------------|:----------------|------------:|----------:|:-------------------|:-----------------|:--------------------|:-------------|:----------------|----------:|
| pnchome5       | Postnatal care visit within two days of birth - born outside a health facility (in the five years preceding the survey) (%) | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/3341 | DHS                    | PUBLISHED             | Published                | 2006             | AFR             |        2006 |      2006 | Africa             | SWZ              | Eswatini            |              |                 |      3.65 |
| WHOSIS_000008  | Children aged <5 years underweight (%)                                                                                      | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/27   | NLIS_312370            | PUBLISHED             | Published                | 2000             | AFR             |        2000 |      2000 | Africa             | SWZ              | Eswatini            | MLE          | Male            |      9.5  |
| PCV3           | Pneumoccocal conjugate vaccines (PCV3) immunization coverage among 1-year-olds (%)                                          | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4757 |                        | PUBLISHED             | Published                | 2018             | AFR             |        2018 |      2018 | Africa             | SWZ              | Eswatini            |              |                 |     88    |
| WHS4_128       | Neonates protected at birth against neonatal tetanus (PAB) (%)                                                              | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/98   |                        | PUBLISHED             | Published                | 2012             | AFR             |        2012 |      2012 | Africa             | SWZ              | Eswatini            |              |                 |     86    |
| LBW_PREVALENCE | Low birth weight, prevalence (%)                                                                                            | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/76   |                        | PUBLISHED             | Published                | 2006             | AFR             |        2006 |      2006 | Africa             | SWZ              | Eswatini            |              |                 |     10.6  |
| MCV2           | Measles-containing-vaccine second-dose (MCV2) immunization coverage by the nationally recommended age (%)                   | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4756 |                        | PUBLISHED             | Published                | 2005             | AFR             |        2005 |      2005 | Africa             | SWZ              | Eswatini            |              |                 |     99    |
| NUTRITION_WA_2 | Children aged <5 years underweight <br> (% weight-for-age <-2 SD) (%)                                                       | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/27   |                        | PUBLISHED             | Published                | 2008             | AFR             |        2008 |      2008 | Africa             | SWZ              | Eswatini            | BTSX         | Both sexes      |      7.3  |
| WHS4_544       | Polio (Pol3) immunization coverage among 1-year-olds (%)                                                                    | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/2443 |                        | PUBLISHED             | Published                | 2007             | AFR             |        2007 |      2007 | Africa             | SWZ              | Eswatini            |              |                 |     88    |
| NUTRITION_564  | Children aged <5 years wasted for age (%)                                                                                   | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/302  | NLIS_310124            | PUBLISHED             | Published                | 1983-1984        | AFR             |        1983 |      1984 | Africa             | SWZ              | Eswatini            | BTSX         | Both sexes      |      1.3  |
| MDG_0000000027 | Children aged <5 years stunted (%)                                                                                          | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/72   | NLIS_313289            | PUBLISHED             | Published                | 2014             | AFR             |        2014 |      2014 | Africa             | SWZ              | Eswatini            | BTSX         | Both sexes      |     25.5  |

TableB:
| GHO (CODE)   | GHO (DISPLAY)                                                                      | GHO (URL)                                                                 | DATASOURCE (DISPLAY)   | PUBLISHSTATE (CODE)   | PUBLISHSTATE (DISPLAY)   | YEAR (DISPLAY)   | REGION (CODE)   |   STARTYEAR |   ENDYEAR | REGION (DISPLAY)   | COUNTRY (CODE)   | COUNTRY (DISPLAY)   | SEX (CODE)   | SEX (DISPLAY)   |   Numeric |
|:-------------|:-----------------------------------------------------------------------------------|:--------------------------------------------------------------------------|:-----------------------|:----------------------|:-------------------------|:-----------------|:----------------|------------:|----------:|:-------------------|:-----------------|:--------------------|:-------------|:----------------|----------:|
| WHS4_106     | Children aged < 5 years with pneumonia symptoms taken to a healthcare provider (%) | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4737 | SWZ MICS 2000          | PUBLISHED             | Published                | 2000             | AFR             |        2000 |      2000 | Africa             | SWZ              | Eswatini            |              |                 |      63   |
| WHS4_106     | Children aged < 5 years with pneumonia symptoms taken to a healthcare provider (%) | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4737 | SWZ MICS 2014          | PUBLISHED             | Published                | 2014             | AFR             |        2014 |      2014 | Africa             | SWZ              | Eswatini            |              |                 |      62.6 |
| WHS4_106     | Children aged < 5 years with pneumonia symptoms taken to a healthcare provider (%) | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4737 | SWZ MICS 2010          | PUBLISHED             | Published                | 2010             | AFR             |        2010 |      2010 | Africa             | SWZ              | Eswatini            | MLE          | Male            |      57.2 |
| WHS4_106     | Children aged < 5 years with pneumonia symptoms taken to a healthcare provider (%) | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4737 | SWZ DHS 2006-2007      | PUBLISHED             | Published                | 2006-2007        | AFR             |        2006 |      2007 | Africa             | SWZ              | Eswatini            | MLE          | Male            |      70.6 |
| WHS4_106     | Children aged < 5 years with pneumonia symptoms taken to a healthcare provider (%) | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4737 | SWZ MICS 2010          | PUBLISHED             | Published                | 2010             | AFR             |        2010 |      2010 | Africa             | SWZ              | Eswatini            | BTSX         | Both sexes      |      57.6 |
| WHS4_106     | Children aged < 5 years with pneumonia symptoms taken to a healthcare provider (%) | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4737 | SWZ MICS 2014          | PUBLISHED             | Published                | 2014             | AFR             |        2014 |      2014 | Africa             | SWZ              | Eswatini            |              |                 |      59.6 |
| WHS4_106     | Children aged < 5 years with pneumonia symptoms taken to a healthcare provider (%) | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4737 | SWZ DHS 2006-2007      | PUBLISHED             | Published                | 2006-2007        | AFR             |        2006 |      2007 | Africa             | SWZ              | Eswatini            | FMLE         | Female          |      76.9 |
| WHS4_106     | Children aged < 5 years with pneumonia symptoms taken to a healthcare provider (%) | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4737 | SWZ MICS 2010          | PUBLISHED             | Published                | 2010             | AFR             |        2010 |      2010 | Africa             | SWZ              | Eswatini            |              |                 |      57.6 |
| WHS6_102     | Hospital beds (per 10 000 population)                                              | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/97   |                        | PUBLISHED             | Published                | 2006             | AFR             |        2006 |      2006 | Africa             | SWZ              | Eswatini            |              |                 |      21   |
| WHS6_102     | Hospital beds (per 10 000 population)                                              | https://www.who.int/data/gho/indicator-metadata-registry/imr-details/97   |                        | PUBLISHED             | Published                | 2011             | AFR             |        2011 |      2011 | Africa             | SWZ              | Eswatini            |              |                 |      21   |


````

### Model Response

```
```json
{
  "column_mappings": [
    ["GHO (CODE)", "GHO (CODE)"],
    ["GHO (DISPLAY)", "GHO (DISPLAY)"],
    ["GHO (URL)", "GHO (URL)"],
    ["DATASOURCE (DISPLAY)", "DATASOURCE (DISPLAY)"],
    ["PUBLISHSTATE (CODE)", "PUBLISHSTATE (CODE)"],
    ["PUBLISHSTATE (DISPLAY)", "PUBLISHSTATE (DISPLAY)"],
    ["YEAR (DISPLAY)", "YEAR (DISPLAY)"],
    ["REGION (CODE)", "REGION (CODE)"],
    ["STARTYEAR", "STARTYEAR"],
    ["ENDYEAR", "ENDYEAR"],
    ["REGION (DISPLAY)", "REGION (DISPLAY)"],
    ["COUNTRY (CODE)", "COUNTRY (CODE)"],
    ["COUNTRY (DISPLAY)", "COUNTRY (DISPLAY)"],
    ["SEX (CODE)", "SEX (CODE)"],
    ["SEX (DISPLAY)", "SEX (DISPLAY)"],
    ["Numeric", "Numeric"]
  ]
}
```
```

### Correct Answer

```
{
  "column_mappings": [
    [
      "GHO (CODE)",
      "GHO (CODE)"
    ],
    [
      "GHO (DISPLAY)",
      "GHO (DISPLAY)"
    ],
    [
      "GHO (URL)",
      "GHO (URL)"
    ],
    [
      "DATASOURCE (DISPLAY)",
      "DATASOURCE (DISPLAY)"
    ],
    [
      "PUBLISHSTATE (CODE)",
      "PUBLISHSTATE (CODE)"
    ],
    [
      "PUBLISHSTATE (DISPLAY)",
      "PUBLISHSTATE (DISPLAY)"
    ],
    [
      "YEAR (DISPLAY)",
      "YEAR (DISPLAY)"
    ],
    [
      "REGION (CODE)",
      "REGION (CODE)"
    ],
    [
      "STARTYEAR",
      "STARTYEAR"
    ],
    [
      "ENDYEAR",
      "ENDYEAR"
    ],
    [
      "REGION (DISPLAY)",
      "REGION (DISPLAY)"
    ],
    [
      "COUNTRY (CODE)",
      "COUNTRY (CODE)"
    ],
    [
      "COUNTRY (DISPLAY)",
      "COUNTRY (DISPLAY)"
    ],
    [
      "SEX (CODE)",
      "SEX (CODE)"
    ],
    [
      "SEX (DISPLAY)",
      "SEX (DISPLAY)"
    ],
    [
      "Numeric",
      "Numeric"
    ]
  ]
}
```

