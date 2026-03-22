# MMTU Evaluation Questions

Total questions: 129

---

## Arithmetic-Relationship__case_695

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|   A | B                      |         C |          D |       E |       F |         G |
|----:|:-----------------------|----------:|-----------:|--------:|--------:|----------:|
| 610 | Allan Hancock          |   7534.91 |    0       |  547.44 |  411.48 |   8493.83 |
| 620 | Antelope Valley        |  11613    |  319.57    |   43.96 |    0    |  11657    |
| 910 | Barstow                |   2464.42 |  114.402   |   32.55 |    0    |   2496.97 |
| 110 | Butte-Glenn            |   9656.1  |    7e-06   | 1177.11 |   32.15 |  10865.4  |
| 410 | Cabrillo               |   9184.82 |    0       |  182.39 |    0    |   9367.21 |
| 810 | Cerritos               |  17325    |  555.83    |  117.31 |  298.48 |  17740.8  |
| 480 | Chabot-Las Positas     |  17504.2  |  429.39    |  135.85 |    0    |  17640    |
| 920 | Chaffey                |  15489.4  | 1152.03    |  359.9  |    0    |  15849.3  |
| 820 | Citrus                 |  11378.5  |  261.81    |  272.26 |  132.19 |  11783    |
| 830 | Coast                  |  32335.1  |    0       |  288.66 |    0    |  32623.8  |
| 710 | Compton                |   5982.99 |   -7.2e-05 |   23.01 |    0    |   6006    |
| 310 | Contra Costa           |  29353.1  |  667.893   |  135.74 |    0    |  29488.8  |
| 970 | Copper Mountain        |   1397.72 |   -7.5e-05 |   82.1  |    2.46 |   1482.28 |
| 930 | Desert                 |   8435.03 | 1093.58    |   24.92 |  593.5  |   9053.45 |
| 720 | El Camino              |  19463.2  |  325.99    |   22.76 |    0    |  19486    |
| 120 | Feather River          |   1576.62 |   57.5786  |   43.26 |    0    |   1619.88 |
| 420 | Foothill-DeAnza        |  26757.6  |    0       |  215.89 |  169.43 |  27142.9  |
| 440 | Gavilan                |   4294.03 |    0       |  439.07 |   85.28 |   4818.38 |
| 730 | Glendale               |  11297.3  |    0       |  257.1  | 2538.98 |  14093.4  |
|  20 | Grossmont-Cuyamaca     |  18727.6  |  592.65    |   21.93 |    0    |  18749.5  |
| 450 | Hartnell               |   7276.54 |  250.306   |   17.8  |    0    |   7294.34 |
|  30 | Imperial               |   6770.48 |    0       |   24.72 |   16.7  |   6811.9  |
| 520 | Kern                   |  20732.1  |  936.992   |   61.47 |    0    |  20793.5  |
| 220 | Lake Tahoe             |   1620.22 |    0       |   36.4  |   22.09 |   1678.71 |
| 130 | Lassen                 |   1302.78 |    0       |   63.14 |    0    |   1365.92 |
| 840 | Long Beach             |  18622.6  |    0       |   64.72 |  389.99 |  19077.3  |
| 740 | Los Angeles            | 101464    | 2408.38    | 2034.51 | 4102.57 | 107601    |
| 230 | Los Rios               |  47527.5  |    0       |  251.75 |    0    |  47779.2  |
| 330 | Marin                  |   3566.03 |    0       |  240.72 |    0    |   3806.75 |
| 140 | Mendocino-Lake         |   2502.68 |    0       |   38.53 |   43.1  |   2584.31 |
| 530 | Merced                 |   8194.74 |    0       |  318.14 |  633.52 |   9146.4  |
|  50 | Mira Costa             |  10684.6  |  774.84    |  663.74 |    0    |  11348.3  |
| 460 | Monterey Peninsula     |   5789.88 |    0       |  355.9  |  115.98 |   6261.76 |
| 850 | Mt. San Antonio        |  25096.3  |  814.96    | 1644.62 | 4643.56 |  31384.5  |
| 940 | Mt. San Jacinto        |  11249.8  | 1259.06    |  323.88 |  315.98 |  11889.6  |
| 240 | Napa Valley            |   5036.74 |    0       |  539.61 |   13.89 |   5590.24 |
| 860 | North Orange County    |  30332.1  | 1645.43    | 2724.79 | 2777.81 |  35834.7  |
| 430 | Ohlone                 |   7065.28 |    0       |    0    |    0    |   7065.28 |
| 950 | Palo Verde             |   1948.66 |  203.951   |  108.07 |    0    |   2056.73 |
|  60 | Palomar                |  15801.9  |    0       |  280.2  |  520.71 |  16602.8  |
| 770 | Pasadena Area          |  22282.7  | 1187.95    |  183.34 | 1036.18 |  23502.2  |
| 340 | Peralta                |  19409.3  |    0       |  119.13 |    0    |  19528.5  |
| 870 | Rancho Santiago        |  22274.1  |  -91.69    |  702.14 | 5925.41 |  28901.6  |
| 160 | Redwoods               |   3549.91 |    0       |   54.32 |   31.68 |   3635.91 |
| 880 | Rio Hondo              |  12503.3  |  111.9     |  365.21 |   37.38 |  12905.9  |
| 960 | Riverside              |  28599.6  | 1716.81    |   82.8  |    0    |  28682.4  |
| 980 | San Bernardino         |  15275.7  | 1087.12    |   67.08 |    0    |  15342.7  |
|  70 | San Diego              |  34919    | 1507.74    | 2077.72 | 6289.53 |  43286.3  |
| 360 | San Francisco          |  15012.2  |    0       | 2110.73 | 4806.76 |  21929.7  |
| 550 | San Joaquin Delta      |  16165.3  |  476.91    |  171.42 |    0    |  16336.7  |
| 470 | San Jose-Evergreen     |  11493.1  |    0       |   87.43 |    0    |  11580.5  |
| 640 | San Luis Obispo County |   8036.95 |   -6.8e-05 |  109.19 |  173.86 |   8320    |
| 370 | San Mateo County       |  17216.7  |    0       |   87.46 |    0    |  17304.1  |
| 650 | Santa Barbara          |  12675    |    0       |  147.59 |  387.68 |  13210.3  |
| 660 | Santa Clarita          |  15566.4  |  729.436   |  246.74 |  181.64 |  15994.8  |
| 780 | Santa Monica           |  21263.9  |  360.63    |  597.29 |  167.26 |  22028.4  |
| 560 | Sequoias               |   8921.49 |  463.98    |  339.26 |  169.53 |   9430.28 |
| 170 | Shasta-Tehama-Trinity  |   5907.72 |    0       |  177.17 |   34.34 |   6119.23 |
| 270 | Sierra                 |  14578.9  |  177.29    |  296.83 |    0    |  14875.7  |
| 180 | Siskiyou               |   2354.38 |  195.941   |   63.79 |  401.67 |   2819.84 |
| 280 | Solano County          |   8272.73 |    0       |   15.12 |    0    |   8287.85 |
| 260 | Sonoma County          |  16518.8  |   -9.9e-05 | 2303.55 |  592.23 |  19414.6  |
| 890 | South Orange County    |  21433.6  |    0       | 2030.21 |  169.1  |  23632.9  |
|  90 | Southwestern           |  13509.5  |    0       |  220.62 |   37.32 |  13767.4  |
| 570 | State Center           |  28765.4  | 1757.88    |  270.64 |  158.08 |  29194.2  |
| 680 | Ventura County         |  26405.2  |  561.99    |   61.88 |    0    |  26467    |
| 990 | Victor Valley          |   9141.67 |    3.82442 |   70.88 |    0    |   9212.55 |
| 580 | West Hills             |   4934.96 |  209.99    |  346.65 |    0    |   5281.61 |
| 690 | West Kern              |   2519.69 |   50.4596  |   44.69 |    0    |   2564.38 |
| 490 | West Valley-Mission    |  12344.3  |    0       | 1087.3  |    0    |  13431.6  |
| 590 | Yosemite               |  16226.9  |    0       |  175.66 |  168.85 |  16571.4  |
| 290 | Yuba                   |   7484.81 |    0       |  141.61 |    0    |   7626.42 |



---

## Arithmetic-Relationship__case_111

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
| M                 |      N |      O |        P |
|:------------------|-------:|-------:|---------:|
| yw                | 1025.9 |  409.4 | 2.50586  |
| yw                |  752.8 |  786   | 0.957761 |
| yw                |  666.8 |  560.3 | 1.19008  |
| yw                |  277.3 |  234.4 | 1.18302  |
| yw                |  448.1 |  771.9 | 0.580516 |
| yw                |  456.3 |  313.8 | 1.45411  |
| yw                |  128.8 |  135.5 | 0.950554 |
| yw                | 1214.4 | 1012.8 | 1.19905  |
| yw                | 1237.2 | 1194.1 | 1.03609  |
| yw                |  119.1 |  172.8 | 0.689236 |
| yw                |  102.6 |  164.2 | 0.624848 |
| yw                |  508.9 |  368.5 | 1.381    |
| yw                |  732.6 |  568.9 | 1.28775  |
| yw                |  254.7 |  129.8 | 1.96225  |
| fascin-/-         |  655.9 |  411.8 | 1.59276  |
| fascin-/-         |  649.8 |  246.3 | 2.63825  |
| fascin-/-         |  783.1 |  266.3 | 2.94067  |
| fascin-/-         | 1286.4 |  453.6 | 2.83598  |
| fascin-/-         |   67.8 |   29.9 | 2.26756  |
| fascin-/-         |  297.4 |   98.5 | 3.01929  |
| fascin-/-         |  279.1 |  118.2 | 2.36125  |
| fascin-/-         |  115.9 |   85.1 | 1.36193  |
| fascin-/-  y27632 |  522.1 |  716.7 | 0.728478 |
| fascin-/-  y27633 |  436.7 |  439.8 | 0.992951 |
| fascin-/-  y27634 |  341.3 |  344.1 | 0.991863 |
| fascin-/-  y27635 | 1451.7 | 1901.1 | 0.763611 |
| fascin-/-  y27636 |  850.3 | 1253.3 | 0.678449 |
| fascin-/-  y27637 |  295.9 |  268.4 | 1.10246  |
| fascin-/-  y27638 |  323.7 |  307.3 | 1.05337  |
| fascin-/-  y27639 |  891.5 |  778.1 | 1.14574  |
| fascin-/-  y27640 |  742   |  747.5 | 0.992642 |
| fascin-/-  y27641 |  184.1 |  134.1 | 1.37286  |
| fascin-/-  y27642 |  101   |  132.3 | 0.763416 |
| fascin-/-  y27643 |  118.2 |  121.4 | 0.973641 |
| fascin-/-  y27644 |  106.8 |  137.7 | 0.775599 |
| fascin-/-  y27645 |  733.1 |  421.6 | 1.73885  |
| fascin-/-  y27646 |  696.8 |  450   | 1.54844  |
| fascin-/-  y27647 |  149.4 |  187.1 | 0.798503 |
| fascin-/-  y27648 |  205.6 |  218.6 | 0.940531 |
| fascin-/-  y27649 |  145.9 |  156.6 | 0.931673 |
| fascin-/-  y27650 |  114.3 |  114.9 | 0.994778 |
| fascin-/-  y27651 |  201.2 |  182.8 | 1.10066  |
| fascin-/-  y27652 |  109.6 |  102.5 | 1.06927  |
| fascin-/-  y27653 |  124.6 |  163.1 | 0.763948 |
| fascin-/-  y27654 |   85.3 |  133.4 | 0.63943  |
| fascin-/- bleb    | 1332.5 | 1721.6 | 0.773989 |
| fascin-/- bleb    |  412.5 |  441.6 | 0.934103 |
| fascin-/- bleb    |  980.2 | 1009.1 | 0.971361 |
| fascin-/- bleb    | 1800.6 | 1078.2 | 1.67001  |
| fascin-/- bleb    |  450.2 |  497.3 | 0.905289 |
| fascin-/- bleb    |  529.3 |  579.4 | 0.913531 |
| fascin-/- bleb    |  234.8 |  179.4 | 1.30881  |
| fascin-/- bleb    |  457.5 |  442.2 | 1.0346   |
| fascin-/- bleb    |  505.6 |  512.2 | 0.987114 |
| fascin-/- bleb    |  331.3 |  338.1 | 0.979888 |
| fascin-/- bleb    |  234   |  223.4 | 1.04745  |
| fascin-/- bleb    |  280.1 |  260.1 | 1.07689  |
| fascin-/- bleb    |  179.3 |  221   | 0.811312 |
| fascin-/- bleb    |  173.3 |  164.8 | 1.05158  |
| fascin-/- bleb    |  437   |  331.3 | 1.31905  |
| fascin-/- bleb    |  577.7 |  435.9 | 1.3253   |
| fascin-/- bleb    |  396.2 |  378.5 | 1.04676  |



---

## Arithmetic-Relationship__case_3

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|    A | B   | C           | D   |   E |    F |         G |    H |    I |       J |
|-----:|:----|:------------|:----|----:|-----:|----------:|-----:|-----:|--------:|
| 1234 | A   | Clothing    | Jan | 872 | 1286 | 0.321928  |  414 |  414 |  532404 |
| 1235 | B   | Accessories | Jan | 312 | 1197 | 0.739348  |  885 |  885 | 1059345 |
| 1236 | C   | Jewlery     | Jan | 363 |  742 | 0.510782  |  379 |  379 |  281218 |
| 1237 | D   | Clothing    | Jan | 744 |  594 | 0.252525  |  150 |  150 |   89100 |
| 1238 | E   | Accessories | Jan | 215 |  697 | 0.691535  |  482 |  482 |  335954 |
| 1239 | F   | Jewlery     | Jan | 954 |  657 | 0.452055  |  297 |  297 |  195129 |
| 1240 | G   | Clothing    | Jan | 621 |  486 | 0.277778  |  135 |  135 |   65610 |
| 1241 | H   | Accessories | Jan | 617 | 1375 | 0.551273  |  758 |  758 | 1042250 |
| 1242 | I   | Jewlery     | Jan | 252 |  797 | 0.683814  |  545 |  545 |  434365 |
| 1243 | J   | Clothing    | Jan | 842 |  977 | 0.138178  |  135 |  135 |  131895 |
| 1244 | K   | Accessories | Jan |  54 |  572 | 0.905594  |  518 |  518 |  296296 |
| 1245 | L   | Jewlery     | Jan |  78 |  437 | 0.82151   |  359 |  359 |  156883 |
| 1246 | M   | Clothing    | Jan | 326 | 1445 | 0.774394  | 1119 | 1119 | 1616955 |
| 1247 | N   | Accessories | Jan | 122 |  362 | 0.662983  |  240 |  240 |   86880 |
| 1248 | O   | Jewlery     | Jan | 627 |  765 | 0.180392  |  138 |  138 |  105570 |
| 1249 | P   | Clothing    | Jan | 717 |  500 | 0.434     |  217 |  217 |  108500 |
| 1250 | Q   | Accessories | Jan | 402 |  858 | 0.531469  |  456 |  456 |  391248 |
| 1234 | A   | Clothing    | Feb | 898 |  872 | 0.0298165 |   26 |   26 |   22672 |
| 1235 | B   | Accessories | Feb | 324 | 1283 | 0.747467  |  959 |  959 | 1230397 |
| 1236 | C   | Jewlery     | Feb | 235 |  101 | 1.32673   |  134 |  134 |   13534 |
| 1237 | D   | Clothing    | Feb | 913 |  643 | 0.419907  |  270 |  270 |  173610 |
| 1238 | E   | Accessories | Feb | 271 | 1103 | 0.754306  |  832 |  832 |  917696 |
| 1239 | F   | Jewlery     | Feb | 499 | 1360 | 0.633088  |  861 |  861 | 1170960 |
| 1240 | G   | Clothing    | Feb | 971 |  681 | 0.425844  |  290 |  290 |  197490 |
| 1241 | H   | Accessories | Feb | 764 | 1480 | 0.483784  |  716 |  716 | 1059680 |
| 1242 | I   | Jewlery     | Feb | 977 | 1077 | 0.0928505 |  100 |  100 |  107700 |
| 1243 | J   | Clothing    | Feb | 533 |  181 | 1.94475   |  352 |  352 |   63712 |
| 1244 | K   | Accessories | Feb | 388 | 1102 | 0.647913  |  714 |  714 |  786828 |
| 1245 | L   | Jewlery     | Feb | 209 |  354 | 0.409605  |  145 |  145 |   51330 |
| 1246 | M   | Clothing    | Feb | 300 | 1030 | 0.708738  |  730 |  730 |  751900 |
| 1247 | N   | Accessories | Feb | 256 |   49 | 4.22449   |  207 |  207 |   10143 |
| 1248 | O   | Jewlery     | Feb | 383 |  674 | 0.431751  |  291 |  291 |  196134 |
| 1249 | P   | Clothing    | Feb | 567 |  701 | 0.191155  |  134 |  134 |   93934 |
| 1250 | Q   | Accessories | Feb | 383 |  411 | 0.0681265 |   28 |   28 |   11508 |
| 1234 | A   | Clothing    | Mar | 561 |  381 | 0.472441  |  180 |  180 |   68580 |
| 1235 | B   | Accessories | Mar | 701 |  406 | 0.726601  |  295 |  295 |  119770 |
| 1236 | C   | Jewlery     | Mar | 923 |  615 | 0.500813  |  308 |  308 |  189420 |
| 1237 | D   | Clothing    | Mar | 678 | 1367 | 0.504023  |  689 |  689 |  941863 |
| 1238 | E   | Accessories | Mar | 442 | 1463 | 0.697881  | 1021 | 1021 | 1493723 |
| 1239 | F   | Jewlery     | Mar | 964 | 1466 | 0.342428  |  502 |  502 |  735932 |
| 1240 | G   | Clothing    | Mar | 159 | 1401 | 0.88651   | 1242 | 1242 | 1740042 |
| 1241 | H   | Accessories | Mar | 487 | 1368 | 0.644006  |  881 |  881 | 1205208 |
| 1242 | I   | Jewlery     | Mar | 564 |  800 | 0.295     |  236 |  236 |  188800 |
| 1243 | J   | Clothing    | Mar |  81 | 1059 | 0.923513  |  978 |  978 | 1035702 |
| 1244 | K   | Accessories | Mar | 162 | 1106 | 0.853526  |  944 |  944 | 1044064 |
| 1245 | L   | Jewlery     | Mar | 679 | 1192 | 0.430369  |  513 |  513 |  611496 |
| 1246 | M   | Clothing    | Mar | 212 |  621 | 0.658615  |  409 |  409 |  253989 |
| 1247 | N   | Accessories | Mar |  65 |  452 | 0.856195  |  387 |  387 |  174924 |
| 1248 | O   | Jewlery     | Mar | 841 | 1282 | 0.343994  |  441 |  441 |  565362 |
| 1249 | P   | Clothing    | Mar | 165 |  836 | 0.802632  |  671 |  671 |  560956 |
| 1250 | Q   | Accessories | Mar | 153 | 1363 | 0.887748  | 1210 | 1210 | 1649230 |



---

## Arithmetic-Relationship__case_820

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|   CF | CG                                       |   CH |   CI |   CJ |
|-----:|:-----------------------------------------|-----:|-----:|-----:|
|    1 | Cash and cash equivalents                |    0 |    0 |    0 |
|    2 | Short-term investments                   |    0 |    0 |    0 |
|    3 | Medicaid capitation receivable           |    0 |    0 |    0 |
|    4 | Investment income receivable             |    0 |    0 |    0 |
|    5 | Reinsurance receivable                   |    0 |    0 |    0 |
|    6 | Withhold receivable current year         |    0 |    0 |    0 |
|    7 | Withhold receivable prior years          |    0 |    0 |    0 |
|    8 | Quality incentive receivables            |    0 |    0 |    0 |
|    9 | VBP receivables                          |    0 |    0 |    0 |
|   10 | Due from affiliates (current)            |    0 |    0 |    0 |
|   11 | Other current assets                     |    0 |    0 |    0 |
|   12 | Total Current Assets                     |    0 |    0 |    0 |
|   13 | Statutory Deposits                       |    0 |    0 |    0 |
|   14 | Restricted cash and other assets         |    0 |    0 |    0 |
|   15 | Due from affiliates (non-current)        |    0 |    0 |    0 |
|   16 | Long-term investments                    |    0 |    0 |    0 |
|   17 | Other non-current assets                 |    0 |    0 |    0 |
|   18 | Total Other Assets                       |    0 |    0 |    0 |
|   19 | Land                                     |    0 |    0 |    0 |
|   20 | Buildings                                |    0 |    0 |    0 |
|   21 | Leasehold improvements                   |    0 |    0 |    0 |
|   22 | Furniture and equipment                  |    0 |    0 |    0 |
|   23 | Other property and equipment             |    0 |    0 |    0 |
|   24 | Total Property and Equipment             |    0 |    0 |    0 |
|   25 | Accumulated depreciation/amortization    |    0 |    0 |    0 |
|   26 | Net Property and Equipment               |    0 |    0 |    0 |
|   27 | TOTAL ASSETS                             |    0 |    0 |    0 |
|   28 | Accounts payable                         |    0 |    0 |    0 |
|   29 | Accrued administrative expenses          |    0 |    0 |    0 |
|   30 | Subcapitation payable                    |    0 |    0 |    0 |
|   31 | Claims payable                           |    0 |    0 |    0 |
|   32 | Incurred but not reported (IBNR)         |    0 |    0 |    0 |
|   33 | VBP payable                              |    0 |    0 |    0 |
|   34 | Other services payable                   |    0 |    0 |    0 |
|   35 | Due to affiliates (current)              |    0 |    0 |    0 |
|   36 | Current portion long-term debt           |    0 |    0 |    0 |
|   37 | MLR payable to State                     |    0 |    0 |    0 |
|   38 | Other current liabilities                |    0 |    0 |    0 |
|   39 | Total Current Liabilities                |    0 |    0 |    0 |
|   40 | Non-current portion long-term debt       |    0 |    0 |    0 |
|   41 | MLR payable (non-current)                |    0 |    0 |    0 |
|   42 | Due to affiliates (non-current)          |    0 |    0 |    0 |
|   43 | Other non-current liabilities            |    0 |    0 |    0 |
|   44 | Total Other Liabilities                  |    0 |    0 |    0 |
|   45 | TOTAL LIABILITIES                        |    0 |    0 |    0 |
|   46 | Preferred stock/Restricted Funds         |    0 |    0 |    0 |
|   47 | Common stock/Unrestricted Funds          |    0 |    0 |    0 |
|   48 | Treasury stock                           |    0 |    0 |    0 |
|   49 | Unrealized gain on long term investments |    0 |    0 |    0 |
|   50 | Additional paid-in capital               |    0 |    0 |    0 |
|   51 | Contributed capital                      |    0 |    0 |    0 |
|   52 | Retained earnings - beginning            |    0 |    0 |    0 |
|   53 | Increase (decrease) YTD                  |    0 |    0 |    0 |
|   54 | Total Equity/Net Assets                  |    0 |    0 |    0 |
|   55 | TOTAL LIABILITIES & FUND BALANCES        |    0 |    0 |    0 |



---

## Arithmetic-Relationship__case_288

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|   A |       B |       C |            D |           E |          F |         G |           H |
|----:|--------:|--------:|-------------:|------------:|-----------:|----------:|------------:|
|   1 | 6.0845  | 6.0881  | -0.00360106  | -0.0103392  | 0.0103392  | 0.0421591 | 2.35257e-06 |
|   2 | 4.58497 | 4.21284 |  0.372123    |  1.06281    | 1.06281    | 0.0320072 | 0.0186747   |
|   3 | 4.2485  | 4.21284 |  0.0356507   |  0.101821   | 0.101821   | 0.0320072 | 0.000171403 |
|   4 | 3.95124 | 4.21284 | -0.261601    | -0.747148   | 0.747148   | 0.0320072 | 0.0092291   |
|   5 | 4.15888 | 4.21284 | -0.0539615   | -0.154117   | 0.154117   | 0.0320072 | 0.000392689 |
|   6 | 4.27667 | 4.21284 |  0.0638216   |  0.182278   | 0.182278   | 0.0320072 | 0.000549308 |
|   7 | 3.85015 | 4.21284 | -0.362697    | -1.03588    | 1.03588    | 0.0320072 | 0.0177406   |
|   8 | 4.44265 | 4.18414 |  0.258508    |  0.738669   | 0.738669   | 0.0329386 | 0.00929225  |
|   9 | 4.07754 | 4.17699 | -0.0994503   | -0.284208   | 0.284208   | 0.0331759 | 0.00138585  |
|  10 | 4.14313 | 4.17699 | -0.033853    | -0.0967446  | 0.0967446  | 0.0331759 | 0.000160583 |
|  11 | 4.04305 | 4.17699 | -0.133936    | -0.382762   | 0.382762   | 0.0331759 | 0.00251364  |
|  12 | 3.98898 | 4.17699 | -0.188004    | -0.537274   | 0.537274   | 0.0331759 | 0.00495266  |
|  13 | 6.00141 | 6.19838 | -0.196963    | -0.56698    | 0.56698    | 0.0471106 | 0.00794661  |
|  14 | 5.94017 | 6.00774 | -0.0675697   | -0.19367    | 0.19367    | 0.0388555 | 0.000758153 |
|  15 | 4.17439 | 4.17341 |  0.000974722 |  0.00278572 | 0.00278572 | 0.0332953 | 1.33639e-07 |
|  16 | 3.68888 | 4.16984 | -0.48096     | -1.37465    | 1.37465    | 0.0334151 | 0.0326631   |
|  17 | 6.12249 | 6.19838 | -0.0758854   | -0.218444   | 0.218444   | 0.0471106 | 0.00117958  |
|  18 | 5.17048 | 6.06911 | -0.898622    | -2.579      | 2.579      | 0.041355  | 0.143464    |
|  19 | 4.11087 | 4.17341 | -0.0625387   | -0.178733   | 0.178733   | 0.0332953 | 0.000550135 |
|  20 | 4.51086 | 4.18772 |  0.323135    |  0.923281   | 0.923281   | 0.0328206 | 0.0144636   |
|  21 | 4.07754 | 4.17341 | -0.0958751   | -0.274008   | 0.274008   | 0.0332953 | 0.00129296  |
|  22 | 4.41884 | 4.17341 |  0.245428    |  0.701424   | 0.701424   | 0.0332953 | 0.00847268  |
|  23 | 3.71357 | 4.18056 | -0.466993    | -1.33448    | 1.33448    | 0.0330571 | 0.0304411   |
|  24 | 3.85015 | 4.17699 | -0.32684     | -0.934039   | 0.934039   | 0.0331759 | 0.0149684   |
|  25 | 4.43082 | 4.17699 |  0.253829    |  0.72539    | 0.72539    | 0.0331759 | 0.00902794  |
|  26 | 4.44265 | 4.17699 |  0.265664    |  0.75921    | 0.75921    | 0.0331759 | 0.00988939  |
|  27 | 4.75359 | 4.17699 |  0.576602    |  1.64781    | 1.64781    | 0.0331759 | 0.0465863   |
|  28 | 6.29895 | 6.23716 |  0.0617845   |  0.178027   | 0.178027   | 0.0489671 | 0.000815924 |
|  29 | 6.79122 | 6.38465 |  0.406575    |  1.17623    | 1.17623    | 0.0565727 | 0.041481    |
|  30 | 5.9162  | 5.72257 |  0.193637    |  0.552239   | 0.552239   | 0.0292052 | 0.0045873   |
|  31 | 6.32257 | 6.16462 |  0.157942    |  0.45428    | 0.45428    | 0.0455436 | 0.00492367  |
|  32 | 6.65286 | 6.29577 |  0.357094    |  1.03052    | 1.03052    | 0.0518857 | 0.0290583   |
|  33 | 5.46383 | 5.93298 | -0.469146    | -1.34269    | 1.34269    | 0.0360127 | 0.033675    |
|  34 | 3.7612  | 4.17699 | -0.415788    | -1.18823    | 1.18823    | 0.0331759 | 0.0242242   |
|  35 | 4.14313 | 4.36925 | -0.226117    | -0.644309   | 0.644309   | 0.0275074 | 0.00587113  |
|  36 | 6.1506  | 6.10715 |  0.0434534   |  0.124815   | 0.124815   | 0.0429798 | 0.000349822 |
|  37 | 5.81413 | 5.93298 | -0.118848    | -0.340141   | 0.340141   | 0.0360127 | 0.00216109  |
|  38 | 4.31749 | 3.92089 |  0.396603    |  1.13922    | 1.13922    | 0.0430103 | 0.029164    |
|  39 | 6.1334  | 5.60649 |  0.526904    |  1.50038    | 1.50038    | 0.0262036 | 0.0302876   |
|  40 | 6.70564 | 6.23716 |  0.468474    |  1.34987    | 1.34987    | 0.0489671 | 0.0469097   |
|  41 | 5.29832 | 5.98897 | -0.690655    | -1.97881    | 1.97881    | 0.0381209 | 0.0775929   |
|  42 | 3.46574 | 3.914   | -0.448269    | -1.28782    | 1.28782    | 0.0433105 | 0.0375409   |
|  43 | 6.13123 | 6.20805 | -0.0768273   | -0.221209   | 0.221209   | 0.0475681 | 0.00122196  |
|  44 | 6.62141 | 6.02656 |  0.594843    |  1.70562    | 1.70562    | 0.0396062 | 0.0599856   |
|  45 | 4.2485  | 3.97966 |  0.268838    |  0.771216   | 0.771216   | 0.0405228 | 0.0125599   |
|  46 | 4.38203 | 3.98661 |  0.395421    |  1.13418    | 1.13418    | 0.0402377 | 0.0269651   |
|  47 | 6.25958 | 6.25177 |  0.00781369  |  0.0225229  | 0.0225229  | 0.0496816 | 1.32601e-05 |
|  48 | 6.608   | 6.40456 |  0.203443    |  0.588903   | 0.588903   | 0.0576658 | 0.0106114   |
|  49 | 4.86753 | 5.61535 | -0.747817    | -2.12967    | 2.12967    | 0.0264137 | 0.0615246   |
|  50 | 4.23411 | 3.93812 |  0.295989    |  0.849878   | 0.849878   | 0.0422667 | 0.0159381   |
|  51 | 6.20051 | 6.49995 | -0.299444    | -0.869317   | 0.869317   | 0.0631217 | 0.0254578   |
|  52 | 6.70196 | 6.17425 |  0.52771     |  1.51818    | 1.51818    | 0.0459859 | 0.0555499   |



---

## Arithmetic-Relationship__case_236

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|   A |     B | C                                                         |         D |   E |         F |            G |           H | I   |          J |          K |          L |
|----:|------:|:----------------------------------------------------------|----------:|----:|----------:|-------------:|------------:|:----|-----------:|-----------:|-----------:|
|   1 |   200 | Pathuri Venkata Subrahmanyam                              | 0.0863638 |   0 | 0.0863638 |     1.32729  |   -5.43588  | No  |   18.4581  |   19.6966  |  14.8396   |
|   2 |   367 | Sahara India Financial Corporation Limited                | 2.1405    |   0 | 2.1405    |   105.13     |  -58.1611   | No  |  292.202   |  306.732   |   2.91765  |
|   3 |   678 | The Karur Vysya Bank Limited                              | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|   4 |   893 | IDBI Capital Market Services Limited                      | 0.540841  |   0 | 0.540841  |    15.3462   |  -49.0551   | No  |  148.564   |  147.412   |   9.60577  |
|   5 |  2101 | Corporation Bank                                          | 0.969495  |   0 | 0.969495  |     1.115    | -413.704    | No  |  238.526   |    6.40749 |   5.74663  |
|   6 |  2122 | Andhra Bank                                               | 5.10423   |   0 | 5.10423   |   168.4      | -147.902    | No  | 1138.19    | 1223.91    |   7.26785  |
|   7 |  2649 | IFCI Financial Service Ltd                                | 0.0159202 |   0 | 0.0159202 |     3.57517  |  -46.449    | No  |   43.1979  |    5.02037 |   1.40423  |
|   8 |  3071 | KFIC Securities Ltd                                       | 1.60303   |   0 | 1.60303   |    51.4003   |   21.7654   | No  |  179.539   |  211.252   |   4.10993  |
|   9 |  3845 | The South Indian Bank Ltd                                 | 2.06702   |   0 | 2.06702   |   109.444    |   20.0293   | No  |  274.009   |  337.025   |   3.07943  |
|  10 |  4844 | Keynote Capitals Limited                                  | 0.112692  |   0 | 0.112692  |   348.45     |   11.6436   | No  |   88.5064  |  111.235   |   0.319227 |
|  11 |  5888 | Techno Shares & Stocks Ltd                                | 2.04058   |   0 | 2.04058   |    51.0297   | -358.79     | No  |  494.765   |  235.092   |   4.60696  |
|  12 |  5957 | Aditya Birla Money Ltd                                    | 0         |   0 | 0         |     6.18682  |   -3.96126  | No  |   25.6975  |   29.2263  |   4.72397  |
|  13 |  8488 | State Bank of Mysore                                      | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  14 | 11770 | Money Control Dot Com India Ltd                           | 0.209516  |   0 | 0.209516  |     8.93256  |    1.90653  | No  |   21.9111  |   26.1452  |   2.92696  |
|  15 | 12417 | Ashika Stock Broking Ltd.                                 | 0.233129  |   0 | 0.233129  |   424.071    |   32.0907   | No  |  283.131   |  277.51    |   0.654396 |
|  16 | 17795 | Indiabulls Securities Ltd                                 | 0.106376  |   0 | 0.106376  |     0.06353  |   -0.109238 | No  |   24.2256  |   27.6422  | 435.105    |
|  17 | 19897 | Allahabad Bank                                            | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  18 | 20558 | Narnolia Securities Ltd                                   | 0.872726  |   0 | 0.872726  |    38.8155   |  -39.5376   | No  |  128.432   |  124.502   |   3.20753  |
|  19 | 20626 | The Lakshmi Vilas Bank Ltd                                | 0.0828448 |   0 | 0.0828448 |     3.5926   |   -1.91483  | No  |   11.5723  |   12.4774  |   3.47307  |
|  21 | 21539 | Sundaram Finance Distribution Limited                     | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  22 | 25813 | BMA Commodities Private Limited                           | 0.139975  |   0 | 0.139975  |    76.6954   |   -3.97293  | No  |   77.266   |   57.3414  |   0.74765  |
|  23 | 28003 | Indian Overseas Bank                                      | 1.76114   |   0 | 1.76114   |    44.7282   |  -53.7262   | No  |  423.927   |  455.209   |  10.1772   |
|  24 | 31184 | Dena Bank                                                 | 0.227382  |   0 | 0.227382  |    34.9458   |  -18.9134   | No  |   50.0481  |   49.8105  |   1.42537  |
|  25 | 31751 | LKP Securities Limited                                    | 1.65921   |   0 | 1.65921   |   110.652    | -121.321    | No  |  683.922   |  706.788   |   6.38745  |
|  26 | 33794 | Oriental Bank Of Commerce                                 | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  27 | 35323 | The Dhanalakshmi Bank Limited                             | 0         |   0 | 0         |     0.626661 |    0.626661 | No  |    2.45428 |    3.12214 |   4.98219  |
|  28 | 36031 | Syndicate Bank                                            | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  30 | 39091 | Central Bank Of India                                     | 3.60562   |   0 | 3.60562   |   666.558    | -599.1      | No  |  730.607   |  359.988   |   0.54007  |
|  31 | 39103 | HDFC Sales Private Limited                                | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  32 | 40733 | Karan Agarwal                                             | 0.522344  |   0 | 0.522344  |    50.322    |  -42.3802   | No  |   56.3499  |   34.7051  |   0.689662 |
|  33 | 41778 | Canara Bank Securities Limited                            | 2.00342   |   0 | 2.00342   | 40000        | -598.494    | No  | 4052.21    |    0       |   0        |
|  34 | 44459 | Bank of Maharashtra                                       | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  35 | 45888 | Shriram Fortune Solutions Ltd.                            | 0.94856   |   0 | 0.94856   |    41.6531   |  -18.8401   | No  |  139.929   |  151.672   |   3.64131  |
|  36 | 50327 | Bajaj Allianz Financial Distributors Limited              | 0.173249  |   0 | 0.173249  |    29.5767   |   -7.86575  | No  |   37.0341  |   37.111   |   1.25474  |
|  37 | 50915 | The Peerless General Finance & Investment Co Ltd          | 2.42654   |   0 | 2.42654   |    32.7333   | -145.068    | No  |  404.506   |  399.212   |  12.1959   |
|  38 | 51289 | Affluenz Financial Services India Private Limited         | 1.88404   |   0 | 1.88404   |   114.587    |  106.069    | No  |   23.1209  |  125.21    |   1.09271  |
|  39 | 53315 | Inditrade Capital Limited                                 | 0.0108943 |   0 | 0.0108943 |     3.95437  |   -3.6797   | No  |   14.4796  |   15.4021  |   3.89496  |
|  40 | 53552 | The Cosmos Co-Operative Bank Ltd                          | 0.03021   |   0 | 0.03021   |     0.482977 |   -1.39982  | No  |    6.44635 |    6.56576 |  13.5943   |
|  41 | 54846 | The Shamrao Vithal Co Operative Bank Ltd                  | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  42 | 55612 | Reliance Financial Distribution and Advisory Services Ltd | 0.160598  |   0 | 0.160598  |     0.978988 |   -4.04553  | No  |   33.3458  |   36.8355  |  37.6261   |
|  45 | 62713 | Fullerton Securities And Wealth Advisors Ltd              | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  46 | 66907 | Networth Wealth Solutions Ltd                             | 1.06648   |   0 | 1.06648   |   125.04     |  -43.9717   | No  |  203.992   |  216.646   |   1.73261  |
|  47 | 71722 | Abira Management Services Ltd                             | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  48 | 78747 | Konark Star Financial Consultants Pvt Ltd                 | 0.0921798 |   0 | 0.0921798 |     1.60197  |   -4.27068  | No  |   11.7515  |   11.4189  |   7.12804  |
|  49 | 79713 | Sahaj Rural Development Foundation                        | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  51 | 85308 | SIP SWP SERVICES                                          | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |
|  52 | 96547 | Datacomp Web Technologies (India)Pvt Ltd                  | 0         |   0 | 0         |     0        |    0        | No  |    0       |    0       |   0        |



---

## Arithmetic-Relationship__case_219

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
| A                        |       B |      C |   D |   E |   F |   G |
|:-------------------------|--------:|-------:|----:|----:|----:|----:|
| Pearson                  | 1002905 | 953390 |   1 |   1 |   0 |   0 |
| City & Guilds            |  878465 | 848905 |   2 |   2 |   0 |   0 |
| NCFE                     |  402400 | 419050 |   3 |   3 |   0 |   0 |
| Highfield Qualifications |  302315 | 297845 |   4 |   4 |   0 |   0 |
| TCL                      |  224415 | 236060 |   5 |   5 |   0 |   0 |
| OCR                      |  215990 | 219205 |   6 |   6 |   0 |   0 |
| ABRSM                    |  213120 | 217955 |   7 |   7 |   0 |   0 |
| QA                       |  201965 | 216185 |   8 |   8 |   0 |   0 |
| NOCN                     |  134890 | 136745 |   9 |   9 |   0 |   0 |
| FAA                      |  105205 | 120045 |  10 |  10 |   0 |   0 |
| Ascentis                 |   96950 | 112280 |  12 |  11 |   1 |   1 |
| TQUK                     |   82415 | 110315 |  14 |  12 |   2 |   2 |
| Cambridge English        |   87215 |  96890 |  13 |  13 |   0 |   0 |
| AQA                      |   78185 |  77625 |  15 |  14 |   1 |   1 |
| EAL                      |   64105 |  69440 |  17 |  15 |   2 |   2 |
| ISTD                     |   56755 |  63730 |  19 |  16 |   3 |   3 |
| IQL                      |   40735 |  60670 |  29 |  17 |  12 |  12 |
| VTCT                     |   55205 |  56830 |  21 |  18 |   3 |   3 |
| Gateway Qualifications   |   45640 |  53585 |  23 |  19 |   4 |   4 |
| BIIAB                    |   63250 |  52865 |  18 |  20 |  -2 |  -2 |
| QNUK                     |   19385 |  47010 |  49 |  21 |  28 |  28 |
| BSC                      |   64465 |  46970 |  16 |  22 |  -6 |  -6 |
| UAL                      |   38280 |  46025 |  32 |  23 |   9 |   9 |
| 1st4sport                |   55055 |  45615 |  22 |  24 |  -2 |  -2 |
| LIBF                     |   34830 |  43620 |  35 |  25 |  10 |  10 |
| ESB                      |   44010 |  40730 |  24 |  26 |  -2 |  -2 |
| IMI                      |   42800 |  39520 |  25 |  27 |  -2 |  -2 |
| RAD                      |   26030 |  39295 |  43 |  28 |  15 |  15 |
| IBO                      |   37040 |  37615 |  33 |  29 |   4 |   4 |
| Active IQ                |   41910 |  36600 |  28 |  30 |  -2 |  -2 |
| RSL                      |   36805 |  36460 |  34 |  31 |   3 |   3 |
| AAT                      |   38355 |  35935 |  31 |  32 |  -1 |  -1 |
| LAMDA                    |   56300 |  35790 |  20 |  33 | -13 | -13 |
| Skillsfirst              |   42790 |  34725 |  26 |  34 |  -8 |  -8 |
| IDTA                     |   31925 |  33555 |  39 |  35 |   4 |   4 |
| WJEC                     |   21000 |  33280 |  46 |  36 |  10 |  10 |
| RSPH                     |   32610 |  32255 |  38 |  37 |   1 |   1 |
| SLQ                      |   31635 |  31995 |  40 |  38 |   2 |   2 |
| LASER                    |   26185 |  30980 |  42 |  39 |   3 |   3 |
| AIM                      |   22465 |  28170 |  45 |  40 |   5 |   5 |
| GQA                      |   19895 |  26860 |  48 |  41 |   7 |   7 |
| ProQual                  |   20690 |  23655 |  47 |  42 |   5 |   5 |
| TLM                      |  103105 |  23560 |  11 |  43 | -32 | -32 |
| BCS                      |   26685 |  22385 |  41 |  44 |  -3 |  -3 |
| CMI                      |   17550 |  22280 |  52 |  45 |   7 |   7 |
| UWLQ                     |   23180 |  22185 |  44 |  46 |  -2 |  -2 |
| iCQ                      |   33450 |  21670 |  37 |  47 | -10 | -10 |
| SEG Awards               |   17570 |  21315 |  51 |  48 |   3 |   3 |
| IAO                      |   33745 |  19830 |  36 |  49 | -13 | -13 |
| Cambridge International  |   38590 |  18135 |  30 |  50 | -20 | -20 |



---

## Arithmetic-Relationship__case_134

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|    A |                B |        C |           D |                 E |                F |
|-----:|-----------------:|---------:|------------:|------------------:|-----------------:|
| 1945 |      0           |  600     |  0.358211   |     107.463       |    707.463       |
| 1946 |    707.463       |  618     | -0.0842915  |     -85.6792      |   1239.78        |
| 1947 |   1239.78        |  636.54  |  0.052      |      81.0188      |   1957.34        |
| 1948 |   1957.34        |  655.636 |  0.0570458  |     130.359       |   2743.34        |
| 1949 |   2743.34        |  675.305 |  0.183032   |     563.921       |   3982.56        |
| 1950 |   3982.56        |  695.564 |  0.308055   |    1333.99        |   6012.11        |
| 1951 |   6012.11        |  716.431 |  0.236785   |    1508.4         |   8236.94        |
| 1952 |   8236.94        |  737.924 |  0.18151    |    1562.06        |  10536.9         |
| 1953 |  10536.9         |  760.062 | -0.012082   |    -131.899       |  11165.1         |
| 1954 |  11165.1         |  782.864 |  0.525633   |    6074.49        |  18022.4         |
| 1955 |  18022.4         |  806.35  |  0.325973   |    6006.26        |  24835           |
| 1956 |  24835           |  830.54  |  0.0743951  |    1878.5         |  27544.1         |
| 1957 |  27544.1         |  855.457 | -0.104574   |   -2925.11        |  25474.4         |
| 1958 |  25474.4         |  881.12  |  0.4372     |   11330           |  37685.6         |
| 1959 |  37685.6         |  907.554 |  0.120565   |    4598.25        |  43191.4         |
| 1960 |  43191.4         |  934.78  |  0.00336535 |     146.927       |  44273.1         |
| 1961 |  44273.1         |  962.824 |  0.266377   |   11921.6         |  57157.5         |
| 1962 |  57157.5         |  991.709 | -0.0881146  |   -5080.1         |  53069.1         |
| 1963 |  53069.1         | 1021.46  |  0.226119   |   12115.4         |  66206           |
| 1964 |  66206           | 1052.1   |  0.164155   |   10954.4         |  78212.5         |
| 1965 |  78212.5         | 1083.67  |  0.123992   |    9764.94        |  89061.1         |
| 1966 |  89061.1         | 1116.18  | -0.0997095  |   -8935.88        |  81241.4         |
| 1967 |  81241.4         | 1149.66  |  0.23803    |   19474.7         | 101866           |
| 1968 | 101866           | 1184.15  |  0.108149   |   11080.7         | 114131           |
| 1969 | 114131           | 1219.68  | -0.0824137  |   -9456.18        | 105894           |
| 1970 | 105894           | 1256.27  |  0.0356114  |    3793.41        | 110944           |
| 1971 | 110944           | 1293.95  |  0.142212   |   15869.5         | 128107           |
| 1972 | 128107           | 1332.77  |  0.187554   |   24151.9         | 153592           |
| 1973 | 153592           | 1372.76  | -0.14308    |  -22074.2         | 132890           |
| 1974 | 132890           | 1413.94  | -0.259018   |  -34604.1         |  99700.2         |
| 1975 |  99700.2         | 1456.36  |  0.369951   |   37153.6         | 138310           |
| 1976 | 138310           | 1500.05  |  0.23831    |   33139.4         | 172950           |
| 1977 | 172950           | 1545.05  | -0.069797   |  -12125.3         | 162369           |
| 1978 | 162369           | 1591.4   |  0.0650928  |   10620.9         | 174582           |
| 1979 | 174582           |  819.572 |  0.185195   |   32407.5         | 207809           |
| 1980 | 207809           |  844.159 |  0.317352   |   66082.6         | 274736           |
| 1981 | 274736           |  869.483 | -0.0470239  |  -12939.6         | 262666           |
| 1982 | 262666           |  895.568 |  0.204191   |   53725.2         | 317286           |
| 1983 | 317286           |  922.435 |  0.223372   |   70975.8         | 389185           |
| 1984 | 389185           |  950.108 |  0.0614614  |   23949           | 414084           |
| 1985 | 414084           |  978.611 |  0.312351   |  129492           | 544555           |
| 1986 | 544555           | 1007.97  |  0.184946   |  100806           | 646369           |
| 1987 | 646369           | 1038.21  |  0.0581272  |   37601.8         | 685009           |
| 1988 | 685009           | 1069.36  |  0.165372   |  113370           | 799448           |
| 1989 | 799448           | 1101.44  |  0.314752   |  251801           |      1.05235e+06 |
| 1990 |      1.05235e+06 | 1134.48  | -0.0306445  |  -32266.2         |      1.02122e+06 |
| 1991 |      1.02122e+06 | 1168.51  |  0.302348   |  308941           |      1.33133e+06 |
| 1992 |      1.33133e+06 | 1203.57  |  0.0749373  |   99811.2         |      1.43234e+06 |
| 1993 |      1.43234e+06 | 1239.68  |  0.0996705  |  142824           |      1.57641e+06 |
| 1994 |      1.57641e+06 | 1276.87  |  0.0132592  |   20910.4         |      1.59859e+06 |
| 1995 |      1.59859e+06 | 1315.17  |  0.371952   |  594845           |      2.19475e+06 |
| 1996 |      2.19475e+06 | 1354.63  |  0.22681    |  497945           |      2.69405e+06 |
| 1997 |      2.69405e+06 |    0     |  0.331037   |  891830           |      3.58588e+06 |
| 1998 |      3.58588e+06 |    0     |  0.28338    |       1.01617e+06 |      4.60205e+06 |
| 1999 |      4.60205e+06 |    0     |  0.208854   |  961154           |      5.5632e+06  |
| 2000 |      5.5632e+06  |    0     | -0.0903182  | -502458           |      5.06075e+06 |
| 2001 |      5.06075e+06 |    0     | -0.118498   | -599686           |      4.46106e+06 |
| 2002 |      4.46106e+06 |    0     | -0.21966    | -979918           |      3.48114e+06 |
| 2003 |      3.48114e+06 |    0     |  0.283558   |  987105           |      4.46825e+06 |
| 2004 |      4.46825e+06 |    0     |  0.107428   |  480014           |      4.94826e+06 |
| 2005 |      4.94826e+06 |    0     |  0.0483448  |  239223           |      5.18748e+06 |
| 2006 |      5.18748e+06 |    0     |  0.156126   |  809899           |      5.99738e+06 |
| 2007 |      5.99738e+06 |    0     |  0.0548474  |  328940           |      6.32632e+06 |
| 2008 |      6.32632e+06 |    0     | -0.365523   |      -2.31242e+06 |      4.0139e+06  |
| 2009 |      4.0139e+06  |    0     |  0.259352   |       1.04102e+06 |      5.05492e+06 |
| 2010 |      5.05492e+06 |    0     |  0.148211   |  749194           |      5.80411e+06 |
| 2011 |      5.80411e+06 |    0     |  0.0209837  |  121792           |      5.9259e+06  |
| 2012 |      5.9259e+06  |    0     |  0.158906   |  941661           |      6.86756e+06 |
| 2013 |      6.86756e+06 |    0     |  0.321451   |       2.20758e+06 |      9.07515e+06 |
| 2014 |      9.07515e+06 |    0     |  0.134774   |       1.22309e+06 |      1.02982e+07 |



---

## Arithmetic-Relationship__case_805

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|     A |     B |   C |     D |     E |   F |     G |     H |   I |     J |
|------:|------:|----:|------:|------:|----:|------:|------:|----:|------:|
| 41279 | 17724 |   0 | 17724 |  9283 |   0 |  9283 | 27007 |   0 | 27007 |
| 41286 | 21299 |   0 | 21299 | 11506 |   0 | 11506 | 32805 |   0 | 32805 |
| 41293 | 20502 |   0 | 20502 | 11659 |   0 | 11659 | 32161 |   0 | 32161 |
| 41300 | 19852 |   0 | 19852 | 12183 |   0 | 12183 | 32035 |   0 | 32035 |
| 41307 | 20267 |   0 | 20267 | 10625 |   0 | 10625 | 30892 |   0 | 30892 |
| 41314 | 19216 |   0 | 19216 | 11786 |   0 | 11786 | 31002 |   0 | 31002 |
| 41321 | 19999 |   0 | 19999 | 12649 |   0 | 12649 | 32648 |   0 | 32648 |
| 41328 | 19346 |   0 | 19346 | 12137 |   0 | 12137 | 31483 |   0 | 31483 |
| 41335 | 19736 |   0 | 19736 | 11709 |   0 | 11709 | 31445 |   0 | 31445 |
| 41342 | 19926 |   0 | 19926 | 11373 |   0 | 11373 | 31299 |   0 | 31299 |
| 41349 | 21240 |   0 | 21240 | 11853 |   0 | 11853 | 33093 |   0 | 33093 |
| 41356 | 16383 |   0 | 16383 |  9828 |   0 |  9828 | 26211 |   0 | 26211 |
| 41363 | 18948 |   0 | 18948 |  9951 |   0 |  9951 | 28899 |   0 | 28899 |
| 41370 | 15440 |   0 | 15440 |  9584 |   0 |  9584 | 25024 |   0 | 25024 |
| 41377 | 20955 |   0 | 20955 | 11233 |   0 | 11233 | 32188 |   0 | 32188 |
| 41384 | 20049 |   0 | 20049 | 11402 |   0 | 11402 | 31451 |   0 | 31451 |
| 41391 | 19278 |   0 | 19278 | 11210 |   0 | 11210 | 30488 |   0 | 30488 |
| 41398 | 20811 |   0 | 20811 | 11608 |   0 | 11608 | 32419 |   0 | 32419 |
| 41405 | 15646 |   0 | 15646 | 10486 |   0 | 10486 | 26132 |   0 | 26132 |
| 41412 | 19938 |   0 | 19938 | 10804 |   0 | 10804 | 30742 |   0 | 30742 |
| 41419 | 18875 |   0 | 18875 |  9473 |   0 |  9473 | 28348 |   0 | 28348 |
| 41426 | 17074 |   0 | 17074 | 10136 |   0 | 10136 | 27210 |   0 | 27210 |
| 41433 | 18133 |   0 | 18133 | 11945 |   0 | 11945 | 30078 |   0 | 30078 |
| 41440 | 18831 |   0 | 18831 | 11007 |   0 | 11007 | 29838 |   0 | 29838 |
| 41447 | 19535 |   0 | 19535 |  9935 |   0 |  9935 | 29470 |   0 | 29470 |
| 41454 | 18710 |   0 | 18710 | 10677 |   0 | 10677 | 29387 |   0 | 29387 |
| 41461 | 20057 |   0 | 20057 | 11121 |   0 | 11121 | 31178 |   0 | 31178 |
| 41468 | 17252 |   0 | 17252 |  9822 |   0 |  9822 | 27074 |   0 | 27074 |
| 41475 | 17832 |   0 | 17832 | 12774 |   0 | 12774 | 30606 |   0 | 30606 |
| 41482 | 19726 |   0 | 19726 | 10935 |   0 | 10935 | 30661 |   0 | 30661 |
| 41489 | 19148 |   0 | 19148 | 11746 |   0 | 11746 | 30894 |   0 | 30894 |
| 41496 | 19430 |   0 | 19430 | 11225 |   0 | 11225 | 30655 |   0 | 30655 |
| 41503 | 19148 |   0 | 19148 | 14008 |   0 | 14008 | 33156 |   0 | 33156 |
| 41510 | 20023 |   0 | 20023 | 12815 |   0 | 12815 | 32838 |   0 | 32838 |
| 41517 | 19421 |   0 | 19421 | 12283 |   0 | 12283 | 31704 |   0 | 31704 |
| 41524 | 19588 |   0 | 19588 | 11323 |   0 | 11323 | 30911 |   0 | 30911 |
| 41531 | 19810 |   0 | 19810 | 11915 |   0 | 11915 | 31725 |   0 | 31725 |
| 41538 | 20241 |   0 | 20241 | 10457 |   0 | 10457 | 30698 |   0 | 30698 |
| 41545 | 20396 |   0 | 20396 | 11670 |   0 | 11670 | 32066 |   0 | 32066 |
| 41552 | 20477 |   0 | 20477 | 11211 |   0 | 11211 | 31688 |   0 | 31688 |
| 41559 | 20618 |   0 | 20618 | 11779 |   0 | 11779 | 32397 |   0 | 32397 |
| 41566 | 20025 |   0 | 20025 | 11415 |   0 | 11415 | 31440 |   0 | 31440 |
| 41573 | 19844 |   0 | 19844 | 11170 |   0 | 11170 | 31014 |   0 | 31014 |
| 41580 | 19691 |   0 | 19691 | 10700 |   0 | 10700 | 30391 |   0 | 30391 |
| 41587 | 21507 |   0 | 21507 | 10674 |   0 | 10674 | 32181 |   0 | 32181 |
| 41594 | 21310 |   0 | 21310 |  9086 |   0 |  9086 | 30396 |   0 | 30396 |
| 41601 | 21949 |   0 | 21949 |  9915 |   0 |  9915 | 31864 |   0 | 31864 |
| 41608 | 22526 |   0 | 22526 |  9344 |   0 |  9344 | 31870 |   0 | 31870 |
| 41615 | 22446 |   0 | 22446 | 11017 |   0 | 11017 | 33463 |   0 | 33463 |
| 41622 | 21840 |   0 | 21840 | 12235 |   0 | 12235 | 34075 |   0 | 34075 |
| 41629 | 20973 |   0 | 20973 |  9532 |   0 |  9532 | 30505 |   0 | 30505 |
| 41636 |  9162 |   0 |  9162 |  5039 |   0 |  5039 | 14201 |   0 | 14201 |



---

## Arithmetic-Relationship__case_102

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
| J   | K   | L   |    M |    N |    O | P        | Q          |
|:----|:----|:----|-----:|-----:|-----:|:---------|:-----------|
| E   | M   | U   | 1907 | 1907 |    0 | 1/1/1907 | 12/31/1907 |
| E   | M   | U   | 1907 | 1912 |    5 | 1/1/1907 | 12/31/1912 |
| E   | M   | U   | 1907 | 1916 |    9 | 1/1/1907 | 12/31/1916 |
| E   | M   | U   | 1908 | 1915 |    7 | 1/1/1908 | 12/31/1915 |
| E   | M   | U   | 1913 | 1918 |    5 | 1/1/1913 | 12/31/1918 |
| E   | M   | U   | 1915 | 1920 |    5 | 1/1/1915 | 12/31/1920 |
| E   | M   | U   | 1917 | 1932 |   15 | 1/1/1917 | 12/31/1932 |
| E   | M   | U   | 1919 | 1924 |    5 | 1/1/1919 | 12/31/1924 |
| E   | M   | U   | 1921 | 1926 |    5 | 1/1/1921 | 12/31/1926 |
| E   | M   | U   | 1925 | 1936 |   11 | 1/1/1925 | 12/31/1936 |
| E   | M   | U   | 1927 | 1932 |    5 | 1/1/1927 | 12/31/1932 |
| E   | M   | U   | 1933 | 1934 |    1 | 1/1/1933 | 12/31/1934 |
| E   | M   | U   | 1933 | 1938 |    5 | 1/1/1933 | 12/31/1938 |
| E   | M   | U   | 1935 | 1936 |    1 | 1/1/1935 | 12/31/1936 |
| E   | M   | U   | 1937 | 1938 |    1 | 1/1/1937 | 12/31/1938 |
| E   | M   | U   | 1937 | 1942 |    5 | 1/1/1937 | 12/31/1942 |
| E   | M   | U   | 1939 | 1944 |    5 | 1/1/1939 | 12/31/1944 |
| E   | M   | U   | 1939 | 1952 |   13 | 1/1/1939 | 12/31/1952 |
| E   | M   | U   | 1943 | 1948 |    5 | 1/1/1943 | 12/31/1948 |
| E   | M   | U   | 1945 | 1950 |    5 | 1/1/1945 | 12/31/1950 |
| E   | M   | U   | 1949 | 1960 |   11 | 1/1/1949 | 12/31/1960 |
| E   | M   | U   | 1951 | 1956 |    5 | 1/1/1951 | 12/31/1956 |
| E   | M   | U   | 1953 | 1954 |    1 | 1/1/1953 | 12/31/1954 |
| E   | M   | U   | 1954 | 1954 |    0 | 1/1/1954 | 12/31/1954 |
| E   | M   | U   | 1955 | 1970 |   15 | 1/1/1955 | 12/31/1970 |
| E   | M   | U   | 1957 | 1958 |    1 | 1/1/1957 | 12/31/1958 |
| E   | M   | U   | 1960 | 1966 |    6 | 1/1/1960 | 12/31/1966 |
| E   | M   | D   | 1960 | 1974 |   14 | 1/1/1960 | 12/31/1974 |
| E   | M   | R   | 1966 | 1974 |    8 | 1/1/1966 | 12/31/1974 |
| E   | M   | U   | 1971 | 1972 |    1 | 1/1/1971 | 12/31/1972 |
| E   | M   | D   | 1972 | 1974 |    2 | 1/1/1972 | 12/31/1974 |
| E   | M   | U   | 1974 | 1974 |    0 | 1/1/1974 | 12/31/1974 |
| E   | M   | D   | 1975 | 1976 |    1 | 1/1/1975 | 12/31/1976 |
| E   | M   | D   | 1975 | 1977 |    2 | 1/1/1975 | 12/31/1977 |
| E   | M   | D   | 1975 | 1980 |    5 | 1/1/1975 | 12/31/1980 |
| E   | M   | D   | 1975 | 1981 |    6 | 1/1/1975 | 12/31/1981 |
| E   | M   | D   | 1975 | 1983 |    8 | 1/1/1975 | 12/31/1983 |
| E   | M   | D   | 1977 | 1984 |    7 | 1/1/1977 | 12/31/1984 |
| E   | M   | D   | 1979 | 1990 |   11 | 1/1/1979 | 12/31/1990 |
| E   | M   | D   | 1981 | 1992 |   11 | 1/5/1981 | 12/31/1992 |
| E   | M   | R   | 1981 | 1992 |   11 | 1/5/1981 | 12/31/1992 |
| E   | M   | D   | 1983 | 1998 |   15 | 1/3/1983 | 12/31/1998 |
| E   | M   | D   | 1985 | 1988 |    3 | 1/1/1985 | 12/31/1988 |
| E   | M   | R   | 1989 | 1992 |    3 | 1/1/1989 | 12/31/1992 |
| E   | M   | U   | 1990 | 1991 |    1 | 7/2/1990 | 12/31/1991 |
| E   | M   | D   | 1991 | 2002 |   11 | 1/7/1991 | 12/31/2002 |
| E   | F   | D   | 1993 | 2000 |    7 | 1/1993   | 12/31/2000 |
| E   | M   | D   | 1993 | 2000 |    7 | 1/1993   | 12/31/2000 |
| E   | M   | D   | 1993 | 2004 |   11 | 1/4/1993 | 12/31/2004 |
| E   | M   | R   | 1999 | 2002 |    3 | 1/1999   | 12/31/2002 |
| E   | M   | R   | 2001 | 2004 |    3 | 1/2/2001 | 12/31/2004 |
| E   | M   | R   | 2001 | 2004 |    3 | 1/1/2001 | 12/31/2004 |
| E   | M   | D   | 2003 | 2007 |    4 | 1/6/2003 | 12/31/2007 |
| E   | M   | D   | 2003 | 2010 |    7 | 1/6/2003 | 12/31/2010 |
| E   | M   | D   | 2005 | 2009 |    4 | 1/2005   | 12/31/2009 |
| E   | M   | R   | 2005 | 2009 |    4 | 1/2005   | 12/31/2009 |
| E   | M   | R   | 2005 | 2012 |    7 | 1/1/2005 | 12/31/2012 |
| E   | M   | D   | 2007 | 2010 |    3 | 1/1/2007 | 12/31/2010 |
| E   | F   | D   | 2009 | 2012 |    3 | 1/1/2009 | 12/31/2012 |
| E   | M   | D   | 2009 | 2012 |    3 | 1/1/2009 | 12/31/2012 |
| E   | M   | R   | 2011 | 2019 |    8 | 1/1/2011 | 43466      |
| E   | M   | R   | 2011 | 2014 |    3 | 1/1/2011 | 42004      |
| E   | M   | R   | 2013 | 9999 | 7986 | 1/7/2013 | 9999       |
| E   | M   | R   | 2013 | 9999 | 7986 | 1/7/2013 | 9999       |
| E   | M   | R   | 2013 | 2017 |    4 | 1/7/2013 | 42736      |
| E   | M   | R   | 2015 | 9999 | 7984 | 42005    | 9999       |
| E   | M   | R   | 2017 | 9999 | 7982 | 42736    | 9999       |
| E   | M   | R   | 2018 | 9999 | 7981 | 43410    | 9999       |



---

## Arithmetic-Relationship__case_743

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|   A |     B |       C |        D |   E |   F |
|----:|------:|--------:|---------:|----:|----:|
|  10 |   0   |   2     | 2        |  74 | 115 |
|  10 |   2   |   4     | 2        | 325 | 327 |
|  10 |   4   |   6     | 2        | 325 | 298 |
|  10 |   6   |   8     | 2        | 203 | 214 |
|  10 |   8   |  10     | 2        | 243 | 211 |
|  10 |  10   |  12     | 2        | 406 | 402 |
|  10 |  12   |  14     | 2        | 299 | 223 |
|  10 |  14   |  16     | 2        | 292 | 302 |
|  10 |  16   |  18     | 2        | 107 |  71 |
|  10 |  18   |  20     | 2        | 155 | 117 |
|  10 |  20   |  22     | 2        |  98 | 193 |
|  10 |  22   |  24     | 2        | 310 | 244 |
|  10 |  24   |  26     | 2        | 200 | 212 |
|  10 |  26   |  28     | 2        | 242 | 227 |
|  10 |  28   |  30     | 2        |  93 |  75 |
|  10 |  30   |  32     | 2        | 121 | 130 |
|  10 |  32   |  34     | 2        |  28 |  45 |
|  10 |  34   |  36     | 2        | 164 | 122 |
|  10 |  36   |  38     | 2        | 143 |  50 |
|  10 |  38   |  40     | 2        |  91 |  50 |
|  10 |  40   |  42     | 2        |  24 |  12 |
|  10 |  42   |  44     | 2        |   4 |  14 |
|  10 |  44   |  46     | 2        |  11 |   4 |
|  10 |  46   |  48     | 2        |   3 |   3 |
|  10 |  48   |  50     | 2        |   2 |   5 |
|  10 |  50   |  51.2   | 1.2      |   2 |   1 |
|  10 |  51.2 |  52.8   | 1.6      |   3 |   2 |
|  10 |  52.8 |  54     | 1.2      |   2 |  10 |
|  10 |  54   |  56     | 2        |  72 | 114 |
|  10 |  56   |  58     | 2        | 176 | 228 |
|  10 |  58   |  60     | 2        | 211 | 188 |
|  10 |  60   |  62     | 2        | 118 | 134 |
|  10 |  62   |  64     | 2        | 190 | 212 |
|  10 |  64   |  66     | 2        | 162 | 172 |
|  10 |  66   |  68     | 2        |  75 |  60 |
|  10 |  68   |  70     | 2        |  90 | 100 |
|  10 |  70   |  72     | 2        | 184 | 145 |
|  10 |  72   |  74     | 2        | 330 | 132 |
|  10 |  74   |  76     | 2        | 188 | 154 |
|  10 |  76   |  78     | 2        | 110 |  86 |
|  10 |  78   |  80     | 2        |   3 |  21 |
|  10 |  80   |  82     | 2        | 184 | 165 |
|  10 |  82   |  84     | 2        | 201 | 197 |
|  10 |  84   |  86     | 2        | 239 | 283 |
|  10 |  86   |  88     | 2        | 148 | 143 |
|  10 |  88   |  90     | 2        | 112 | 126 |
|  10 |  90   |  92     | 2        | 193 | 145 |
|  10 |  92   |  94     | 2        | 264 | 135 |
|  10 |  94   |  96     | 2        |  71 |  65 |
|  10 |  96   |  98     | 2        | 159 | 158 |
|  10 |  98   | 100     | 2        | 222 | 177 |
|  10 | 100   | 102     | 2        |  95 |  98 |
|  10 | 102   | 104     | 2        |  59 |  68 |
|  10 | 104   | 106     | 2        |  48 |  51 |
|  10 | 106   | 108     | 2        | 215 | 190 |
|  10 | 108   | 110     | 2        |  99 | 141 |
|  10 | 110   | 112     | 2        | 273 | 179 |
|  10 | 112   | 114     | 2        | 196 | 292 |
|  10 | 114   | 116     | 2        | 401 | 340 |
|  10 | 116   | 118     | 2        | 230 | 220 |
|  10 | 118   | 120     | 2        | 168 | 167 |
|  10 | 120   | 122     | 2        | 280 | 245 |
|  10 | 122   | 124     | 2        | 183 | 240 |
|  10 | 124   | 126     | 2        | 246 | 243 |
|  10 | 126   | 128     | 2        | 227 | 232 |
|  10 | 128   | 130     | 2        | 174 | 188 |
|  10 | 130   | 132     | 2        | 367 | 329 |
|  10 | 132   | 134     | 2        | 350 | 341 |
|  10 | 134   | 136     | 2        | 489 | 453 |
|  10 | 136   | 138     | 2        | 374 | 389 |
|  10 | 138   | 140     | 2        | 442 | 467 |
|  10 | 140   | 142     | 2        | 366 | 366 |
|  10 | 142   | 144     | 2        | 330 | 361 |
|  10 | 144   | 146     | 2        | 407 | 529 |
|  10 | 146   | 148     | 2        | 424 | 395 |
|  10 | 148   | 150     | 2        | 364 | 210 |
|  10 | 150   | 150.982 | 0.982314 |  19 |   0 |



---

## Arithmetic-Relationship__case_865

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|    T |           U |           V |       W |       X |
|-----:|------------:|------------:|--------:|--------:|
| 1948 | 9.36532e+07 | 1.29286e+11 | 1380.48 | 26.5477 |
| 1949 | 9.44251e+07 | 1.26732e+11 | 1342.15 | 25.8105 |
| 1950 | 9.51316e+07 | 1.28157e+11 | 1347.16 | 25.9069 |
| 1951 | 9.57725e+07 | 1.35115e+11 | 1410.79 | 27.1306 |
| 1952 | 9.65457e+07 | 1.36073e+11 | 1409.41 | 27.1041 |
| 1953 | 9.75266e+07 | 1.37344e+11 | 1408.27 | 27.0822 |
| 1954 | 9.82952e+07 | 1.31418e+11 | 1336.97 | 25.7111 |
| 1955 | 9.90028e+07 | 1.36718e+11 | 1380.95 | 26.5568 |
| 1956 | 9.97344e+07 | 1.39291e+11 | 1396.62 | 26.858  |
| 1957 | 1.00689e+08 | 1.38102e+11 | 1371.57 | 26.3764 |
| 1958 | 1.01696e+08 | 1.33974e+11 | 1317.39 | 25.3344 |
| 1959 | 1.02877e+08 | 1.3757e+11  | 1337.24 | 25.7161 |
| 1960 | 1.044e+08   | 1.38888e+11 | 1330.34 | 25.5834 |
| 1961 | 1.05614e+08 | 1.39244e+11 | 1318.42 | 25.3542 |
| 1962 | 1.06236e+08 | 1.4151e+11  | 1332.04 | 25.6161 |
| 1963 | 1.08163e+08 | 1.43016e+11 | 1322.23 | 25.4275 |
| 1964 | 1.10026e+08 | 1.45929e+11 | 1326.31 | 25.506  |
| 1965 | 1.11791e+08 | 1.50281e+11 | 1344.3  | 25.8519 |
| 1966 | 1.13381e+08 | 1.54391e+11 | 1361.7  | 26.1866 |
| 1967 | 1.15187e+08 | 1.55052e+11 | 1346.09 | 25.8863 |
| 1968 | 1.17149e+08 | 1.57273e+11 | 1342.51 | 25.8175 |
| 1969 | 1.19141e+08 | 1.59749e+11 | 1340.84 | 25.7854 |
| 1970 | 1.21236e+08 | 1.58595e+11 | 1308.15 | 25.1567 |
| 1971 | 1.2357e+08  | 1.57856e+11 | 1277.45 | 24.5664 |
| 1972 | 1.2656e+08  | 1.62747e+11 | 1285.93 | 24.7295 |
| 1973 | 1.28987e+08 | 1.6739e+11  | 1297.73 | 24.9564 |
| 1974 | 1.31361e+08 | 1.68689e+11 | 1284.17 | 24.6955 |
| 1975 | 1.33751e+08 | 1.64626e+11 | 1230.83 | 23.6698 |
| 1976 | 1.36158e+08 | 1.71105e+11 | 1256.66 | 24.1666 |
| 1977 | 1.38514e+08 | 1.78924e+11 | 1291.74 | 24.8411 |
| 1978 | 1.40811e+08 | 1.87759e+11 | 1333.41 | 25.6425 |
| 1979 | 1.43138e+08 | 1.93325e+11 | 1350.62 | 25.9735 |
| 1980 | 1.45437e+08 | 1.91455e+11 | 1316.41 | 25.3155 |
| 1981 | 1.47351e+08 | 1.93199e+11 | 1311.15 | 25.2145 |
| 1982 | 1.48983e+08 | 1.89619e+11 | 1272.76 | 24.4762 |
| 1983 | 1.50441e+08 | 1.94143e+11 | 1290.49 | 24.8171 |
| 1984 | 1.52082e+08 | 2.05053e+11 | 1348.3  | 25.9289 |
| 1985 | 1.53354e+08 | 2.10265e+11 | 1371.1  | 26.3674 |
| 1986 | 1.55253e+08 | 2.15703e+11 | 1389.37 | 26.7186 |
| 1987 | 1.56817e+08 | 2.218e+11   | 1414.39 | 27.1998 |
| 1988 | 1.58152e+08 | 2.2815e+11  | 1442.59 | 27.7422 |
| 1989 | 1.59355e+08 | 2.33084e+11 | 1462.67 | 28.1283 |
| 1990 | 1.61995e+08 | 2.35019e+11 | 1450.78 | 27.8996 |
| 1991 | 1.63233e+08 | 2.32167e+11 | 1422.3  | 27.3519 |
| 1992 | 1.64501e+08 | 2.3302e+11  | 1416.53 | 27.2409 |
| 1993 | 1.65947e+08 | 2.37654e+11 | 1432.11 | 27.5406 |
| 1994 | 1.67448e+08 | 2.42722e+11 | 1449.54 | 27.8758 |
| 1995 | 1.68689e+08 | 2.46774e+11 | 1462.89 | 28.1325 |
| 1996 | 1.70328e+08 | 2.50144e+11 | 1468.6  | 28.2423 |
| 1997 | 1.72595e+08 | 2.57591e+11 | 1492.46 | 28.7012 |
| 1998 | 1.74382e+08 | 2.61947e+11 | 1502.14 | 28.8874 |
| 1999 | 1.76643e+08 | 2.66465e+11 | 1508.5  | 29.0096 |
| 2000 | 1.80484e+08 | 2.73927e+11 | 1517.73 | 29.1872 |
| 2001 | 1.82801e+08 | 2.70796e+11 | 1481.37 | 28.4879 |
| 2002 | 1.85168e+08 | 2.6982e+11  | 1457.16 | 28.0223 |
| 2003 | 1.8834e+08  | 2.71307e+11 | 1440.52 | 27.7022 |
| 2004 | 1.90173e+08 | 2.74587e+11 | 1443.88 | 27.7669 |
| 2005 | 1.92406e+08 | 2.80263e+11 | 1456.62 | 28.012  |
| 2006 | 1.94581e+08 | 2.85686e+11 | 1468.21 | 28.2348 |
| 2007 | 1.97013e+08 | 2.88587e+11 | 1464.81 | 28.1695 |
| 2008 | 1.98015e+08 | 2.85702e+11 | 1442.83 | 27.7467 |
| 2009 | 1.99221e+08 | 2.69099e+11 | 1350.76 | 25.9761 |
| 2010 | 2.00555e+08 | 2.6903e+11  | 1341.43 | 25.7967 |
| 2011 | 2.01318e+08 | 2.71573e+11 | 1348.98 | 25.9418 |
| 2012 | 2.02817e+08 | 2.77467e+11 | 1368.06 | 26.3089 |
| 2013 | 2.03652e+08 | 2.81713e+11 | 1383.31 | 26.6021 |
| 2014 | 2.04338e+08 | 2.86396e+11 | 1401.58 | 26.9535 |
| 2015 | 2.05605e+08 | 2.92463e+11 | 1422.45 | 27.3548 |
| 2016 | 2.06804e+08 | 2.9719e+11  | 1437.06 | 27.6358 |
| 2017 | 2.06836e+08 | 3.00181e+11 | 1451.3  | 27.9096 |



---

## Arithmetic-Relationship__case_595

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
| A     | B                                              | C            | D                                                                                                    |       E |         F |                G |   H |
|:------|:-----------------------------------------------|:-------------|:-----------------------------------------------------------------------------------------------------|--------:|----------:|-----------------:|----:|
| CAMHS | Children and Adolescent Mental Health Services | CAMHSAPC     | Children and Adolescent Mental Health Services, Admitted Patients                                    |  180356 |  771.253  |      1.391e+08   |  39 |
| CAMHS | Children and Adolescent Mental Health Services | CAMHSAPCPICU | Children and Adolescent Mental Health Services, Admitted Patients, Psychiatric Intensive Care Unit   |    6849 | 1503.07   |      1.02946e+07 |   5 |
| CAMHS | Children and Adolescent Mental Health Services | CAMHSCC      | Children and Adolescent Mental Health Services, Community Contacts                                   | 2094938 |  221.419  |      4.63858e+08 |  51 |
| CAMHS | Children and Adolescent Mental Health Services | CAMHSCCCRHT  | Children and Adolescent Mental Health Services, Community Contacts, Crisis Resolution Home Treatment |   94074 |  247.404  |      2.32743e+07 |  17 |
| CAMHS | Children and Adolescent Mental Health Services | CAMHSDC      | Children and Adolescent Mental Health Services, Day Care Facilities                                  |    6702 |  595.23   |      3.98923e+06 |   7 |
| CAMHS | Children and Adolescent Mental Health Services | CAMHSOP      | Children and Adolescent Mental Health Services, Outpatient Attendances                               |  490085 |  282.275  |      1.38339e+08 |  28 |
| DAS   | Drug and Alcohol Services                      | ALCAAP       | Alcohol Services, Adult, Admitted Patient                                                            |   15477 |  498.964  |      7.72247e+06 |   8 |
| DAS   | Drug and Alcohol Services                      | ALCACC       | Alcohol Services, Adult, Community Contacts                                                          |  109058 |   91.4938 |      9.97813e+06 |  12 |
| DAS   | Drug and Alcohol Services                      | ALCAOP       | Alcohol Services, Adult, Outpatient Attendances                                                      |   38243 |   67.1371 |      2.56752e+06 |   3 |
| DAS   | Drug and Alcohol Services                      | ALCCCC       | Alcohol Services, Children and Adolescents, Community Contacts                                       |     857 |  313.017  | 268256           |   5 |
| DAS   | Drug and Alcohol Services                      | DRUAAP       | Drug Services, Adult, Admitted Patient                                                               |    7604 |  487.918  |      3.71013e+06 |   6 |
| DAS   | Drug and Alcohol Services                      | DRUACC       | Drug Services, Adult, Community Contacts                                                             |  449324 |  118.402  |      5.32009e+07 |  16 |
| DAS   | Drug and Alcohol Services                      | DRUAOP       | Drug Services, Adult, Outpatient Attendances                                                         |  170505 |  100.752  |      1.71787e+07 |   8 |
| DAS   | Drug and Alcohol Services                      | DRUCCC       | Drug Services, Children and Adolescents, Community Contacts                                          |    4946 |  146.856  | 726352           |   6 |
| MHST  | Mental Health Specialist Teams                 | MHSTAEA      | A&E Mental Health Liaison Services, Adult and Elderly                                                |  689538 |  216.974  |      1.49612e+08 |  39 |
| MHST  | Mental Health Specialist Teams                 | MHSTAEC      | A&E Mental Health Liaison Services, Children and Adolescents                                         |    6916 |  239.991  |      1.65978e+06 |   5 |
| MHST  | Mental Health Specialist Teams                 | MHSTCJA      | Criminal Justice Liaison Services, Adult and Elderly                                                 |  141966 |  254.992  |      3.62002e+07 |  37 |
| MHST  | Mental Health Specialist Teams                 | MHSTCJC      | Criminal Justice Liaison Services, Children and Adolescents                                          |    6133 |  400.055  |      2.45354e+06 |  11 |
| MHST  | Mental Health Specialist Teams                 | MHSTFA       | Forensic Community, Adult and Elderly                                                                |  168144 |  287.015  |      4.82598e+07 |  36 |
| MHST  | Mental Health Specialist Teams                 | MHSTFC       | Forensic Community, Children and Adolescents                                                         |    3519 | 1313.43   |      4.62196e+06 |  11 |
| MHST  | Mental Health Specialist Teams                 | MHSTFLA      | Forensic liaison services, Adult and Elderly                                                         |    1478 |  534.023  | 789287           |   2 |
| MHST  | Mental Health Specialist Teams                 | MHSTFLC      | Forensic liaison services, Children and Adolescents                                                  |     454 |  898.32   | 407837           |   1 |
| MHST  | Mental Health Specialist Teams                 | MHSTIAPTC    | IAPT, Children and Adolescents                                                                       |   24541 |  267.645  |      6.56829e+06 |   4 |
| MHST  | Mental Health Specialist Teams                 | MHSTOTHA     | Other Mental Health Specialist Teams, Adult and Elderly                                              |  463438 |  154.847  |      7.17618e+07 |  33 |
| MHST  | Mental Health Specialist Teams                 | MHSTOTHC     | Other Mental Health Specialist Teams, Children and Adolescents                                       |   84509 |  170.294  |      1.43914e+07 |  11 |
| MHST  | Mental Health Specialist Teams                 | MHSTOTHPLA   | Other psychiatric liaison services, Adult and Elderly                                                |   80697 |  182.712  |      1.47443e+07 |  10 |
| MHST  | Mental Health Specialist Teams                 | MHSTOTHPLC   | Other psychiatric liaison services, Children and Adolescents                                         |    3007 |  233.165  | 701126           |   3 |
| MHST  | Mental Health Specialist Teams                 | MHSTPLA      | Psychiatric liaison – acute hospital/ Nursing Homes, Adult and Elderly                               |  174505 |  225.84   |      3.94101e+07 |  15 |
| MHST  | Mental Health Specialist Teams                 | MHSTPRIA     | Prison Health Adult and Elderly                                                                      |  156237 |  144.117  |      2.25164e+07 |   6 |
| MHST  | Mental Health Specialist Teams                 | MHSTPRIC     | Prison Health Children and Adolescents                                                               |   16576 |  149.555  |      2.47902e+06 |   2 |
| MHST  | Mental Health Specialist Teams                 | MHSTPSA      | Psycho – sexual services, Adult and Elderly                                                          |    6974 |  263.19   |      1.83548e+06 |   8 |
| MHST  | Mental Health Specialist Teams                 | MHSTPSC      | Psycho – sexual services, Children and Adolescents                                                   |     303 |  376.22   | 113995           |   1 |
| SCU   | Secure Mental Health Services                  | SCU02        | Child and Adolescent Low Secure Services                                                             |    5748 | 1455.35   |      8.36538e+06 |   3 |
| SCU   | Secure Mental Health Services                  | SCU03        | Child and Adolescent Medium Secure Services                                                          |   11040 | 1814.33   |      2.00302e+07 |   5 |
| SCU   | Secure Mental Health Services                  | SCU04        | High Dependency Secure Provision, Learning Disabilities                                              |     365 | 3203.95   |      1.16944e+06 |   1 |
| SCU   | Secure Mental Health Services                  | SCU05        | High Dependency Secure Provision, Mental Health or Psychosis                                         |    4015 |  809.02   |      3.24822e+06 |   1 |
| SCU   | Secure Mental Health Services                  | SCU06        | High Dependency Secure Provision, Personality Disorder                                               |    9356 |  710.149  |      6.64416e+06 |   2 |
| SPMHS | Specialist Mental Health Services              | SPHMSASDAPC  | Specialised Services For Asperger Syndrome and Autistic Spectrum Disorder, Admitted Patient          |    5956 | 1447.97   |      8.62411e+06 |   1 |
| SPMHS | Specialist Mental Health Services              | SPHMSASDCC   | Specialised Services For Asperger Syndrome and Autistic Spectrum Disorder, Community Contacts        |   32212 |  354.347  |      1.14142e+07 |  22 |
| SPMHS | Specialist Mental Health Services              | SPHMSASDOP   | Specialised Services For Asperger Syndrome and Autistic Spectrum Disorder, Outpatient Attendances    |    9370 |  292.651  |      2.74214e+06 |   8 |
| SPMHS | Specialist Mental Health Services              | SPHMSDAAPC   | Specialist Mental Health Services For Deaf Adults, Admitted Patient                                  |   14089 |  502.914  |      7.08556e+06 |   3 |
| SPMHS | Specialist Mental Health Services              | SPHMSDACC    | Specialist Mental Health Services For Deaf Adults, Community Contacts                                |    1750 |  474.866  | 831016           |   5 |
| SPMHS | Specialist Mental Health Services              | SPHMSDAOP    | Specialist Mental Health Services For Deaf Adults, Outpatient Attendances                            |    4346 |  401.666  |      1.74564e+06 |   3 |
| SPMHS | Specialist Mental Health Services              | SPHMSDCAPC   | Mental Health Services for Deaf Children And Adolescents, Admitted Patient                           |    1033 | 1722.84   |      1.77969e+06 |   1 |
| SPMHS | Specialist Mental Health Services              | SPHMSDCCC    | Mental Health Services for Deaf Children And Adolescents, Community Contacts                         |    4081 |  590.817  |      2.41113e+06 |   3 |
| SPMHS | Specialist Mental Health Services              | SPHMSDCOP    | Mental Health Services for Deaf Children And Adolescents, Outpatient Attendances                     |    4288 |  670.173  |      2.8737e+06  |   3 |
| SPMHS | Specialist Mental Health Services              | SPHMSEDSAAPC | Adult Specialist Eating Disorder Services, Admitted Patient                                          |   74913 |  532.319  |      3.98776e+07 |  17 |
| SPMHS | Specialist Mental Health Services              | SPHMSEDSACC  | Adult Specialist Eating Disorder Services, Community Contacts                                        |   82273 |  184.361  |      1.5168e+07  |  17 |
| SPMHS | Specialist Mental Health Services              | SPHMSEDSAOP  | Adult Specialist Eating Disorder Services, Outpatient Attendances                                    |   62213 |  192.306  |      1.19639e+07 |  12 |
| SPMHS | Specialist Mental Health Services              | SPHMSEDSCAPC | Child and Adolescent Eating Disorder Services, Admitted Patient                                      |   11937 |  787.108  |      9.39571e+06 |   5 |
| SPMHS | Specialist Mental Health Services              | SPHMSEDSCCC  | Child and Adolescent Eating Disorder Services, Community Contacts                                    |  105369 |  199.362  |      2.10065e+07 |  23 |
| SPMHS | Specialist Mental Health Services              | SPHMSEDSCOP  | Child and Adolescent Eating Disorder Services, Outpatient Attendances                                |   43693 |  206.237  |      9.01111e+06 |   9 |
| SPMHS | Specialist Mental Health Services              | SPHMSGIDCC   | Gender Identity Disorder Services, Community Contacts                                                |   25413 |  246.704  |      6.26948e+06 |   6 |
| SPMHS | Specialist Mental Health Services              | SPHMSGIDOP   | Gender Identity Disorder Services, Outpatient Attendances                                            |    9956 |  126.87   |      1.26312e+06 |   1 |
| SPMHS | Specialist Mental Health Services              | SPHMSMBUAPC  | Specialist Perinatal Mental Health Services, Admitted Patient                                        |   35837 |  839.636  |      3.009e+07   |  17 |
| SPMHS | Specialist Mental Health Services              | SPHMSMBUCC   | Specialist Perinatal Mental Health Services, Community Contacts                                      |  163062 |  232.225  |      3.78672e+07 |  39 |
| SPMHS | Specialist Mental Health Services              | SPHMSMBUOP   | Specialist Perinatal Mental Health Services, Outpatient Attendances                                  |   24289 |  349.686  |      8.49353e+06 |  12 |
| SPMHS | Specialist Mental Health Services              | SPHMSMVCC    | Mental Health Services For Veterans, Community Contacts                                              |   11239 |  264.761  |      2.97565e+06 |   9 |
| SPMHS | Specialist Mental Health Services              | SPHMSMVOP    | Mental Health Services For Veterans, Outpatient Attendances                                          |    9237 |  371.028  |      3.42719e+06 |   4 |
| SPMHS | Specialist Mental Health Services              | SPHMSOTHAPC  | Other Specialist Mental Health Services, Admitted Patient                                            |   95764 |  407.882  |      3.90604e+07 |  13 |



---

## Arithmetic-Relationship__case_101

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
| J   | K   | L   |    M |    N |    O | P         | Q          |
|:----|:----|:----|-----:|-----:|-----:|:----------|:-----------|
| A   | M   | U   | 1872 | 1875 |    3 | 3/1/1872  | 12/31/1875 |
| A   | M   | U   | 1874 | 1875 |    1 | 3/1/1874  | 12/31/1875 |
| A   | M   | U   | 1874 | 1882 |    8 | 3/1/1874  | 12/31/1882 |
| A   | M   | U   | 1882 | 1887 |    5 | 3/1/1882  | 12/31/1887 |
| A   | M   | U   | 1885 | 1887 |    2 | 3/1/1885  | 12/31/1887 |
| A   | M   | U   | 1885 | 1887 |    2 | 3/1/1885  | 12/31/1887 |
| A   | M   | U   | 1885 | 1900 |   15 | 3/1/1885  | 12/31/1900 |
| A   | M   | U   | 1887 | 1890 |    3 | 3/1/1887  | 12/31/1890 |
| A   | M   | U   | 1889 | 1892 |    3 | 3/1/1889  | 12/31/1892 |
| A   | M   | U   | 1891 | 1896 |    5 | 3/1/1891  | 12/31/1896 |
| A   | M   | U   | 1893 | 1899 |    6 | 3/1/1893  | 12/31/1899 |
| A   | M   | U   | 1896 | 1898 |    2 | 3/1/1896  | 12/31/1898 |
| A   | M   | U   | 1899 | 1900 |    1 | 3/1/1899  | 12/31/1900 |
| A   | M   | U   | 1900 | 1900 |    0 | 3/1/1900  | 12/31/1900 |
| A   | M   | U   | 1901 | 1904 |    3 | 3/1/1901  | 12/31/1904 |
| A   | M   | U   | 1901 | 1914 |   13 | 3/1/1901  | 12/31/1914 |
| A   | M   | U   | 1901 | 1921 |   20 | 3/1/1901  | 12/31/1921 |
| A   | M   | U   | 1905 | 1908 |    3 | 3/1/1905  | 12/31/1908 |
| A   | M   | U   | 1909 | 1917 |    8 | 3/1/1909  | 12/31/1917 |
| E   | M   | U   | 1914 | 1932 |   18 | 1/1/1914  | 12/31/1932 |
| E   | M   | U   | 1917 | 1923 |    6 | 1/1/1917  | 12/31/1923 |
| E   | M   | U   | 1921 | 1927 |    6 | 1/1/1921  | 12/31/1927 |
| E   | M   | U   | 1923 | 1923 |    0 | 1/1/1923  | 12/31/1923 |
| E   | M   | U   | 1923 | 1936 |   13 | 1/1/1923  | 12/31/1936 |
| E   | M   | U   | 1928 | 1934 |    6 | 1/1/1928  | 12/31/1934 |
| E   | M   | U   | 1933 | 1936 |    3 | 1/1/1933  | 12/31/1936 |
| E   | M   | U   | 1935 | 1940 |    5 | 1/1/1935  | 12/31/1940 |
| E   | M   | U   | 1936 | 1938 |    2 | 1/1/1936  | 12/31/1938 |
| E   | M   | U   | 1937 | 1942 |    5 | 1/1/1937  | 12/31/1942 |
| E   | M   | U   | 1939 | 1949 |   10 | 1/1/1939  | 12/31/1949 |
| E   | M   | U   | 1941 | 1951 |   10 | 1/1/1941  | 12/31/1951 |
| E   | M   | U   | 1943 | 1943 |    0 | 1/1/1943  | 12/31/1943 |
| E   | M   | U   | 1943 | 1944 |    1 | 1/1/1943  | 12/31/1944 |
| E   | M   | U   | 1944 | 1948 |    4 | 1/1/1944  | 12/31/1948 |
| E   | M   | U   | 1948 | 1948 |    0 | 1/1/1948  | 12/31/1948 |
| E   | M   | U   | 1949 | 1952 |    3 | 1/1/1949  | 12/31/1952 |
| E   | M   | U   | 1949 | 1954 |    5 | 1/1/1949  | 12/31/1954 |
| E   | M   | U   | 1951 | 1958 |    7 | 1/1/1951  | 12/31/1958 |
| E   | M   | U   | 1952 | 1952 |    0 | 1/1/1952  | 12/31/1952 |
| E   | M   | U   | 1952 | 1970 |   18 | 1/1/1952  | 12/31/1970 |
| E   | M   | U   | 1955 | 1966 |   11 | 1/1/1955  | 12/31/1966 |
| E   | M   | D   | 1959 | 1972 |   13 | 1/1/1959  | 12/31/1972 |
| E   | M   | U   | 1967 | 1972 |    5 | 1/1/1967  | 12/31/1972 |
| E   | M   | R   | 1970 | 1975 |    5 | 1/1/1970  | 12/31/1975 |
| E   | M   | D   | 1972 | 1977 |    5 | 1/1/1972  | 12/31/1977 |
| A   | F   | R   | 1975 | 1979 |    4 | 3/1/1975  | 12/31/1979 |
| A   | F   | R   | 1975 | 1981 |    6 | 3/1/1975  | 12/31/1981 |
| A   | M   | D   | 1975 | 1976 |    1 | 3/1/1975  | 12/31/1976 |
| A   | M   | D   | 1976 | 1981 |    5 | 3/1/1976  | 12/31/1981 |
| A   | F   | D   | 1977 | 1983 |    6 | 3/1/1977  | 12/31/1983 |
| A   | F   | D   | 1978 | 1980 |    2 | 3/1/1978  | 12/31/1980 |
| A   | F   | R   | 1979 | 1984 |    5 | 3/1/1979  | 12/31/1984 |
| A   | M   | D   | 1980 | 1984 |    4 | 3/1/1980  | 12/31/1984 |
| A   | M   | R   | 1980 | 1986 |    6 | 3/1/1980  | 12/31/1986 |
| A   | F   | R   | 1983 | 1985 |    2 | 3/1/1983  | 12/31/1985 |
| A   | F   | D   | 1983 | 1995 |   12 | 9/14/1983 | 12/31/1995 |
| A   | M   | D   | 1984 | 1987 |    3 | 3/1/1984  | 12/31/1987 |
| A   | M   | U   | 1985 | 1990 |    5 | 1/2/1985  | 12/31/1990 |
| A   | F   | D   | 1986 | 1989 |    3 | 3/1/1986  | 12/31/1989 |
| A   | M   | R   | 1986 | 1992 |    6 | 4/1986    | 12/31/1992 |
| A   | F   | D   | 1987 | 1993 |    6 | 12/1/1987 | 12/31/1993 |
| A   | F   | D   | 1989 | 1991 |    2 | 12/4/1989 | 12/31/1991 |
| A   | F   | R   | 1991 | 1996 |    5 | 1/8/1991  | 12/31/1996 |
| A   | M   | I   | 1992 | 1996 |    4 | 4/1992    | 12/31/1996 |
| A   | M   | R   | 1992 | 1998 |    6 | 1/1992    | 12/31/1998 |
| A   | M   | I   | 1993 | 2007 |   14 | 8/1993    | 12/31/2007 |
| A   | M   | D   | 1995 | 2001 |    6 | 3/1995    | 12/31/2001 |
| A   | M   | U   | 1996 | 1997 |    1 | 3/1/1996  | 12/31/1997 |
| A   | M   | R   | 1997 | 2002 |    5 | 2/1997    | 12/31/2002 |
| A   | M   | I   | 1997 | 2004 |    7 | 8/19/1997 | 12/31/2004 |
| A   | M   | R   | 1998 | 2008 |   10 | 1/6/1998  | 12/31/2008 |
| A   | F   | D   | 2001 | 2013 |   12 | 5/16/2001 | 3/3/2013   |
| A   | F   | D   | 2002 | 2003 |    1 | 11/8/2002 | 12/31/2003 |
| A   | M   | U   | 2003 | 2007 |    4 | 9/2003    | 12/31/2007 |
| A   | M   | D   | 2004 | 2011 |    7 | 9/2004    | 3/2011     |
| A   | M   | R   | 2007 | 2015 |    8 | 7/10/2007 | 42009      |
| A   | F   | R   | 2008 | 2016 |    8 | 8/1/2008  | 42373      |
| A   | M   | R   | 2008 | 2014 |    6 | 2/7/2008  | 41645      |
| A   | F   | D   | 2012 | 2017 |    5 | 7/2/2012  | 42737      |
| A   | F   | I   | 2013 | 2019 |    6 | 3/4/2013  | 43466      |
| A   | M   | D   | 2014 | 2020 |    6 | 41671     | 43836      |
| A   | M   | U   | 2015 | 9999 | 7984 | 42036     | 9999       |
| A   | M   | U   | 2016 | 9999 | 7983 | 42370     | 9999       |
| A   | F   | D   | 2017 | 9999 | 7982 | 42736     | 9999       |
| A   | F   | D   | 2019 | 9999 | 7980 | 43577     | 9999       |



---

## Arithmetic-Relationship__case_644

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
| A    | B                                       |   C |   D |   E |   F |   G |   H |   I |   J |   K |   L |   M | N   |
|:-----|:----------------------------------------|----:|----:|----:|----:|----:|----:|----:|----:|----:|----:|----:|:----|
| ACR  | Comm Ag Rec & Res Studies               |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   0 |   0 |   0 |   1 | A   |
| AL   | Arts and Letters                        |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   1 | H   |
| ANP  | Anthropology                            |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   0 |   0 |   1 | H   |
| BMB  | Biochem and Molecular Biology           |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   1 | S   |
| CAS  | Communication Arts and Sciences         |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   1 |   0 |   0 |   2 | C   |
| CHE  | Chemical Engineering                    |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   2 |   0 |   3 | E   |
| CHS  | Chinese                                 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   1 | L   |
| CSE  | Computer Science and Engineering        |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   0 |   0 |   0 |   1 | E   |
| CSS  | Crop and Soil Sciences                  |   0 |   0 |   0 |   0 |   3 |   0 |   0 |   2 |   0 |   0 |   5 | A   |
| EC   | Economics                               |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   0 |   0 |   0 |   1 | B   |
| ENG  | English                                 |   0 |   0 |   0 |   0 |   2 |   0 |   0 |   0 |   0 |   0 |   2 | H   |
| ENT  | Entomology                              |   0 |   0 |   0 |   0 |   0 |   1 |   1 |   0 |   0 |   0 |   2 | S   |
| EPI  | Epidemiology                            |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   1 | S   |
| FI   | Finance                                 |   0 |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   0 |   1 | B   |
| FSC  | Food Science                            |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   0 |   0 |   1 | S   |
| FW   | Fisheries and Wildlife                  |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   2 |   0 |   3 | A   |
| GSAH | Global Studies in Arts and Humanities   |   0 |   0 |   0 |   0 |   2 |   0 |   0 |   0 |   0 |   0 |   2 | H   |
| HA   | History of Art                          |   0 |   0 |   0 |   0 |   5 |   4 |   0 |   0 |   0 |   0 |   9 | H   |
| HM   | Human Medicine                          |   0 |   0 |   0 |   0 |   4 |   0 |   0 |  16 |  10 |   0 |  30 | S   |
| HST  | History                                 |   0 |   0 |   0 |   0 |   0 |   4 |   0 |   5 |  12 |   0 |  21 | H   |
| LIN  | Linguistics                             |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   2 |   0 |   2 | L   |
| LIR  | Labor and Industrial Relations          |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   0 |   0 |   1 | B   |
| MKT  | Marketing                               |   0 |   0 |   0 |   0 |   0 |   1 |   1 |   0 |   0 |   0 |   2 | N   |
| MSE  | Materials Science and Engineering       |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   0 |   0 |   1 | E   |
| MTHE | Mathematics Education                   |   0 |   0 |   0 |   0 |   1 |   1 |   0 |   1 |   0 |   0 |   3 | Ed  |
| NEU  | Neurology                               |   0 |   0 |   0 |   0 |   0 |   4 |   0 |   4 |   0 |   0 |   8 | S   |
| PHL  | Philosophy                              |   0 |   0 |   0 |   0 |   0 |   1 |   1 |   0 |   0 |   0 |   2 | H   |
| PKG  | Packaging                               |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   1 |   0 |   0 |   2 | B   |
| PIM  | Program in Integrative Management       |   0 |   0 |   0 |   0 |   4 |   0 |   0 |   4 |   1 |   0 |   9 | B   |
| PPL  | Public Policy                           |   0 |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   0 |   1 | PS  |
| RCAH | Residential College in Arts and Letters |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   0 |   0 |   0 |   1 | H   |
| REL  | Religious Studies                       |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   1 |   1 |   0 |   3 | H   |
| SOC  | Sociology                               |   0 |   0 |   0 |   0 |   2 |   2 |   0 |   3 |   2 |   0 |   9 | SS  |
| SPN  | Spanish                                 |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |   1 |   0 |   2 | L   |
| TC   | Telecommunication                       |   0 |   0 |   0 |   0 |   4 |   3 |   0 |   0 |   0 |   0 |   7 | C   |
| TE   | Teacher Education                       |   0 |   0 |   0 |   0 |   5 |   3 |   0 |   6 |   0 |   0 |  14 | Ed  |
| WRA  | Writing, Rhetoric, and American Culture |   0 |   0 |   0 |   0 |   2 |   2 |   0 |   1 |   7 |   0 |  12 | H   |
| WS   | Women's Studies                         |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   1 |   0 |   1 | H   |
| ZOL  | Zoology                                 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   2 |   0 |   0 |   2 | S   |



---

## Arithmetic-Relationship__case_462

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
| A           |    B |   C |        D |
|:------------|-----:|----:|---------:|
| FA2103      |    1 |   1 | 1        |
| FA2486      |    1 |   0 | 0        |
| FA2487      |    6 |   5 | 0.833333 |
| FA2517      |    4 |   4 | 1        |
| FA2860      |    1 |   0 | 0        |
| FA4654      |    3 |   0 | 0        |
| FA4877      |    1 |   0 | 0        |
| FA5587      |    1 |   1 | 1        |
| FA6606      |    2 |   0 | 0        |
| FA6643      |    5 |   0 | 0        |
| FA6670      |    9 |   0 | 0        |
| FA7014      |    8 |   8 | 1        |
| FA7022      |    3 |   3 | 1        |
| FA7037      |    1 |   1 | 1        |
| FA8075      |   18 |  18 | 1        |
| FA8101      |   12 |   0 | 0        |
| FA8102      |    1 |   0 | 0        |
| FA8207      |    1 |   1 | 1        |
| FA8210      |    1 |   1 | 1        |
| FA8213      |    1 |   1 | 1        |
| FA8220      |    2 |   2 | 1        |
| FA8224      |    1 |   1 | 1        |
| FA8232      |    3 |   3 | 1        |
| FA8501      |    2 |   1 | 0.5      |
| FA8504      |    3 |   3 | 1        |
| FA8505      |    2 |   2 | 1        |
| FA8509      |    2 |   2 | 1        |
| FA8520      |    2 |   2 | 1        |
| FA8527      |    2 |   2 | 1        |
| FA8528      |    1 |   1 | 1        |
| FA8533      |    5 |   5 | 1        |
| FA8538      |    2 |   2 | 1        |
| FA8539      |    1 |   1 | 1        |
| FA8540      |    2 |   2 | 1        |
| FA8553      |    1 |   1 | 1        |
| FA8604      |   10 |  10 | 1        |
| FA8606      |    4 |   4 | 1        |
| FA8616      |    1 |   1 | 1        |
| FA8617      |    1 |   1 | 1        |
| FA8620      |   11 |  10 | 0.909091 |
| FA8625      |    1 |   1 | 1        |
| FA8634      |    2 |   2 | 1        |
| FA8637      |    2 |   1 | 0.5      |
| FA8650      |   46 |  44 | 0.956522 |
| FA8651      |    5 |   5 | 1        |
| FA8675      |    2 |   2 | 1        |
| FA8678      |    1 |   1 | 1        |
| FA8681      |    3 |   3 | 1        |
| FA8682      |    1 |   1 | 1        |
| FA8702      |    1 |   1 | 1        |
| FA8721      |    9 |   4 | 0.444444 |
| FA8723      |    1 |   1 | 1        |
| FA8726      |    3 |   3 | 1        |
| FA8730      |    5 |   5 | 1        |
| FA8735      |    1 |   1 | 1        |
| FA8750      |   57 |  56 | 0.982456 |
| FA8751      |    2 |   0 | 0        |
| FA8770      |    1 |   0 | 0        |
| FA8773      |    3 |   2 | 0.666667 |
| FA8802      |    1 |   1 | 1        |
| FA8807      |    1 |   1 | 1        |
| FA8810      |    4 |   4 | 1        |
| FA8811      |    2 |   2 | 1        |
| FA8814      |    1 |   0 | 0        |
| FA8818      |    2 |   1 | 0.5      |
| FA8819      |    3 |   2 | 0.666667 |
| FA8823      |    4 |   3 | 0.75     |
| FA9101      |    1 |   1 | 1        |
| FA9300      |    1 |   1 | 1        |
| FA9302      |    1 |   1 | 1        |
| FA9401      |    2 |   0 | 0        |
| FA9451      |    1 |   1 | 1        |
| FA9453      |    9 |   9 | 1        |
| H92241      |    3 |   3 | 1        |
| H92400      |    1 |   0 | 0        |
| H92401      |   12 |  12 | 1        |
| H92402      |    2 |   2 | 1        |
| H92403      |    3 |   3 | 1        |
| H92404      |    8 |   8 | 1        |
| H92405      |    5 |   5 | 1        |
| HC1028      |   21 |  21 | 1        |
| HDTRA1      |    4 |   4 | 1        |
| HQ0034      |   15 |   5 | 0.333333 |
| HQ0147      |   42 |  42 | 1        |
| HQ0276      |    1 |   1 | 1        |
| HQ0277      |    1 |   1 | 1        |
| HQ0727      |    1 |   0 | 0        |
| HQ0796      |    1 |   1 | 1        |
| HR0011      |   36 |  36 | 1        |
| HT0011      |    3 |   1 | 0.333333 |
| HTC711      |    2 |   2 | 1        |
| M67854      |   11 |  10 | 0.909091 |
| M95494      |    1 |   1 | 1        |
| N00014      |   26 |  26 | 1        |
| N00019      |   18 |  10 | 0.555556 |
| N00024      |   27 |  24 | 0.888889 |
| N00039      |   10 |   8 | 0.8      |
| N00164      |    6 |   6 | 1        |
| N00167      |    3 |   3 | 1        |
| N00174      |    3 |   2 | 0.666667 |
| N00178      |    5 |   5 | 1        |
| N00189      |   17 |  16 | 0.941176 |
| N00253      |    1 |   1 | 1        |
| N00421      |   34 |  21 | 0.617647 |
| N32253      |    1 |   1 | 1        |
| N39040      |    4 |   4 | 1        |
| N40080      |    3 |   3 | 1        |
| N40085      |    1 |   0 | 0        |
| N50054      |   18 |   0 | 0        |
| N61331      |    1 |   1 | 1        |
| N61340      |   11 |  10 | 0.909091 |
| N62645      |    5 |   5 | 1        |
| N63394      |    1 |   1 | 1        |
| N64267      |    4 |   4 | 1        |
| N64498      |   19 |  18 | 0.947368 |
| N65236      |    7 |   7 | 1        |
| N66001      |   31 |  31 | 1        |
| N66604      |   26 |  26 | 1        |
| N68335      |   82 |  80 | 0.97561  |
| N68936      |    6 |   6 | 1        |
| N69450      |    2 |   0 | 0        |
| SPRDL1      |    1 |   1 | 1        |
| W15P7T      |   14 |  12 | 0.857143 |
| W15QKN      |   30 |  28 | 0.933333 |
| W31P4Q      |   22 |  22 | 1        |
| W56HZV      |   23 |  20 | 0.869565 |
| W56JSR      |    5 |   5 | 1        |
| W56KGU      |    6 |   3 | 0.5      |
| W56KGY      |    1 |   1 | 1        |
| W56KGZ      |    4 |   2 | 0.5      |
| W58RGZ      |    4 |   3 | 0.75     |
| W81XWH      |   37 |  34 | 0.918919 |
| W900KK      |   12 |   7 | 0.583333 |
| W909MY      |   20 |  18 | 0.9      |
| W9113M      |    7 |   4 | 0.571429 |
| W91151      |    1 |   1 | 1        |
| W911NF      |   22 |  16 | 0.727273 |
| W911QX      |    9 |   9 | 1        |
| W911QY      |   15 |   8 | 0.533333 |
| W911RP      |    1 |   1 | 1        |
| W911S0      |    1 |   1 | 1        |
| W911S8      |    1 |   1 | 1        |
| W911SD      |    2 |   2 | 1        |
| W911SR      |    3 |   3 | 1        |
| W911W4      |    1 |   1 | 1        |
| W911W5      |    1 |   1 | 1        |
| W911W6      |   11 |   7 | 0.636364 |
| W9124J      |    1 |   1 | 1        |
| W9124R      |    3 |   0 | 0        |
| W9124V      |    2 |   0 | 0        |
| W91278      |    1 |   1 | 1        |
| W9128Z      |    1 |   0 | 0        |
| W912BV      |    4 |   0 | 0        |
| W912GB      |    2 |   1 | 0.5      |
| W912HN      |    1 |   1 | 1        |
| W912HQ      |   29 |  28 | 0.965517 |
| W912HZ      |    2 |   1 | 0.5      |
| W912JD      |    1 |   1 | 1        |
| W912JM      |    6 |   0 | 0        |
| W912L7      |    1 |   1 | 1        |
| W912L8      |    1 |   0 | 0        |
| W912LA      |    1 |   0 | 0        |
| W912NR      |    6 |   0 | 0        |
| W912P9      |    1 |   1 | 1        |
| W912PP      |    5 |   0 | 0        |
| W912QG      |    1 |   0 | 0        |
| W9132T      |    1 |   0 | 0        |
| W9133L      |    1 |   1 | 1        |
| W91364      |    1 |   0 | 0        |
| W91CRB      |   11 |   4 | 0.363636 |
| W91RUS      |    5 |   3 | 0.6      |
| W91ZRU      |    1 |   1 | 1        |
| Grand Total | 1205 | 993 | 0.824066 |



---

## Arithmetic-Relationship__case_36

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
| A            |        B |         C |        D |   E |          F |   G |   H |          I |          J |     K |
|:-------------|---------:|----------:|---------:|----:|-----------:|----:|----:|-----------:|-----------:|------:|
| ALLEGANY     |  4452.29 |  22574.3  |  9953.23 |   0 |   824.753  |   0 |   0 |   148.448  |  11647.9   |  1514 |
| BROOME       | 14867.2  |  46110.3  | 25181.9  |   0 |  3245.03   |   0 |   0 |  1149.94   |  16533.4   |  3434 |
| CATTARAUGUS  |  7753.55 |  34804.5  | 18176.2  |   0 |  1235.4    |   0 |   0 |   515.098  |  14877.7   |  2259 |
| CAYUGA       |  6596.25 |  26760.7  | 12374.5  |   0 |  1210      |   0 |   0 |   317.966  |  12858.2   |  1890 |
| CHAUTAUQUA   | 11250.3  |  51444    | 24347.7  |   0 |  2512.14   |   0 |   0 |   910.264  |  23673.8   |  3960 |
| CHEMUNG      |  7743.22 |  41221.3  | 18233.6  |   0 |  1658.32   |   0 |   0 |   822.27   |  20507.1   |  2614 |
| CHENANGO     |  4620.36 |  17289.9  |  9218.53 |   0 |   707.126  |   0 |   0 |   141.635  |   7222.63  |  1028 |
| CLINTON      |  6886.68 |  28353.1  | 17771.9  |   0 |  1424.93   |   0 |   0 |   552.084  |   8604.14  |  1993 |
| COLUMBIA     |  5481.72 |  26185    |  7120.33 |   0 |  5408.25   |   0 |   0 |   417.739  |  13238.7   |  1187 |
| CORTLAND     |  3368.34 |  14520.8  |  5464.03 |   0 |   657.328  |   0 |   0 |   196.709  |   8202.76  |  1082 |
| DELAWARE     |  4128.61 |  13282.7  |  6598.95 |   0 |   784.8    |   0 |   0 |   307.984  |   5590.94  |   855 |
| ESSEX        |  4108.29 |  12260.7  |  6781.3  |   0 |   379.024  |   0 |   0 |   326.75   |   4773.66  |   885 |
| FRANKLIN     |  4042.56 |  14744.3  |  8361.41 |   0 |   671.019  |   0 |   0 |   218.9    |   5492.97  |  1012 |
| FULTON       |  4837.97 |  16949.5  |  8369.82 |   0 |   919.142  |   0 |   0 |   255.578  |   7404.92  |  1021 |
| GREENE       |  4219.89 |  23100.9  |  7644.13 |   0 |  1515.58   |   0 |   0 |   300.55   |  13640.7   |  1166 |
| HAMILTON     |   637.74 |   1180.48 |   637.4  |   0 |    27.7094 |   0 |   0 |    39.2427 |    476.126 |    87 |
| HERKIMER     |  5810.59 |  20580.3  | 11530.7  |   0 |   813.982  |   0 |   0 |   239.706  |   7995.94  |  1235 |
| JEFFERSON    | 10748.7  |  57764.8  | 31868.4  |   0 |  8843.84   |   0 |   0 |   744.09   |  16308.5   |  3214 |
| LEWIS        |  2386.31 |   8738.22 |  4873.79 |   0 |   433.117  |   0 |   0 |   286.754  |   3144.56  |   649 |
| LIVINGSTON   |  5138.08 |  17962.8  |  7715.68 |   0 |   955.268  |   0 |   0 |   348.307  |   8943.55  |  1249 |
| MADISON      |  5310.48 |  21363.7  |  9333.9  |   0 |  1296.86   |   0 |   0 |   304.178  |  10428.7   |  1359 |
| MONTGOMERY   |  4224.24 |  17548.9  |  8520.81 |   0 |   809.85   |   0 |   0 |   270.48   |   7947.72  |   914 |
| NASSAU       | 68231.8  | 184242    | 74665.1  |   0 | 16696.3    |   0 |   0 | 12285.3    |  80595.6   | 12633 |
| NIAGARA      | 17136    |  72834.5  | 34109    |   0 |  4462.23   |   0 |   0 |  1319.92   |  32943.3   |  4359 |
| ONEIDA       | 18991.9  |  75543.8  | 41987.4  |   0 |  3729.98   |   0 |   0 |  1324.74   |  28501.8   |  4650 |
| ORANGE       | 23023.7  |  99367.4  | 42151.8  |   0 |  8575.5    |   0 |   0 |  1356.45   |  47283.7   |  5008 |
| ORLEANS      |  3325.9  |  16141.6  |  7606.18 |   0 |   562.9    |   0 |   0 |   199.875  |   7772.69  |   922 |
| OSWEGO       | 10198.8  |  47198.6  | 18218.3  |   0 |  2404.22   |   0 |   0 |   814.309  |  25761.8   |  3125 |
| OTSEGO       |  4682.74 |  16551.4  |  9763.64 |   0 |   919.698  |   0 |   0 |   278.321  |   5589.72  |   874 |
| PUTNAM       |  6520.42 |  16400.9  |  7217.72 |   0 |  1063.21   |   0 |   0 |   650.82   |   7469.14  |  1090 |
| QUEENS       | 60849.4  | 301702    | 92023.6  |   0 | 51229.6    |   0 |   0 |  6647.66   | 151801     | 11484 |
| RENSSELAER   | 11003.7  |  47248.6  | 18841    |   0 |  3260.78   |   0 |   0 |   815.838  |  24331     |  2759 |
| RICHMOND     | 24312.1  |  87620    | 35615.1  |   0 | 12153      |   0 |   0 |  1609.15   |  38242.8   |  3880 |
| ROCKLAND     | 13156.5  |  42269.8  | 19481.4  |   0 |  3018.45   |   0 |   0 |  2073.22   |  17696.8   |  3164 |
| ST. LAWRENCE |  9019.14 |  37147.6  | 22143.5  |   0 |  2085.08   |   0 |   0 |   536.735  |  12382.2   |  2424 |
| SARATOGA     | 17334    |  50275.3  | 24252.3  |   0 |  4429.63   |   0 |   0 |   854.582  |  20738.8   |  3304 |
| SCHENECTADY  | 11417.3  |  40016.8  | 15846.8  |   0 |  5953.14   |   0 |   0 |   895.021  |  17321.9   |  2283 |
| SCHOHARIE    |  2867.81 |  10380.5  |  4127.53 |   0 |   513.531  |   0 |   0 |   146.138  |   5593.34  |   612 |
| SCHUYLER     |  1876.35 |   7081.26 |  3013.6  |   0 |   173.779  |   0 |   0 |    57.7755 |   3836.1   |   530 |
| SENECA       |  2660.28 |  14895.2  |  6410.4  |   0 |   363.688  |   0 |   0 |   189.322  |   7931.76  |   841 |
| SULLIVAN     |  5394.11 |  22813.2  |  9770.19 |   0 |   935.301  |   0 |   0 |   290.403  |  11817.3   |  1369 |
| TIOGA        |  4589.97 |  12859.5  |  7056.12 |   0 |   839.099  |   0 |   0 |   280.456  |   4683.8   |  1063 |
| TOMPKINS     |  5029.19 |  16578.3  |  7887.62 |   0 |  2161.76   |   0 |   0 |   507.387  |   6021.55  |  1066 |
| ULSTER       | 12948.9  |  45240.8  | 16973.1  |   0 |  4898.91   |   0 |   0 |  1076.65   |  22292.1   |  2824 |
| WARREN       |  6472.98 |  17891.5  |  9517.03 |   0 |   958.07   |   0 |   0 |   387.273  |   7029.13  |  1348 |
| WASHINGTON   |  5837.13 |  17037.1  |  8561.48 |   0 |   880.56   |   0 |   0 |   173.71   |   7421.33  |  1203 |
| WAYNE        |  7271.04 |  30427.8  | 11891.7  |   0 |  1704.42   |   0 |   0 |   332.732  |  16499     |  2029 |
| WYOMING      |  3435.97 |  13074.4  |  5840.14 |   0 |   507.659  |   0 |   0 |   181.087  |   6545.53  |   970 |
| YATES        |  2154.46 |  14066.4  |  5231.37 |   0 |   338.775  |   0 |   0 |   115.92   |   8380.31  |   731 |



---

## Arithmetic-Relationship__case_28

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|     A |   B |   C |   D |   E |   F |   G |   H |
|------:|----:|----:|----:|----:|----:|----:|----:|
| 42443 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42444 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42446 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42447 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42448 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42449 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42450 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42451 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42453 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42454 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42455 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42456 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42457 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42458 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42460 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42461 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42462 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42463 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42464 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42465 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42467 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42468 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42469 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42470 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42471 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42472 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42474 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42475 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42476 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42477 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42478 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42479 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42481 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42482 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42483 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42484 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42485 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42486 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42488 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42489 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42490 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42491 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42492 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42493 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42495 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42496 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42497 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42498 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42499 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42500 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42502 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42503 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42504 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42505 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42506 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42507 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42509 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42510 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42511 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42512 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42513 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42514 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42516 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42517 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42518 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42519 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42520 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42521 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42523 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42524 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42525 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42526 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |
| 42527 |   0 |   5 |  50 |  90 |   0 | 500 |   0 |



---

## Arithmetic-Relationship__case_105

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
| J   | K   | L   |    M |    N |    O | P         | Q          |
|:----|:----|:----|-----:|-----:|-----:|:----------|:-----------|
| E   | M   | U   | 1889 | 1890 |    1 | 1/1/1889  | 12/31/1890 |
| E   | M   | U   | 1889 | 1890 |    1 | 1/1/1889  | 12/31/1890 |
| E   | M   | U   | 1891 | 1892 |    1 | 1/1/1891  | 12/31/1892 |
| E   | M   | U   | 1891 | 1892 |    1 | 1/1/1891  | 12/31/1892 |
| E   | M   | U   | 1893 | 1894 |    1 | 1/1/1893  | 12/31/1894 |
| E   | M   | U   | 1893 | 1894 |    1 | 1/1/1893  | 12/31/1894 |
| E   | M   | U   | 1893 | 1894 |    1 | 1/1/1893  | 12/31/1894 |
| E   | M   | U   | 1895 | 1896 |    1 | 1/1/1895  | 12/31/1896 |
| E   | M   | U   | 1895 | 1896 |    1 | 1/1/1895  | 12/31/1896 |
| E   | M   | U   | 1895 | 1898 |    3 | 1/1/1895  | 12/31/1898 |
| E   | M   | U   | 1897 | 1898 |    1 | 1/1/1897  | 12/31/1898 |
| E   | M   | U   | 1897 | 1900 |    3 | 1/1/1897  | 12/31/1900 |
| E   | M   | U   | 1899 | 1900 |    1 | 1/1/1899  | 12/31/1900 |
| E   | M   | U   | 1899 | 1900 |    1 | 1/1/1899  | 12/31/1900 |
| E   | M   | U   | 1901 | 1902 |    1 | 1/1/1901  | 12/31/1902 |
| E   | M   | U   | 1901 | 1904 |    3 | 1/1/1901  | 12/31/1904 |
| E   | M   | U   | 1901 | 1904 |    3 | 1/1/1901  | 12/31/1904 |
| E   | M   | U   | 1903 | 1904 |    1 | 1/1/1903  | 12/31/1904 |
| E   | M   | U   | 1905 | 1906 |    1 | 1/1/1905  | 12/31/1906 |
| E   | M   | U   | 1905 | 1908 |    3 | 1/1/1905  | 12/31/1908 |
| E   | M   | U   | 1905 | 1908 |    3 | 1/1/1905  | 12/31/1908 |
| E   | M   | U   | 1907 | 1908 |    1 | 1/1/1907  | 12/31/1908 |
| E   | M   | U   | 1909 | 1916 |    7 | 1/1/1909  | 12/31/1916 |
| E   | M   | U   | 1909 | 1916 |    7 | 1/1/1909  | 12/31/1916 |
| E   | M   | U   | 1909 | 1916 |    7 | 1/1/1909  | 12/31/1916 |
| E   | M   | U   | 1917 | 1918 |    1 | 1/1/1917  | 12/31/1918 |
| E   | M   | U   | 1917 | 1918 |    1 | 1/1/1917  | 12/31/1918 |
| E   | M   | U   | 1917 | 1920 |    3 | 1/1/1917  | 12/31/1920 |
| E   | M   | U   | 1919 | 1920 |    1 | 1/1/1919  | 12/31/1920 |
| E   | M   | U   | 1919 | 1932 |   13 | 1/1/1919  | 12/31/1932 |
| E   | M   | U   | 1921 | 1922 |    1 | 1/1/1921  | 12/31/1922 |
| E   | M   | U   | 1921 | 1936 |   15 | 1/1/1921  | 12/31/1936 |
| E   | M   | U   | 1923 | 1934 |   11 | 1/1/1923  | 12/31/1934 |
| E   | M   | U   | 1928 | 1949 |   21 | 1/1/1928  | 12/31/1949 |
| E   | M   | U   | 1935 | 1940 |    5 | 1/1/1935  | 12/31/1940 |
| E   | M   | U   | 1937 | 1948 |   11 | 1/1/1937  | 12/31/1948 |
| E   | M   | U   | 1940 | 1950 |   10 | 1/1/1940  | 12/31/1950 |
| E   | M   | U   | 1949 | 1954 |    5 | 1/1/1949  | 12/31/1954 |
| E   | M   | U   | 1949 | 1961 |   12 | 1/1/1949  | 12/31/1961 |
| E   | M   | U   | 1951 | 1954 |    3 | 1/1/1951  | 12/31/1954 |
| E   | M   | U   | 1954 | 1962 |    8 | 1/1/1954  | 12/31/1962 |
| E   | M   | U   | 1955 | 1960 |    5 | 1/1/1955  | 12/31/1960 |
| E   | M   | U   | 1961 | 1966 |    5 | 1/1/1961  | 12/31/1966 |
| E   | M   | D   | 1961 | 2000 |   39 | 9/19/1961 | 12/2000    |
| E   | M   | R   | 1963 | 1980 |   17 | 1/1/1963  | 12/31/1980 |
| E   | M   | R   | 1967 | 1983 |   16 | 1/1/1967  | 12/31/1983 |
| E   | M   | R   | 1981 | 2003 |   22 | 1/2/1981  | 7/2003     |
| E   | M   | R   | 1983 | 1992 |    9 | 5/5/1983  | 12/1991    |
| E   | F   | R   | 1993 | 2008 |   15 | 1/1993    | 12/2008    |
| E   | M   | R   | 2001 | 2012 |   11 | 1/1/2001  | 41090      |
| E   | M   | R   | 2003 | 2012 |    9 | 8/1/2003  | 41274      |
| E   | M   | R   | 2009 | 2017 |    8 | 1/1/2009  | 42736      |
| E   | F   | R   | 2013 | 9999 | 7986 | 1/2/2013  | 9999       |
| E   | M   | R   | 2013 | 9999 | 7986 | 1/1/2013  | 9999       |
| E   | M   | R   | 2017 | 9999 | 7982 | 42738     | 9999       |



---

## Arithmetic-Relationship__case_210

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|   A |   B |          C |          D |          E |
|----:|----:|-----------:|-----------:|-----------:|
|  29 | 890 | 557.516    |  332.484   |  2.54721   |
|  18 | 176 | 497.061    | -321.061   | -2.4597    |
|  52 | 814 | 517.523    |  296.477   |  2.27136   |
|  40 | 817 | 529.614    |  287.386   |  2.20171   |
|  41 | 200 | 481.25     | -281.25    | -2.1547    |
|  49 | 130 | 404.984    | -274.984   | -2.1067    |
|  44 | 751 | 488.69     |  262.31    |  2.0096    |
|  32 | 775 | 540.775    |  234.225   |  1.79444   |
|  33 | 236 | 470.089    | -234.089   | -1.79339   |
|  48 | 741 | 561.236    |  179.764   |  1.3772    |
|  37 | 335 | 470.089    | -135.089   | -1.03494   |
|  13 | 404 | 522.173    | -118.173   | -0.905343  |
|  14 | 380 | 484.97     | -104.97    | -0.804193  |
|  51 | 493 | 578.908    |  -85.9075  | -0.658151  |
|  38 |  75 |   0.402269 |   74.5977  |  0.571505  |
|  17 | 456 | 522.173    |  -66.1731  | -0.506962  |
|  43 | 460 | 524.033    |  -64.0332  | -0.490569  |
|  50 |  69 |   5.05263  |   63.9474  |  0.489911  |
|  46 |  80 |  18.0737   |   61.9263  |  0.474428  |
|   1 | 439 | 500.781    |  -61.7814  | -0.473317  |
|  39 | 461 | 403.124    |   57.8762  |  0.443399  |
|  30 | 371 | 427.306    |  -56.3057  | -0.431367  |
|  35 |  63 | 117.591    |  -54.5914  | -0.418234  |
|  45 |  70 |  16.2135   |   53.7865  |  0.412067  |
|  27 | 116 |  68.2976   |   47.7024  |  0.365456  |
|  31 | 557 | 515.663    |   41.3374  |  0.316693  |
|  36 | 469 | 504.502    |  -35.5017  | -0.271984  |
|  42 |  32 |  -1.45788  |   33.4579  |  0.256326  |
|   7 |  47 |  77.5983   |  -30.5983  | -0.234419  |
|  23 |  41 |  69.2277   |  -28.2277  | -0.216257  |
|  16 |  40 |  66.4374   |  -26.4374  | -0.202541  |
|   4 |  52 |  77.5983   |  -25.5983  | -0.196113  |
|  34 |  43 |  68.2976   |  -25.2976  | -0.193809  |
|  24 |  47 |  68.2976   |  -21.2976  | -0.163164  |
|   2 |  98 |  77.5983   |   20.4017  |  0.156301  |
|  20 |  91 |  71.0878   |   19.9122  |  0.152551  |
|  26 |  85 |  68.2976   |   16.7024  |  0.12796   |
|  25 |  84 |  68.2976   |   15.7024  |  0.120299  |
|  22 |  83 |  67.3675   |   15.6325  |  0.119763  |
|   8 |  85 |  70.1577   |   14.8423  |  0.113709  |
|  28 | 544 | 529.614    |   14.3864  |  0.110216  |
|  12 |  54 |  68.2976   |  -14.2976  | -0.109536  |
|   5 |  64 |  77.5983   |  -13.5983  | -0.104179  |
|  11 |  57 |  68.2976   |  -11.2976  | -0.0865526 |
|  47 | 523 | 532.404    |   -9.40387 | -0.0720445 |
|   9 |  59 |  68.2976   |   -9.29758 | -0.0712302 |
|  21 |  59 |  67.3675   |   -8.36751 | -0.0641048 |
|   3 |  70 |  77.5983   |   -7.59831 | -0.0582118 |
|  19 |  61 |  67.3675   |   -6.36751 | -0.0487825 |
|   6 |  72 |  77.5983   |   -5.59831 | -0.0428895 |
|  10 |  63 |  68.2976   |   -5.29758 | -0.0405856 |
|  15 |  65 |  67.3675   |   -2.36751 | -0.0181378 |



---

## Arithmetic-Relationship__case_228

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|     A |   B |   C |   D |   E |   F |   G |   H |
|------:|----:|----:|----:|----:|----:|----:|----:|
| 44445 |   0 |   0 |   0 |   1 |   0 |   0 |   1 |
| 44446 |   0 |   0 |   0 |   1 |   0 |   0 |   1 |
| 44449 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44451 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44452 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44453 |   3 |   0 |   0 |   0 |   0 |   0 |   3 |
| 44454 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44456 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44457 |   1 |   0 |   0 |   0 |   0 |   0 |   1 |
| 44458 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44459 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44463 |   0 |   0 |   0 |   1 |   0 |   0 |   1 |
| 44465 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44466 |   0 |   0 |   0 |   1 |   0 |   0 |   1 |
| 44469 |   1 |   0 |   0 |   0 |   0 |   0 |   1 |
| 44470 |   1 |   0 |   0 |   0 |   0 |   0 |   1 |
| 44471 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44472 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44474 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44475 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44477 |   1 |   0 |   0 |   0 |   0 |   0 |   1 |
| 44478 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44479 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44480 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44482 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44484 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44485 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44486 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44487 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44488 |   2 |   0 |   0 |   0 |   0 |   0 |   2 |
| 44489 |   1 |   0 |   0 |   0 |   0 |   0 |   1 |
| 44490 |   2 |   0 |   0 |   0 |   0 |   0 |   2 |
| 44491 |   2 |   0 |   0 |   0 |   0 |   0 |   2 |
| 44492 |   2 |   0 |   0 |   0 |   0 |   0 |   2 |
| 44494 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44496 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44497 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44498 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44499 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44500 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44501 |   0 |   0 |   0 |   4 |   0 |   0 |   4 |
| 44503 |   1 |   0 |   0 |   0 |   0 |   0 |   1 |
| 44506 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |
| 44507 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |



---

## Arithmetic-Relationship__case_526

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|     A |    B |    C |    D |    E |    F |   G |    H |   I |   J |   K |     L |    M |    N |    O |
|------:|-----:|-----:|-----:|-----:|-----:|----:|-----:|----:|----:|----:|------:|-----:|-----:|-----:|
| 40551 | 2260 | 2368 | 1354 | 5982 | 1514 | 151 | 1665 |   4 | 162 | 166 |  7813 | 3910 |  465 | 4375 |
| 40558 | 3309 | 3049 | 1424 | 7782 | 1544 | 228 | 1772 |   1 |  75 |  76 |  9630 | 3818 |  929 | 4747 |
| 40565 | 3539 | 2996 | 1353 | 7888 | 2055 | 378 | 2433 |  10 | 152 | 162 | 10483 | 3975 |  917 | 4892 |
| 40572 | 4011 | 3002 | 1253 | 8266 | 1634 | 319 | 1953 |   5 | 123 | 128 | 10347 | 3518 | 1056 | 4574 |
| 40579 | 3253 | 3208 | 1431 | 7892 | 1848 | 214 | 2062 |   8 | 134 | 142 | 10096 | 3476 |  543 | 4019 |
| 40586 | 3143 | 3057 | 1275 | 7475 | 1802 | 239 | 2041 |   0 | 100 | 100 |  9616 | 3610 |  733 | 4343 |
| 40593 | 3624 | 3081 | 1332 | 8037 | 1716 | 170 | 1886 |   2 |  99 | 101 | 10024 | 3341 |  478 | 3819 |
| 40600 | 3530 | 3130 | 1541 | 8201 | 1741 | 140 | 1881 |   0 | 125 | 125 | 10207 | 3181 |  529 | 3710 |
| 40607 | 3506 | 3104 | 1234 | 7844 | 1602 | 190 | 1792 |   5 | 110 | 115 |  9751 | 3082 |  596 | 3678 |
| 40614 | 3483 | 2740 | 1315 | 7538 | 1590 | 295 | 1885 |   1 | 113 | 114 |  9537 | 3080 |  434 | 3514 |
| 40621 | 2832 | 2679 | 1174 | 6685 | 1298 | 177 | 1475 |   6 | 118 | 124 |  8284 | 3288 |  361 | 3649 |
| 40628 | 3373 | 2855 | 1353 | 7581 | 1562 | 146 | 1708 |   6 |  94 | 100 |  9389 | 2841 |  420 | 3261 |
| 40635 | 2940 | 2787 | 1276 | 7003 | 1048 | 123 | 1171 |   6 | 117 | 123 |  8297 | 2927 |  684 | 3611 |
| 40642 | 3152 | 2707 | 1074 | 6933 | 1448 | 156 | 1604 |   1 |  72 |  73 |  8610 | 3137 |  643 | 3780 |
| 40649 | 3121 | 2545 | 1220 | 6886 | 1098 | 149 | 1247 |   0 | 106 | 106 |  8239 | 3215 |  668 | 3883 |
| 40656 | 3000 | 2608 | 1020 | 6628 | 1329 | 132 | 1461 |   1 | 120 | 121 |  8210 | 3087 |  316 | 3403 |
| 40663 | 2396 | 2020 |  904 | 5320 |  870 |  81 |  951 |   1 |  98 |  99 |  6370 | 2870 |  665 | 3535 |
| 40670 | 2860 | 2208 | 1178 | 6246 | 1318 | 144 | 1462 |   1 |  79 |  80 |  7788 | 2953 |  648 | 3601 |
| 40677 | 2959 | 2654 | 1511 | 7124 | 1179 | 172 | 1351 |   2 |  50 |  52 |  8527 | 3231 |  874 | 4105 |
| 40684 | 2730 | 2626 | 1359 | 6715 | 1557 | 218 | 1775 |   0 |  87 |  87 |  8577 | 4105 |  819 | 4924 |
| 40691 | 2990 | 2469 | 1613 | 7072 | 1208 | 143 | 1351 |   8 |  76 |  84 |  8507 | 4466 |  567 | 5033 |
| 40698 | 2702 | 2229 | 1408 | 6339 | 1914 | 175 | 2089 |   1 |  73 |  74 |  8502 | 5111 |  578 | 5689 |
| 40705 | 2667 | 2207 | 1542 | 6416 | 1505 | 204 | 1709 |   1 |  62 |  63 |  8188 | 4670 |  408 | 5078 |
| 40712 | 2585 | 2149 | 1190 | 5924 | 2267 | 228 | 2495 |   2 |  61 |  63 |  8482 | 5018 |  697 | 5715 |
| 40719 | 2973 | 2071 | 1394 | 6438 | 1602 | 138 | 1740 |   1 | 106 | 107 |  8285 | 5038 |  368 | 5406 |
| 40726 | 2247 | 2031 | 1474 | 5752 | 2146 | 174 | 2320 |   0 | 114 | 114 |  8186 | 6032 |  555 | 6587 |
| 40733 | 2210 | 1976 | 1038 | 5224 | 1728 | 128 | 1856 |   1 |  76 |  77 |  7157 | 5584 |  594 | 6178 |
| 40740 | 1459 |  952 |  705 | 3116 |  935 | 131 | 1066 |   5 |  96 | 101 |  4283 | 3473 |  345 | 3818 |
| 40747 | 1846 | 1574 |  833 | 4253 | 1628 | 132 | 1760 |   8 |  68 |  76 |  6089 | 6657 |  668 | 7325 |
| 40754 | 2102 | 1761 |  934 | 4797 | 1774 | 154 | 1928 |   0 |  87 |  87 |  6812 | 5582 |  974 | 6556 |
| 40761 | 2213 | 1885 | 1030 | 5128 | 1845 | 158 | 2003 |   1 | 123 | 124 |  7255 | 6626 |  991 | 7617 |
| 40768 | 2981 | 2013 |  897 | 5891 | 1760 | 139 | 1899 |   3 | 101 | 104 |  7894 | 6436 |  981 | 7417 |
| 40775 | 3413 | 1893 | 1061 | 6367 | 1671 | 216 | 1887 |  10 |  66 |  76 |  8330 | 6272 | 1050 | 7322 |
| 40782 | 3523 | 2328 |  988 | 6839 | 1874 | 112 | 1986 |   5 |  93 |  98 |  8923 | 6129 |  957 | 7086 |
| 40789 | 3616 | 1978 |  864 | 6458 | 1589 |  95 | 1684 |   2 | 124 | 126 |  8268 | 6346 |  876 | 7222 |
| 40796 | 3842 | 2471 |  840 | 7153 | 1866 | 103 | 1969 |   0 | 109 | 109 |  9231 | 8118 | 1017 | 9135 |
| 40803 | 4008 | 2347 |  923 | 7278 | 1847 | 135 | 1982 |   0 | 140 | 140 |  9400 | 7574 | 1146 | 8720 |
| 40810 | 4530 | 2253 |  976 | 7759 | 1893 | 100 | 1993 |   2 | 129 | 131 |  9883 | 7178 | 1116 | 8294 |
| 40817 | 4142 | 2283 | 1182 | 7607 | 1952 | 115 | 2067 |  11 | 150 | 161 |  9835 | 7282 | 1055 | 8337 |
| 40824 | 4554 | 2389 | 1004 | 7947 | 1851 | 151 | 2002 |   4 | 143 | 147 | 10096 | 6847 | 1103 | 7950 |
| 40831 | 4005 | 2361 |  924 | 7290 | 2008 | 129 | 2137 |   8 | 128 | 136 |  9563 | 6687 |  917 | 7604 |
| 40838 | 4349 | 2422 |  939 | 7710 | 2331 | 142 | 2473 |   3 |  92 |  95 | 10278 | 6746 | 1167 | 7913 |
| 40845 | 3920 | 2157 |  926 | 7003 | 2717 | 129 | 2846 |   0 | 137 | 137 |  9986 | 6430 |  805 | 7235 |
| 40852 | 3215 | 2023 |  971 | 6209 | 2619 | 149 | 2768 |   0 | 133 | 133 |  9110 | 6895 |  590 | 7485 |
| 40859 | 2942 | 2288 |  814 | 6044 | 2323 | 125 | 2448 |   1 | 137 | 138 |  8630 | 7335 |  834 | 8169 |
| 40866 | 3034 | 2428 | 1211 | 6673 | 2260 | 122 | 2382 |   4 | 117 | 121 |  9176 | 5549 | 1091 | 6640 |
| 40873 | 3381 | 2471 | 1016 | 6868 | 2286 | 117 | 2403 |   5 | 129 | 134 |  9405 | 5910 |  933 | 6843 |
| 40880 | 3552 | 2920 | 1300 | 7772 | 1697 | 136 | 1833 |   1 | 162 | 163 |  9768 | 6261 |  890 | 7151 |
| 40887 | 3531 | 2599 |  968 | 7098 | 2398 | 127 | 2525 |   2 |  76 |  78 |  9701 | 7069 |  495 | 7564 |
| 40894 | 2940 | 2460 |  907 | 6307 | 2302 | 133 | 2435 |   3 | 162 | 165 |  8907 | 7273 |  816 | 8089 |
| 40901 | 2742 | 2311 |  978 | 6031 | 1850 | 124 | 1974 |  10 | 106 | 116 |  8121 | 5787 |  529 | 6316 |
| 40908 | 2072 | 1954 |  877 | 4903 |  599 |  83 |  682 |   1 |  84 |  85 |  5670 | 3880 |  604 | 4484 |



---

## Arithmetic-Relationship__case_648

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
| A                    |      B |      C |      D |      E |      F |    G |    H |   I |     J |     K |
|:---------------------|-------:|-------:|-------:|-------:|-------:|-----:|-----:|----:|------:|------:|
| Alabama              | 101160 |  30363 |  29472 |  57245 |  54462 |  488 |  475 | -13 | 0.398 | 0.412 |
| Alaska               |  19358 |   3423 |   3104 |   5606 |   5260 |  244 |  230 | -14 | 0.59  | 0.598 |
| Arizona              | 149942 |  40793 |  40860 |  72143 |  72533 |  362 |  363 |   1 | 0.573 | 0.594 |
| Arkansas             |  65955 |  27794 |  27724 |  48193 |  47899 |  609 |  605 |  -4 | 0.357 | 0.371 |
| California           | 932046 | 421141 | 423174 | 794126 | 793695 |  694 |  694 |   0 | 0.59  | 0.601 |
| Colorado             | 133570 |  53220 |  53755 |  89675 |  91101 |  524 |  521 |  -3 | 0.612 | 0.614 |
| Connecticut          |  78812 |  37105 |  37469 |  69640 |  70423 |  768 |  778 |  10 | 0.694 | 0.692 |
| Delaware             |  18767 |   7416 |   7586 |  13307 |  13361 |  583 |  570 | -13 | 0.597 | 0.576 |
| District of Columbia |   7790 |   6574 |   6642 |  12302 |  12532 | 1285 | 1295 |  10 | 0.548 | 0.56  |
| Florida              | 392503 | 219770 | 217393 | 398873 | 394624 |  702 |  694 |  -8 | 0.526 | 0.545 |
| Georgia              | 230751 |  99169 |  96311 | 178201 | 175394 |  551 |  539 | -12 | 0.603 | 0.616 |
| Hawaii               |  22390 |   9903 |   9887 |  15829 |  16022 |  627 |  631 |   4 | 0.536 | 0.542 |
| Idaho                |  43460 |   8158 |   8528 |  14038 |  13984 |  279 |  264 | -15 | 0.589 | 0.595 |
| Illinois             | 260843 | 125609 | 128748 | 231728 | 234674 |  705 |  718 |  13 | 0.644 | 0.637 |
| Indiana              | 148643 |  51814 |  52065 |  88225 |  88555 |  496 |  498 |   2 | 0.521 | 0.523 |
| Iowa                 |  72437 |  13591 |  13658 |  20986 |  21111 |  223 |  219 |  -4 | 0.62  | 0.604 |
| Kansas               |  67706 |  10112 |  10147 |  16314 |  16378 |  200 |  199 |  -1 | 0.653 | 0.66  |
| Kentucky             |  93800 |  35094 |  33849 |  57408 |  54791 |  423 |  397 | -26 | 0.522 | 0.529 |
| Louisiana            |  95249 |  24230 |  25295 |  35675 |  37544 |  270 |  274 |   4 | 0.441 | 0.421 |
| Maine                |  25512 |   8472 |   8640 |  15021 |  15056 |  528 |  525 |  -3 | 0.567 | 0.571 |
| Maryland             | 118348 |  67535 |  66428 | 127155 | 123872 |  835 |  799 | -36 | 0.657 | 0.671 |
| Massachusetts        | 137778 |  66467 |  66820 | 124064 | 125437 |  807 |  821 |  14 | 0.676 | 0.687 |
| Michigan             | 225379 |  66130 |  65327 | 110345 | 110149 |  401 |  405 |   4 | 0.641 | 0.644 |
| Minnesota            | 137584 |  45958 |  45656 |  75185 |  74291 |  394 |  382 | -12 | 0.664 | 0.661 |
| Mississippi          |  60616 |  10712 |  10562 |  16087 |  15882 |  214 |  210 |  -4 | 0.352 | 0.368 |
| Missouri             | 128353 |  27630 |  28380 |  45896 |  47277 |  294 |  303 |   9 | 0.631 | 0.634 |
| Montana              |  20242 |   3500 |   3698 |   5599 |   5706 |  244 |  235 |  -9 | 0.631 | 0.654 |
| Nebraska             |  48128 |   8888 |   9251 |  15240 |  15506 |  256 |  252 |  -4 | 0.563 | 0.573 |
| Nevada               |  65332 |  21780 |  22324 |  39112 |  39223 |  491 |  474 | -17 | 0.501 | 0.516 |
| New Hampshire        |  26473 |   7681 |   7646 |  12800 |  12697 |  420 |  418 |  -2 | 0.685 | 0.695 |
| New Jersey           | 189023 |  79033 |  80788 | 154215 | 159398 |  723 |  751 |  28 | 0.693 | 0.692 |
| New Mexico           |  40627 |  10612 |  10881 |  17292 |  17430 |  348 |  346 |  -2 | 0.394 | 0.392 |
| New York             | 367645 | 173644 | 179974 | 309055 | 319337 |  695 |  716 |  21 | 0.619 | 0.613 |
| North Carolina       | 217763 |  83378 |  82148 | 157532 | 152602 |  586 |  559 | -27 | 0.553 | 0.564 |
| North Dakota         |  15688 |   2937 |   3274 |   4595 |   5053 |  261 |  269 |   8 | 0.561 | 0.563 |
| Ohio                 | 230386 |  73282 |  72745 | 129177 | 128221 |  461 |  463 |   2 | 0.648 | 0.655 |
| Oklahoma             |  84319 |  19224 |  18025 |  33222 |  30559 |  320 |  295 | -25 | 0.452 | 0.477 |
| Oregon               |  86574 |  21121 |  21557 |  34989 |  35521 |  314 |  317 |   3 | 0.598 | 0.602 |
| Pennsylvania         | 241806 |  77232 |  77481 | 139358 | 138647 |  491 |  487 |  -4 | 0.669 | 0.678 |
| Rhode Island         |  20571 |   7878 |   8159 |  14342 |  14896 |  639 |  654 |  15 | 0.555 | 0.562 |
| South Carolina       |  97755 |  35286 |  34952 |  57332 |  57895 |  431 |  430 |  -1 | 0.593 | 0.593 |
| South Dakota         |  17488 |   2861 |   2932 |   4771 |   4895 |  234 |  226 |  -8 | 0.673 | 0.682 |
| Tennessee            | 146100 |  38742 |  40161 |  66389 |  68620 |  350 |  359 |   9 | 0.565 | 0.565 |
| Texas                | 679131 | 318150 | 325088 | 594643 | 598008 |  650 |  636 | -14 | 0.482 | 0.489 |
| Utah                 |  88511 |  28304 |  29679 |  43569 |  45542 |  355 |  357 |   2 | 0.684 | 0.674 |
| Vermont              |  10492 |   3739 |   3800 |   6431 |   6555 |  557 |  565 |   8 | 0.659 | 0.665 |
| Virginia             | 184377 |  79597 |  79554 | 158833 | 159084 |  707 |  703 |  -4 | 0.658 | 0.653 |
| Washington           | 170527 |  54195 |  53517 |  93123 |  92346 |  399 |  386 | -13 | 0.628 | 0.634 |
| West Virginia        |  36118 |   7970 |   8054 |  13110 |  12895 |  300 |  293 |  -7 | 0.46  | 0.45  |
| Wisconsin            | 128493 |  48066 |  47624 |  81735 |  79817 |  523 |  511 | -12 | 0.667 | 0.665 |
| Wyoming              |  12936 |   2197 |   2242 |   3341 |   3387 |  219 |  214 |  -5 | 0.556 | 0.548 |



---

## Arithmetic-Relationship__case_871

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
|   A |   B |   C |   D |   E |     F |     G |     H |         I |
|----:|----:|----:|----:|----:|------:|------:|------:|----------:|
|   1 |   1 |   1 |   5 |   1 |  2200 | 10000 | 12200 | 10000     |
|   2 |   2 |   1 |   5 |   2 |  2200 | 10000 | 12200 |  5000     |
|   3 |   3 |   1 |   5 |   3 |  2200 | 10000 | 12200 |  3333.33  |
|   4 |   4 |   1 |   5 |   4 |  2200 | 10000 | 12200 |  2500     |
|   5 |   5 |   1 |   5 |   5 |  2200 | 10000 | 12200 |  2000     |
|   6 |   6 |   2 |   8 |   6 |  4400 | 16000 | 20400 |  2666.67  |
|   7 |   7 |   2 |   8 |   7 |  4400 | 16000 | 20400 |  2285.71  |
|   8 |   8 |   2 |   8 |   8 |  4400 | 16000 | 20400 |  2000     |
|   9 |   9 |   2 |   8 |   9 |  4400 | 16000 | 20400 |  1777.78  |
|  10 |  10 |   2 |   8 |  10 |  4400 | 16000 | 20400 |  1600     |
|  11 |  11 |   3 |   8 |  11 |  6600 | 16000 | 22600 |  1454.55  |
|  12 |  12 |   3 |   8 |  12 |  6600 | 16000 | 22600 |  1333.33  |
|  13 |  13 |   3 |   8 |  13 |  6600 | 16000 | 22600 |  1230.77  |
|  14 |  14 |   3 |   8 |  14 |  6600 | 16000 | 22600 |  1142.86  |
|  15 |  15 |   3 |   8 |  15 |  6600 | 16000 | 22600 |  1066.67  |
|  16 |  16 |   4 |   8 |  16 |  8800 | 16000 | 24800 |  1000     |
|  17 |  17 |   4 |   8 |  17 |  8800 | 16000 | 24800 |   941.176 |
|  18 |  18 |   4 |   8 |  18 |  8800 | 16000 | 24800 |   888.889 |
|  19 |  19 |   4 |   8 |  19 |  8800 | 16000 | 24800 |   842.105 |
|  20 |  20 |   4 |   8 |  20 |  8800 | 16000 | 24800 |   800     |
|  21 |  21 |   5 |   8 |  21 | 11000 | 16000 | 27000 |   761.905 |
|  22 |  22 |   5 |   8 |  22 | 11000 | 16000 | 27000 |   727.273 |
|  23 |  23 |   5 |   8 |  23 | 11000 | 16000 | 27000 |   695.652 |
|  24 |  24 |   5 |   8 |  24 | 11000 | 16000 | 27000 |   666.667 |
|  25 |  25 |   5 |   8 |  25 | 11000 | 16000 | 27000 |   640     |
|  26 |  26 |   6 |   8 |  26 | 13200 | 16000 | 29200 |   615.385 |
|  27 |  27 |   6 |   8 |  27 | 13200 | 16000 | 29200 |   592.593 |
|  28 |  28 |   6 |   8 |  28 | 13200 | 16000 | 29200 |   571.429 |
|  29 |  29 |   6 |   8 |  29 | 13200 | 16000 | 29200 |   551.724 |
|  30 |  30 |   6 |   8 |  30 | 13200 | 16000 | 29200 |   533.333 |
|  31 |  31 |   7 |   8 |  31 | 15400 | 16000 | 31400 |   516.129 |
|  32 |  32 |   7 |   8 |  32 | 15400 | 16000 | 31400 |   500     |
|  33 |  33 |   7 |   8 |  33 | 15400 | 16000 | 31400 |   484.848 |
|  34 |  34 |   7 |   8 |  34 | 15400 | 16000 | 31400 |   470.588 |
|  35 |  35 |   7 |   8 |  35 | 15400 | 16000 | 31400 |   457.143 |
|  36 |  36 |   8 |   8 |  36 | 17600 | 16000 | 33600 |   444.444 |
|  37 |  37 |   8 |   8 |  37 | 17600 | 16000 | 33600 |   432.432 |
|  38 |  38 |   8 |   8 |  38 | 17600 | 16000 | 33600 |   421.053 |
|  39 |  39 |   8 |   8 |  39 | 17600 | 16000 | 33600 |   410.256 |
|  40 |  40 |   8 |   8 |  40 | 17600 | 16000 | 33600 |   400     |
|  41 |  41 |   9 |   8 |  41 | 19800 | 16000 | 35800 |   390.244 |
|  42 |  42 |   9 |   8 |  42 | 19800 | 16000 | 35800 |   380.952 |
|  43 |  43 |   9 |   8 |  43 | 19800 | 16000 | 35800 |   372.093 |
|  44 |  44 |   9 |   8 |  44 | 19800 | 16000 | 35800 |   363.636 |
|  45 |  45 |   9 |   8 |  45 | 19800 | 16000 | 35800 |   355.556 |
|  46 |  46 |  10 |   8 |  46 | 22000 | 16000 | 38000 |   347.826 |
|  47 |  47 |  10 |   8 |  47 | 22000 | 16000 | 38000 |   340.426 |
|  48 |  48 |  10 |   8 |  48 | 22000 | 16000 | 38000 |   333.333 |
|  49 |  49 |  10 |   9 |  49 | 22000 | 18000 | 40000 |   367.347 |
|  50 |  50 |  10 |   9 |  50 | 22000 | 18000 | 40000 |   360     |



---

## Arithmetic-Relationship__case_617

**Task:** Arithmetic-Relationship

**Input:**

You are given a table with numerical values in multiple columns. Your task is to analyze the data and identify semantic relationships, expressed in arithmetic relationships, that exist between columns.

These relationships may involve any combination of the following operations: addition (+), subtraction (−), multiplication (*), and division (/). The expressions can involve two or more columns and may be nested (e.g., B = (A + C) / D).

Please only identify arithmetic relationships that hold semantically based on the data, and do not return relationships that are likely spurious, e.g., (A = B * 0), where A is an all 0 column. Please only return minimal atomic relationships, e.g., if A = B + C and D = E + F, then there is no need to return A = B + C + E + F - D.

No explanation, return all the formula(s) in JSON format: {"Arithmetic-Relationship": [<list-of-formulas>]}. If no relationship is found, return {"Arithmetic-Relationship": []}.

Input Table:
| A                      |   B | C   |      D |        E |       F |
|:-----------------------|----:|:----|-------:|---------:|--------:|
| Alimony                |   0 | -   |   0    | 0        |    0    |
| Car Insurance          |   0 | -   |   0    | 0        |    0    |
| Car Payment            |   0 | -   | 115.2  | 0.229235 | -115.2  |
| Car Repair / Licenses  |   0 | -   |   0    | 0        |    0    |
| Car Replacement Fund   |   0 | -   |   0    | 0        |    0    |
| Charity                |   0 | -   |   0    | 0        |    0    |
| Child Care             |   0 | -   |   0    | 0        |    0    |
| Cleaning               |   0 | -   |   0    | 0        |    0    |
| Clothing               |   0 | -   |   0    | 0        |    0    |
| Debt                   |   0 | -   |   0    | 0        |    0    |
| Dining                 |   0 | -   |   0    | 0        |    0    |
| Discretionary          |   0 | -   |   0    | 0        |    0    |
| Doctor / Dentist       |   0 | -   |   0    | 0        |    0    |
| Education              |   0 | -   |   0    | 0        |    0    |
| Emergency Fund         |   0 | -   |   0    | 0        |    0    |
| Fuel                   |   0 | -   |   0    | 0        |    0    |
| Fun / Entertainment    |   0 | -   |   0    | 0        |    0    |
| Furniture / Appliances |   0 | -   |   0    | 0        |    0    |
| Gifts Given            |   0 | -   |   0    | 0        |    0    |
| Groceries              |   0 | -   |  87.34 | 0.173797 |  -87.34 |
| Health Insurance       |   0 | -   | 200    | 0.397978 | -200    |
| Home Insurance         |   0 | -   |   0    | 0        |    0    |
| Home Supplies          |   0 | -   |   0    | 0        |    0    |
| Interest Expense       |   0 | -   |   0    | 0        |    0    |
| Life Insurance         |   0 | -   |   0    | 0        |    0    |
| Medicine               |   0 | -   |   0    | 0        |    0    |
| Miscellaneous          |   0 | -   |   0    | 0        |    0    |
| Mortgage / Rent        |   0 | -   |   0    | 0        |    0    |
| Other Savings          |   0 | -   |   0    | 0        |    0    |
| Other_1                |   0 | -   |   0    | 0        |    0    |
| Other_2                |   0 | -   |   0    | 0        |    0    |
| Other_3                |   0 | -   |   0    | 0        |    0    |
| Other_4                |   0 | -   |   0    | 0        |    0    |
| Other_5                |   0 | -   |   0    | 0        |    0    |
| Personal Supplies      |   0 | -   |   0    | 0        |    0    |
| Retirement Fund        |   0 | -   |   0    | 0        |    0    |
| Subscriptions/Dues     |   0 | -   |   0    | 0        |    0    |
| Taxes                  |   0 | -   |   0    | 0        |    0    |
| Util. Electricity      |   0 | -   |   0    | 0        |    0    |
| Util. Gas              |   0 | -   | 100    | 0.198989 | -100    |
| Util. Phone(s)         |   0 | -   |   0    | 0        |    0    |
| Util. TV / Internet    |   0 | -   |   0    | 0        |    0    |
| Util. Water            |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |
| -                      |   0 | -   |   0    | 0        |    0    |



---

## Data-transform-reshape__multistep_test2

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Column1   |   Column2 |    2012 |    2013 | 2014               |
|:----------|----------:|--------:|--------:|:-------------------|
| Company 1 |         0 | 0       | 2.52    | 2.64               |
|           |         1 | 0       | 2.20667 | 2.0585714285714287 |
|           |         2 | 0       | 2.09413 | 2.3811069090909087 |
|           |         3 | 0       | 1.9075  | 2.0625             |
| Company 2 |         0 | 2.46667 | 2.54667 | 0.0                |
|           |         1 | 2.35    | 2.44    | 0.0                |
|           |         2 | 2.073   | 2.272   | 0.0                |
|           |         3 | 0       | 0       | 0.0                |
| Company 3 |         0 | 0       | 2.60833 | 3.155              |
|           |         1 | 0       | 2.308   | 2.4778333333333333 |
|           |         2 | 0       | 2.30389 | 2.54425            |
|           |         3 | 0       | 0       | 0.0                |
| Company 4 |         0 | 0       | 0       | 0.0                |
|           |         1 | 2.15    | 2.21    | 0.0                |
|           |         2 | 2.05    | 2.21    | 0.0                |
|           |         3 | 0       | 0       | 0.0                |
| Company 5 |         0 | 2.2     | 2.47    | 0.0                |
|           |         1 | 0       | 0       | 0.0                |
|           |         2 | 1.67    | 1.87    | 0.0                |
|           |         3 | 0       | 0       | 0.0                |
| Company 6 |         0 | 0       | 0       | 0.0                |
|           |         1 | 0       | 0       |                    |
|           |         2 | 0       | 1.84786 | 1.55               |
|           |         3 | 0       | 0       |                    |

## Output:


---

## Data-transform-reshape__wide_to_long_test8

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
|   ID | Category_1   |   Quantity_1 | Category_2   |   Quantity_2 | Category_3   |   Quantity_3 |
|-----:|:-------------|-------------:|:-------------|-------------:|:-------------|-------------:|
|    1 | kitchen      |           64 | Home         |           24 | Bath         |           45 |
|    2 | Bed          |           24 | Men          |           35 | Cosemestics  |           49 |
|    3 | Kids         |           22 | Kitchen      |           45 | Men          |           52 |

## Output:


---

## Data-transform-reshape__transpose_test27

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Unnamed: 0    | Rank     | Net worth   | Minimum assets   | Minimum liabilities   |
|:--------------|:---------|:------------|:-----------------|:----------------------|
| This year     | #120     | $2.19M      | $2.24M           | $0.05M                |
| Previous year | freshman |             |                  |                       |
| Change        |          | 0.00%       | 0.00%            | 0.00%                 |

## Output:


---

## Data-transform-reshape__stack_test53

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Tanakh (Jewish Bible) (24 books)    | Protestant Old Testament (39 books)   | Catholic Old Testament (46 books)                 | Eastern Orthodox Old Testament (51 books)   |
|:------------------------------------|:--------------------------------------|:--------------------------------------------------|:--------------------------------------------|
| Torah                               | Pentateuch or the Five Books of Moses | Pentateuch or the Five Books of Moses             | Pentateuch or the Five Books of Moses       |
| Bereishit                           | Genesis                               | Genesis                                           | Genesis                                     |
| Shemot                              | Exodus                                | Exodus                                            | Exodus                                      |
| Vayikra                             | Leviticus                             | Leviticus                                         | Leviticus                                   |
| Bamidbar                            | Numbers                               | Numbers                                           | Numbers                                     |
| Devarim                             | Deuteronomy                           | Deuteronomy                                       | Deuteronomy                                 |
| Nevi'im (Prophets)                  | Historical books                      | Historical books                                  | Historical books                            |
| Yehoshua                            | Joshua                                | Joshua (Josue)                                    | Joshua (Iesous)                             |
| Shofetim                            | Judges                                | Judges                                            | Judges                                      |
| Rut (Ruth)                          | Ruth                                  | Ruth                                              | Ruth                                        |
| Shemuel                             | 1 Samuel                              | 1 Samuel (1 Kings)                                | 1 Samuel (1 Kingdoms)                       |
| Shemuel                             | 2 Samuel                              | 2 Samuel (2 Kings)                                | 2 Samuel (2 Kingdoms)                       |
| Melakhim                            | 1 Kings                               | 1 Kings (3 Kings)                                 | 1 Kings (3 Kingdoms)                        |
| Melakhim                            | 2 Kings                               | 2 Kings (4 Kings)                                 | 2 Kings (4 Kingdoms)                        |
| Divrei Hayamim (Chronicles)         | 1 Chronicles                          | 1 Chronicles (1 Paralipomenon)                    | 1 Chronicles (1 Paralipomenon)              |
| Divrei Hayamim (Chronicles)         | 2 Chronicles                          | 2 Chronicles (2 Paralipomenon)                    | 2 Chronicles (2 Paralipomenon)              |
|                                     |                                       |                                                   | 1 Esdras                                    |
| Ezra-Nehemiah                       | Ezra                                  | Ezra (1 Esdras)                                   | Ezra (2 Esdras)                             |
| Ezra-Nehemiah                       | Nehemiah                              | Nehemiah (2 Esdras)                               | Nehemiah (2 Esdras)                         |
|                                     |                                       | Tobit (Tobias)                                    | Tobit (Tobias)                              |
|                                     |                                       | Judith                                            | Judith                                      |
| Esther                              | Esther                                | Esther                                            | Esther                                      |
|                                     |                                       | 1 Maccabees (1 Machabees)                         | 1 Maccabees                                 |
|                                     |                                       | 2 Maccabees (2 Machabees)                         | 2 Maccabees                                 |
|                                     |                                       |                                                   | 3 Maccabees                                 |
|                                     |                                       |                                                   | 4 Maccabees                                 |
| Ketuvim (Writings)                  | Wisdom books                          | Wisdom books                                      | Wisdom books                                |
| Iyov (Job)                          | Job                                   | Job                                               | Job                                         |
| Tehillim (Psalms)                   | Psalms                                | Psalms                                            | Psalms                                      |
|                                     |                                       |                                                   | Prayer of Manasseh                          |
| Mishlei (Proverbs)                  | Proverbs                              | Proverbs                                          | Proverbs                                    |
| Qoheleth (Ecclesiastes)             | Ecclesiastes                          | Ecclesiastes                                      | Ecclesiastes                                |
| Shir Hashirim (Song of Songs)       | Song of Solomon                       | Song of Songs (Canticle of Canticles)             | Song of Songs (Aisma Aismaton)              |
|                                     |                                       | Wisdom                                            | Wisdom                                      |
|                                     |                                       | Sirach (Ecclesiasticus)                           | Sirach                                      |
| Nevi'im (Latter Prophets)           | Major prophets                        | Major prophets                                    | Major prophets                              |
| Yeshayahu                           | Isaiah                                | Isaiah (Isaias)                                   | Isaiah                                      |
| Yirmeyahu                           | Jeremiah                              | Jeremiah (Jeremias)                               | Jeremiah                                    |
| Eikhah (Lamentations)               | Lamentations                          | Lamentations                                      | Lamentations                                |
|                                     |                                       | Baruch with Letter of Jeremiah as the 6th Chapter | Baruch                                      |
|                                     |                                       | Baruch with Letter of Jeremiah as the 6th Chapter | Letter of Jeremiah as standalone book       |
| Yekhezqel                           | Ezekiel                               | Ezekiel (Ezechiel)                                | Ezekiel                                     |
| Daniel                              | Daniel                                | Daniel                                            | Daniel                                      |
| The Twelve or Trei Asar             | Hosea                                 | Hosea (Osee)                                      | Hosea                                       |
| The Twelve or Trei Asar             | Joel                                  | Joel                                              | Joel                                        |
| The Twelve or Trei Asar             | Amos                                  | Amos                                              | Amos                                        |
| The Twelve or Trei Asar             | Obadiah                               | Obadiah (Abdias)                                  | Obadiah                                     |
| The Twelve or Trei Asar             | Jonah                                 | Jonah (Jonas)                                     | Jonah                                       |
| The Twelve or Trei Asar             | Micah                                 | Micah (Micheas)                                   | Micah                                       |
| The Twelve or Trei Asar             | Nahum                                 | Nahum                                             | Nahum                                       |
| The Twelve or Trei Asar             | Habakkuk                              | Habakkuk (Habacuc)                                | Habakkuk                                    |
| The Twelve or Trei Asar             | Zephaniah                             | Zephaniah (Sophonias)                             | Zephaniah                                   |
| The Twelve or Trei Asar             | Haggai                                | Haggai (Aggeus)                                   | Haggai                                      |
| The Twelve or Trei Asar             | Zechariah                             | Zechariah (Zacharias)                             | Zechariah                                   |
| The Twelve or Trei Asar             | Malachi                               | Malachi (Malachias)                               | Malachi                                     |

## Output:


---

## Data-transform-reshape__pivot_test1

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Address   | 123 ABC St   |
|:----------|:-------------|
| Phone     | 555-555555   |
| Age       | 55           |
| Address   | 456 DEF St   |
| Phone     | 123-4567890  |
| Age       | 33           |
| Address   | 789 OPQ St   |
| Phone     | 666-666666   |
| Age       | 66           |
| Address   | 012 XYZ St   |
| Phone     | 777-777777   |
| Age       | 88           |
| Address   | 342 BCD St   |
| Phone     | 888-888888   |
| Age       | 56           |
| Address   | 367 CDE St   |
| Phone     | 999-999999   |
| Age       | 58           |
| Address   | 783 EFG St   |
| Phone     | 123-789362   |
| Age       | 62           |
| Address   | 467 UGF St   |
| Phone     | 234-123123   |
| Age       | 33           |
| Address   | 783 BSL St   |
| Phone     | 456-142342   |
| Age       | 44           |

## Output:


---

## Data-transform-reshape__subtitle_test17

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
|                                                 | Essentials   | Enterprise   |
|:------------------------------------------------|:-------------|:-------------|
| I) User Interface                               |              |              |
| Web-based Interface                             | 0.0          | 0.0          |
| Multilingual, Arabic, English & French Support  | 0.0          | 0.0          |
| User Customizable Localisation                  | 0.0          | 0.0          |
| Basic Dashboards                                | 0.0          | 0.0          |
| User-defined Dashboards                         |              | 0.0          |
| II) Functional Features                         |              |              |
| Multiple Companies Support                      |              | 0.0          |
| Multiple Branches Support                       | 0.0          | 0.0          |
| Multiple Currencies Support                     |              | 0.0          |
| III) Reporting                                  |              |              |
| Grouping Data                                   | 0.0          | 0.0          |
| Filtering Data                                  | 0.0          | 0.0          |
| Pivoting                                        |              | 0.0          |
| Data Visualization (User-defined Charts)        | 0.0          | 0.0          |
| Show/Hide Columns                               | 0.0          | 0.0          |
| Aggregate Functions                             | 0.0          | 0.0          |
| Save Reports Layouts                            |              | 0.0          |
| Report Printing                                 | 0.0          | 0.0          |
| Export to Excel                                 | 0.0          | 0.0          |
| Export to CSV                                   | 0.0          | 0.0          |
| Export to PDF                                   | 0.0          | 0.0          |
| IV) Notifications                               |              |              |
| Email                                           | 0.0          | 0.0          |
| System News bar                                 | 0.0          | 0.0          |
| SMS                                             |              | 0.0          |
| Mobile Push Notifications                       |              | 0.0          |
| V) Workflow                                     |              |              |
| Transaction-based Single Level Approval         | 0.0          | 0.0          |
| User-defined Approval Cycle                     |              | 0.0          |
| User-defined Approval Notifications             |              | 0.0          |
| VI) Administration & User Privileges            |              |              |
| Unlimited User-defined Roles                    | 0.0          | 0.0          |
| User-defined Roles-Forms Privileges             | 0.0          | 0.0          |
| User-defined Roles-Reports Privileges           | 0.0          | 0.0          |
| User-defined Roles-Page Controls Privileges     | 0.0          | 0.0          |
| User-defined Roles-Transaction Types Privileges | 0.0          | 0.0          |
| User-defined Roles-Widgets Privileges           | 0.0          | 0.0          |
| Linking single User to Multiple Roles           | 0.0          | 0.0          |
| VII) Mobile Application                         |              | 0.0          |
| Android Support                                 |              | 0.0          |
| iOS Support                                     |              | 0.0          |
| Dashboard                                       |              | 0.0          |
| Leads & Activities Recording                    |              | 0.0          |
| Expenses Recording                              |              | 0.0          |

## Output:


---

## Data-transform-reshape__wide_to_long_test11

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Title   | 1st Platform Impacted   | 1st Vendor Used   |   1st Vendor Spend | 2nd Platform Impacted   | 2nd Vendor Used   |   2nd Vendor Spend |
|:--------|:------------------------|:------------------|-------------------:|:------------------------|:------------------|-------------------:|
| Nori    | Engagement              | AXTRIA            |               0.01 | Pricing                 | ACCENTURE         |               0.01 |
| Deliver | Experience              | ACCENTURE         |               0.01 | Engagement              | AXTRIA            |               0.01 |

## Output:


---

## Data-transform-reshape__pivot_test6

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Id: 02398123-a642-4e3f-88a7            |
|:---------------------------------------|
| Type: LINE                             |
| Detected Text: BUCK                    |
| Confidence: 77.965172                  |
| Id: c85bbbe                            |
| Type: LINE                             |
| Detected Text: NIP                     |
| Confidence: 97.186539                  |
| Id: 28926a7a-78024c80-b9c5             |
| Type: LINE                             |
| Detected Text: Preerfal Deet Attracter |
| Confidence: 47.749722                  |

## Output:


---

## Data-transform-reshape__explode_test25

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
|   Customer_ID | Challenges   |
|--------------:|:-------------|
|             1 | A,B,C        |
|             2 | A,C          |
|             3 | C,V          |
|             4 | D,E,F        |
|             5 | X,Y,Z,H      |
|             6 | A,B,C,D      |
|             7 | U,S,K,L      |
|             8 | O,P,Q        |
|             9 | R,S          |
|            10 | T            |

## Output:


---

## Data-transform-reshape__ffill_test16

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Volume    | Release Date       | Season/Box Set   | Episodes        |
|:----------|:-------------------|:-----------------|:----------------|
| Volume 1  | June 10, 2008      | Season 1         | 1–4             |
| Volume 2  | June 10, 2008      | Season 1         | 5–8             |
| Volume 3  | June 10, 2008      | Season 1         | 9–12            |
| Volume 4  | June 10, 2008      | Season 1         | 13–16           |
| Volume 5  | June 10, 2008      | Season 1         | 17–20           |
| Volume 6  | August 19, 2008    | Season 2         | 21–24           |
| Volume 7  | August 19, 2008    | Season 2         | 25–28           |
| Volume 8  | August 19, 2008    | Season 2         | 29–32           |
| Volume 9  | August 19, 2008    | Season 2         | 33–36           |
| Volume 10 | August 19, 2008    | Season 2         | 37–41           |
| Volume 11 | July 7, 2009       | Season 3         | 42–45           |
| Volume 12 | July 7, 2009       | Season 3         | 46–49           |
| Volume 13 | July 7, 2009       | Season 3         | 50–53           |
| Volume 14 | July 7, 2009       | Season 3         | 54–58           |
| Volume 15 | July 7, 2009       | Season 3         | 59–63           |
| Volume 16 | November 3, 2009   | Season 4 Part 1  | 64–67           |
| Volume 17 | November 3, 2009   | Season 4 Part 1  | 68–71           |
| Volume 18 | November 3, 2009   | Season 4 Part 1  | 72–75           |
| Volume 19 | November 3, 2009   | Season 4 Part 1  | 76–79           |
| Volume 20 | February 16, 2010  | Season 4 Part 2  | 80–83           |
| Volume 21 | February 16, 2010  | Season 4 Part 2  | 84–87           |
| Volume 22 | February 16, 2010  | Season 4 Part 2  | 88–91           |
| Volume 23 | June 8, 2010       | Season 5         | 92–95           |
| Volume 24 | June 8, 2010       | Season 5         | 96–99           |
| Volume 25 | June 8, 2010       | Season 5         | 100–104         |
| Volume 26 | June 8, 2010       | Season 5         | 105–109         |
| Volume 27 | September 28, 2010 | Box Set 6        | 110–113         |
| Volume 28 | September 28, 2010 | Box Set 6        | 114–117         |
| Volume 29 | September 28, 2010 | Box Set 6        | 118–121         |
| Volume 30 | December 21, 2010  | Box Set 7        | 122–133 134–145 |
| Volume 31 | December 21, 2010  | Box Set 7        | 122–133 134–145 |
| Volume 32 | March 22, 2011     | Box Set 8        | 122–133 134–145 |
|           | June 21, 2011      | Box Set 9        | 146–156         |
|           | September 6, 2011  | Box Set 10       | 157–167         |
|           | December 13, 2011  | Box Set 11       | 168–179         |
|           | March 13, 2012     | Box Set 12       | 180–193         |
|           | June 12, 2012      | Box Set 13       | 194–205         |
|           | September 11, 2012 | Box Set 14       | 206–217         |
|           | December 11, 2012  | Box Set 15       | 218–229         |
|           | March 12, 2013     | Box Set 16       | 230–242         |
|           | June 11, 2013      | Box Set 17       | 243–255         |
|           | September 10, 2013 | Box Set 18       | 256–267         |
|           | December 10, 2013  | Box Set 19       | 268–279         |
|           | March 18, 2014     | Box Set 20       | 280–291         |
|           | June 3, 2014       | Box Set 21       | 292–303         |
|           | September 30, 2014 | Box Set 22       | 304–316         |
|           | December 16, 2014  | Box Set 23       | 317–329         |
|           | March 17, 2015     | Box Set 24       | 330–342         |
|           | June 23, 2015      | Box Set 25       | 343–354         |
|           | September 29, 2015 | Box Set 26       | 355–366         |

## Output:


---

## Data-transform-reshape__stack_test50

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
|   No. | President              | R-McI 1996   | Schl. 1996   | C-SPAN 1999   | WSJ 2000   | Siena 2002   | WSJ 2005   | C-SPAN 2009   | Siena 2010   | USPC 2011   | APSA 2015   |
|------:|:-----------------------|:-------------|:-------------|:--------------|:-----------|:-------------|:-----------|:--------------|:-------------|:------------|:------------|
|     1 | George Washington      | 3            | 2            | 3             | 1          | 4            | 1          | 2             | 4            | 3           | 2           |
|     2 | John Adams             | 14           | 11           | 16            | 13         | 12           | 13         | 17            | 17           | 12          | 15          |
|     3 | Thomas Jefferson       | 4            | 4            | 7             | 4          | 5            | 4          | 7             | 5            | 4           | 5           |
|     4 | James Madison          | 10           | 17           | 18            | 15         | 8            | 17         | 20            | 6            | 14          | 13          |
|     5 | James Monroe           | 13           | 15           | 14            | 16         | 9            | 16         | 14            | 7            | 13          | 16          |
|     6 | John Quincy Adams      | 18           | 18           | 19            | 20         | 17           | 25         | 19            | 19           | 20          | 22          |
|     7 | Andrew Jackson         | 8            | 5            | 13            | 6          | 13           | 10         | 13            | 14           | 9           | 9           |
|     8 | Martin Van Buren       | 21           | 21           | 30            | 23         | 24           | 27         | 31            | 23           | 27          | 25          |
|     9 | William Henry Harrison | 35           | -            | 37            | -          | 36           | -          | 39            | 35           | -           | 39          |
|    10 | John Tyler             | 34           | 32           | 36            | 34         | 37           | 35         | 35            | 37           | 37          | 36          |
|    11 | James K. Polk          | 11           | 9            | 12            | 10         | 11           | 9          | 12            | 12           | 16          | 19          |
|    12 | Zachary Taylor         | 29           | 29           | 28            | 31         | 34           | 33         | 29            | 33           | 33          | 33          |
|    13 | Millard Fillmore       | 36           | 31           | 35            | 35         | 38           | 36         | 37            | 38           | 35          | 37          |
|    14 | Franklin Pierce        | 37           | 33           | 39            | 37 (tie)   | 39           | 38         | 40            | 40           | 39          | 40          |
|    15 | James Buchanan         | 40           | 38           | 41            | 39         | 41           | 40         | 42            | 42           | 40          | 43          |
|    16 | Abraham Lincoln        | 1            | 1            | 1             | 2          | 2            | 2          | 1             | 3            | 2           | 1           |
|    17 | Andrew Johnson         | 39           | 37           | 40            | 36         | 42           | 37         | 41            | 43           | 36          | 41          |
|    18 | Ulysses S. Grant       | 38           | 34           | 33            | 32         | 35           | 29         | 23            | 26           | 29          | 28          |
|    19 | Rutherford B. Hayes    | 25           | 23           | 26            | 22         | 27           | 24         | 33            | 31           | 30          | 30          |
|    20 | James A. Garfield      | 30           | -            | 29            | -          | 33           | -          | 28            | 27           | -           | 31          |
|    21 | Chester A. Arthur      | 28           | 26           | 32            | 26         | 30           | 26         | 32            | 25           | 32          | 32          |
|    22 | Grover Cleveland       | 16           | 13           | 17            | 12         | 20           | 12         | 21            | 20           | 21          | 23          |
|    23 | Benjamin Harrison      | 31           | 19           | 31            | 27         | 32           | 30         | 30            | 34           | 34          | 29          |
|    25 | William McKinley       | 17           | 16           | 15            | 14         | 19           | 14         | 16            | 21           | 17          | 21          |
|    26 | Theodore Roosevelt     | 5            | 6            | 4             | 5          | 3            | 5          | 4             | 2            | 5           | 4           |
|    27 | William Howard Taft    | 20           | 22           | 24            | 19         | 21           | 20         | 24            | 24           | 25          | 20          |
|    28 | Woodrow Wilson         | 6            | 7            | 6             | 11         | 6            | 11         | 9             | 8            | 6           | 10          |
|    29 | Warren G. Harding      | 41           | 39           | 38            | 37 (tie)   | 40           | 39         | 38            | 41           | 38          | 42          |
|    30 | Calvin Coolidge        | 33           | 30           | 27            | 25         | 29           | 23         | 26            | 29           | 28          | 27          |
|    31 | Herbert Hoover         | 24           | 35           | 34            | 29         | 31           | 31         | 34            | 36           | 26          | 38          |
|    32 | Franklin D. Roosevelt  | 2            | 3            | 2             | 3          | 1            | 3          | 3             | 1            | 1           | 3           |
|    33 | Harry S. Truman        | 7            | 8            | 5             | 7          | 7            | 7          | 5             | 9            | 7           | 6           |
|    34 | Dwight D. Eisenhower   | 9            | 10           | 9             | 9          | 10           | 8          | 8             | 10           | 10          | 7           |
|    35 | John F. Kennedy        | 15           | 12           | 8             | 18         | 14           | 15         | 6             | 11           | 15          | 14          |
|    36 | Lyndon B. Johnson      | 12           | 14           | 10            | 17         | 15           | 18         | 11            | 16           | 11          | 12          |
|    37 | Richard M. Nixon       | 32           | 36           | 25            | 33         | 26           | 32         | 27            | 30           | 23          | 34          |
|    38 | Gerald R. Ford         | 27           | 28           | 23            | 28         | 28           | 28         | 22            | 28           | 24          | 24          |
|    39 | Jimmy Carter           | 19           | 27           | 22            | 30         | 25           | 34         | 25            | 32           | 18          | 26          |
|    40 | Ronald Reagan          | 26           | 25           | 11            | 8          | 16           | 6          | 10            | 18           | 8           | 11          |
|    41 | George H. W. Bush      | 22           | 24           | 20            | 21         | 22           | 21         | 18            | 22           | 22          | 17          |
|    42 | Bill Clinton           | 23 *         | 20 *         | 21 *          | 24 *       | 18           | 22         | 15            | 13           | 19          | 8           |
|    43 | George W. Bush         | -            | -            | -             | -          | 23 *         | 19 *       | 36            | 39           | 31          | 35          |
|    44 | Barack Obama           | -            | -            | -             | -          | -            | -          | -             | 15 *         | -           | 18 *        |
|    45 | Donald Trump           | -            | -            | -             | -          | -            | -          | -             | -            | -           | -           |

## Output:


---

## Data-transform-reshape__stack_test36

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Film                | North America(Opening)   | North America(Gross (unadjusted))   | Worldwide gross (unadjusted)   |
|:--------------------|:-------------------------|:------------------------------------|:-------------------------------|
| Toy Story           | $29.1 million            | $191.8 million                      | $373.6 million                 |
| A Bug's Life        | $33.3 million            | $162.8 million                      | $363.3 million                 |
| Toy Story 2         | $57.4 million            | $245.9 million                      | $497.4 million                 |
| Monsters, Inc.      | $62.6 million            | $255.9 million                      | $525.4 million                 |
| Finding Nemo        | $70.3 million            | $339.7 million                      | $867.9 million                 |
| The Incredibles     | $70.5 million            | $261.4 million                      | $633.0 million                 |
| Cars                | $60.1 million            | $244.1 million                      | $462.2 million                 |
| Ratatouille         | $47.0 million            | $206.4 million                      | $620.7 million                 |
| WALL-E              | $63.1 million            | $223.8 million                      | $533.3 million                 |
| Up                  | $68.1 million            | $293.0 million                      | $735.1 million                 |
| Toy Story 3         | $110.3 million           | $415.0 million                      | $1,067.0 million               |
| Cars 2              | $66.1 million            | $191.5 million                      | $562.1 million                 |
| Brave               | $66.3 million            | $237.3 million                      | $540.4 million                 |
| Monsters University | $82.4 million            | $268.5 million                      | $744.2 million                 |
| Inside Out          | $90.4 million            | $356.5 million                      | $857.6 million                 |
| The Good Dinosaur   | $39.2 million            | $123.1 million                      | $332.2 million                 |
| Finding Dory        | $135.1 million           | $486.3 million                      | $1,028.6 million               |
| Cars 3              | $53.7 million            | $141.6 million                      | $224.8 million                 |

## Output:


---

## Data-transform-reshape__wide_to_long_test33

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Volume   | Book 1: Water(Released)   |   Book 1: Water(Discs) |   Book 1: Water(Episodes) | Book 2: Earth(Released)                      | Book 2: Earth(Discs)                         | Book 2: Earth(Episodes)                      | Book 3: Fire(Released)                       | Book 3: Fire(Discs)                          | Book 3: Fire(Episodes)                       |
|:---------|:--------------------------|-----------------------:|--------------------------:|:---------------------------------------------|:---------------------------------------------|:---------------------------------------------|:---------------------------------------------|:---------------------------------------------|:---------------------------------------------|
| 1        | March 15, 2007            |                      1 |                         4 | June 4, 2009                                 | 1                                            | 5                                            | June 3, 2010                                 | 1                                            | 5                                            |
| 2        | July 5, 2007              |                      1 |                         4 | August 4, 2009                               | 1                                            | 5                                            | September 23, 2010                           | 1                                            | 5                                            |
| 3        | March 13, 2008            |                      1 |                         4 | October 29, 2009                             | 1                                            | 5                                            | October 7, 2010                              | 1                                            | 5                                            |
| 4        | June 19, 2008             |                      1 |                         4 | March 31, 2010                               | 1                                            | 5                                            | November 4, 2010                             | 1                                            | 6                                            |
| 5        | March 5, 2009             |                      1 |                         4 | There is no volume five DVD for this season. | There is no volume five DVD for this season. | There is no volume five DVD for this season. | There is no volume five DVD for this season. | There is no volume five DVD for this season. | There is no volume five DVD for this season. |
| Box set  | June 4, 2009              |                      5 |                        20 | September 9, 2010                            | 4                                            | 20                                           | December 2, 2010                             | 4                                            | 21                                           |

## Output:


---

## Data-transform-reshape__ffill_test5

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Category        | Description              |        $ |         % |
|:----------------|:-------------------------|---------:|----------:|
| Income          | Person 1                 | 4034.87  | 0.545455  |
|                 | Person 2                 | 3362.39  | 0.454545  |
| Expense - Needs | Rent/Mortgage            | 1650     | 0.223055  |
|                 | Utilities                |  155     | 0.0209537 |
|                 | Children                 | 1500     | 0.202778  |
|                 | Groceries                |  250     | 0.0337963 |
|                 | Car Payment              |  275     | 0.0371759 |
|                 | Auto Exp                 |  225     | 0.0304166 |
|                 | Auto Insurance           |  100     | 0.0135185 |
|                 | Health Insurance         |  395     | 0.0533981 |
|                 | Medical (HSA/FSA)        |  225     | 0.0304166 |
|                 | Life Insurance           |   60     | 0.0081111 |
|                 | Donation                 |  250     | 0.0337963 |
|                 | Clothes                  |  100     | 0.0135185 |
| Expense - Wants | Entertainment            |  125     | 0.0168981 |
|                 | Cell Phone               |  100     | 0.0135185 |
|                 | Cable/Internet           |  100     | 0.0135185 |
| Savings         | 401(k)                   |  295.891 | 0.04      |
|                 | Roth IRA                 |  917     | 0.123965  |
|                 | Emergency Fund           |    0     | 0         |
|                 | 529 Plan                 |  225     | 0.0304166 |
|                 | Investment (Rental Prop) |  449.378 | 0.0607492 |
|                 | 0                        | 1887.27  | 0.25513   |

## Output:


---

## Data-transform-reshape__multistep_test20

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Rozliczenie zwykłego kredytu hipo.   | Opcja 0   | Opcja 1            | Opcja 2            | Opcja 3            | Opcja 4            |
|:-------------------------------------|:----------|:-------------------|:-------------------|:-------------------|:-------------------|
| Odsetki lata 0-2                     | 25962.62  | 25962.62           | 25962.62           | 25962.62           | 25962.62           |
| Odsetki lata 3-8                     | 56461.26  | 56461.26           | 28960.89           | 56461.26           | 43440.71           |
| Odsetki lata 9-18                    | 43336.95  | 43336.95           | 3139.83            | 8838.9             | 5733.17            |
| SUMA kosztów odsetek                 | 125760.83 | 125760.83          | 58063.34           | 91262.78           | 75136.5            |
| Całkowita wartość kredytu            | 333727.83 | 333727.83          | 266030.33999999997 | 299229.78000000003 | 283103.5           |
| Przychody z lokaty 72 000 zł         | 0         | 63895.74           | 0                  | 19366.080000000002 | 0                  |
| Termin spłaty kredytu                | 18 lat    | 18 lat             | 11,5 roku          | 13,5 roku          | 12,5 roku          |
| Koszt po uwzględnieniu przychodów    | 333727.83 | 269832.09000000003 | 266030.33999999997 | 279863.7           | 283103.5           |
| Marcin oszczędza                     | 0         | 63895.739999999991 | 67697.490000000049 | 53864.130000000005 | 50624.330000000016 |

## Output:


---

## Data-transform-reshape__stack_test27

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
|   year |   Jan |   Feb |   Mar |   Apr |   May |   Jun |   Jul |   Aug |   Sep |   Oct |   Nov |   Dec |
|-------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
|   1876 |   3.6 |  -4.8 |   1.5 |  -0.1 |  -4.7 |   6.9 |  -5   |   9.2 |   8.6 |   4.5 |   1.7 |  -1.8 |
|   1877 |   7.2 |  -1.7 |  -5.1 |  -9.7 |   5.3 |  -6.8 |   0.7 |  -5.8 |  -6.2 |   8.9 |   2.2 |  -1.2 |
|   1878 |  -4.5 |   3.1 |   2.8 |   3.6 |   7.6 |   6.8 |   0.3 |  -2   |  -7.2 |  -6.3 |   6.7 |  -5.5 |
|   1879 |   2.6 |  -3.4 |  -4.8 |   2.7 |  -6   |  -8.1 |  -9.1 |   3.2 |   5.3 |   2   |   9.7 |  -8.4 |
|   1880 |  -6.6 |  -2.8 |  -7   |  -1   |  -1.9 |   4.8 |   5.8 |  -7   |  -9.2 |  -4.7 |   5   |  -2.9 |
|   1881 |   0.2 |  -6.5 |   1.6 |  -8.3 |   2.5 |  -0.3 |   4.7 |   4.7 |   1.8 |   9.4 |   1   |   4.4 |
|   1882 |  -9.7 |  -2   |  -0.1 |   2.5 |   2.5 |  -6   |  -8.1 |  -3.1 |   8.9 |  -3   |  -1.5 |  -9.8 |
|   1883 |   4.5 |  -8.1 |  -9.7 |  -7.3 |  -2.3 |   8.9 |   7.7 |   5.3 |   3   |  -1.5 |   4   |  -9.4 |
|   1884 |  -4.7 |  -0.4 |  -4.1 |   8.1 |  -1.2 |   2.4 |  -4.3 |  -0.3 |  -7.3 |  -4.8 |   4.5 |  -5.4 |
|   1885 |   2.7 |   4.3 |  -3.7 |   6.4 |   2.2 |   0.4 |  -5   |  -5.2 |   9.2 |   6.6 |  -9.8 |   2.9 |
|   1886 | -10   |  -5.1 |   1.3 |   6.1 |  -1.5 |  -9   |   9.1 |   4.8 |  -4.5 |   1.2 |   9.7 |   0.4 |
|   1887 |   6.6 |  -0.8 |   6.6 |  -8.1 |   2.9 |   5.7 |   0.2 |  -2.6 |   1.2 |  -6   |   3.2 |   2.4 |
|   1888 |   4.2 |   0.8 |   4.8 |  -8.5 |   4.8 |   7.8 |   5.3 |   7   |   7.8 |   9.5 |   6.2 |   6.5 |
|   1889 |  -2   |  -0.7 |  -6.3 |  -5.3 |   3.1 |   1.8 |   8.2 |  -7.7 |  -5.9 |  -0.3 |  -5.7 |  -9.1 |
|   1890 |  -5.1 |  -9.6 |   7.5 |  -9.9 |  -5.1 |  -6.3 |  -6   |   9.8 |   7.8 |   4.3 |   2.6 |   4   |
|   1891 |  -7.9 |  -3.6 |   4.3 |  -3.6 |  -5.1 |  -3.5 |   0.9 |  -8.3 |   8.9 |   9.9 |   8.9 |   2.6 |
|   1892 |  -8.8 |   9.8 |  -8.6 |  -8.1 |   0.4 |  -4.9 |   8.8 |   6.1 |  -3.7 |  -2   |  -5.9 |   8.1 |
|   1893 |  -6.2 |  -0.6 |  -3.5 |  -1.9 |  -2.8 |  -7.6 |   3.3 |  -0.6 |  -8.6 |  -1.5 |   6.9 |  -9.6 |
|   1894 |  -8.2 |   6.1 |   9.1 |  -3.3 |  -7.7 |  -9.8 |   4.1 |  -9.4 |  -6.2 |   9.6 |  -4   |  -3.6 |
|   1895 |  -1.6 |   7.3 |   2.4 |   6.7 |   5.6 |  -5.3 |   5.1 |   7.3 |  -2.6 |   5   |   7.7 |  -1.5 |
|   1896 |   0.1 |  -3.9 |   2.7 |   1.6 |  -1.8 |   1.9 |  -7.8 |  -9.6 |   1.7 |  -2.8 |  -4.4 |   4.8 |
|   1897 |  -5.8 |  -1.5 |   5.2 |  -0.5 |   8   |  -0.2 |  -0.2 |  -8   |  -7.9 |  -4.3 |   6.1 |   5   |
|   1898 |  -9.1 |   5.1 |   4.2 |  -5.3 |   2.3 |   2.1 |  -9.1 |  -4.6 |  -8.5 |   8.7 |   1   |  -4.5 |
|   1899 |   8.3 |   4.6 |   3.2 |  -7.5 |  -6.8 |  -9.5 |   2.2 |   4   |   9.5 |   4.2 |  -6.3 |  -1.6 |
|   1900 |  -3.8 |  -9.7 |  -0.7 |  -7.1 |  -3.8 |  -0.5 |  -8.7 |   0.6 |  -1.4 |   8.2 |   6.9 |  -9.3 |
|   1901 |  -0.3 |   8.7 |   7   |  -7.8 |   5.1 |   8.3 |   5.1 |   1.9 |  -1.5 |   9.8 |   1.3 |  -3.8 |
|   1902 |  -3.6 |  -1.2 |  -2.1 |  -5.1 |   6.1 |  -9.3 |   7.5 |   2.1 |   5.3 |   9.1 |   5.1 |  -3.2 |
|   1903 |   0.9 |   5.6 |   0.3 |  -2.7 |  -2.3 |   1.6 |   6.6 |   2.7 |   8.4 |   6.9 |  -2.6 |   4.1 |
|   1904 |   5.8 |   2.6 |  -8.3 |  -7   |   2.6 |  10   |   9   |  -3.8 |   6.7 |   4   |   7.8 |  -5.8 |
|   1905 |  -8.9 |  -8.2 |   4.1 |   2.6 |  -9.5 |   4.5 |  -9   |   5.3 |   4.1 |  -6.1 |   0.1 |   6   |

## Output:


---

## Data-transform-reshape__ffill_test11

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Year   |   KPI-JAE |
|:-------|----------:|
| 2000.0 |       2   |
|        |       2.2 |
|        |       1.6 |
|        |       1.8 |
|        |       2   |
|        |       2.2 |
|        |       2.3 |
|        |       2.8 |
|        |       2.7 |
|        |       2.6 |
|        |       2.6 |
|        |       2.7 |
| 2001.0 |       2.8 |
|        |       2.9 |
|        |       2.8 |
|        |       2.6 |
|        |       2.7 |
|        |       2.4 |
|        |       2.6 |
|        |       2.4 |
|        |       2.3 |
|        |       2.5 |
|        |       2.5 |
|        |       2.7 |
| 2002.0 |       2.5 |
|        |       2.1 |
|        |       2.6 |
|        |       2.4 |
|        |       2.6 |
|        |       2.7 |
|        |       2.7 |
|        |       2.3 |
|        |       2.2 |
|        |       2.1 |
|        |       2   |
|        |       1.8 |
| 2003.0 |       1.8 |
|        |       2   |
|        |       1.5 |
|        |       1.6 |
|        |       1.2 |
|        |       0.8 |
|        |       0.7 |
|        |       0.9 |
|        |       0.9 |
|        |       0.8 |
|        |       0.5 |
|        |       0.4 |
| 2004.0 |       0   |
|        |       0   |
|        |       0.3 |
|        |       0.3 |
|        |       0.1 |
|        |       0.3 |
|        |       0.2 |
|        |       0.2 |
|        |       0.5 |
|        |       0.6 |
|        |       1   |
|        |       1   |
| 2005.0 |       0.7 |
|        |       0.7 |
|        |       0.7 |
|        |       0.8 |
|        |       1.1 |
|        |       1.1 |
|        |       1.1 |
|        |       1.3 |
|        |       1.3 |
|        |       1.2 |
|        |       1.1 |
|        |       0.9 |
| 2006.0 |       0.8 |
|        |       1   |
|        |       0.9 |
|        |       0.8 |
|        |       0.7 |
|        |       0.8 |
|        |       0.6 |
|        |       0.4 |
|        |       0.5 |
|        |       0.7 |
|        |       0.8 |
|        |       1   |
| 2007.0 |       1   |
|        |       1.1 |
|        |       1.5 |
|        |       1.4 |
|        |       1.4 |
|        |       1.3 |
|        |       1.4 |
|        |       1.8 |
|        |       1.6 |
|        |       1.4 |
|        |       1.5 |
|        |       1.8 |
| 2008.0 |       1.9 |
|        |       2.2 |
|        |       2.1 |
|        |       2.4 |

## Output:


---

## Data-transform-reshape__explode_test8

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Native American                     | Column1   |          Dollars |   M/F |   Contract |   Prime | Districts     |
|:------------------------------------|:----------|-----------------:|------:|-----------:|--------:|:--------------|
| ADANTA INC                          | -4142.0   |   9750           |     0 |          6 |       5 | 5,7,9,10      |
| AMERICAN STEEL PLACERS              | 33.0      | 732108           |     1 |          1 |       1 | 6             |
| CREST EQUIPMENT INC                 | -4142.0   | 140000           |     0 |          1 |       1 | 11            |
| DISABLED AMERICAN VETERAN           | 33.0      |      1.88873e+06 |     1 |          3 |       2 | 5,6,10        |
| FINE GRADE EQUIPMENT                | -4142.0   |      1.33112e+07 |     0 |          2 |       2 | 6             |
| FORCE TRAFFIC CONTROL               | -4142.0   | 385930           |     1 |          3 |       2 | 9,10          |
| GLOBAL TRANSLOADING                 | 43.0      |   6120           |     0 |          1 |       1 | 7             |
| GR SUNDBERG INC                     | -4142.0   | 881575           |     1 |          5 |       3 | 1, 4          |
| KRC SAFETY COMPANY                  | -4142.0   |      4.47559e+06 |     1 |         22 |      10 | 3,4,5,6,7,8,9 |
| RAPER ELCETRICAL                    | 33.0      | 221019           |     1 |          4 |       3 | 3,5,10        |
| S.T. RHOADES                        | -4142.0   |      2.1679e+06  |     1 |          6 |       5 | 1,2           |
| SAMS EQUIPMENT                      | 43.0      |  83205           |     1 |          1 |       1 | 1             |
| SPIRIT ROAD OILS                    |           |  15981.4         |     0 |          3 |       2 | 4,5           |
| TRINITY VALLEY CONSULTING ENGINEERS |           |  25200           |     1 |          1 |       1 | 2             |

## Output:


---

## Data-transform-reshape__stack_test48

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Unnamed: 0    | Asian   | Black   | Hispanic (of any race)   | Non-Hispanic White   | Other/international   | Unknown   |
|:--------------|:--------|:--------|:-------------------------|:---------------------|:----------------------|:----------|
| Brown         | 14%     | 6%      | 10%                      | 45%                  | 14%                   | 11%       |
| Columbia      | 15%     | 8%      | 13%                      | 41%                  | 17%                   | 6%        |
| Cornell       | 17%     | 6%      | 10%                      | 46%                  | 13%                   | 10%       |
| Dartmouth     | 14%     | 8%      | 9%                       | 48%                  | 13%                   | 8%        |
| Harvard       | 12%     | 7%      | 9%                       | 45%                  | 22%                   | 6%        |
| Penn          | 19%     | 7%      | 8%                       | 46%                  | 13%                   | 7%        |
| Princeton     | 18%     | 7%      | 8%                       | 49%                  | 15%                   | 3%        |
| Yale          | 15%     | 6%      | 8%                       | 58%                  | 5%                    | 8%        |
| United States | 5%      | 13%     | 17%                      | 63%                  | 4%                    |           |

## Output:


---

## Data-transform-reshape__explode_test46

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Title                                                            | Runtime          | Netflix exclusive region                                                                                                                                                                                                                     |
|:-----------------------------------------------------------------|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The 101-Year-Old Man Who Skipped Out on the Bill and Disappeared | 1 hour, 48 min   | Worldwide except Nordics, DACH, Japan and Luxembourg                                                                                                                                                                                         |
| 6 Days                                                           | TBA              | Germany, France, Japan, Latin America, Benelux, Scandinavia, Eastern Europe, Italy, Switzerland                                                                                                                                              |
| Bad Moms                                                         | 1 hour, 40 min.  | Japan                                                                                                                                                                                                                                        |
| Before I Fall                                                    | 1 hour, 38 min.  | Japan                                                                                                                                                                                                                                        |
| Before I Wake                                                    | 1 hour, 37 min.  | United Kingdom, Ireland, France and Nordics                                                                                                                                                                                                  |
| Bushwick                                                         | 1 hour, 34 min.  | France, South Korea                                                                                                                                                                                                                          |
| Cargo                                                            | TBA              | Worldwide except Australia                                                                                                                                                                                                                   |
| David Brent: Life on the Road                                    | 1 hour, 36 min.  | Worldwide except United Kingdom, Ireland, Australia, and New Zealand                                                                                                                                                                         |
| Divines                                                          | 1 hour, 45 min.  | Worldwide except France                                                                                                                                                                                                                      |
| El Faro De Las Orcas (The Lighthouse of the Orcas)               | 1 hour, 50 min.  | Wordwide except Spain and Argentina                                                                                                                                                                                                          |
| Good Time                                                        | 1 hour, 50 min   | Spain, Italy, United Kingdom, Ireland, Scandinavia, Israel, Portugal, Bulgaria, Russia, CIS, the Baltics, ex-Yugoslavia, Hungary, Poland, Czech Republic, Romania, South Korea, Singapore, Malaysia, Thailand, Japan, Australia, New Zealand |
| Hell or High Water                                               | 1 hour, 43 min.  | Italy, San Marino, Vatican City, Japan                                                                                                                                                                                                       |
| In the Shadow of Iris                                            | 1 hour, 38 min.  | Worldwide except France                                                                                                                                                                                                                      |
| Journey to Greenland                                             | 1 hour, 38 min.  | Worldwide except France                                                                                                                                                                                                                      |
| Kevin Hart: What Now?                                            | 1 hour, 36 min.  | Worldwide except United States                                                                                                                                                                                                               |
| Kung Fu Panda 3                                                  | 1 hour, 34 min.  | Japan                                                                                                                                                                                                                                        |
| The Little Prince                                                | 1 hour, 46 min.  | United States, United Kingdom, Ireland, Australia, New Zealand                                                                                                                                                                               |
| Lucid Dream                                                      | 1 hour, 41 min   | Worldwide except South Korea                                                                                                                                                                                                                 |
| Mercenary                                                        | 1 hour, 38 min.  | Multiple territories                                                                                                                                                                                                                         |
| Message from the King                                            | TBA              | United States and some foreign territories                                                                                                                                                                                                   |
| Middle School: The Worst Years of My Life                        | 1 hour, 32 min.  | United Kingdom, Ireland, Benelux, DACH, Italy, Spain, Japan, India                                                                                                                                                                           |
| Mindhorn                                                         | 1 hour, 28 min.  | Worldwide except the United Kingdom and Ireland                                                                                                                                                                                              |
| Mudbound                                                         | 2 hours          | United States and select other territories                                                                                                                                                                                                   |
| My Happy Family                                                  | 2 hours          | Worldwide except France                                                                                                                                                                                                                      |
| Pandora                                                          | 2 hours, 16 min. | Worldwide except South Korea                                                                                                                                                                                                                 |
| Sahara                                                           | 1 hour, 24 min.  | Canada, United States, and United Kingdom, Germany                                                                                                                                                                                           |
| Sand Storm                                                       | 1 hour, 28 min.  | Worldwide except Israel                                                                                                                                                                                                                      |
| Seven Sisters                                                    | TBA              | United States                                                                                                                                                                                                                                |
| Skiptrace                                                        | 1 hour, 47 min.  | United Kingdom, Ireland, France                                                                                                                                                                                                              |
| Slam                                                             | 1 hour, 40 min.  | Worldwide except Italy                                                                                                                                                                                                                       |
| The Space Between Us                                             | 2 hours          | Japan                                                                                                                                                                                                                                        |
| Strange Weather                                                  | TBA              | Worldwide except Japan                                                                                                                                                                                                                       |

## Output:


---

## Data-transform-reshape__stack_test37

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Title                              | Distributor(s)   | Release date (United States)   | Budget (millions)   | Box office gross(Opening weekend (North America))   | Box office gross(North America)   | Box office gross(Worldwide)   |
|:-----------------------------------|:-----------------|:-------------------------------|:--------------------|:----------------------------------------------------|:----------------------------------|:------------------------------|
| Superman                           | Warner Bros.     | December 10, 1978              | $55                 | $6,535,784                                          | $134,218,018                      | $300,218,018                  |
| Superman II                        | Warner Bros.     | June 19, 1981                  | $54                 | $14,100,523                                         | $108,185,706                      | $108,185,706                  |
| Superman III                       | Warner Bros.     | June 17, 1983                  | $39                 | $13,352,357                                         | $59,950,623                       | $59,950,623                   |
| Supergirl                          | TriStar Pictures | November 21, 1984              | $35                 | $5,738,249                                          | $14,296,438                       | $14,296,438                   |
| Superman IV: The Quest for Peace   | Warner Bros.     | July 24, 1987                  | $17                 | $5,683,122                                          | $15,681,020                       | $15,681,020                   |
| The Return of Swamp Thing          | Millimeter Films | May 12, 1989                   | Unknown             | Unknown                                             | $192,816                          | $192,816                      |
| Batman                             | Warner Bros.     | June 23, 1989                  | $35                 | $40,489,746                                         | $251,188,924                      | $411,348,924                  |
| Batman Returns                     | Warner Bros.     | June 19, 1992                  | $80                 | $45,687,711                                         | $162,831,698                      | $266,822,354                  |
| Batman: Mask of the Phantasm       | Warner Bros.     | December 25, 1993              | $6                  | $1,189,975                                          | $5,617,391                        | $5,617,391                    |
| Batman Forever                     | Warner Bros.     | June 16, 1995                  | $100                | $52,784,433                                         | $184,031,112                      | $336,529,144                  |
| Batman & Robin                     | Warner Bros.     | June 20, 1997                  | $125                | $42,872,605                                         | $107,325,195                      | $238,207,122                  |
| Steel                              | Warner Bros.     | August 15, 1997                | $16                 | $870,068                                            | $1,710,972                        | $1,710,972                    |
| Catwoman                           | Warner Bros.     | July 23, 2004                  | $100                | $16,728,411                                         | $40,202,379                       | $82,102,379                   |
| Constantine                        | Warner Bros.     | February 18, 2005              | $100                | $29,769,098                                         | $75,976,178                       | $230,884,728                  |
| Batman Begins                      | Warner Bros.     | June 28, 2005                  | $150                | $48,745,440                                         | $206,852,432                      | $374,218,673                  |
| V for Vendetta                     | Warner Bros.     | March 17, 2006                 | $54                 | $25,642,340                                         | $70,511,035                       | $132,511,035                  |
| Superman Returns                   | Warner Bros.     | June 20, 2006                  | $204                | $52,535,096                                         | $200,081,192                      | $391,081,192                  |
| The Dark Knight                    | Warner Bros.     | July 18, 2008                  | $185                | $158,411,483                                        | $534,858,444                      | $1,004,558,444                |
| Watchmen                           | Warner Bros.     | March 6, 2009                  | $130                | $55,214,334                                         | $107,509,799                      | $185,258,983                  |
| The Losers                         | Warner Bros.     | April 23, 2010                 | $25                 | $9,406,348                                          | $23,591,432                       | $29,379,723                   |
| Jonah Hex                          | Warner Bros.     | June 18, 2010                  | $47                 | $5,379,365                                          | $10,547,117                       | $10,903,312                   |
| Green Lantern                      | Warner Bros.     | June 17, 2011                  | $200                | $53,174,303                                         | $116,601,172                      | $219,851,172                  |
| The Dark Knight Rises              | Warner Bros.     | July 20, 2012                  | $230                | $160,887,295                                        | $448,139,099                      | $1,084,939,099                |
| Man of Steel                       | Warner Bros.     | June 14, 2013                  | $225                | $116,619,362                                        | $291,045,518                      | $668,045,518                  |
| Batman v Superman: Dawn of Justice | Warner Bros.     | March 25, 2016                 | $250                | $166,007,347                                        | $330,360,194                      | $873,260,194                  |
| Batman: The Killing Joke           | Warner Bros.     | July 26, 2016                  | $3.5                |                                                     | $3,775,000                        | $3,775,000                    |
| Suicide Squad                      | Warner Bros.     | August 5, 2016                 | $175                | $133,682,248                                        | $325,100,054                      | $745,600,054                  |
| The Lego Batman Movie              | Warner Bros.     | February 10, 2017              | $80                 | $53,003,578                                         | $175,750,384                      | $310,850,384                  |
| Wonder Woman                       | Warner Bros.     | June 2, 2017                   | $149                | $103,251,471                                        | $383,576,840                      | $768,876,840                  |

## Output:


---

## Data-transform-reshape__stack_test25

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| token            | is_authority   | is_ingredient   | is_ailment   | is_body_part   | is_treatment   |
|:-----------------|:---------------|:----------------|:-------------|:---------------|:---------------|
| abcess           | False          | False           | True         | False          | False          |
| abcesses         | False          | False           | True         | False          | False          |
| abdomen          | False          | False           | False        | True           | False          |
| abdominal        | False          | False           | False        | True           | False          |
| abnormal         | False          | False           | True         | False          | False          |
| abnormality      | False          | False           | True         | False          | False          |
| abortifacient    | False          | False           | False        | False          | True           |
| abortion         | False          | False           | False        | False          | True           |
| abortive         | False          | False           | True         | False          | False          |
| abrotanum        | False          | True            | False        | False          | False          |
| abscess          | False          | False           | True         | False          | False          |
| absentmindedness | False          | False           | True         | False          | False          |
| absinth          | False          | True            | False        | False          | False          |
| acacia           | False          | True            | False        | False          | False          |
| accident         | False          | False           | True         | False          | False          |
| ache             | False          | False           | True         | False          | False          |
| acne             | False          | False           | True         | False          | False          |
| acorn            | False          | True            | False        | False          | False          |
| acute            | False          | False           | True         | False          | False          |
| aesculapius      | True           | False           | False        | False          | False          |
| affectis         | True           | False           | False        | False          | False          |
| afflicted        | False          | False           | True         | False          | False          |
| agaric           | False          | True            | False        | False          | False          |
| age              | False          | False           | True         | False          | False          |
| aged             | False          | False           | True         | False          | False          |
| agent            | False          | True            | False        | False          | False          |
| aid              | False          | False           | False        | False          | True           |
| ailing           | False          | False           | True         | False          | False          |
| ailment          | False          | False           | True         | False          | False          |
| air              | False          | True            | False        | False          | False          |
| al-kaḥḥalīn      | True           | False           | False        | False          | False          |
| al-kaḥḥlīn       | True           | False           | False        | False          | False          |
| al-kaḥḥāl        | True           | False           | False        | False          | False          |
| al-kaḥḥālīn      | True           | False           | False        | False          | False          |
| al-kindī         | True           | False           | False        | False          | False          |
| alchemical       | False          | False           | False        | False          | True           |
| alchemist        | True           | False           | False        | False          | False          |
| alcoholic        | False          | False           | True         | False          | False          |
| alcoholism       | False          | False           | True         | False          | False          |
| alignment        | False          | False           | True         | False          | False          |
| alimentation     | False          | False           | True         | False          | False          |
| alleviated       | False          | False           | False        | False          | True           |
| alleviating      | False          | False           | False        | False          | True           |
| allāh            | True           | False           | False        | False          | False          |
| almond           | False          | True            | False        | False          | False          |
| aloe             | False          | True            | False        | False          | False          |
| aloe-wood        | False          | True            | False        | False          | False          |
| alopecia         | False          | False           | True         | False          | False          |
| althea           | False          | True            | False        | False          | False          |
| alum             | False          | True            | False        | False          | False          |
| amber            | False          | True            | False        | False          | False          |
| ambergris        | False          | True            | False        | False          | False          |
| amenorrhoea      | False          | False           | True         | False          | False          |
| ammonia          | False          | True            | False        | False          | False          |
| ammoniac         | False          | True            | False        | False          | False          |
| amnesia          | False          | False           | True         | False          | False          |
| amomum           | False          | True            | False        | False          | False          |
| amulet           | False          | False           | False        | False          | True           |
| anachroid        | False          | False           | False        | True           | False          |
| anal             | False          | False           | False        | True           | False          |
| anaphrodisiac    | False          | False           | False        | False          | True           |
| anarcardium      | False          | True            | False        | False          | False          |
| anasarca         | False          | True            | False        | False          | False          |
| anatomical       | False          | False           | False        | True           | False          |
| anatomy          | False          | False           | False        | True           | False          |
| anchusa          | False          | True            | False        | False          | False          |
| andara           | False          | True            | False        | False          | False          |
| anemone          | False          | True            | False        | False          | False          |
| anguish          | False          | False           | True         | False          | False          |
| anima            | True           | False           | False        | False          | False          |
| anise            | False          | True            | False        | False          | False          |
| aniseed          | False          | True            | False        | False          | False          |
| anorectal        | False          | False           | True         | False          | False          |
| antihemorrhagic  | False          | True            | False        | False          | False          |
| antimony         | False          | True            | False        | False          | False          |
| antipyretic      | False          | True            | False        | False          | False          |
| anus             | False          | False           | False        | True           | False          |
| anxiety          | False          | False           | True         | False          | False          |
| aperient         | False          | False           | False        | False          | True           |
| aphasia          | False          | False           | True         | False          | False          |
| aphrodisiac      | False          | True            | False        | False          | False          |
| apoplexy         | False          | False           | True         | False          | False          |
| apparatus        | False          | True            | False        | False          | False          |
| appetite         | False          | False           | True         | False          | False          |
| apple            | False          | True            | False        | False          | False          |
| application      | False          | False           | False        | False          | True           |
| applied          | False          | False           | False        | False          | True           |
| apprentice       | True           | False           | False        | False          | False          |
| apricot          | False          | True            | False        | False          | False          |
| arachnoid        | False          | False           | True         | False          | False          |
| archigenes       | True           | False           | False        | False          | False          |
| argilla          | False          | True            | False        | False          | False          |
| aristolochia     | True           | False           | False        | False          | False          |
| aristotle        | True           | False           | False        | False          | False          |
| arm              | False          | False           | False        | True           | False          |
| armpit           | False          | False           | False        | True           | False          |
| aromatic         | False          | True            | False        | False          | False          |
| arsenic          | False          | True            | False        | False          | False          |
| artemisia        | False          | True            | False        | False          | False          |
| artery           | False          | False           | False        | True           | False          |

## Output:


---

## Data-transform-reshape__pivot_test4

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Found: 21-Oct-19 10:21:14                                        |
|:-----------------------------------------------------------------|
| Title: Canon EF 100mm f/2.8L Macro IS USM                        |
| Price: 6900 kr                                                   |
| Link: https://www.finn.no/bap/forsale/ad.html?finnkode=161065896 |
| Found: 21-Oct-19 10:21:14                                        |
| Title: Canon EF 100mm f/2.8L Macro IS USM                        |
| Price: 7500 kr                                                   |
| Link: https://www.finn.no/bap/forsale/ad.html?finnkode=155541389 |
| Found: 21-Oct-19 10:21:14                                        |
| Title: Panasonic Lumix G 25mm F1.4 ASPH                          |
| Price: 3200 kr                                                   |
| Link: https://www.finn.no/bap/forsale/ad.html?finnkode=161066674 |

## Output:


---

## Data-transform-reshape__explode_test16

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| Model # Final   | Colour1                                 |
|:----------------|:----------------------------------------|
| D1-A3621        | Natural                                 |
| D1-A3626        | Natural                                 |
| D1-A3629        | Black                                   |
| D1-AM5199       | Clear                                   |
| D1-B0003        | Silver                                  |
| D1-B0005        | Silver                                  |
| D1-B0020        | Silver                                  |
| D1-B1822        | Green/Red/Royal/White/Yellow            |
| D1-B4049        | Red/Black/Grey                          |
| D1-B4255        | Navy Plaid with Koskin pocket           |
| D1-B4394        | Black                                   |
| D1-B4878        | Black/Grey                              |
| D1-B4976        | Black                                   |
| D1-B5060        | Black                                   |
| D1-B6647        | Black/Grey                              |
| D1-B8074        | Black/White Gingham                     |
| D1-B9074        | Navy Blue/White Gingham                 |
| D1-BC0006       | Black                                   |
| D1-BL1991       | Black                                   |
| D1-BL3250       | Black                                   |
| D1-BL3264       | Black with White stitching              |
| D1-BL3275       | Black with Black stitching              |
| D1-BL3283       | Black/Black stitching                   |
| D1-BL3292       | Black with Black stitching              |
| D1-BL3711       | Black                                   |
| D1-BL3901       | Black with White stitching              |
| D1-BL5272       | Brown                                   |
| D1-BL6827       | Black                                   |
| D1-BL6953       | Brown                                   |
| D1-BL7261       | Brown                                   |
| D1-BL8590       | Brown                                   |
| D1-BQ4023       | Black/Silver (oven mitt) Silver (tools) |
| D1-BQ8875       | White/Black                             |
| D1-BQ9446       | Brown                                   |
| D1-BQ9535       | Brown                                   |
| D1-C3740        | Black                                   |
| D1-CA3499       | Black                                   |
| D1-CA3530       | Black                                   |
| D1-CA5988       | Brown                                   |
| D1-CA6499       | Black                                   |
| D1-CA6540       | Black                                   |
| D1-CA6625       | Black                                   |
| D1-CA8361       | Brown with white paper                  |
| D1-CA8634       | Brown                                   |
| D1-CA8677       | Black                                   |
| D1-CA8816       | Black                                   |
| D1-CA8993       | Black                                   |
| D1-CA8994       | Black                                   |
| D1-CA9224       | Black                                   |
| D1-CA9266       | White                                   |
| D1-CA9334       | Black                                   |
| D1-CA9394       | Black                                   |
| D1-CA9414       | Black                                   |
| D1-CA9429       | Black                                   |
| D1-CA9445       | Royal Blue                              |
| D1-CA9447       | Natural                                 |
| D1-CA9487       | Black                                   |
| D1-CA9511       | Black                                   |
| D1-CA9517       | Black                                   |
| D1-CA9530       | Black                                   |
| D1-CA9558       | Black                                   |
| D1-CA9563       | Natural                                 |
| D1-CA9633       | Black                                   |
| D1-CA9645       | Black                                   |
| D1-CA9788       | Brown/White                             |
| D1-CB2315       | Navy and Black with Black highlights    |
| D1-CB2466       | Black                                   |
| D1-CB2864       | Royal with Black highlights             |
| D1-CB290        | Black                                   |
| D1-CB297        | Navy                                    |
| D1-CB3103       | Black                                   |
| D1-CB4027       | Black                                   |
| D1-CB5027       | Black                                   |
| D1-CB5032       | Black with White Accents                |
| D1-CB5990       | Red/Black                               |
| D1-CB6544       | Grey/Black                              |
| D1-CB6657       | Grey/Black                              |
| D1-CB700        | Black with Black highlights             |
| D1-CB702        | Black                                   |
| D1-CB729        | Black with two-toned Grey/Black         |
| D1-CB730        | Black with Black trim                   |
| D1-CB734        | Black                                   |
| D1-CB790        | Black                                   |
| D1-CB800        | Heathered Grey                          |
| D1-CB800        | Black                                   |
| D1-CB801        | Black                                   |
| D1-CB847        | Black                                   |
| D1-CB8569       | Black                                   |
| D1-CB8759       | Black                                   |
| D1-CB9157       | Black                                   |
| D1-CB9178       | Black                                   |
| D1-CB9227       | Black/Grey                              |
| D1-CB9238       | Grey                                    |
| D1-CB9389       | Black                                   |
| D1-CB9391       | Light Grey/Black                        |
| D1-CB9406       | Black                                   |
| D1-CB9434       | Light Grey/Black                        |
| D1-CB9564       | Black                                   |
| D1-CB9570       | Black                                   |
| D1-CM1308       | White/Black                             |

## Output:


---

## Data-transform-reshape__subtitle_test11

**Task:** Data-transform-reshape

**Input:**

Given a table, predict what python pandas transformation may be needed on the given input table. Valid choices for transformation include: {"stack", "wide_to_long", "transpose", "pivot", "explode", "ffill", "subtitles"}. Note that each of these is a common Python Pandas operator. Some transformations can have parameters. Each transformation and its parameters are describe as follows.
 
- stack: collapse homogeneous cols into rows.
@param (int): stack_start_idx: zero-based starting column index of the homogeneous column-group.
@param (int): stack_end_idx: zero-based ending column index of the homogeneous column-group.
 
- wide_to_long: collapse repeating col-groups into rows.
@param (int): wide_to_long_start_idx: zero-based starting column index of the repeating col-groups.
@param (int): wide_to_long_end_idx: zero-based ending column index of the repeating col-groups.
 
- transpose: convert rows to columns and vice versa.
 
- pivot: pivot repeating row-groups into cols.
@param (int): pivot_row_frequency: frequency of repeating row-groups.
 
- ffill: fill structurally empty cells in tables.
@param (int): ffill_end_idx: zero-based ending column index of the columns to be filled.
 
- explode: convert composite cells into atomic values
@param (int): explode_column_idx: zero-based column index of the column to be exploded.
 
- subtitle: convert table subtitles into a column.
 
OUTPUT the predicted transformation name along with its parameters for the given INPUT table in a JSON, e.g., {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}. If the input table needs multi-step transformations (e.g, ffill followed by stack), list JSON of each transformation sequentially in a list, e.g., [{"transformation": "ffill", "ffill_end_idx": 1}, {"transformation": "stack", "stack_start_idx": 1, "stack_end_idx": 5}]. No explanation is needed.

## Input:
| State/Loan Type               | Balance            | Interest Payments   | Principal Payments   | Total Payments     | Volume Weighted Avg Interest Rate     | Debt Waived   | Balance            |
|                               | 30/06/2017         |                     |                      |                    | (for 2017-18)                         |               | 29/06/2018         |
|                               |                    | '$'000              |                      |                    | %                                     |               |                    |
|                               | '$'000             |                     | '$'000               | '$'000             |                                       | '$'000        | '$'000             |
|:------------------------------|:-------------------|:--------------------|:---------------------|:-------------------|:--------------------------------------|:--------------|:-------------------|
| New South Wales Government    |                    |                     |                      |                    |                                       |               |                    |
| 0                             | 521047.68033000006 | 23231.52181         | 37418.22822          | 60649.75003        | 4.4586172603794259                    | 0.0           | 483629.4521100001  |
| 1                             | 1189.7793300000003 | 47.59117            | 112.42583            | 160.017            | 3.9999997310425606                    | 0.0           | 1077.3535000000006 |
| 2                             | 375999.35841       | 16919.971129999998  | 9791.89425           | 26711.865380000003 | 4.5000000004122347                    | 0.0           | 366207.46416       |
| 3                             | 898236.81807       | 40199.08411         | 47322.5483           | 87521.63240999998  | 4.4753324848533715                    | 0.0           | 850914.2697700001  |
| Queensland Government         |                    |                     |                      |                    |                                       |               |                    |
| 0                             | 152256.84152000005 | 6683.1175           | 10097.77933          | 16780.896829999998 | 4.3893709033246457                    | 0.0           | 142159.06219000006 |
| 1                             | 118.97822          | 4.75911             | 11.24259             | 16.0017            | 3.9999841987886522                    | 0.0           | 107.73563          |
| 2                             | 134752.80206999995 | 6063.8761           | 3602.4334200000003   | 9666.30952         | 4.5000000050833835                    | 0.0           | 131150.36864999993 |
| 3                             | 287128.62181       | 12751.75271         | 13711.45534          | 26463.20805        | 4.4411290764451019                    | 0.0           | 273417.16647000005 |
| South Australia Government    |                    |                     |                      |                    |                                       |               |                    |
| 0                             | 38192.16307000002  | 2002.81765          | 2883.0807600000003   | 4885.89841         | 5.2440539864923643                    | 0.0           | 35309.08231000001  |
| 1                             | 0.0                | 0.0                 | 0.0                  | 0.0                | ..                                    | 0.0           | 0.0                |
| 2                             | 163779.2486895259  | 7370.0662           | 4096.32305           | 11466.38925        | 4.5000000054776992                    | 0.0           | 159682.9256395259  |
| 3                             | 201971.411759526   | 9372.88385          | 6979.40381           | 16352.28766        | 4.6406982891022599                    | 0.0           | 194992.0079495259  |
| Western Australia Government  |                    |                     |                      |                    |                                       |               |                    |
| 0                             | 142421.76752000005 | 6365.1939600000005  | 9724.58473           | 16089.77869        | 4.4692564000837489                    | 0.0           | 132697.18279000005 |
| 1                             | 135.97477999999995 | 5.43899             | 12.84865             | 18.28764           | 3.9999991174834051                    | 0.0           | 123.12612999999996 |
| 2                             | 229864.31296       | 10343.89408         | 6245.72417           | 16589.61825        | 4.4999999986078745                    | 0.0           | 223618.58879       |
| 3                             | 372422.05526000005 | 16714.527029999994  | 15983.15755          | 32697.68458        | 4.4880604663252388                    | 0.0           | 356438.8977100001  |
| Tasmania Government           |                    |                     |                      |                    |                                       |               |                    |
| 0                             | 73607.10866000001  | 3241.68287          | 5140.974020000001    | 8382.65689         | 4.4040350572302982                    | 0.0           | 68466.13464000003  |
| 1                             | 101.98122          | 4.07925             | 9.63649              | 13.71574           | 4.0000011766872365                    | 0.0           | 92.34473           |
| 2                             | 99582.51227        | 4481.21305          | 2625.5371800000007   | 7106.75023         | 4.4999999978409848                    | 0.0           | 96956.97509        |
| 3                             | 173291.60215000005 | 7726.975169999998   | 7776.147690000001    | 15503.12286        | 4.4589438115481101                    | 0.0           | 165515.45446000007 |
| Northern Territory Government |                    |                     |                      |                    |                                       |               |                    |
| 0                             | 23973.87107        | 1078.8242           | 904.09792            | 1982.92212         | 4.5000000077167357                    | 0.0           | 23069.77315        |
| 2                             | 132070.58797999992 | 5943.17644          | 3259.595810000001    | 9202.77225         | 4.4999999855380395                    | 0.0           | 128810.99216999992 |
| 3                             | 156044.45904999992 | 7022.00064          | 4163.69373           | 11185.69437        | 4.4999999889454605                    | 0.0           | 151880.76531999992 |
| All State and NT Governments  |                    |                     |                      |                    |                                       |               |                    |
| 0                             | 951499.43217       | 42603.15799         | 66168.74497999999    | 108771.90297       | 4.4774759237468764                    | 0.0           | 885330.6871900002  |
| 1                             | 133617.30152999994 | 61.86852            | 146.15356            | 208.02208          | 4.630277613121022E-2                  | 0.0           | 130211.55215999992 |
| 2                             | 1003978.234399526  | 51122.197           | 29621.50788          | 80743.70487999999  | 5.0919626789096597                    | 0.0           | 977616.3223295256  |
| 3                             | 2089094.968099526  | 93787.22351         | 95936.40641999998    | 189723.62993       | 4.4893709928045702                    | 0.0           | 1993158.5616795253 |

## Output:


---

## Formula-prediction-context__case-464

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A                                                                                                                              | B        | C             | D                | E                   | F                   | G   | H                  | I                  | J                   | K                   | L   |
|---:|:-------------------------------------------------------------------------------------------------------------------------------|:---------|:--------------|:-----------------|:--------------------|:--------------------|:----|:-------------------|:-------------------|:--------------------|:--------------------|:----|
|  1 |                                                                                                                                |          |               |                  |                     |                     |     |                    |                    |                     |                     |     |
|  2 | Conditions: 107 sps; BckCal off; A=64; CHScan from CH0 to CH1; ScanMode 2; 24 bit values; quiet sensors plugged at CH0 and CH1 |          |               |                  |                     |                     |     |                    |                    |                     |                     |     |
|  3 | CH0 and CH1 are raw data collected from consecutives samples.                                                                  |          |               |                  |                     |                     |     |                    |                    |                     |                     |     |
|  4 | For each channel and sample ErrorCHx is calculated as Chxi - CHx average                                                       |          |               |                  |                     |                     |     |                    |                    |                     |                     |     |
|  5 |                                                                                                                                |          |               |                  |                     |                     |     |                    |                    |                     |                     |     |
|  6 |                                                                                                                                |          | Noisy chip    |                  |                     |                     |     | Clean chip         |                    |                     |                     |     |
|  7 |                                                                                                                                |          | CH0 Avg       | CH1 Avg.         | CH0 Sigma           | CH1 Sigma           |     | CH0 Avg            | CH1 Avg.           | CH0 Sigma           | CH1 Sigma           |     |
|  8 |                                                                                                                                |          | [Target Cell] | 268171.717884131 | 701.0669740700016   | 729.3689267572686   |     | 199440.67088607594 | 268134.56962025317 | 70.59790363081156   | 75.95090652947542   |     |
|  9 | Ram Address                                                                                                                    | Sample N | CH0           | CH1              | Error CH0           | ErrorCH1            |     | CH0                | CH1                | Error CH0           | ErrorCH1            |     |
| 10 | 0x2D1A                                                                                                                         | 0        | 199465        | 268144           | -12.496221662469907 | -27.71788413100876  |     | 199486             | 268184             | 45.32911392406095   | 49.43037974683102   |     |
| 11 | 0x2D1E                                                                                                                         | 1        | 199265        | 268204           | -212.4962216624699  | 32.28211586899124   |     | 199520             | 268207             | 79.32911392406095   | 72.43037974683102   |     |
| 12 | 0x2D22                                                                                                                         | 2        | 199371        | 268103           | -106.4962216624699  | -68.71788413100876  |     | 199446             | 268103             | 5.329113924060948   | -31.569620253168978 |     |
| 13 | 0x2D26                                                                                                                         | 3        | 199405        | 268356           | -72.4962216624699   | 184.28211586899124  |     | 199480             | 268116             | 39.32911392406095   | -18.569620253168978 |     |
| 14 | 0x2D2A                                                                                                                         | 4        | 199226        | 268230           | -251.4962216624699  | 58.28211586899124   |     | 199375             | 268141             | -65.67088607593905  | 6.430379746831022   |     |
| 15 | 0x2D2E                                                                                                                         | 5        | 199307        | 268268           | -170.4962216624699  | 96.28211586899124   |     | 199584             | 268050             | 143.32911392406095  | -84.56962025316898  |     |
| 16 | 0x2D32                                                                                                                         | 6        | 199418        | 268377           | -59.49622166246991  | 205.28211586899124  |     | 199411             | 268074             | -29.670886075939052 | -60.56962025316898  |     |
| 17 | 0x2D36                                                                                                                         | 7        | 199359        | 268237           | -118.4962216624699  | 65.28211586899124   |     | 199530             | 268035             | 89.32911392406095   | -99.56962025316898  |     |
| 18 | 0x2D3A                                                                                                                         | 8        | 199504        | 268064           | 26.503778337530093  | -107.71788413100876 |     | 199380             | 268059             | -60.67088607593905  | -75.56962025316898  |     |



---

## Formula-prediction-context__case-433

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | B   | C   | D   |   E |   F | G   |   H |   I |   J |   K | L             |   M |   N |   O |   P |   Q |   R |   S |   T |   U |   V |
|---:|:----|:----|:----|----:|----:|:----|----:|----:|----:|----:|:--------------|----:|----:|----:|----:|----:|----:|----:|----:|----:|----:|
| 45 |     |     |     |   1 |   3 | A   |  11 |  11 |   3 | -10 | -5            |  13 |  18 |  17 |  22 |  17 |  14 |  13 |  14 |  13 |  13 |
| 46 |     |     |     |   1 |   4 | A   |  11 |  11 |   3 | -10 | -4            |  12 |  18 |  17 |  23 |  17 |  14 |  12 |  13 |  13 |  13 |
| 47 |     |     |     |   0 |   1 | A   |  12 |  12 |   3 | -10 | -10           | -99 | -99 | -99 | -99 | -99 | -99 | -99 | -99 | -99 | -99 |
| 48 |     |     |     |   0 |   2 | A   |  12 |  12 |   3 | -10 | -7            | -99 | -96 | -99 | -96 | -99 | -99 | -99 | -99 | -99 | -99 |
| 49 |     |     |     |   0 |   3 | A   |  12 |  12 |   3 | -10 | -5            | -99 | -94 | -99 | -94 | -99 | -99 | -99 | -99 | -99 | -99 |
| 50 |     |     |     |   0 |   4 | A   |  12 |  12 |   3 | -10 | -4            | -99 | -93 | -99 | -93 | -99 | -99 | -99 | -99 | -99 | -99 |
| 51 |     |     |     |   0 |   1 | A   |  13 |  13 |   3 | -10 | -10           | -99 | -99 | -99 | -99 | -99 | -99 | -99 | -99 | -99 | -99 |
| 52 |     |     |     |   0 |   2 | A   |  13 |  13 |   3 | -10 | -7            | -99 | -96 | -99 | -96 | -99 | -99 | -99 | -99 | -99 | -99 |
| 53 |     |     |     |   0 |   3 | A   |  13 |  13 |   3 | -10 | -5            | -99 | -94 | -99 | -94 | -99 | -99 | -99 | -99 | -99 | -99 |
| 54 |     |     |     |   0 |   4 | A   |  13 |  13 |   3 | -10 | -4            | -99 | -93 | -99 | -93 | -99 | -99 | -99 | -99 | -99 | -99 |
| 55 |     |     |     |   1 |   1 | E   |   1 |   1 |   3 | -10 | [Target Cell] |  13 |  13 |  16 |  16 |  13 |  16 | -99 |  16 | -99 | -99 |
| 56 |     |     |     |   1 |   2 | E   |   1 |   1 |   3 | -10 | -7            |  10 |  13 |  13 |  16 |  10 |  13 |  10 |  13 |  13 | -99 |
| 57 |     |     |     |   1 |   3 | E   |   1 |   1 |   3 | -10 | -5            |   7 |  12 |  12 |  17 |   8 |  11 |   7 |  11 |  11 |  11 |
| 58 |     |     |     |   1 |   4 | E   |   1 |   1 |   3 | -10 | -4            |   4 |  10 |  10 |  16 |   7 |  10 |   4 |  10 |  10 |  10 |
| 59 |     |     |     |   1 |   1 | E   |   2 |   2 |   3 | -10 | -10           |  13 |  13 |  16 |  16 |  13 |  16 | -99 |  16 | -99 | -99 |
| 60 |     |     |     |   1 |   2 | E   |   2 |   2 |   3 | -10 | -7            |  10 |  13 |  13 |  16 |  10 |  13 |  10 |  13 |  13 | -99 |
| 61 |     |     |     |   1 |   3 | E   |   2 |   2 |   3 | -10 | -5            |   7 |  12 |  12 |  17 |   8 |  11 |   7 |  11 |  11 |  11 |
| 62 |     |     |     |   1 |   4 | E   |   2 |   2 |   3 | -10 | -4            |   4 |  10 |  10 |  16 |   7 |  10 |   4 |  10 |  10 |  10 |
| 63 |     |     |     |   1 |   1 | E   |   3 |   3 |   3 | -10 | -10           |  13 |  13 |  16 |  16 |  13 |  16 | -99 |  16 | -99 | -99 |
| 64 |     |     |     |   1 |   2 | E   |   3 |   3 |   3 | -10 | -7            |  10 |  13 |  13 |  16 |  10 |  13 |  10 |  13 |  13 | -99 |
| 65 |     |     |     |   1 |   3 | E   |   3 |   3 |   3 | -10 | -5            |   7 |  12 |  12 |  17 |   8 |  11 |   7 |  11 |  11 |  11 |



---

## Formula-prediction-context__case-751

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    |      D |       E | F   | G                  |      H |      I |      J |      K |       L | M                  | N                  |      O |      P |      Q |       R | S                  |      T |      U |      V |      W | X   |
|---:|-------:|--------:|:----|:-------------------|-------:|-------:|-------:|-------:|--------:|:-------------------|:-------------------|-------:|-------:|-------:|--------:|:-------------------|-------:|-------:|-------:|-------:|:----|
| 44 | 0.3129 | 8557    | N/A | ---                | 3.2797 | 2.994  | 2.4639 | 3.0192 | 8557    | ---                | 3.2797             | 2.994  | 2.4639 | 3.0192 | 8557    | ---                | 3.2797 | 2.994  | 2.4639 | 3.0192 |     |
| 45 | 0.3134 | 8769    | N/A | 3.2779             | 3.7024 | 2.9586 | 2.1584 | 3.0167 | 8769    | 3.2779             | 3.7024             | 2.9586 | 2.1584 | 3.0167 | 8769    | 3.2779             | 3.7024 | 2.9586 | 2.1584 | 3.0167 |     |
| 46 | 0.3139 | 8692.34 | N/A | 3.5644             | 4.026  | 3.1519 | 2.3471 | 3.2803 | 8692.34 | 3.5644             | 4.026              | 3.1519 | 2.3471 | 3.2803 | 8692.34 | 3.5644             | 4.026  | 3.1519 | 2.3471 | 3.2803 |     |
| 47 | 0.3145 | 8680.54 | N/A | 3.7103             | 4.1907 | 3.2734 | 2.4431 | 3.4146 | 8680.54 | 3.7103             | 4.1907             | 3.2734 | 2.4431 | 3.4146 | 8680.54 | 3.7103             | 4.1907 | 3.2734 | 2.4431 | 3.4146 |     |
| 48 | 0.315  | 8512    | N/A | 3.6706             | 4.1459 | 3.29   | 2.417  | 3.3781 | 8512    | 3.6706             | 4.1459             | 3.29   | 2.417  | 3.3781 | 8512    | 3.6706             | 4.1459 | 3.29   | 2.417  | 3.3781 |     |
| 49 | 0.3155 | 8383    | N/A | 3.4099             | 3.8514 | 3.0404 | 2.2453 | 3.1381 | 8383    | 3.4099             | 3.8514             | 3.0404 | 2.2453 | 3.1381 | 8383    | 3.4099             | 3.8514 | 3.0404 | 2.2453 | 3.1381 |     |
| 50 | 0.316  | 8356.59 | N/A | 3.3335             | 3.7651 | 2.9653 | 2.195  | 3.0678 | 8356.59 | 3.3335             | 3.7651             | 2.9653 | 2.195  | 3.0678 | 8356.59 | 3.3335             | 3.7651 | 2.9653 | 2.195  | 3.0678 |     |
| 51 | 0.3165 | 8553    | N/A | ---                | 3.0413 | 2.8071 | 2.2848 | 2.7996 | 8553    | ---                | 3.0413             | 2.8071 | 2.2848 | 2.7996 | 8553    | ---                | 3.0413 | 2.8071 | 2.2848 | 2.7996 |     |
| 52 | 0.3171 | 8545    | N/A | ---                | 3.2399 | 2.9657 | 2.434  | 2.9825 | 8545    | ---                | 3.2399             | 2.9657 | 2.434  | 2.9825 | 8545    | ---                | 3.2399 | 2.9657 | 2.434  | 2.9825 |     |
| 53 | 0.3176 | 8361    | N/A | ---                | 3.2939 | 3.0514 | 2.5084 | 3.0456 | 8361    | ---                | 3.2939             | 3.0514 | 2.5084 | 3.0456 | 8361    | ---                | 3.2939 | 3.0514 | 2.5084 | 3.0456 |     |
| 54 | 0.3181 | 8168.76 | N/A | ---                | 2.9817 | 2.7508 | 2.2707 | 2.757  | 8168.76 | ---                | [Target Cell]      | 2.7508 | 2.2707 | 2.757  | 8168.76 | ---                | 2.9817 | 2.7508 | 2.2707 | 2.757  |     |
| 55 | 0.3186 | 8231.98 | N/A | ---                | 2.4558 | 2.2518 | 1.8702 | 2.2707 | 8231.98 | ---                | 2.4558             | 2.2518 | 1.8702 | 2.2707 | 8231.98 | ---                | 2.4558 | 2.2518 | 1.8702 | 2.2707 |     |
| 56 | 0.3192 | 8151    | N/A | ---                | 2.4536 | 2.2612 | 1.8685 | 2.2687 | 8151    | ---                | 2.4536             | 2.2612 | 1.8685 | 2.2687 | 8151    | ---                | 2.4536 | 2.2612 | 1.8685 | 2.2687 |     |
| 57 | 0.3197 | 7959    | N/A | 2.5953             | 2.9199 | 2.3324 | 1.7356 | 2.3935 | 7959    | 2.5953             | 2.9199             | 2.3324 | 1.7356 | 2.3935 | 7959    | 2.5953             | 2.9199 | 2.3324 | 1.7356 | 2.3935 |     |
| 58 | 0.3202 | 8250.4  | N/A | 2.728              | 3.0691 | 2.4197 | 1.8243 | 2.5159 | 8250.4  | 2.728              | 3.0691             | 2.4197 | 1.8243 | 2.5159 | 8250.4  | 2.728              | 3.0691 | 2.4197 | 1.8243 | 2.5159 |     |
| 59 | 0.3207 | 7908    | N/A | 3.3676999999999997 | 3.7889 | 3.0471 | 2.2521 | 3.1059 | 7908    | 3.3676999999999997 | 3.7889             | 3.0471 | 2.2521 | 3.1059 | 7908    | 3.3676999999999997 | 3.7889 | 3.0471 | 2.2521 | 3.1059 |     |
| 60 | 0.3213 | 6562.41 | N/A | 3.4542             | 3.8862 | 3.0571 | 2.3099 | 3.1857 | 6562.41 | 3.4542             | 3.8862             | 3.0571 | 2.3099 | 3.1857 | 6562.41 | 3.4542             | 3.8862 | 3.0571 | 2.3099 | 3.1857 |     |
| 61 | 0.3218 | 6686.54 | N/A | 3.5742999999999996 | 4.0213 | 3.196  | 2.3903 | 3.2964 | 6686.54 | 3.5742999999999996 | 4.0213             | 3.196  | 2.3903 | 3.2964 | 6686.54 | 3.5742999999999996 | 4.0213 | 3.196  | 2.3903 | 3.2964 |     |
| 62 | 0.3223 | 6514.84 | N/A | 3.5173             | 3.9571 | 3.161  | 2.3521 | 3.2438 | 6514.84 | 3.5173             | 3.9571             | 3.161  | 2.3521 | 3.2438 | 6514.84 | 3.5173             | 3.9571 | 3.161  | 2.3521 | 3.2438 |     |
| 63 | 0.3229 | 6415    | N/A | ---                | 3.3939 | 3.1396 | 2.5846 | 3.1381 | 6415    | ---                | 3.3938999999999995 | 3.1396 | 2.5846 | 3.1381 | 6415    | ---                | 3.3939 | 3.1396 | 2.5846 | 3.1381 |     |
| 64 | 0.3234 | 6448    | N/A | ---                | 3.787  | 3.4978 | 2.8839 | 3.5016 | 6448    | ---                | 3.787              | 3.4978 | 2.8839 | 3.5016 | 6448    | ---                | 3.787  | 3.4978 | 2.8839 | 3.5016 |     |



---

## Formula-prediction-context__case-166

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|      | BG     | BH                                            | BI        |       BJ | BK                                      | BL                                    |    BM |   BN | BO   | BP   | BQ            | BR   | BS   |
|-----:|:-------|:----------------------------------------------|:----------|---------:|:----------------------------------------|:--------------------------------------|------:|-----:|:-----|:-----|:--------------|:-----|:-----|
| 8959 | Orange | Select Operate: CTS-500 (No Remote Asst Svc)  | ROS RMS F |    10390 | INTERNATIONAL PAPER COMPANY             | INTERNATIONAL PAPER                   |  0    |    0 |      |      | 0             |      |      |
| 8960 | Orange | Select Operate: CTS-1300 (No Remote Asst Svc) | ROS RMS F | 89159470 | SWISS RE                                | SWISS REINSURANCE                     |  0    |    0 |      |      | 0             |      |      |
| 8961 | Orange | Select Operate: CTS-1300 (No Remote Asst Svc) | ROS RMS F |   218124 | SWISS RE AMERICA HOLDING CORPORATION    | SWISS REINSURANCE                     |  0    |    0 |      |      | 0             |      |      |
| 8962 | Orange | Select Operate: CTS-1300 (No Remote Asst Svc) | ROS RMS F |   218124 | SWISS RE AMERICA HOLDING CORPORATION    | SWISS RE AMERICA HOLDING CORPORATION  |  0    |    0 |      |      | 0             |      |      |
| 8963 | Orange | Select Operate: CTS-1300 (No Remote Asst Svc) | ROS RMS F |    48772 | SWISS RE INVESTORS INC                  | SWISS RE                              |  0    |    0 |      |      | 0             |      |      |
| 8964 | Orange | Select Operate: CTS-1300 (No Remote Asst Svc) | ROS RMS F |    41297 | SWISS RE TREASURY US CORP               | SWISS RE AMERICAS HOLDING CORPORATION |  0    |    0 |      |      | 0             |      |      |
| 8965 | Orange | Select Operate: CTS-1300 (No Remote Asst Svc) | ROS RMS F |   223103 | SWISS RE FINANCIAL SERVICES CORPORATION | SWISS RE                              |  0    |    0 |      |      | 0             |      |      |
| 8966 | Orange | Select Operate: CTS-1300 (No Remote Asst Svc) | ROS RMS F |   136628 | SWISS RE UNDERWRITERS AGENCY            | SWISS RE                              |  0    |    0 |      |      | 0             |      |      |
| 8967 | Orange | Select Operate: CTS-1300 (No Remote Asst Svc) | ROS RMS F |    15612 | SWISS REINSURANCE AMERICA CORPORATION   | SWISS REINSURANCE                     |  0    |    0 |      |      | 0             |      |      |
| 8968 | Orange | Select Operate: CTS-1300 (No Remote Asst Svc) | ROS RMS F |   831008 | SWISS REINSURANCE COMPANY CANADA        | SWISS RE CANADA                       |  0    |    0 |      |      | 0             |      |      |
| 8969 | Orange | SMARTnet Maintenance                          | SMARTNET  |    15501 | AT&T CORP.                              | AT&T CORPORATION                      | 40.55 |    0 |      |      | [Target Cell] |      |      |
| 8970 | Orange | SMARTnet Maintenance                          | SMARTNET  |    10173 | STANLEY BLACK & DECKER INC              | STANLEY BLACK & DECKER                |  0    |    0 |      |      | 0             |      |      |
| 8971 | Orange | SMARTnet Maintenance                          | SMARTNET  |    10173 | STANLEY BLACK & DECKER INC              | STANLEY BLACK & DECKER                |  0    |    0 |      |      | 0             |      |      |
| 8972 | Orange | SMARTnet Maintenance                          | SMARTNET  |    10173 | STANLEY BLACK & DECKER INC              | STANLEY BLACK & DECKER                |  0    |    0 |      |      | 0             |      |      |
| 8973 | Orange | SMARTnet Maintenance                          | SMARTNET  |    10924 | STANLEY SECURITY SOLUTIONS INC          | STANLEY                               |  0    |    0 |      |      | 0             |      |      |
| 8974 | Orange | SMARTnet Maintenance                          | SMARTNET  |    10173 | STANLEY BLACK & DECKER INC              | STANLEY BLACK & DECKER                |  0    |    0 |      |      | 0             |      |      |
| 8975 | Orange | SMARTnet Maintenance                          | SMARTNET  |    10173 | STANLEY BLACK & DECKER INC              | STANLEY BLACK & DECKER                |  0    |    0 |      |      | 0             |      |      |
| 8976 | Orange | SMARTnet Maintenance                          | SMARTNET  |    10924 | STANLEY SECURITY SOLUTIONS INC          | STANLEY                               |  0    |    0 |      |      | 0             |      |      |
| 8977 | Orange | SMARTnet Maintenance                          | SMARTNET  |    10400 | THE BLACK & DECKER CORPORATION          | STANLEY BLACK & DECKER                |  0    |    0 |      |      | 0             |      |      |
| 8978 | Orange | SMARTnet Maintenance                          | SMARTNET  |    10400 | THE BLACK & DECKER CORPORATION          | STANLEY BLACK & DECKER                |  0    |    0 |      |      | 0             |      |      |
| 8979 | Orange | SMARTnet Maintenance                          | SMARTNET  |    10400 | THE BLACK & DECKER CORPORATION          | STANLEY BLACK & DECKER                |  0    |    0 |      |      | 0             |      |      |



---

## Formula-prediction-context__case-529

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A   | B                                                                   | C   | D   | E                                                        | F                   | G    | H   | I   | J   | K   | L   | M   | N   | O   | P   |
|---:|:----|:--------------------------------------------------------------------|:----|:----|:---------------------------------------------------------|:--------------------|:-----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
| 37 |     |                                                                     |     |     |                                                          |                     |      |     |     |     |     |     |     |     |     |     |
| 38 |     | Step 2: Current Limit and Circuit Breaker                           |     |     | Current Limit Range (CL)                                 | 26 mV               |      |     |     |     |     |     |     |     |     |     |
| 39 |     |                                                                     |     |     | Maximum Recommended Value for Effective Sense Resistance | 0.16849684968496847 | mW   |     |     |     |     |     |     |     |     |     |
| 40 |     |                                                                     |     |     | Use External Resistor Divider to Reduce Effecitve RS     | Yes                 |      |     |     |     |     |     |     |     |     |     |
| 41 |     |                                                                     |     |     | Enter the Resistance for RS                              | 0.25                | mW   |     |     |     |     |     |     |     |     |     |
| 42 |     |                                                                     |     |     | Recommended Value for RCL1                               | 10                  | W    |     |     |     |     |     |     |     |     |     |
| 43 |     |                                                                     |     |     | Recommended Value for RCL2                               | 4.690170940170941   | W    |     |     |     |     |     |     |     |     |     |
| 44 |     |                                                                     |     |     | Enter value for RCL1                                     | 10                  | W    |     |     |     |     |     |     |     |     |     |
| 45 |     | Steps 1 & 2: Operating Conditions, Current Limit, & Circuit Breaker |     |     | Enter value for RCL2                                     | 4.7                 | W    |     |     |     |     |     |     |     |     |     |
| 46 |     |                                                                     |     |     | Effective Sense Resistance (RS,EFF)                      | 0.17006802721088435 | mW   |     |     |     |     |     |     |     |     |     |
| 47 |     |                                                                     |     |     | Resulting Minimum Current Limit                          | [Target Cell]       | A    |     |     |     |     |     |     |     |     |     |
| 48 |     |                                                                     |     |     | Resulting Typical Current Limit                          | 152.88              | A    |     |     |     |     |     |     |     |     |     |
| 49 |     |                                                                     |     |     | Resulting Maximum Current Limit                          | 168.168             | A    |     |     |     |     |     |     |     |     |     |
| 50 |     |                                                                     |     |     | Maximum Power Dissipation in RS                          | 7.070119056         | W    |     |     |     |     |     |     |     |     |     |
| 51 |     |                                                                     |     |     | Fault Response                                           | Latch Off           |      |     |     |     |     |     |     |     |     |     |
| 52 |     |                                                                     |     |     | Circuit Breaker to Current Limit Raitio                  | 1.9 x Current Limit |      |     |     |     |     |     |     |     |     |     |
| 53 |     | Step 3: MOSFET Selection                                            |     |     | Q1 FET Name                                              | SQM120N10-3m8       |      |     |     |     |     |     |     |     |     |     |
| 54 |     |                                                                     |     |     | Estimated MOSFET RQJA                                    | 30                  | oC/W |     |     |     |     |     |     |     |     |     |
| 55 |     |                                                                     |     |     | Number of MosFETs                                        | 6                   | #    |     |     |     |     |     |     |     |     |     |
| 56 |     |                                                                     |     |     | MOSFET On resistance @ TJ,DC                             | 6.4                 | mW   |     |     |     |     |     |     |     |     |     |
| 57 |     |                                                                     |     |     | Maximum FET Junction Temperature                         | 125                 | oC   |     |     |     |     |     |     |     |     |     |



---

## Formula-prediction-context__case-417

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A   | B                                                                                            | C   | D   | E   | F   | G                                                               | H   | I   | J                        | K      | L        | M   | N   | O   |
|---:|:----|:---------------------------------------------------------------------------------------------|:----|:----|:----|:----|:----------------------------------------------------------------|:----|:----|:-------------------------|:-------|:---------|:----|:----|:----|
|  1 |     |                                                                                              |     |     |     |     | Pacific Gas and Electric Company                                |     |     |                          |        |          |     |     |     |
|  2 |     |                                                                                              |     |     |     |     | ENERGY PRICES FOR QUALIFYING FACILITIES                         |     |     |                          |        |          |     |     |     |
|  3 |     |                                                                                              |     |     |     |     | PER LEGACY AMENDMENT PRICING OPTION B                           |     |     |                          |        |          |     |     |     |
|  4 |     |                                                                                              |     |     |     |     |                                                                 |     |     |                          |        |          |     |     |     |
|  5 |     |                                                                                              |     |     |     |     | [Target Cell]                                                   |     |     |                          |        |          |     |     |     |
|  6 |     |                                                                                              |     |     |     |     | Submitted 07/09/2021                                            |     |     |                          |        |          |     |     |     |
|  7 |     |                                                                                              |     |     |     |     | Prepared pursuant to Decision D.10-12-035 and Resolution E-4246 |     |     |                          |        |          |     |     |     |
|  8 |     | 2021-07-01 00:00:00                                                                          |     |     |     |     |                                                                 |     |     | Energy Prices ($/kWh)    | Winter | Summer   |     |     |     |
|  9 |     |                                                                                              |     |     |     |     |                                                                 |     |     |                          |        |          |     |     |     |
| 10 |     | Energy price (EP) in $/kWh is calculated based on substituting the variables below           |     |     |     |     |                                                                 |     |     | Peak                     | 0      | 0.059089 |     |     |     |
| 11 |     | into the formula adopted in D.10-12-035:                                                     |     |     |     |     |                                                                 |     |     | Partial-Peak             | 0      | 0.059089 |     |     |     |
| 12 |     |                                                                                              |     |     |     |     |                                                                 |     |     | Off-Peak                 | 0      | 0.059089 |     |     |     |
| 13 |     | EP = [(Applicable HR * BTGP / 10^6) + VOM] * TOU                                             |     |     |     |     |                                                                 |     |     | Super Off-Peak           | 0      | 0.059089 |     |     |     |
| 14 |     | These energy prices do not include applicable Locational Adjustments (LA) under D.10-12-035. |     |     |     |     |                                                                 |     |     | Monthly Weighted Average | 0      | 0.059089 |     |     |     |
| 15 |     |                                                                                              |     |     |     |     |                                                                 |     |     |                          |        |          |     |     |     |



---

## Formula-prediction-context__case-810

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A    | B   | C     | D      | E                   | F   | G   | H    | I   | J      | K             | L                   | M                   | N   | O    | P   | Q                  | R   | S                   | T   | U   |
|---:|:-----|:----|:------|:-------|:--------------------|:----|:----|:-----|:----|:-------|:--------------|:--------------------|:--------------------|:----|:-----|:----|:-------------------|:----|:--------------------|:----|:----|
| 22 | 15.0 |     | 8.66  | 50.0   | -58.66              | 0.0 |     | 15.0 |     | -11.04 | 140.8         | -144.43             | -14.669999999999987 |     | 15.0 |     | 2.38               | 0.0 | -2.38               | 0.0 |     |
| 23 | 16.0 |     | 8.94  | 50.0   | -58.94              | 0.0 |     | 16.0 |     | -11.33 | 140.8         | -142.24             | -12.77000000000001  |     | 16.0 |     | 2.39               | 0.0 | -2.39               | 0.0 |     |
| 24 | 17.0 |     | 9.23  | 50.0   | -59.23              | 0.0 |     | 17.0 |     | -11.63 | 140.8         | -139.84             | -10.669999999999987 |     | 17.0 |     | 2.4                | 0.0 | -2.4                | 0.0 |     |
| 25 | 18.0 |     | 9.54  | 50.0   | -59.54              | 0.0 |     | 18.0 |     | -11.96 | 140.8         | -138.29             | -9.449999999999989  |     | 18.0 |     | 2.42               | 0.0 | -2.42               | 0.0 |     |
| 26 | 19.0 |     | 9.42  | 50.0   | -59.42              | 0.0 |     | 19.0 |     | -11.83 | 140.8         | -136.42             | -7.449999999999989  |     | 19.0 |     | 2.41               | 0.0 | -2.41               | 0.0 |     |
| 27 | 20.0 |     | 8.16  | 50.0   | -58.16              | 0.0 |     | 20.0 |     | -10.52 | 140.8         | -136.4              | -6.1200000000000045 |     | 20.0 |     | 2.36               | 0.0 | -2.36               | 0.0 |     |
| 28 | 21.0 |     | 8.42  | 50.0   | -58.42              | 0.0 |     | 21.0 |     | -10.79 | 140.8         | -134.73             | -4.71999999999997   |     | 21.0 |     | 2.37               | 0.0 | -2.37               | 0.0 |     |
| 29 | 22.0 |     | 6.92  | 50.0   | -56.92              | 0.0 |     | 22.0 |     | -9.24  | 140.8         | -127.62             | 3.9399999999999977  |     | 22.0 |     | 2.32               | 0.0 | -2.32               | 0.0 |     |
| 30 | 23.0 |     | 4.56  | 50.0   | -54.56              | 0.0 |     | 23.0 |     | -6.77  | 115.8         | -118.32             | -9.289999999999992  |     | 23.0 |     | 2.21               | 0.0 | -2.21               | 0.0 |     |
| 31 | 24.0 |     | 1.66  | 50.0   | -51.66              | 0.0 |     | 24.0 |     | -3.76  | 115.8         | -107.98             | 4.059999999999988   |     | 24.0 |     | 2.1                | 0.0 | -2.1                | 0.0 |     |
| 32 |      | 0.0 | 120.2 | 1200.0 | -1320.2000000000003 | 0.0 |     |      | 0.0 |        | [Target Cell] | -3017.0500000000006 | -11.589999999999861 |     |      | 0.0 | 53.540000000000006 | 0.0 | -53.540000000000006 | 0.0 |     |
| 33 |      |     |       |        |                     |     |     |      |     |        |               |                     |                     |     |      |     |                    |     |                     |     |     |
| 34 |      |     |       |        |                     |     |     |      |     |        |               |                     |                     |     |      |     |                    |     |                     |     |     |
| 35 |      |     |       |        |                     |     |     |      |     |        |               |                     |                     |     |      |     |                    |     |                     |     |     |
| 36 |      |     |       |        |                     |     |     |      |     |        |               |                     |                     |     |      |     |                    |     |                     |     |     |
| 37 |      |     |       |        |                     |     |     |      |     |        |               |                     |                     |     |      |     |                    |     |                     |     |     |
| 38 |      |     |       |        |                     |     |     |      |     |        |               |                     |                     |     |      |     |                    |     |                     |     |     |
| 39 |      |     |       |        |                     |     |     |      |     |        |               |                     |                     |     |      |     |                    |     |                     |     |     |
| 40 |      |     |       |        |                     |     |     |      |     |        |               |                     |                     |     |      |     |                    |     |                     |     |     |
| 41 |      |     |       |        |                     |     |     |      |     |        |               |                     |                     |     |      |     |                    |     |                     |     |     |
| 42 |      |     |       |        |                     |     |     |      |     |        |               |                     |                     |     |      |     |                    |     |                     |     |     |



---

## Formula-prediction-context__case-920

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A   | B                               | C                | D     | E                                      | F                                  |
|---:|:----|:--------------------------------|:-----------------|:------|:---------------------------------------|:-----------------------------------|
| 11 |     |                                 |                  |       |                                        |                                    |
| 12 |     | SDRAM Timings                   |                  |       |                                        |                                    |
| 13 |     |                                 |                  |       |                                        |                                    |
| 14 |     | SDTIM1                          | Selected         | Units | Corresponding Register Value (decimal) | Corresponding Register Value (hex) |
|    |     | Configuration                   | Datasheet Values |       |                                        |                                    |
| 15 |     | T_RP                            | 13.75            | ns    | 9                                      | 9                                  |
| 16 |     | T_RCD                           | 13.75            | ns    | 9                                      | 9                                  |
| 17 |     | T_WR                            | 15               | ns    | 9                                      | 9                                  |
| 18 |     | T_RAS                           | 35               | ns    | 23                                     | 17                                 |
| 19 |     | T_RC                            | 48.75            | ns    | 32                                     | 20                                 |
| 20 |     | T_RRD (use T_FAW since 8 banks) | 40               | ns    | 6                                      | 6                                  |
| 21 |     | T_WTR                           | 7.5              | ns    | [Target Cell]                          | 4                                  |
| 22 |     |                                 |                  |       |                                        |                                    |
| 23 |     | SDTIM2                          | Selected         | Units | Corresponding Register Value (decimal) | Corresponding Register Value (hex) |
|    |     | Configuration                   | Datasheet Values |       |                                        |                                    |
| 24 |     | T_XP                            | 6                | ns    | 3                                      | 3                                  |
| 25 |     | T_XSNR (use T_XS)               | 270              | ns    | 179                                    | B3                                 |
| 26 |     | T_XSRD (use T_XSDLL)            | 512              | tCK   | 511                                    | 1FF                                |
| 27 |     | T_RTP                           | 7.5              | ns    | 4                                      | 4                                  |
| 28 |     | T_CKE                           | 5.625            | ns    | 3                                      | 3                                  |
| 29 |     |                                 |                  |       |                                        |                                    |
| 30 |     | SDTIM3                          | Selected         | Units | Corresponding Register Value (decimal) | Corresponding Register Value (hex) |
|    |     | Configuration                   | Datasheet Values |       |                                        |                                    |
| 31 |     | T_CKESR                         | 7.125            | ns    | 4                                      | 4                                  |



---

## Formula-prediction-context__case-879

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A              | B                                                                 |
|---:|:---------------|:------------------------------------------------------------------|
|  1 | 16             | bits                                                              |
|  2 | 65535          | steps                                                             |
|  3 | 2048           | +-range (mV)                                                      |
|  4 | 4096           | range (mV)                                                        |
|  5 |                |                                                                   |
|  6 | number of LSBs | Equivalent in (mV)                                                |
|  7 | 1              | [Target Cell]                                                     |
|  8 | 2              | 0.125001907377737                                                 |
|  9 | 3              | 0.187502861066606                                                 |
| 10 |                |                                                                   |
| 11 |                | values read by program (in mV) when measuring GND in channel zero |
| 12 | 1              | 0.0625019074068                                                   |
| 13 | 2              | 0.1250038148137                                                   |
| 14 | 3              | 0.1875057222205                                                   |
| 15 |                |                                                                   |
| 16 |                | difference between the read values and its equivalent LSB         |
| 17 | 1              | -9.53717931448383e-07                                             |



---

## Formula-prediction-context__case-663

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A          | B   |      C |      D |    E | F                  | G      |      H |      I |      J | K                  | L      | M      | N      | O      | P      | Q                  | R      | S      | T      | U      |
|---:|:-----------|:----|-------:|-------:|-----:|:-------------------|:-------|-------:|-------:|-------:|:-------------------|:-------|:-------|:-------|:-------|:-------|:-------------------|:-------|:-------|:-------|:-------|
|  7 | 2012-03-01 | B   | 3.2426 | 0.2944 | 8225 |                    | ---    | 3.5034 | 2.8162 | 2.0958 | 2.9614             |        |        |        |        |        |                    |        |        |        |        |
|  8 | 2012-04-01 | B   | 2.9129 | 0.2949 | 8225 |                    | ---    | 3.1832 | 2.5683 | 1.9043 | 2.6908000000000003 |        |        |        |        |        |                    |        |        |        |        |
|  9 | 2012-05-01 | A   | 2.7326 | 0.2953 | 8225 |                    | 3.3197 | 2.9884 | 2.369  | 1.631  | 2.5429             |        |        |        |        |        |                    | 8335.0 | 3.3811 | 3.0364 | 2.392  |
| 10 | 2012-06-01 | A   | 3.2622 | 0.2958 | 8225 |                    | 3.889  | 3.5009 | 2.7857 | 1.9107 | 2.9789999999999996 | 8600.0 | 4.0487 | 3.6446 | 2.9001 | 1.9892 | 3.1012999999999997 | 8335.0 | 3.9623 | 3.5582 | 2.8136 |
| 11 | 2012-07-01 | A   | 3.4023 | 0.2963 | 8225 |                    | 4.0401 | 3.6369 | 2.9183 | 1.9849 | 3.0947             | 8600.0 | 4.2067 | 3.7868 | 3.0386 | 2.0668 | 3.2223             | 8335.0 | 4.1165 | 3.6967 | 2.9484 |
| 12 | 2012-08-01 | A   | 3.689  | 0.2968 | 8225 |                    | 4.3486 | 3.9146 | 3.0622 | 2.1365 | 3.331              | 8600.0 | 4.5292 | 4.0772 | 3.1894 | 2.2252 | 3.4693             | 8335.0 | 4.4315 | 3.9794 | 3.0917 |
| 13 | 2012-09-01 | A   | 3.3909 | 0.2973 | 8225 |                    | 4.0292 | 3.627  | 2.9543 | 1.9796 | 3.0863             | 8600.0 | 4.1952 | 3.7765 | 3.076  | 2.0611 | 3.2135             | 8335.0 | 4.1053 | 3.6866 | 2.9862 |
| 14 | 2012-10-01 | A   | 3.7336 | 0.2978 | 8225 |                    | 4.3978 | 3.9589 | 3.0969 | 2.1607 | 3.3687             | 8600.0 | 4.5806 | 4.1234 | 3.2256 | 2.2505 | 3.5087             | 8335.0 | 4.4817 | 4.0245 | 3.1267 |
| 15 | 2012-11-01 | B   | 4.308  | 0.2983 | 8225 |                    | ---    | 4.5446 | 3.7037 | 2.7187 | 3.8415999999999997 | 8600.0 | ---    | 4.7358 | 3.8594 | 2.8331 | 4.0032             | 8335.0 | ---    | 4.6216 | 3.7452 |
| 16 | 2012-12-01 | B   | 4.564  | 0.2988 | 8225 |                    | ---    | 4.7943 | 3.9251 | 2.8681 | 4.0527             | 8600.0 | ---    | 4.9968 | 4.0909 | 2.9892 | 4.2238             | 8335.0 | ---    | 4.8759 | 3.9699 |
| 17 | 2013-01-01 | B   | 4.172  | 0.2993 | 8125 | 0.5355             | ---    | 4.6194 | 4.1533 | 2.903  | [Target Cell]      | 8500.0 | ---    | 4.3073 | 3.8728 | 2.7068 | 3.8455             | 8235.0 | ---    | 4.1968 | 3.7622 |
| 18 | 2013-02-01 | B   | 4.353  | 0.2998 | 8125 | 0.5355             | ---    | 4.7847 | 4.3194 | 3.0068 | 4.2717             | 8500.0 | ---    | 4.4802 | 4.0446 | 2.8155 | 3.9999             | 8235.0 | ---    | 4.3649 | 3.9292 |
| 19 | 2013-03-01 | B   | 4.2842 | 0.3003 | 8125 | 0.7228250022679852 | ---    | 4.8932 | 4.4142 | 3.075  | 4.3685             | 8500.0 | ---    | 4.4153 | 3.9831 | 2.7747 | 3.9419             | 8235.0 | ---    | 4.3018 | 3.8696 |
| 20 | 2013-04-01 | B   | 4.8697 | 0.3008 | 8125 | 0.7228             | ---    | 5.4265 | 4.863  | 3.4102 | 4.8447             | 8500.0 | ---    | 4.9733 | 4.4568 | 3.1253 | 4.44               | 8235.0 | ---    | 4.8442 | 4.3277 |
| 21 | 2013-05-01 | A   | 4.8988 | 0.3012 | 8125 | 0.7228             | 6.3489 | 6.1848 | 4.4048 | 2.9086 | 4.8688             | 8500.0 | 5.8226 | 5.6721 | 4.0396 | 2.6675 | 4.4652             | 8235.0 | 5.6928 | 5.5423 | 3.9098 |
| 22 | 2013-06-01 | A   | 4.9362 | 0.3017 | 8125 | 0.743              | 6.4105 | 6.2448 | 4.5399 | 2.9368 | 4.916              | 8500.0 | 5.8647 | 5.7131 | 4.1534 | 2.6868 | 4.4975             | 8235.0 | 5.7339 | 5.5823 | 4.0226 |
| 23 | 2013-07-01 | A   | 4.5056 | 0.3022 | 8125 | 0.743              | 5.955  | 5.8011 | 4.1315 | 2.7281 | 4.5667             | 8500.0 | 5.3881 | 5.2488 | 3.7382 | 2.4684 | 4.132              | 8235.0 | 5.2687 | 5.1294 | 3.6188 |
| 24 | 2013-08-01 | A   | 4.3594 | 0.3027 | 8125 | 0.743              | 5.8007 | 5.6508 | 4.0244 | 2.6575 | 4.4484             | 8500.0 | 5.2267 | 5.0916 | 3.6262 | 2.3945 | 4.0082             | 8235.0 | 5.1112 | 4.9761 | 3.5107 |
| 25 | 2013-09-01 | A   | 4.3818 | 0.3032 | 8125 | 0.6485             | 5.725  | 5.577  | 4.0544 | 2.6228 | 4.3903             | 8500.0 | 5.2522 | 5.1164 | 3.7196 | 2.4062 | 4.0277             | 8235.0 | 5.136  | 5.0003 | 3.6035 |
| 26 | 2013-10-01 | A   | 4.3159 | 0.3037 | 8125 | 0.6485             | 5.6558 | 5.5097 | 3.857  | 2.5911 | 4.3373             | 8500.0 | 5.1798 | 5.0459 | 3.5323 | 2.373  | 3.9722             | 8235.0 | 5.0654 | 4.9315 | 3.418  |
| 27 | 2013-11-01 | B   | 4.5698 | 0.3042 | 8125 | 0.6485             | ---    | 5.0898 | 4.6234 | 3.1986 | 4.5441             | 8500.0 | ---    | 4.6916 | 4.2617 | 2.9483 | 4.1885             | 8235.0 | ---    | 4.5705 | 4.1406 |



---

## Formula-prediction-context__case-696

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A                    | B                  | C                  | D      | E              | F         | G                  | H                        | I                     | J                      | K                  |
|---:|:---------------------|:-------------------|:-------------------|:-------|:---------------|:----------|:-------------------|:-------------------------|:----------------------|:-----------------------|:-------------------|
|  1 |                      | Ideal value        |                    |        | Measured value |           |                    | Error (measured - ideal) |                       |                        |                    |
|  2 | VIN                  | OUT+               | OUT-               | Vcm_in | OUT+           | OUT-      | Vcm_in             | OUT+                     | OUT-                  | Vcm_in                 | gain               |
|  3 | 0.01                 | 2.5008264462809917 | 2.4991735537190083 | 2.5    | 2.5208716      | 2.4764791 | 2.49867535         | 0.02004515371900828      | -0.022694453719008134 | -0.0013246499999999273 | 4.4392499999999835 |
|  4 | [Target Cell]        | 2.5016528925619834 | 2.4983471074380166 | 2.5    | 2.5216747      | 2.4756632 | 2.49866895         | 0.020021807438016737     | -0.022683907438016515 | -0.0013310500000001113 | 2.3005750000000047 |
|  5 | 0.03                 | 2.502479338842975  | 2.497520661157025  | 2.5    | 2.5227595      | 2.4748461 | 2.4988028          | 0.02028016115702469      | -0.02267456115702471  | -0.0011972000000000094 | 1.597113333333322  |
|  6 | 0.04                 | 2.503305785123967  | 2.496694214876033  | 2.5    | 2.5235958      | 2.4740251 | 2.4988104499999997 | 0.02029001487603299      | -0.02266911487603318  | -0.0011895500000003167 | 1.2392674999999964 |
|  7 | 0.05                 | 2.5041322314049586 | 2.4958677685950414 | 2.5    | 2.5240878      | 2.4732106 | 2.4986492          | 0.01995556859504166      | -0.022657168595041632 | -0.0013507999999999853 | 1.017544000000008  |
|  8 | 0.060000000000000005 | 2.5049586776859503 | 2.4950413223140497 | 2.5    | 2.5249406      | 2.4723731 | 2.4986568499999997 | 0.019981922314049605     | -0.022668222314049746 | -0.0013431500000002927 | 0.8761249999999979 |
|  9 | 0.07                 | 2.505785123966942  | 2.494214876033058  | 2.5    | 2.5257527      | 2.4714986 | 2.49862565         | 0.019967576033057988     | -0.022716276033058147 | -0.0013743499999998576 | 0.7750585714285725 |
| 10 | 0.08                 | 2.5066115702479337 | 2.4933884297520663 | 2.5    | 2.5265596      | 2.4705196 | 2.4985396          | 0.019948029752066443     | -0.0228688297520665   | -0.0014604000000000283 | 0.7005000000000039 |
| 11 | 0.09                 | 2.507438016528926  | 2.492561983471074  | 2.5    | 2.5274035      | 2.469909  | 2.49865625         | 0.019965483471074297     | -0.02265298347107425  | -0.001343750000000199  | 0.6388277777777803 |
| 12 | 0.09999999999999999  | 2.5082644628099175 | 2.4917355371900825 | 2.5    | 2.5281441      | 2.4690472 | 2.49859565         | 0.019879637190082455     | -0.022688337190082564 | -0.0014043500000000542 | 0.5909690000000012 |
| 13 | 0.10999999999999999  | 2.5090909090909093 | 2.4909090909090907 | 2.5    | 2.529025       | 2.4679866 | 2.4985058          | 0.019934090909090596     | -0.022922490909090598 | -0.001494199999999779  | 0.554894545454543  |
| 14 | 0.11999999999999998  | 2.509917355371901  | 2.490082644628099  | 2.5    | 2.5299211      | 2.4674257 | 2.4986734000000004 | 0.020003744628099174     | -0.022656944628098863 | -0.0013265999999996225 | 0.5207949999999999 |



---

## Formula-prediction-context__case-883

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | AFP   | AFQ       | AFR           | AFS   | AFT   | AFU   | AFV   | AFW   | AFX   | AFY   | AFZ                | AGA           | AGB   | AGC   | AGD   | AGE   | AGF   | AGG   | AGH   | AGI                | AGJ             |
|---:|:------|:----------|:--------------|:------|:------|:------|:------|:------|:------|:------|:-------------------|:--------------|:------|:------|:------|:------|:------|:------|:------|:-------------------|:----------------|
|  1 |       |           |               |       |       |       |       |       |       |       |                    |               |       |       |       |       |       |       |       |                    |                 |
|  2 |       |           |               |       |       |       |       |       |       |       |                    |               |       |       |       |       |       |       |       |                    |                 |
|  3 |       |           |               |       |       |       |       |       |       |       |                    |               |       |       |       |       |       |       |       |                    |                 |
|  4 |       |           | Dual Antennas |       |       |       |       |       |       |       |                    | Dual Antennas |       |       |       |       |       |       |       |                    | Triple Antennas |
|  5 |       |           | M0.1 to M9.1  |       |       |       |       |       |       |       |                    | M0.2 to M9.2  |       |       |       |       |       |       |       |                    | M0.1 to M9.1    |
|  6 |       |           |               |       |       |       |       |       |       |       |                    |               |       |       |       |       |       |       |       |                    |                 |
|  7 | D     | Total Pwr | E             | F     | G     | H     | A     | B     | C     | D     | Total Pwr          | E             | F     | G     | H     | A     | B     | C     | D     | Total Pwr          | E               |
|  8 |       | 15        | 9             | 9     |       |       |       |       |       |       | [Target Cell]      | 13            | 13    |       |       |       |       |       |       | 16.010299956639813 | 6               |
|  9 |       | 16        | 9             | 9     |       |       |       |       |       |       | 12.010299956639814 | 12            | 12    |       |       |       |       |       |       | 15.010299956639813 | 5               |
| 10 |       | 17        | 9             | 9     |       |       |       |       |       |       | 12                 | 12            | 12    |       |       |       |       |       |       | 15                 | 5               |
| 11 |       | 15        | 9             | 9     |       |       |       |       |       |       | 12.010299956639814 | 13            | 13    |       |       |       |       |       |       | 16.010299956639813 | 5               |
| 12 |       | 17        | 16            | 16    |       |       |       |       |       |       | 19.010299956639816 | 17            | 17    |       |       |       |       |       |       | 20                 | 13              |
| 13 |       | 17        | 14            | 14    |       |       |       |       |       |       | 17.010299956639813 | 12            | 12    |       |       |       |       |       |       | 15.010299956639813 | 14              |
| 14 |       | 17        | 15            | 15    |       |       |       |       |       |       | 18                 | 17            | 17    |       |       |       |       |       |       | 20                 | 13              |
| 15 |       | 17        | 16            | 16    |       |       |       |       |       |       | 19.010299956639816 | 17            | 17    |       |       |       |       |       |       | 20.010299956639813 | 12              |
| 16 |       | 17        | 16            | 16    |       |       |       |       |       |       | 19.010299956639816 | 16            | 16    |       |       |       |       |       |       | 19.010299956639816 | 16              |
| 17 |       | 17        | 17            | 17    |       |       |       |       |       |       | 20                 | 17            | 17    |       |       |       |       |       |       | 20                 | 17              |
| 18 |       | 17        | 17            | 17    |       |       |       |       |       |       | 20                 | 17            | 17    |       |       |       |       |       |       | 20                 | 17              |



---

## Formula-prediction-context__case-221

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | C   | D        | E      | F   | G      | H    | I     | J   | K      | L          | M             | N      | O                 | P      | Q   | R   | S       | T   | U       | V   | W   |
|---:|:----|:---------|:-------|:----|:-------|:-----|:------|:----|:-------|:-----------|:--------------|:-------|:------------------|:-------|:----|:----|:--------|:----|:--------|:----|:----|
| 22 |     |          |        |     |        |      |       |     |        |            |               |        |                   |        |     |     |         |     |         |     |     |
| 23 | 4.0 | 25.0     | CHOICE | CMD | 19E-25 | PRIM | Kara  |     | 186.0  |            |               |        |                   |        |     |     | 74.0    |     |         |     |     |
| 24 | 4.0 | 25.0     | CHOICE | CMD | 19E-25 | SEC  |       |     | 0.0    |            |               |        |                   |        |     |     |         |     |         |     |     |
| 25 |     | 25.0     |        |     |        |      |       |     |        |            |               |        |                   |        |     |     |         |     |         |     |     |
| 26 | 4.0 | 25.0     | CHOICE | CPA | 25E-25 | PRIM | Heidi |     | 4050.0 | 2091.30608 |               |        |                   |        |     |     | 4427.0  |     |         |     |     |
| 27 | 4.0 | 25.0     | CHOICE | CPA | 25E-25 | SEC  |       |     | 0.0    |            |               |        |                   |        |     |     |         |     |         |     |     |
| 28 |     | 25.0     |        |     |        |      |       |     |        |            |               |        |                   |        |     |     |         |     |         |     |     |
| 29 | 4.0 | 25.0     | C & I  | CPA | 25E-25 | PRIM |       |     |        |            |               |        |                   |        |     |     |         |     |         |     |     |
| 30 | 4.0 | 25.0     | C & I  | CPA | 25E-25 | SEC  | Heidi |     |        |            |               |        |                   |        |     |     |         |     |         |     |     |
| 31 | 4.0 | 25.0     | Osram  | CPA | 25E-25 | SEC  | Heidi |     |        |            |               |        |                   |        |     |     |         |     |         |     |     |
| 32 | 4.0 | 25 Total |        |     |        |      |       |     | 4236.0 | 2091.30608 | [Target Cell] | 4152.0 | 4567.200000000001 |        |     |     | 4501.0  |     | 265.0   |     |     |
| 33 |     |          |        |     |        |      |       |     |        |            |               |        |                   |        |     |     |         |     |         |     |     |
| 34 | 5.0 | 2.0      | CHOICE | COH | 23N-2  | PRIM | Kara  |     | 4860.0 |            |               |        |                   |        |     |     | 8000.0  |     |         |     |     |
| 35 | 5.0 | 2.0      | CHOICE | COH | 23N-2  | SEC  | Kara  |     | 0.0    |            |               |        |                   |        |     |     |         |     |         |     |     |
| 36 | 5.0 | 2.0      | CHOICE | COH | 23N-2  | STOR | Kara  |     | 0.0    |            |               |        |                   |        |     |     | 7377.0  |     |         |     |     |
| 37 |     | 2.0      |        |     |        |      |       |     |        |            |               |        |                   |        |     |     |         |     |         |     |     |
| 38 | 5.0 | 2 Total  |        |     |        |      |       |     | 4860.0 | 0.0        | 4860.0        | 2769.0 | 3045.9            | 1814.1 |     |     | 15377.0 |     | 10517.0 |     |     |
| 39 |     |          |        |     |        |      |       |     |        |            |               |        |                   |        |     |     |         |     |         |     |     |
| 40 | 5.0 | 7.0      | CHOICE | COH | 23N-7  | PRIM | Kara  |     | 1942.0 |            |               |        |                   |        |     |     | 5100.0  |     |         |     |     |
| 41 | 5.0 | 7.0      | CHOICE | COH | 23N-7  | SEC  | Kara  |     | 0.0    |            |               |        |                   |        |     |     |         |     |         |     |     |
| 42 | 5.0 | 7.0      | CHOICE | COH | 23N-7  | STOR | Kara  |     | 0.0    |            |               |        |                   |        |     |     | 2977.0  |     |         |     |     |



---

## Formula-prediction-context__case-365

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A                                                                                                                                                                                                                                                                                              | B                               | C                     | D                            | E                | F                        | G              | H   | I   | J   | K   | L   | M   | N   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|:----------------------|:-----------------------------|:-----------------|:-------------------------|:---------------|:----|:----|:----|:----|:----|:----|:----|
|  1 | NOTE: SKU Finder may not work with Version of Excel prior to 2013.                                                                                                                                                                                                                             |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|    | Step 1:  Paste or type SKU/ list of SKUs into Column A.                                                                                                                                                                                                                                        |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|    | • The “Contract Approved SKU” will appear in Column C and the “Contract Approved List Price” will appear in Column D.  “Not Found” will appear if the SKU is not listed on the PL.  Double check spelling, contract carve-outs and US Global Price List to ensure SKU is listed if “Not Found” |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|    | Step 2:  Paste or Type Product/ Service List Price into Column B                                                                                                                                                                                                                               |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|    | • A green or red result will return in Column E, “Variance from List Price”  |  Green = no variance from list price, Red = Variance exists and is listed                                                                                                                                       |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|    | Step 3:  Filter and Sort by “Not Found” in Column C to have each “Not Found” descend one after the other                                                                                                                                                                                       |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|  2 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|  3 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|  4 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|  5 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|  6 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|  7 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|  8 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
|  9 | Product/Service SKU                                                                                                                                                                                                                                                                            | Product/Service Unit List Price | Contract Approved SKU | Contract Approved List Price | Minimum Discount | Variance from List Price | eRATE Eligible |     |     |     |     |     |     |     |
| 10 |                                                                                                                                                                                                                                                                                                |                                 |                       | [Target Cell]                |                  |                          |                |     |     |     |     |     |     |     |
| 11 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
| 12 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
| 13 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
| 14 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
| 15 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
| 16 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
| 17 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
| 18 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
| 19 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |
| 20 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |



---

## Formula-prediction-context__case-93

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|     | A                                                 | B                       | C           | D        | E                            | F                                                | G                                                                | H                                                                               | I             | J    | K                                    | L   | M   | N   | O   | P   |
|----:|:--------------------------------------------------|:------------------------|:------------|:---------|:-----------------------------|:-------------------------------------------------|:-----------------------------------------------------------------|:--------------------------------------------------------------------------------|:--------------|:-----|:-------------------------------------|:----|:----|:----|:----|:----|
| 328 | Cisco Catalyst 3750E-24TD-E,S Switch (Deprecated) | OID:1.3.6.1.4.1.9.1.789 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 329 | Cisco Catalyst 3750E-48TD-E,S Switch (Deprecated) | OID:1.3.6.1.4.1.9.1.790 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 330 | Cisco Catalyst 3750E-48PD-E,S Switch (Deprecated) | OID:1.3.6.1.4.1.9.1.791 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 331 | Cisco Catalyst 3750E-24PD-E,S Switch (Deprecated) | OID:1.3.6.1.4.1.9.1.792 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 332 |                                                   |                         |             |          |                              |                                                  |                                                                  |                                                                                 |               |      |                                      |     |     |     |     |     |
| 333 |                                                   |                         |             |          |                              |                                                  |                                                                  |                                                                                 |               |      |                                      |     |     |     |     |     |
| 334 | Cisco Catalyst 3750 Series Switches               |                         |             |          |                              |                                                  |                                                                  |                                                                                 |               |      |                                      |     |     |     |     |     |
| 335 |                                                   |                         |             |          |                              |                                                  |                                                                  |                                                                                 |               |      |                                      |     |     |     |     |     |
| 336 | Device Type                                       | SYSOIDS                 | S/W Version | Software | Cisco.com Image Support(Y/N) | Image Import from Device ( FTP, TFTP, SFTP, SCP) | Image Distribution via Local File Server ( FTP, TFTP, SFTP, SCP) | Image Distribution via Software Image Management server ( FTP, TFTP, SFTP, SCP) | TFTP Fallback | ISSU | Activation without Distribution flow |     |     |     |     |     |
| 337 | Cisco 3750 Stackable Switches (Deprecated)        | OID:1.3.6.1.4.1.9.1.516 | >=12.2      | IOS      | N                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 338 | Cisco Catalyst 3750G-24PS Switch (Deprecated)     | OID:1.3.6.1.4.1.9.1.602 | >=12.2      | IOS      | Y                            | [Target Cell]                                    | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 339 | Cisco Catalyst 3750G-48PS Switch (Deprecated)     | OID:1.3.6.1.4.1.9.1.603 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 340 | Cisco Catalyst 3750G-24TS-1U Switch (Deprecated)  | OID:1.3.6.1.4.1.9.1.624 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 341 | Cisco Catalyst 3750-24FS Switch (Deprecated)      | OID:1.3.6.1.4.1.9.1.656 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 342 | Cisco Catalyst 3750-24PS Switch (Deprecated)      | OID:1.3.6.1.4.1.9.1.536 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 343 | Cisco Catalyst 3750-24TS Switch (Deprecated)      | OID:1.3.6.1.4.1.9.1.513 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 344 | Cisco Catalyst 3750-48PS Switch (Deprecated)      | OID:1.3.6.1.4.1.9.1.535 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 345 | Cisco Catalyst 3750G-16TD Switch (Deprecated)     | OID:1.3.6.1.4.1.9.1.591 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 346 | Cisco Catalyst 3750G-48TS Switch (Deprecated)     | OID:1.3.6.1.4.1.9.1.604 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 347 | Cisco Catalyst 3750G-12S-SD Switch (Deprecated)   | OID:1.3.6.1.4.1.9.1.688 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |
| 348 | Cisco Catalyst 3750G-12S Switch (Deprecated)      | OID:1.3.6.1.4.1.9.1.530 | >=12.2      | IOS      | Y                            | FTP, TFTP, SCP                                   | FTP, TFTP, SCP                                                   | FTP, TFTP, SCP                                                                  | No            | NA   | Yes                                  |     |     |     |     |     |



---

## Formula-prediction-context__case-330

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A   | B                          | C                     | D     | E                                      | F                                  | G                    |
|---:|:----|:---------------------------|:----------------------|:------|:---------------------------------------|:-----------------------------------|:---------------------|
| 29 |     | ADDRESS_MIRRORING          | Address Mirroring Off |       | 0                                      | 0                                  |                      |
| 30 |     | PHY Data ZO                | RZQ/6 = 40 Ohms       | RZQ/6 | 11                                     | B                                  |                      |
| 31 |     | PHY ACCC ZO                | RZQ/7 = 34 Ohms       | RZQ/7 | 13                                     | D                                  |                      |
| 32 |     | PHY ODT                    | RZQ/4 = 60 Ohms       | RZQ/4 | 5                                      | 5                                  |                      |
| 33 |     | DDR3 or DDR3L              | DDR3L                 |       | 2                                      | 2                                  |                      |
| 34 |     |                            |                       |       |                                        |                                    |                      |
| 35 |     |                            |                       |       |                                        |                                    |                      |
| 36 |     | Refresh Configuration      |                       |       |                                        |                                    |                      |
| 37 |     |                            |                       |       |                                        |                                    |                      |
| 38 |     |                            | Selected              | Units | Corresponding Register Value (decimal) | Corresponding Register Value (hex) |                      |
|    |     |                            | Datasheet Values /    |       |                                        |                                    |                      |
|    |     |                            |  Settings             |       |                                        |                                    |                      |
| 39 |     | INITREF_DIS                | Normal Operation      |       | 0                                      | [Target Cell]                      |                      |
| 40 |     | SRT                        | Normal Temp Range     |       | 0                                      | 0                                  |                      |
| 41 |     | ASR                        | Auto Self-Refresh     |       | 1                                      | 1                                  |                      |
| 42 |     | PASR                       | Full Array            |       | 0                                      | 0                                  |                      |
| 43 |     | REFRESH_PERIOD - Normal    | 7.8125                | us    | 6250                                   | 186A                               |                      |
| 44 |     | REFRESH_PERIOD - Ext. Temp | 3.90625               | us    | 3125                                   | 0C35                               |                      |
| 45 |     |                            |                       |       |                                        |                                    |                      |
| 46 |     |                            |                       |       |                                        |                                    |                      |
| 47 |     | SDRAM Timing Values        |                       |       |                                        |                                    |                      |
| 48 |     |                            |                       |       |                                        |                                    |                      |
| 49 |     | Timing Parameter           | Selected              | Units | Corresponding Register Value (decimal) | Corresponding Register Value (hex) | Lookup Value for PHY |
|    |     |                            | Datasheet Values      |       |                                        |                                    |                      |



---

## Formula-prediction-context__case-103

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A   | B                | C   | D                                                                            | E   | F                                                                 | G   | H         | I              | J                         | K                 | L       | M   | N   | O   |
|---:|:----|:-----------------|:----|:-----------------------------------------------------------------------------|:----|:------------------------------------------------------------------|:----|:----------|:---------------|:--------------------------|:------------------|:--------|:----|:----|:----|
| 18 |     | Applicable HR    | =   | The Heat Rate for the specified time-period, per the following table:        |     |                                                                   |     |           |                |                           |                   |         |     |     |     |
| 19 |     | Applicable BTU   | =   | Heat Rate subtractor for the specified time-period, per the following table: |     |                                                                   |     |           |                |                           |                   |         |     |     |     |
| 20 |     | Market Heat Rate | =   | 12-month forward market heat rate per CPUC D.07-09-040 and Res. E-4246       |     |                                                                   |     |           |                |                           |                   |         |     |     |     |
| 21 |     |                  |     |                                                                              |     |                                                                   |     |           |                |                           |                   |         |     |     |     |
| 22 |     |                  |     |                                                                              |     | Calendar Year(s)                                                  |     | Heat Rate | Applicable BTU |                           |                   |         |     |     |     |
| 23 |     |                  |     |                                                                              |     | 2013 - 2014                                                       |     | 8500      | 265            | Btu/kWh                   |                   |         |     |     |     |
| 24 |     |                  |     |                                                                              |     | 2015 and beyond (Market Heat Rate)                                |     | MHR       | 0              | Btu/kWh                   |                   |         |     |     |     |
| 25 |     |                  |     |                                                                              |     |                                                                   |     |           |                |                           |                   |         |     |     |     |
| 26 |     |                  |     |                                                                              |     |                                                                   |     |           |                | Applicable HR             | 7297.250109174158 | Btu/kWh |     |     |     |
| 27 |     |                  |     |                                                                              |     |                                                                   |     |           |                |                           |                   |         |     |     |     |
| 28 |     |                  |     |                                                                              |     |                                                                   |     |           |                | Applicable BTU            | [Target Cell]     | Btu/kWh |     |     |     |
| 29 |     |                  |     |                                                                              |     |                                                                   |     |           |                |                           |                   |         |     |     |     |
| 30 |     |                  |     |                                                                              |     |                                                                   |     |           |                |                           |                   |         |     |     |     |
| 31 |     | BTGP             | =   | GPn + GTn   (Calendar month Burner Tip Gas Price), where                     |     |                                                                   |     |           |                |                           |                   |         |     |     |     |
| 32 |     |                  |     |                                                                              |     |                                                                   |     |           |                |                           |                   |         |     |     |     |
| 33 |     |                  |     | GPn                                                                          | =   | Simple average of natural gas bidweek price indices for Malin and |     | Malin     | 1.5017         | $/MMBtu                   |                   |         |     |     |     |
| 34 |     |                  |     |                                                                              |     | Topock from Gas Daily, Natural Gas Intelligence and Natural Gas   |     | Topock    | 1.7533         | $/MMBtu                   |                   |         |     |     |     |
| 35 |     |                  |     |                                                                              |     | Week                                                              |     |           |                |                           |                   |         |     |     |     |
| 36 |     |                  |     |                                                                              |     |                                                                   |     |           |                | Average Bidweek Gas Price | 1.6275            | $/MMBtu |     |     |     |
| 37 |     |                  |     |                                                                              |     |                                                                   |     |           |                |                           |                   |         |     |     |     |
| 38 |     |                  |     | GTn                                                                          | =   | Intrastate Transportation                                         |     |           |                |                           |                   |         |     |     |     |



---

## Formula-prediction-context__case-544

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | AM                  | AN          | AO                  | AP           | AQ        | AR          | AS                 | AT        | AU                 | AV           | AW            | AX      | AY        | AZ      | BA      | BB            | BC        | BD      | BE        | BF         | BG           |
|---:|:--------------------|:------------|:--------------------|:-------------|:----------|:------------|:-------------------|:----------|:-------------------|:-------------|:--------------|:--------|:----------|:--------|:--------|:--------------|:----------|:--------|:----------|:-----------|:-------------|
|  1 |                     |             |                     |              |           |             |                    |           |                    |              |               |         |           |         |         |               |           |         |           |            |              |
|  2 |                     |             |                     |              |           |             |                    |           |                    |              |               |         |           |         |         |               |           |         |           |            |              |
|  3 |                     |             |                     |              |           |             |                    |           |                    | mdq15000     |               |         |           |         |         |               |           |         |           |            |              |
|  4 |                     |             |                     |              |           |             |                    |           |                    | FT1007       |               |         |           |         |         |               |           |         |           |            |              |
|  5 |                     |             |                     | Central Desk |           |             |                    |           |                    | Central Desk |               |         |           |         |         | Sale to Sithe |           |         |           |            |              |
|  6 | GLGT fuel           | GLGT @      | GLGT fuel           | GLGT @       | GLGT fuel | GLGT @      | GLGT fuel          | GLGT @    | GLGT fuel          | GLGT @       | GLGT fuel     | GLGT @  | GLGT fuel |         |         | GLGT @        | GLGT fuel | GLGT @  | GLGT fuel | GLGT @     | GLGT fuel    |
|  7 | Emerson to          | Emerson     | Emerson to          | Emerson      | Emerson   | Emerson     | Emerson to         | Emerson   | Emerson to         | Emerson      | Emerson       | Emerson | Emerson   | Emerson | Emerson | Emerson       | Emerson   | Farwell | Farwell   | Crystal F. | Crystal Fall |
|  8 | St. Clair           | Belle River | Belle River         | Chippew      | Chippew   | Belle River | Belle River        | St. Clair | St. Clair          | to Carlton   | to Carlton    | Chippew | Chippew   | Farwell | Farwell | to Farwell    | Farwell   |         | St Clair  |            | St Clair     |
|  9 | FT1020              | FT1020      | FT1020              | FT1020       | FT1020    | FT1007      | FT1007             | FT1007    | FT1007             | FT1007       | FT1007        | FT1007  | FT1007    |         |         |               |           |         |           | FT0324     | FT0324       |
| 10 | 0.0                 | 5179.0      | -178.78840219999984 | 0.0          | 0.0       | 15536.0     | -536.3306848000011 | 0.0       | 0.0                | 0.0          | [Target Cell] | 0.0     | 0.0       | 0.0     | 0.0     | 0.0           | 0.0       | 0.0     | 0.0       | 0.0        | 0.0          |
| 11 | -178.78840219999984 | 0.0         | 0.0                 | 0.0          | 0.0       | 0.0         | 0.0                | 15536.0   | -536.3306848000011 | 0.0          | 0.0           | 0.0     | 0.0       | 0.0     | 0.0     | 0.0           | 0.0       | 0.0     | 0.0       | 0.0        | 0.0          |
| 12 | -178.78840219999984 | 0.0         | 0.0                 | 0.0          | 0.0       | 0.0         | 0.0                | 15536.0   | -536.3306848000011 | 0.0          | 0.0           | 0.0     | 0.0       | 0.0     | 0.0     | 0.0           | 0.0       | 0.0     | 0.0       | 0.0        | 0.0          |
| 13 | -178.78840219999984 | 0.0         | 0.0                 | 0.0          | 0.0       | 0.0         | 0.0                | 15536.0   | -536.3306848000011 | 0.0          | 0.0           | 0.0     | 0.0       | 0.0     | 0.0     | 0.0           | 0.0       | 0.0     | 0.0       | 0.0        | 0.0          |
| 14 | -178.78840219999984 | 0.0         | 0.0                 | 0.0          | 0.0       | 0.0         | 0.0                | 15536.0   | -536.3306848000011 | 0.0          | 0.0           | 0.0     | 0.0       | 0.0     | 0.0     | 0.0           | 0.0       | 0.0     | 0.0       | 0.0        | 0.0          |
| 15 | -178.78840219999984 | 0.0         | 0.0                 | 0.0          | 0.0       | 0.0         | 0.0                | 15536.0   | -536.3306848000011 | 0.0          | 0.0           | 0.0     | 0.0       | 0.0     | 0.0     | 0.0           | 0.0       | 0.0     | 0.0       | 0.0        | 0.0          |
| 16 | -178.78840219999984 | 0.0         | 0.0                 | 0.0          | 0.0       | 0.0         | 0.0                | 15536.0   | -536.3306848000011 | 0.0          | 0.0           | 0.0     | 0.0       | 0.0     | 0.0     | 0.0           | 0.0       | 0.0     | 0.0       | 0.0        | 0.0          |
| 17 | -178.78840219999984 | 0.0         | 0.0                 | 0.0          | 0.0       | 0.0         | 0.0                | 15536.0   | -536.3306848000011 | 0.0          | 0.0           | 0.0     | 0.0       | 0.0     | 0.0     | 0.0           | 0.0       | 0.0     | 0.0       | 0.0        | 0.0          |
| 18 | -178.78840219999984 | 0.0         | 0.0                 | 0.0          | 0.0       | 0.0         | 0.0                | 15536.0   | -536.3306848000011 | 0.0          | 0.0           | 0.0     | 0.0       | 0.0     | 0.0     | 0.0           | 0.0       | 0.0     | 0.0       | 0.0        | 0.0          |
| 19 | -178.78840219999984 | 0.0         | 0.0                 | 0.0          | 0.0       | 0.0         | 0.0                | 15536.0   | -536.3306848000011 | 0.0          | 0.0           | 0.0     | 0.0       | 0.0     | 0.0     | 0.0           | 0.0       | 0.0     | 0.0       | 0.0        | 0.0          |
| 20 | -178.78840219999984 | 0.0         | 0.0                 | 0.0          | 0.0       | 0.0         | 0.0                | 15536.0   | -536.3306848000011 | 0.0          | 0.0           | 0.0     | 0.0       | 0.0     | 0.0     | 0.0           | 0.0       | 0.0     | 0.0       | 0.0        | 0.0          |



---

## Formula-prediction-context__case-435

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A   | B                                                                                                                                     | C   | D                                                                                              | E   | F   | G   | H   | I              | J                        | K        | L                     | M   | N   |
|---:|:----|:--------------------------------------------------------------------------------------------------------------------------------------|:----|:-----------------------------------------------------------------------------------------------|:----|:----|:----|:----|:---------------|:-------------------------|:---------|:----------------------|:----|:----|
|  1 |     |                                                                                                                                       |     | Pacific Gas and Electric Company                                                               |     |     |     |     |                |                          |          |                       |     |     |
|  2 |     |                                                                                                                                       |     | VARIABLE ENERGY PRICES FOR QUALIFYING FACILITIES                                               |     |     |     |     |                |                          |          |                       |     |     |
|  3 |     |                                                                                                                                       |     |                                                                                                |     |     |     |     |                |                          |          |                       |     |     |
|  4 |     |                                                                                                                                       |     | [Target Cell]                                                                                  |     |     |     |     |                |                          |          |                       |     |     |
|  5 |     |                                                                                                                                       |     | Submitted 07/11/2019                                                                           |     |     |     |     |                |                          |          |                       |     |     |
|  6 |     |                                                                                                                                       |     | Submitted to the California Public Utilities Commission in accordance with Decision 07-09-040. |     |     |     |     |                |                          |          |                       |     |     |
|  7 |     |                                                                                                                                       |     |                                                                                                |     |     |     |     |                |                          |          |                       |     |     |
|  8 |     | 2019-07-01 00:00:00                                                                                                                   |     |                                                                                                |     |     |     |     |                |                          |          | Energy Prices ($/kWh) |     |     |
|  9 |     |                                                                                                                                       |     |                                                                                                |     |     |     |     |                |                          |          |                       |     |     |
| 10 |     | Variable energy price (VP) in $/kWh is calculated based on substituting the variables below into the formula adopted in D. 06-07-032: |     |                                                                                                |     |     |     |     | Peak           |                          | 0.042275 |                       |     |     |
| 11 |     |                                                                                                                                       |     |                                                                                                |     |     |     |     | Partial-Peak   |                          | 0.042275 |                       |     |     |
| 12 |     |                                                                                                                                       |     |                                                                                                |     |     |     |     | Off-Peak       |                          | 0.031371 |                       |     |     |
| 13 |     | VP = ((Heat Rate x Seasonal Factor x BTGP) x TOD Factor)) + VOM                                                                       |     |                                                                                                |     |     |     |     | Super Off-Peak |                          | 0.031371 |                       |     |     |
| 14 |     | These energy prices do not include applicable line loss adjustments.                                                                  |     |                                                                                                |     |     |     |     |                | Monthly Weighted Average | 0.035563 |                       |     |     |



---

## Formula-prediction-context__case-543

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A                                                                                                                                                                                                                                                                                              | B                               | C                     | D                            | E                | F                        | G              | H   | I   | J   | K   | L   | M   | N   | O   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|:----------------------|:-----------------------------|:-----------------|:-------------------------|:---------------|:----|:----|:----|:----|:----|:----|:----|:----|
|  1 | NOTE: SKU Finder may not work with Version of Excel prior to 2013.                                                                                                                                                                                                                             |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|    | Step 1:  Paste or type SKU/ list of SKUs into Column A.                                                                                                                                                                                                                                        |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|    | • The “Contract Approved SKU” will appear in Column C and the “Contract Approved List Price” will appear in Column D.  “Not Found” will appear if the SKU is not listed on the PL.  Double check spelling, contract carve-outs and US Global Price List to ensure SKU is listed if “Not Found” |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|    | Step 2:  Paste or Type Product/ Service List Price into Column B                                                                                                                                                                                                                               |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|    | • A green or red result will return in Column E, “Variance from List Price”  |  Green = no variance from list price, Red = Variance exists and is listed                                                                                                                                       |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|    | Step 3:  Filter and Sort by “Not Found” in Column C to have each “Not Found” descend one after the other                                                                                                                                                                                       |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|  2 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|  3 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|  4 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|  5 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|  6 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|  7 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|  8 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
|  9 | Product/Service SKU                                                                                                                                                                                                                                                                            | Product/Service Unit List Price | Contract Approved SKU | Contract Approved List Price | Minimum Discount | Variance from List Price | eRATE Eligible |     |     |     |     |     |     |     |     |
| 10 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          | [Target Cell]  |     |     |     |     |     |     |     |     |
| 11 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
| 12 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
| 13 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
| 14 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
| 15 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
| 16 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
| 17 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
| 18 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
| 19 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |
| 20 |                                                                                                                                                                                                                                                                                                |                                 |                       |                              |                  |                          |                |     |     |     |     |     |     |     |     |



---

## Formula-prediction-context__case-135

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A                                        | B                                                                                              | C                         | D                | E                        | F         | G                              | H               | I             | J                                                                            | K                            | L                              | M                   | N                    | O                      | P   | Q   | R   |
|---:|:-----------------------------------------|:-----------------------------------------------------------------------------------------------|:--------------------------|:-----------------|:-------------------------|:----------|:-------------------------------|:----------------|:--------------|:-----------------------------------------------------------------------------|:-----------------------------|:-------------------------------|:--------------------|:---------------------|:-----------------------|:----|:----|:----|
|  7 |                                          | Trade Pro Business Name:                                                                       |                           |                  |                          |           | Building Type:                 |                 |               |                                                                              |                              |                                |                     |                      |                        |     |     |     |
|    |                                          |                                                                                                |                           |                  |                          |           | (drop-down menu)               |                 |               |                                                                              |                              |                                |                     |                      |                        |     |     |     |
|  8 |                                          | Trade Pro Contact Name, Title:                                                                 |                           |                  |                          |           | Year Facility Built (approx.): |                 |               |                                                                              |                              |                                |                     |                      |                        |     |     |     |
|  9 |                                          | Trade Pro E-Mail Address:                                                                      |                           |                  |                          |           |                                |                 |               |                                                                              |                              |                                |                     |                      |                        |     |     |     |
| 10 |                                          |                                                                                                |                           |                  |                          |           |                                |                 |               |                                                                              |                              |                                |                     |                      |                        |     |     |     |
| 11 |                                          |                                                                                                |                           |                  |                          |           |                                |                 |               |                                                                              |                              |                                |                     |                      |                        |     |     |     |
| 12 | Deemed Measure Information - PRE-INSTALL |                                                                                                |                           |                  |                          |           |                                |                 |               |                                                                              |                              |                                |                     |                      |                        |     |     |     |
| 13 |                                          |                                                                                                |                           |                  |                          |           |                                |                 |               |                                                                              |                              |                                |                     |                      |                        |     |     |     |
| 14 |                                          | ONLY the following Deemed Rebate Measures available for Financing (SA07 – SA12, HV054 – HV071) |                           |                  |                          |           |                                |                 |               | Input the Proposed Site-Specific Savings as listed on your external document |                              |                                |                     |                      |                        |     |     |     |
| 15 |                                          |                                                                                                |                           |                  |                          |           |                                |                 |               |                                                                              |                              |                                |                     |                      |                        |     |     |     |
| 16 |                                          | Rebate Type:                                                                                   | PG&E Rebate Measure Code* | Rebate Quantity* | Actual Proposal Quantity | Unit Type | Measure Description            | Rebate Per Unit | Total Rebate  | Maximum Rebate Per Measure                                                   | Annual kWh Usate (12-months) | Annual therm Usage (12-months) | kW Savings per Unit | kWh Savings per Unit | Therm Savings per Unit |     |     |     |
|    |                                          | Downstream (Customer/Trade Pro) - HVAC only                                                    |                           | (Unit per Ton)   |                          |           |                                |                 |               |                                                                              |                              |                                |                     |                      |                        |     |     |     |
| 17 |                                          | Downstream (Customer/Trade Pro)                                                                |                           |                  |                          | #N/A      | #N/A                           | #N/A            | [Target Cell] |                                                                              |                              |                                | 0                   | #VALUE!              | #VALUE!                |     |     |     |
| 18 |                                          | Downstream (Customer/Trade Pro)                                                                |                           |                  |                          |           |                                | 0               | 0             |                                                                              |                              |                                | 0                   | 0                    | 0                      |     |     |     |
| 19 |                                          | Downstream (Customer/Trade Pro)                                                                |                           |                  |                          |           |                                | 0               | 0             |                                                                              |                              |                                | 0                   | 0                    | 0                      |     |     |     |
| 20 |                                          | Downstream (Customer/Trade Pro)                                                                |                           |                  |                          |           |                                | 0               | 0             |                                                                              |                              |                                | 0                   | 0                    | 0                      |     |     |     |
| 21 |                                          |                                                                                                |                           |                  |                          |           |                                | 0               | 0             |                                                                              |                              |                                | 0                   | 0                    | 0                      |     |     |     |
| 22 |                                          |                                                                                                |                           |                  |                          |           |                                | 0               | 0             |                                                                              |                              |                                | 0                   | 0                    | 0                      |     |     |     |
| 23 |                                          |                                                                                                |                           |                  |                          |           |                                | 0               | 0             |                                                                              |                              |                                | 0                   | 0                    | 0                      |     |     |     |
| 24 |                                          |                                                                                                |                           |                  |                          |           |                                | 0               | 0             |                                                                              |                              |                                | 0                   | 0                    | 0                      |     |     |     |
| 25 |                                          |                                                                                                |                           |                  |                          |           |                                | 0               | 0             |                                                                              |                              |                                | 0                   | 0                    | 0                      |     |     |     |
| 26 |                                          |                                                                                                |                           |                  |                          |           |                                | 0               | 0             |                                                                              |                              |                                | 0                   | 0                    | 0                      |     |     |     |
| 27 |                                          |                                                                                                |                           |                  |                          |           |                                | 0               | 0             |                                                                              |                              |                                | 0                   | 0                    | 0                      |     |     |     |



---

## Formula-prediction-context__case-875

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | B   | C   | D   |   E |   F | G   |   H |   I |   J |   K | L             |   M |   N |   O |   P |   Q |   R |   S |   T |   U |   V |
|---:|:----|:----|:----|----:|----:|:----|----:|----:|----:|----:|:--------------|----:|----:|----:|----:|----:|----:|----:|----:|----:|----:|
|  5 |     |     |     |   1 |   3 | A   |   1 |   1 |   3 |  -4 | 1             |  10 |  15 |  17 |  22 |  17 |  14 |  11 |  13 |  13 |  13 |
|  6 |     |     |     |   1 |   4 | A   |   1 |   1 |   3 |  -4 | 2             | -99 | -93 | -99 | -93 | -99 | -99 | -99 | -99 | -99 | -99 |
|  7 |     |     |     |   1 |   1 | A   |   2 |   2 |   3 |  -4 | -4            |  17 |  17 |  17 |  17 |  17 |  17 | -99 |  17 | -99 | -99 |
|  8 |     |     |     |   1 |   2 | A   |   2 |   2 |   3 |  -4 | -1            |  15 |  18 |  17 |  20 |  17 |  17 |  16 |  17 |  17 | -99 |
|  9 |     |     |     |   1 |   3 | A   |   2 |   2 |   3 |  -4 | 1             |  13 |  18 |  17 |  22 |  17 |  17 |  14 |  16 |  16 |  16 |
| 10 |     |     |     |   1 |   4 | A   |   2 |   2 |   3 |  -4 | 2             | -99 | -93 | -99 | -93 | -99 | -99 | -99 | -99 | -99 | -99 |
| 11 |     |     |     |   1 |   1 | A   |   3 |   3 |   3 |  -4 | -4            |  17 |  17 |  17 |  17 |  17 |  17 | -99 |  17 | -99 | -99 |
| 12 |     |     |     |   1 |   2 | A   |   3 |   3 |   3 |  -4 | -1            |  17 |  20 |  17 |  20 |  17 |  17 |  17 |  17 |  17 | -99 |
| 13 |     |     |     |   1 |   3 | A   |   3 |   3 |   3 |  -4 | 1             |  17 |  22 |  17 |  22 |  17 |  17 |  17 |  17 |  17 |  17 |
| 14 |     |     |     |   1 |   4 | A   |   3 |   3 |   3 |  -4 | 2             | -99 | -93 | -99 | -93 | -99 | -99 | -99 | -99 | -99 | -99 |
| 15 |     |     |     |   1 |   1 | A   |   4 |   4 |   3 |  -4 | [Target Cell] |  17 |  17 |  17 |  17 |  17 |  17 | -99 |  17 | -99 | -99 |
| 16 |     |     |     |   1 |   2 | A   |   4 |   4 |   3 |  -4 | -1            |  17 |  20 |  17 |  20 |  17 |  17 |  17 |  17 |  17 | -99 |
| 17 |     |     |     |   1 |   3 | A   |   4 |   4 |   3 |  -4 | 1             |  17 |  22 |  17 |  22 |  17 |  17 |  17 |  17 |  17 |  17 |
| 18 |     |     |     |   1 |   4 | A   |   4 |   4 |   3 |  -4 | 2             | -99 | -93 | -99 | -93 | -99 | -99 | -99 | -99 | -99 | -99 |
| 19 |     |     |     |   1 |   1 | A   |   5 |   5 |   3 |  -4 | -4            |  17 |  17 |  17 |  17 |  17 |  17 | -99 |  17 | -99 | -99 |
| 20 |     |     |     |   1 |   2 | A   |   5 |   5 |   3 |  -4 | -1            |  17 |  20 |  17 |  20 |  17 |  17 |  17 |  17 |  17 | -99 |
| 21 |     |     |     |   1 |   3 | A   |   5 |   5 |   3 |  -4 | 1             |  17 |  22 |  17 |  22 |  17 |  17 |  17 |  17 |  17 |  17 |
| 22 |     |     |     |   1 |   4 | A   |   5 |   5 |   3 |  -4 | 2             | -99 | -93 | -99 | -93 | -99 | -99 | -99 | -99 | -99 | -99 |
| 23 |     |     |     |   1 |   1 | A   |   6 |   6 |   3 |  -4 | -4            |  17 |  17 |  17 |  17 |  17 |  17 | -99 |  17 | -99 | -99 |
| 24 |     |     |     |   1 |   2 | A   |   6 |   6 |   3 |  -4 | -1            |  17 |  20 |  17 |  20 |  17 |  17 |  17 |  17 |  17 | -99 |
| 25 |     |     |     |   1 |   3 | A   |   6 |   6 |   3 |  -4 | 1             |  17 |  22 |  17 |  22 |  17 |  17 |  17 |  17 |  17 |  17 |



---

## Formula-prediction-context__case-797

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A   | B   | C   | D   | E   | F                                                                 | G                                    | H      | I         | J                               | K                  | L       | M   | N   | O   | P   |
|---:|:----|:----|:----|:----|:----|:------------------------------------------------------------------|:-------------------------------------|:-------|:----------|:--------------------------------|:-------------------|:--------|:----|:----|:----|:----|
| 27 |     |     |     |     |     |                                                                   |                                      |        |           |                                 |                    |         |     |     |     |     |
| 28 |     |     |     | GPn | =   | Simple average of natural gas bidweek price indices for Malin and |                                      | Malin  | 1.605     | $/MMBtu                         |                    |         |     |     |     |     |
| 29 |     |     |     |     |     | Topock from Gas Daily, Natural Gas Intelligence and Natural Gas   |                                      | Topock | 1.5933    | $/MMBtu                         |                    |         |     |     |     |     |
| 30 |     |     |     |     |     | Week                                                              |                                      |        |           |                                 |                    |         |     |     |     |     |
| 31 |     |     |     |     |     |                                                                   |                                      |        |           | Average Bidweek Gas Price       | 1.5992             | $/MMBtu |     |     |     |     |
| 32 |     |     |     |     |     |                                                                   |                                      |        |           |                                 |                    |         |     |     |     |     |
| 33 |     |     |     | GTn | =   | Intrastate Transportation                                         |                                      |        |           |                                 |                    |         |     |     |     |     |
| 34 |     |     |     |     |     |                                                                   |                                      |        |           |                                 |                    |         |     |     |     |     |
| 35 |     |     |     |     |     | G-AAOFF - Redwood                                                 | PG&E AL 4200-G                       |        |           |                                 | 0.7933             | $/MMBtu |     |     |     |     |
| 36 |     |     |     |     |     | G-AAOFF - Baja                                                    | PG&E AL 4200-G                       |        |           |                                 | 0.9553             | $/MMBtu |     |     |     |     |
| 37 |     |     |     |     |     | Gas Rule 21 Shrinkage                                             | PG&E AL 4141-G, Backbone             |        | Shrinkage | 0.012                           | [Target Cell]      | $/MMBtu |     |     |     |     |
| 38 |     |     |     |     |     | Backbone Transport                                                | Average Redwood, Baja plus shrinkage |        |           |                                 | 0.8937             | $/MMBtu |     |     |     |     |
| 39 |     |     |     |     |     |                                                                   |                                      |        |           |                                 |                    |         |     |     |     |     |
| 40 |     |     |     |     |     | G-EG*                                                             | PG&E AL 4223-G, Non-Backbone         |        |           |                                 | 0.9882000000000001 | $/MMBtu |     |     |     |     |
| 41 |     |     |     |     |     | G-SUR                                                             | PG&E AL 4221-G                       |        |           |                                 | 0.0147             | $/MMBtu |     |     |     |     |
| 42 |     |     |     |     |     |                                                                   |                                      |        |           |                                 |                    |         |     |     |     |     |
| 43 |     |     |     |     |     |                                                                   |                                      |        |           | Total Intrastate Transportation | 1.8966             | $/MMBtu |     |     |     |     |
| 44 |     |     |     |     |     |                                                                   |                                      |        |           |                                 |                    |         |     |     |     |     |
| 45 |     |     |     |     |     |                                                                   |                                      |        |           | Monthly Burner Tip Gas Price    | 3.4958             | $/MMBtu |     |     |     |     |
| 46 |     |     |     |     |     |                                                                   |                                      |        |           |                                 |                    |         |     |     |     |     |
| 47 |     |     |     |     |     |                                                                   |                                      |        |           |                                 |                    |         |     |     |     |     |



---

## Formula-prediction-context__case-347

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A   | B                                                                                            | C   | D   | E                                                                      | F   | G                                                               | H   | I         | J                        | K             | L        | M   | N   | O   | P   |
|---:|:----|:---------------------------------------------------------------------------------------------|:----|:----|:-----------------------------------------------------------------------|:----|:----------------------------------------------------------------|:----|:----------|:-------------------------|:--------------|:---------|:----|:----|:----|:----|
|  1 |     |                                                                                              |     |     |                                                                        |     | Pacific Gas and Electric Company                                |     |           |                          |               |          |     |     |     |     |
|  2 |     |                                                                                              |     |     |                                                                        |     | SHORT RUN AVOIDED COST ("SRAC")                                 |     |           |                          |               |          |     |     |     |     |
|  3 |     |                                                                                              |     |     |                                                                        |     | ENERGY PRICES FOR QUALIFYING FACILITIES AND                     |     |           |                          |               |          |     |     |     |     |
|  4 |     |                                                                                              |     |     |                                                                        |     | COMBINED HEAT & POWER FACILITIES                                |     |           |                          |               |          |     |     |     |     |
|  5 |     |                                                                                              |     |     |                                                                        |     | EFFECTIVE May 1 - 31, 2022                                      |     |           |                          |               |          |     |     |     |     |
|  6 |     |                                                                                              |     |     |                                                                        |     | Submitted 05/10/2022                                            |     |           |                          |               |          |     |     |     |     |
|  7 |     |                                                                                              |     |     |                                                                        |     | Prepared pursuant to Decision D.10-12-035 and Resolution E-4246 |     |           |                          |               |          |     |     |     |     |
|  8 |     | 2022-05-01 00:00:00                                                                          |     |     |                                                                        |     |                                                                 |     |           | Energy Prices ($/kWh)    | Winter        | Summer   |     |     |     |     |
|  9 |     |                                                                                              |     |     |                                                                        |     |                                                                 |     |           |                          |               |          |     |     |     |     |
| 10 |     | Energy price (EP) in $/kWh is calculated based on substituting the variables below           |     |     |                                                                        |     |                                                                 |     |           | Peak                     | [Target Cell] | 0.078362 |     |     |     |     |
| 11 |     | into the formula adopted in D.10-12-035:                                                     |     |     |                                                                        |     |                                                                 |     |           | Partial-Peak             | 0             | 0.078362 |     |     |     |     |
| 12 |     |                                                                                              |     |     |                                                                        |     |                                                                 |     |           | Off-Peak                 | 0             | 0.078362 |     |     |     |     |
| 13 |     | EP = [(Market Heat Rate * BTGP / 10^6) + VOM] * TOU                                          |     |     |                                                                        |     |                                                                 |     |           | Super Off-Peak           | 0             | 0.078362 |     |     |     |     |
| 14 |     | These energy prices do not include applicable Locational Adjustments (LA) under D.10-12-035. |     |     |                                                                        |     |                                                                 |     |           | Monthly Weighted Average | 0             | 0.078362 |     |     |     |     |
| 15 |     |                                                                                              |     |     |                                                                        |     |                                                                 |     |           |                          |               |          |     |     |     |     |
| 16 |     |                                                                                              |     |     |                                                                        |     |                                                                 |     |           |                          |               |          |     |     |     |     |
| 17 |     |                                                                                              |     |     |                                                                        |     |                                                                 |     |           |                          |               |          |     |     |     |     |
| 18 |     | Market Heat Rate (MHR) =                                                                     |     |     | 12-month forward market heat rate per CPUC D.07-09-040 and Res. E-4246 |     |                                                                 |     |           |                          |               |          |     |     |     |     |
| 19 |     |                                                                                              |     |     |                                                                        |     |                                                                 |     |           |                          |               |          |     |     |     |     |
| 20 |     |                                                                                              |     |     |                                                                        |     | Calendar Year(s)                                                |     | Heat Rate |                          |               |          |     |     |     |     |



---

## Formula-prediction-context__case-85

**Task:** Formula-prediction-context

**Input:**

You are given an table region extracted from a real Excel spreadsheet, which is centered around a cell called "Target Cell" (labeled as "[Target Cell]" shown in the table below). The table region below includes up to 10 rows above/below the Target Cell, and 10 columns to the left/right of the Target Cell. 

Your task is to analyze the table context surrounding the Target Cell, and predict the most likely Excel formula that should go in the Target Cell. If multiple formulas are possible, choose the most reasonable or commonly used based on context.

1. Please follow the standard formula syntax in Excel, e.g. always begins with an equal sign (=).
2. Base your predicted formula on the surrounding table context, e.g., column headers, annotations, and data values in nearby cells.
3. No explanation — just output the formula itself in a JSON format: {"formula": "your_formula_here"}.

Input Excel Snippet in Markdown format:
|    | A   | B      | C       | D       | E        | F                 |
|---:|:----|:-------|:--------|:--------|:---------|:------------------|
| 16 |     |        |         |         |          |                   |
| 17 |     |        |         |         |          |                   |
| 18 |     |        |         |         |          |                   |
| 19 |     |        |         |         |          |                   |
| 20 |     |        |         |         |          |                   |
| 21 |     |        |         |         |          |                   |
| 22 |     |        |         |         |          |                   |
| 23 |     |        |         |         |          |                   |
| 24 |     |        |         |         |          |                   |
| 25 |     | Vin[V] | Iin[mA] | Vout[V] | Iout[mA] | Effcy[%]          |
| 26 |     | 12.16  | 40      | 9.11    | 49.9     | [Target Cell]     |
| 27 |     | 12.15  | 80      | 9.1     | 98.8     | 92.49794238683127 |
| 28 |     | 12.12  | 170     | 9.06    | 209.4    | 92.0774606872452  |
| 29 |     | 12.11  | 250     | 9.06    | 300      | 89.77704376548307 |
| 30 |     | 12.11  | 330     | 9.06    | 390      | 88.41678552661213 |
| 31 |     | 12.1   | 420     | 9.07    | 490      | 87.45179063360882 |
| 32 |     | 12.07  | 580     | 9.14    | 610      | 79.6417449932863  |
| 33 |     | 12     | 670     | 9.12    | 700      | 79.40298507462686 |
| 34 |     | 12.06  | 760     | 9.09    | 800      | 79.3401413982718  |
| 35 |     | 12.06  | 850     | 9.05    | 900      | 79.4556628621598  |
| 36 |     | 12.02  | 960     | 8.99    | 1010     | 78.68743067110373 |



---

## Functional-Dependency__case_264

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Created Date            |   Job Number | Team   | Technician   | Line_many   | Group_many   |   Hours Spent | Line_Group      | Line    | Group   |
|:------------------------|-------------:|:-------|:-------------|:------------|:-------------|--------------:|:----------------|:--------|:--------|
| 2019-11-18 18:15:45.000 |      1227138 | TeamB  | CH           | Line_I      | Grp-EC       |          1    | Line_I_Grp-EC   | Line_I  | Grp-EC  |
| 2020-03-09 15:18:34.000 |      1376019 | TeamB  | AM           | Line_MC     | Grp-PAP      |          1    | Line_MC_Grp-PAP | Line_MC | Grp-PAP |
| 2020-03-10 21:58:17.000 |      1377594 | TeamD  | CD           | Line_ML     | Grp-MA       |         17    | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2021-01-28 19:45:30.000 |      1770506 | TeamD  | WM           | Line_ML     | Grp-MA       |          5.5  | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2020-05-25 22:02:55.000 |      1471257 | TeamA  | LCO          | Line_ML     | Grp-MA       |         17    | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2019-10-31 23:06:20.000 |      1206875 | TeamB  | RS           | Line_MC     | Grp-X        |         20.7  | Line_MC_Grp-X   | Line_MC | Grp-X   |
| 2020-10-06 12:50:50.000 |      1634835 | TeamA  | JS           | Line_LA     | Grp-TL       |         22.25 | Line_LA_Grp-TL  | Line_LA | Grp-TL  |
| 2020-09-30 19:13:18.000 |      1627793 | TeamC  | KL           | Line_I      | Grp-EC       |          0.5  | Line_I_Grp-EC   | Line_I  | Grp-EC  |
| 2020-05-19 20:53:54.000 |      1466547 | TeamB  | SW           | Line_MC     | Grp-X        |         17    | Line_MC_Grp-X   | Line_MC | Grp-X   |
| 2019-01-23 20:43:03.000 |       780019 | TeamA  | SD           | Line_LA     | Grp-TL       |          0.5  | Line_LA_Grp-TL  | Line_LA | Grp-TL  |
| 2020-10-26 14:44:05.000 |      1660545 | TeamC  | RD           | Line_LA     | Grp-TL       |          0.98 | Line_LA_Grp-TL  | Line_LA | Grp-TL  |
| 2020-04-10 17:44:53.000 |      1431175 | TeamA  | KT           | Line_I      | Grp-EC       |         18.5  | Line_I_Grp-EC   | Line_I  | Grp-EC  |
| 2020-02-25 16:52:15.000 |      1348686 | TeamB  | BS           | Line_WC     | Grp-TS       |         40.25 | Line_WC_Grp-TS  | Line_WC | Grp-TS  |
| 2020-06-17 16:28:07.000 |      1498870 | TeamA  | KT           | Line_MC     | Grp-P5       |          1    | Line_MC_Grp-P5  | Line_MC | Grp-P5  |
| 2020-06-15 19:54:13.000 |      1495612 | TeamA  | GR           | Line_ML     | Grp-MA       |          8.75 | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2020-07-07 13:50:54.000 |      1525352 | TeamB  | JC           | Line_ML     | Grp-MA       |          0.5  | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2020-10-30 18:13:59.000 |      1668201 | TeamB  | BC           | Line_MC     | Grp-P5       |          1.25 | Line_MC_Grp-P5  | Line_MC | Grp-P5  |
| 2019-03-21 16:43:46.000 |       866460 | TeamD  | CD           | Line_ML     | Grp-VLT      |         12    | Line_ML_Grp-VLT | Line_ML | Grp-VLT |
| 2020-02-02 16:41:48.000 |      1315231 | TeamB  | CH           | Line_MC     | Grp-X        |          0.5  | Line_MC_Grp-X   | Line_MC | Grp-X   |
| 2020-01-24 14:43:20.000 |      1303740 | TeamB  | SL           | Line_I      | Grp-EC       |          1    | Line_I_Grp-EC   | Line_I  | Grp-EC  |
| 2020-06-03 15:19:49.000 |      1482617 | TeamB  | CH           | Line_I      | Grp-EC       |          1.22 | Line_I_Grp-EC   | Line_I  | Grp-EC  |
| 2020-07-28 20:22:08.000 |      1548682 | TeamC  | SG           | Line_I      | Grp-EC       |          1.17 | Line_I_Grp-EC   | Line_I  | Grp-EC  |
| 2019-09-12 21:34:34.000 |      1133257 | TeamB  | EC           | Line_WC     | Grp-TS       |          0.25 | Line_WC_Grp-TS  | Line_WC | Grp-TS  |
| 2020-06-25 11:15:18.000 |      1507539 | TeamB  | BS           | Line_ML     | Grp-VLT      |         17    | Line_ML_Grp-VLT | Line_ML | Grp-VLT |
| 2020-11-19 18:57:08.000 |      1692864 | TeamC  | SG           | Line_I      | Grp-SP       |          1    | Line_I_Grp-SP   | Line_I  | Grp-SP  |
| 2020-02-09 23:08:36.000 |      1323802 | TeamD  | BL           | Line_WC     | Grp-TT       |         46    | Line_WC_Grp-TT  | Line_WC | Grp-TT  |
| 2021-01-29 15:53:25.000 |      1771945 | TeamD  | MB           | Line_LA     | Grp-I        |          0    | Line_LA_Grp-I   | Line_LA | Grp-I   |
| 2021-01-20 23:43:36.000 |      1760332 | TeamA  | AE           | Line_MC     | Grp-X        |          8.75 | Line_MC_Grp-X   | Line_MC | Grp-X   |
| 2019-05-14 03:32:23.000 |       947838 | TeamA  | EL           | Line_MC     | Grp-P5       |         27.25 | Line_MC_Grp-P5  | Line_MC | Grp-P5  |
| 2019-07-31 18:28:59.000 |      1070455 | TeamD  | CD           | Line_ML     | Grp-MA       |          3.5  | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2020-10-21 16:50:01.000 |      1654378 | TeamC  | EC           | Line_I      | Grp-SP       |          5.81 | Line_I_Grp-SP   | Line_I  | Grp-SP  |
| 2019-09-27 14:22:08.000 |      1153905 | TeamA  | RW           | Line_ML     | Grp-B        |          0.33 | Line_ML_Grp-B   | Line_ML | Grp-B   |
| 2020-10-13 13:44:37.000 |      1644326 | TeamA  | RW           | Line_WC     | Grp-TT       |         16.25 | Line_WC_Grp-TT  | Line_WC | Grp-TT  |
| 2019-04-01 02:35:43.000 |       879227 | TeamA  | KT           | Line_MC     | Grp-P5       |         10.25 | Line_MC_Grp-P5  | Line_MC | Grp-P5  |
| 2019-01-29 03:16:08.000 |       786004 | TeamD  | DK           | Line_MC     | Grp-4        |          0.5  | Line_MC_Grp-4   | Line_MC | Grp-4   |
| 2020-05-21 12:55:31.000 |      1468355 | TeamB  | CH           | Line_MC     | Grp-4        |          2    | Line_MC_Grp-4   | Line_MC | Grp-4   |
| 2020-05-05 17:28:48.000 |      1453778 | TeamD  | CD           | Line_ML     | Grp-MA       |          7    | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2020-04-14 19:42:12.000 |      1433112 | TeamA  | CK           | Line_ML     | Grp-MA       |          2    | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2019-01-20 21:48:38.000 |       772533 | TeamB  | BC           | Line_MC     | Grp-X        |          8.5  | Line_MC_Grp-X   | Line_MC | Grp-X   |
| 2020-05-19 17:13:01.000 |      1466367 | TeamB  | JC           | Line_ML     | Grp-MA       |          6.25 | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2019-09-27 18:31:47.000 |      1154122 | TeamB  | SL           | Line_MC     | Grp-P1       |          9    | Line_MC_Grp-P1  | Line_MC | Grp-P1  |
| 2020-11-10 14:47:14.000 |      1680496 | TeamC  | KL           | Line_I      | Grp-EC       |          0.82 | Line_I_Grp-EC   | Line_I  | Grp-EC  |
| 2021-01-13 23:14:36.000 |      1752127 | TeamB  | PB           | Line_ML     | Grp-MA       |         23    | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2020-04-02 19:47:34.000 |      1422882 | TeamA  | CK           | Line_ML     | Grp-MA       |          2    | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2019-06-08 00:54:38.000 |       984789 | TeamA  | LCO          | Line_ML     | Grp-MA       |          0.5  | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2021-01-21 22:23:30.000 |      1761863 | TeamB  | BC           | Line_MC     | Grp-P5       |          1    | Line_MC_Grp-P5  | Line_MC | Grp-P5  |
| 2019-10-22 11:04:38.000 |      1193680 | TeamA  | MW           | Line_ML     | Grp-MA       |          3.5  | Line_ML_Grp-MA  | Line_ML | Grp-MA  |
| 2021-01-02 22:51:38.000 |      1738808 | TeamA  | AE           | Line_I      | Grp-EC       |          0.22 | Line_I_Grp-EC   | Line_I  | Grp-EC  |
| 2020-06-12 17:20:49.000 |      1493766 | TeamC  | KL           | Line_I      | Grp-EC       |          0.72 | Line_I_Grp-EC   | Line_I  | Grp-EC  |
| 2019-06-06 17:49:37.000 |       983120 | TeamB  | EC           | Line_WC     | Grp-TS       |          0.25 | Line_WC_Grp-TS  | Line_WC | Grp-TS  |



---

## Functional-Dependency__case_57

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| OrderDate               | OrderNumber   |   ProductKey |   CustomerKey |   TerritoryKey |   OrderLineItem |   OrderQuantity |   SalesTerritoryKey | Region         | Country        | Continent     |
|:------------------------|:--------------|-------------:|--------------:|---------------:|----------------:|----------------:|--------------------:|:---------------|:---------------|:--------------|
| 2017-12-23 00:00:00.000 | SO60574       |          214 |         13842 |              8 |               3 |               1 |                   8 | Germany        | Germany        | Europe        |
| 2017-02-02 00:00:00.000 | SO63385       |          528 |         23208 |              6 |               1 |               2 |                   6 | Canada         | Canada         | North America |
| 2017-10-23 00:00:00.000 | SO56555       |          529 |         24946 |              4 |               2 |               2 |                   4 | Southwest      | United States  | North America |
| 2017-04-02 00:00:00.000 | SO67442       |          220 |         14618 |              1 |               2 |               1 |                   1 | Northwest      | United States  | North America |
| 2017-11-17 00:00:00.000 | SO58086       |          471 |         16950 |              6 |               3 |               1 |                   6 | Canada         | Canada         | North America |
| 2016-11-12 00:00:00.000 | SO57803       |          479 |         16409 |              8 |               4 |               2 |                   8 | Germany        | Germany        | Europe        |
| 2017-08-11 00:00:00.000 | SO52398       |          584 |         20159 |              9 |               1 |               1 |                   9 | Australia      | Australia      | Pacific       |
| 2017-09-03 00:00:00.000 | SO53740       |          528 |         23049 |              1 |               2 |               2 |                   1 | Northwest      | United States  | North America |
| 2016-12-16 00:00:00.000 | SO60170       |          214 |         22233 |              6 |               2 |               1 |                   6 | Canada         | Canada         | North America |
| 2017-06-11 00:00:00.000 | SO72656       |          487 |         15614 |             10 |               5 |               1 |                  10 | United Kingdom | United Kingdom | Europe        |
| 2017-12-31 00:00:00.000 | SO61155       |          528 |         11797 |              4 |               3 |               1 |                   4 | Southwest      | United States  | North America |
| 2017-02-20 00:00:00.000 | SO64551       |          535 |         25869 |              1 |               1 |               2 |                   1 | Northwest      | United States  | North America |
| 2017-10-10 00:00:00.000 | SO55919       |          490 |         19985 |              1 |               2 |               1 |                   1 | Northwest      | United States  | North America |
| 2017-02-16 00:00:00.000 | SO64253       |          215 |         11732 |              2 |               1 |               1 |                   2 | Northeast      | United States  | North America |
| 2017-12-29 00:00:00.000 | SO60998       |          528 |         11024 |              4 |               1 |               2 |                   4 | Southwest      | United States  | North America |
| 2016-10-02 00:00:00.000 | SO55434       |          477 |         11348 |              8 |               1 |               2 |                   8 | Germany        | Germany        | Europe        |
| 2017-03-27 00:00:00.000 | SO67008       |          215 |         23185 |              4 |               4 |               1 |                   4 | Southwest      | United States  | North America |
| 2016-08-09 00:00:00.000 | SO52328       |          484 |         18302 |              9 |               2 |               2 |                   9 | Australia      | Australia      | Pacific       |
| 2017-11-22 00:00:00.000 | SO58398       |          356 |         13319 |              1 |               1 |               1 |                   1 | Northwest      | United States  | North America |
| 2017-06-03 00:00:00.000 | SO72077       |          529 |         27736 |              1 |               2 |               3 |                   1 | Northwest      | United States  | North America |
| 2017-04-06 00:00:00.000 | SO67726       |          223 |         17636 |              8 |               3 |               2 |                   8 | Germany        | Germany        | Europe        |
| 2017-10-14 00:00:00.000 | SO56075       |          530 |         27914 |              4 |               1 |               2 |                   4 | Southwest      | United States  | North America |
| 2016-12-02 00:00:00.000 | SO59165       |          229 |         17036 |              6 |               2 |               1 |                   6 | Canada         | Canada         | North America |
| 2017-03-31 00:00:00.000 | SO67234       |          537 |         11141 |              4 |               1 |               1 |                   4 | Southwest      | United States  | North America |
| 2016-10-15 00:00:00.000 | SO56184       |          479 |         22045 |              1 |               2 |               1 |                   1 | Northwest      | United States  | North America |
| 2017-06-29 00:00:00.000 | SO74074       |          214 |         13580 |              8 |               2 |               1 |                   8 | Germany        | Germany        | Europe        |
| 2017-04-08 00:00:00.000 | SO67889       |          582 |         23663 |              9 |               1 |               1 |                   9 | Australia      | Australia      | Pacific       |
| 2016-04-17 00:00:00.000 | SO50058       |          381 |         14414 |              4 |               1 |               1 |                   4 | Southwest      | United States  | North America |
| 2017-05-27 00:00:00.000 | SO71430       |          223 |         18793 |              9 |               1 |               2 |                   9 | Australia      | Australia      | Pacific       |
| 2016-09-19 00:00:00.000 | SO54655       |          484 |         13148 |              6 |               3 |               2 |                   6 | Canada         | Canada         | North America |
| 2017-05-26 00:00:00.000 | SO71396       |          220 |         14547 |             10 |               3 |               1 |                  10 | United Kingdom | United Kingdom | Europe        |
| 2017-11-04 00:00:00.000 | SO57423       |          479 |         23066 |              4 |               2 |               2 |                   4 | Southwest      | United States  | North America |
| 2016-10-31 00:00:00.000 | SO57007       |          389 |         19744 |              4 |               1 |               1 |                   4 | Southwest      | United States  | North America |
| 2016-11-27 00:00:00.000 | SO58687       |          580 |         19564 |              9 |               1 |               1 |                   9 | Australia      | Australia      | Pacific       |
| 2016-11-03 00:00:00.000 | SO57307       |          362 |         12226 |              8 |               1 |               1 |                   8 | Germany        | Germany        | Europe        |
| 2017-08-22 00:00:00.000 | SO52956       |          358 |         11317 |              1 |               1 |               1 |                   1 | Northwest      | United States  | North America |
| 2017-10-17 00:00:00.000 | SO56231       |          540 |         18300 |              9 |               1 |               1 |                   9 | Australia      | Australia      | Pacific       |
| 2017-01-12 00:00:00.000 | SO61933       |          477 |         21771 |              4 |               2 |               2 |                   4 | Southwest      | United States  | North America |
| 2017-01-15 00:00:00.000 | SO62127       |          479 |         11248 |              7 |               1 |               2 |                   7 | France         | France         | Europe        |
| 2017-10-17 00:00:00.000 | SO56241       |          536 |         23357 |              4 |               1 |               1 |                   4 | Southwest      | United States  | North America |
| 2017-08-19 00:00:00.000 | SO52794       |          540 |         23801 |              1 |               1 |               1 |                   1 | Northwest      | United States  | North America |
| 2016-10-02 00:00:00.000 | SO55397       |          358 |         12314 |              8 |               1 |               1 |                   8 | Germany        | Germany        | Europe        |
| 2017-06-23 00:00:00.000 | SO73610       |          537 |         11086 |              4 |               2 |               1 |                   4 | Southwest      | United States  | North America |
| 2017-03-02 00:00:00.000 | SO65433       |          483 |         15944 |              1 |               5 |               1 |                   1 | Northwest      | United States  | North America |
| 2016-12-07 00:00:00.000 | SO59488       |          478 |         12854 |             10 |               2 |               2 |                  10 | United Kingdom | United Kingdom | Europe        |
| 2017-09-01 00:00:00.000 | SO53633       |          214 |         23473 |              1 |               3 |               1 |                   1 | Northwest      | United States  | North America |
| 2016-09-12 00:00:00.000 | SO54233       |          540 |         16361 |              4 |               3 |               1 |                   4 | Southwest      | United States  | North America |
| 2016-12-14 00:00:00.000 | SO60035       |          389 |         20207 |              4 |               1 |               1 |                   4 | Southwest      | United States  | North America |
| 2016-07-17 00:00:00.000 | SO51453       |          605 |         25605 |             10 |               1 |               1 |                  10 | United Kingdom | United Kingdom | Europe        |
| 2017-12-18 00:00:00.000 | SO60280       |          485 |         17802 |              8 |               3 |               2 |                   8 | Germany        | Germany        | Europe        |



---

## Functional-Dependency__case_111

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|   CityCOPONbr |   SalesTaxTypeID |   CityID | Effective Date          | SalesTaxType   | Description    |
|--------------:|-----------------:|---------:|:------------------------|:---------------|:---------------|
|          7210 |                5 |       56 | 2018-08-10 00:00:00.000 | 5GET           | Gas Excise Tax |
|          6225 |                5 |      443 | 2020-07-10 00:00:00.000 | 5GET           | Gas Excise Tax |
|           636 |                4 |      282 | 2017-01-11 00:00:00.000 | 4TOB           | Tobacco Tax    |
|          1023 |                1 |      390 | 2017-03-09 00:00:00.000 | 1STS           | Sales Tax      |
|          6155 |                5 |      372 | 2017-01-10 00:00:00.000 | 5GET           | Gas Excise Tax |
|          2314 |                1 |      420 | 2017-12-08 00:00:00.000 | 1STS           | Sales Tax      |
|          3808 |                3 |      281 | 2019-04-10 00:00:00.000 | 3CIG           | Cigarette Tax  |
|          5735 |                4 |      382 | 2018-09-12 00:00:00.000 | 4TOB           | Tobacco Tax    |
|          7214 |                1 |      360 | 2018-01-08 00:00:00.000 | 1STS           | Sales Tax      |
|          3115 |                5 |      303 | 2019-08-12 00:00:00.000 | 5GET           | Gas Excise Tax |
|          6819 |                4 |      409 | 2019-02-12 00:00:00.000 | 4TOB           | Tobacco Tax    |
|          7103 |                4 |      132 | 2018-08-13 00:00:00.000 | 4TOB           | Tobacco Tax    |
|           405 |                5 |       27 | 2019-08-12 00:00:00.000 | 5GET           | Gas Excise Tax |
|          4413 |                4 |      500 | 2019-05-13 00:00:00.000 | 4TOB           | Tobacco Tax    |
|          4603 |                1 |       89 | 2020-01-09 00:00:00.000 | 1STS           | Sales Tax      |
|          3520 |                5 |      312 | 2017-11-13 00:00:00.000 | 5GET           | Gas Excise Tax |
|          2414 |                4 |      187 | 2020-08-12 00:00:00.000 | 4TOB           | Tobacco Tax    |
|          3214 |                1 |       71 | 2020-10-09 00:00:00.000 | 1STS           | Sales Tax      |
|          3818 |                1 |      427 | 2018-05-09 00:00:00.000 | 1STS           | Sales Tax      |
|           637 |                1 |      347 | 2018-02-09 00:00:00.000 | 1STS           | Sales Tax      |
|          6119 |                2 |      216 | 2020-01-09 00:00:00.000 | 2STU           | Use Tax        |
|          7006 |                2 |      198 | 2018-07-09 00:00:00.000 | 2STU           | Use Tax        |
|          4030 |                5 |      233 | 2020-03-10 00:00:00.000 | 5GET           | Gas Excise Tax |
|          4805 |                2 |      258 | 2018-03-09 00:00:00.000 | 2STU           | Use Tax        |
|           105 |                5 |      441 | 2019-11-12 00:00:00.000 | 5GET           | Gas Excise Tax |
|          1404 |                2 |      532 | 2017-01-09 00:00:00.000 | 2STU           | Use Tax        |
|          6135 |                2 |      412 | 2021-02-08 00:00:00.000 | 2STU           | Use Tax        |
|          5715 |                5 |       60 | 2020-08-11 00:00:00.000 | 5GET           | Gas Excise Tax |
|          5118 |                4 |      492 | 2017-08-11 00:00:00.000 | 4TOB           | Tobacco Tax    |
|          4110 |                5 |       80 | 2018-02-12 00:00:00.000 | 5GET           | Gas Excise Tax |
|           814 |                2 |       37 | 2020-06-08 00:00:00.000 | 2STU           | Use Tax        |
|          4909 |                3 |      383 | 2019-12-11 00:00:00.000 | 3CIG           | Cigarette Tax  |
|          2407 |                4 |      144 | 2020-03-11 00:00:00.000 | 4TOB           | Tobacco Tax    |
|          4606 |                2 |      213 | 2019-08-09 00:00:00.000 | 2STU           | Use Tax        |
|           503 |                3 |       81 | 2019-09-11 00:00:00.000 | 3CIG           | Cigarette Tax  |
|          4505 |                5 |       57 | 2020-05-11 00:00:00.000 | 5GET           | Gas Excise Tax |
|          7306 |                5 |      556 | 2018-09-11 00:00:00.000 | 5GET           | Gas Excise Tax |
|          3226 |                3 |      607 | 2018-11-14 00:00:00.000 | 3CIG           | Cigarette Tax  |
|           813 |                3 |       16 | 2018-10-09 00:00:00.000 | 3CIG           | Cigarette Tax  |
|           904 |                1 |       70 | 2018-10-05 00:00:00.000 | 1STS           | Sales Tax      |
|          2504 |                4 |      560 | 2018-01-10 00:00:00.000 | 4TOB           | Tobacco Tax    |
|          5606 |                2 |      137 | 2018-04-09 00:00:00.000 | 2STU           | Use Tax        |
|          4412 |                5 |      139 | 2017-04-12 00:00:00.000 | 5GET           | Gas Excise Tax |
|          2616 |                2 |      373 | 2019-06-10 00:00:00.000 | 2STU           | Use Tax        |
|          5823 |                2 |      386 | 2020-05-08 00:00:00.000 | 2STU           | Use Tax        |
|          3528 |                4 |      311 | 2020-11-12 00:00:00.000 | 4TOB           | Tobacco Tax    |
|          6135 |                4 |      412 | 2019-05-13 00:00:00.000 | 4TOB           | Tobacco Tax    |
|          2617 |                3 |      406 | 2020-04-13 00:00:00.000 | 3CIG           | Cigarette Tax  |
|          4016 |                4 |      233 | 2017-07-12 00:00:00.000 | 4TOB           | Tobacco Tax    |
|          5909 |                1 |      293 | 2020-01-09 00:00:00.000 | 1STS           | Sales Tax      |



---

## Functional-Dependency__case_136

**Task:** Functional-Dependency

**Input:**

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



---

## Functional-Dependency__case_90

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Order ID   | Product ID   | Location ID   | Sales Person ID   | Customer ID   | Purchase Date           |   Quantity | Customer Name       | Customer Address   | Longitude   | Latitude   |
|:-----------|:-------------|:--------------|:------------------|:--------------|:------------------------|-----------:|:--------------------|:-------------------|:------------|:-----------|
| AX15456    | ENX2090      | A105          | EMP1006           | C1667         | 2019-08-16 00:00:00.000 |          2 | Kevin Lopez         |                    |             |            |
| AX14817    | ENX2035      | A177          | EMP1014           | C1584         | 2017-09-18 00:00:00.000 |          1 | Howard Harrison     |                    |             |            |
| AX24882    | ENX2029      | A188          | EMP1011           | C1395         | 2017-07-09 00:00:00.000 |          2 | Billy Reid          |                    |             |            |
| AX18918    | ENX2079      | A139          | EMP1003           | C1775         | 2019-04-01 00:00:00.000 |          1 | Kenneth Marshall    |                    |             |            |
| AX10196    | ENX2083      | A110          | EMP1008           | C1141         | 2019-05-22 00:00:00.000 |          1 | Phillip Harvey      |                    |             |            |
| AX22160    | ENX2068      | A167          | EMP1037           | C1543         | 2018-11-13 00:00:00.000 |          1 | Brian Kim           |                    |             |            |
| AX24319    | ENX2092      | A166          | EMP1044           | C1406         | 2019-09-16 00:00:00.000 |          1 | Paul Richardson     |                    |             |            |
| AX17585    | ENX2057      | A142          | EMP1030           | C1246         | 2018-06-25 00:00:00.000 |          1 | Ronald Bradley      |                    |             |            |
| AX11899    | ENX2064      | A173          | EMP1012           | C1205         | 2018-09-22 00:00:00.000 |          1 | Eric Shaw           |                    |             |            |
| AX16925    | ENX2057      | A126          | EMP1002           | C1047         | 2018-06-30 00:00:00.000 |          1 | Patrick Graham      |                    |             |            |
| AX23507    | ENX2082      | A154          | EMP1023           | C1140         | 2019-05-13 00:00:00.000 |          1 | Henry Reyes         |                    |             |            |
| AX23444    | ENX2056      | A118          | EMP1000           | C1216         | 2018-06-19 00:00:00.000 |          1 | Jimmy Harper        |                    |             |            |
| AX21334    | ENX2032      | A168          | EMP1014           | C1326         | 2017-08-18 00:00:00.000 |          2 | Matthew Duncan      |                    |             |            |
| AX14838    | ENX2025      | A119          | EMP1037           | C1463         | 2017-05-14 00:00:00.000 |          1 | Christopher Nguyen  |                    |             |            |
| AX21981    | ENX2093      | A123          | EMP1037           | C1317         | 2019-09-22 00:00:00.000 |          1 | Mark Morales        |                    |             |            |
| AX19383    | ENX2061      | A180          | EMP1001           | C1125         | 2018-08-16 00:00:00.000 |          1 | Nicholas Williamson |                    |             |            |
| AX19147    | ENX2021      | A105          | EMP1028           | C1191         | 2017-03-24 00:00:00.000 |          1 | Sean Vasquez        |                    |             |            |
| AX18266    | ENX2094      | A196          | EMP1009           | C1638         | 2019-10-07 00:00:00.000 |          2 | Jack Lynch          |                    |             |            |
| AX20023    | ENX2093      | A173          | EMP1037           | C1662         | 2019-09-21 00:00:00.000 |          2 | Jose Ellis          |                    |             |            |
| AX22388    | ENX2074      | A126          | EMP1038           | C1644         | 2019-01-28 00:00:00.000 |          1 | Terry Watson        |                    |             |            |
| AX23089    | ENX2065      | A125          | EMP1002           | C1232         | 2018-10-04 00:00:00.000 |          1 | Justin Butler       |                    |             |            |
| AX11496    | ENX2085      | A144          | EMP1032           | C1622         | 2019-06-18 00:00:00.000 |          1 | Joseph Warren       |                    |             |            |
| AX15912    | ENX2011      | A170          | EMP1005           | C1617         | 2016-11-18 00:00:00.000 |          1 | Albert Rice         |                    |             |            |
| AX16013    | ENX2060      | A152          | EMP1016           | C1250         | 2018-08-04 00:00:00.000 |          3 | Christopher Ramos   |                    |             |            |
| AX23943    | ENX2079      | A103          | EMP1017           | C1584         | 2019-03-28 00:00:00.000 |          1 | Howard Harrison     |                    |             |            |
| AX22644    | ENX2091      | A182          | EMP1021           | C1492         | 2019-09-04 00:00:00.000 |          1 | David Wilson        |                    |             |            |
| AX19054    | ENX2043      | A157          | EMP1012           | C1633         | 2018-01-05 00:00:00.000 |          1 | Ryan Ruiz           |                    |             |            |
| AX19428    | ENX2017      | A126          | EMP1010           | C1512         | 2017-02-05 00:00:00.000 |          1 | Shawn Ray           |                    |             |            |
| AX14442    | ENX2099      | A123          | EMP1014           | C1517         | 2019-12-17 00:00:00.000 |          3 | Eric Alvarez        |                    |             |            |
| AX11261    | ENX2077      | A125          | EMP1036           | C1274         | 2019-03-13 00:00:00.000 |          2 | Paul Henderson      |                    |             |            |
| AX17870    | ENX2036      | A151          | EMP1039           | C1400         | 2017-09-30 00:00:00.000 |          1 | Ralph Elliott       |                    |             |            |
| AX23715    | ENX2051      | A112          | EMP1035           | C1768         | 2018-04-18 00:00:00.000 |          1 | Stephen Greene      |                    |             |            |
| AX10169    | ENX2020      | A180          | EMP1018           | C1215         | 2017-03-21 00:00:00.000 |          1 | Jonathan Freeman    |                    |             |            |
| AX22115    | ENX2054      | A149          | EMP1009           | C1540         | 2018-05-23 00:00:00.000 |          3 | Victor Hughes       |                    |             |            |
| AX12361    | ENX2044      | A141          | EMP1040           | C1014         | 2018-01-19 00:00:00.000 |          3 | Jason Duncan        |                    |             |            |
| AX15107    | ENX2002      | A162          | EMP1009           | C1179         | 2016-07-31 00:00:00.000 |          3 | Juan Scott          |                    |             |            |
| AX11250    | ENX2071      | A137          | EMP1003           | C1459         | 2018-12-26 00:00:00.000 |          1 | Charles Sims        |                    |             |            |
| AX20655    | ENX2092      | A164          | EMP1031           | C1789         | 2019-09-09 00:00:00.000 |          1 | Steven Nichols      |                    |             |            |
| AX18635    | ENX2038      | A181          | EMP1005           | C1426         | 2017-10-25 00:00:00.000 |          4 | Steven Hayes        |                    |             |            |
| AX15771    | ENX2047      | A195          | EMP1025           | C1383         | 2018-02-19 00:00:00.000 |          1 | Gary Jones          |                    |             |            |
| AX22232    | ENX2067      | A154          | EMP1036           | C1438         | 2018-11-04 00:00:00.000 |          3 | George Thompson     |                    |             |            |
| AX24507    | ENX2075      | A153          | EMP1019           | C1286         | 2019-02-17 00:00:00.000 |          1 | Alan Sims           |                    |             |            |
| AX17939    | ENX2072      | A187          | EMP1031           | C1767         | 2019-01-02 00:00:00.000 |          2 | Donald Andrews      |                    |             |            |
| AX18238    | ENX2025      | A107          | EMP1027           | C1796         | 2017-05-25 00:00:00.000 |          1 | Patrick Hall        |                    |             |            |
| AX22651    | ENX2066      | A142          | EMP1029           | C1289         | 2018-10-19 00:00:00.000 |          2 | Ronald Anderson     |                    |             |            |
| AX20784    | ENX2050      | A129          | EMP1000           | C1697         | 2018-04-03 00:00:00.000 |          4 | Justin Miller       |                    |             |            |
| AX22410    | ENX2077      | A177          | EMP1017           | C1738         | 2019-03-07 00:00:00.000 |          1 | Shawn Owens         |                    |             |            |
| AX10625    | ENX2003      | A102          | EMP1035           | C1435         | 2016-08-18 00:00:00.000 |          2 | Kevin Campbell      |                    |             |            |
| AX10838    | ENX2100      | A132          | EMP1023           | C1229         | 2019-12-19 00:00:00.000 |          1 | Larry Ray           |                    |             |            |
| AX16514    | ENX2098      | A150          | EMP1012           | C1408         | 2019-12-05 00:00:00.000 |          1 | Carl Reid           |                    |             |            |



---

## Functional-Dependency__case_251

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Date                    |   ProductId |   Sale Amount | Product Name   | Category   |
|:------------------------|------------:|--------------:|:---------------|:-----------|
| 2015-12-25 00:00:00.000 |           4 |       42548.8 | Product4       | Cat1       |
| 2020-03-18 00:00:00.000 |          12 |      168732   | Product12      | Cat3       |
| 2016-09-29 00:00:00.000 |           7 |       40552.2 | Product7       | Cat2       |
| 2018-04-23 00:00:00.000 |          10 |      106138   | Product10      | Cat3       |
| 2020-06-18 00:00:00.000 |           8 |      235742   | Product8       | Cat3       |
| 2020-03-03 00:00:00.000 |          10 |      237106   | Product10      | Cat3       |
| 2017-10-30 00:00:00.000 |           1 |       65704   | Product1       | Cat1       |
| 2015-07-30 00:00:00.000 |          10 |       60236   | Product10      | Cat3       |
| 2017-06-18 00:00:00.000 |           5 |      101198   | Product5       | Cat2       |
| 2019-01-14 00:00:00.000 |          10 |      105515   | Product10      | Cat3       |
| 2020-05-26 00:00:00.000 |           2 |      190518   | Product2       | Cat1       |
| 2015-03-16 00:00:00.000 |           2 |       46728   | Product2       | Cat1       |
| 2019-06-10 00:00:00.000 |           9 |      223503   | Product9       | Cat3       |
| 2015-10-17 00:00:00.000 |          14 |       58879   | Product14      | Cat4       |
| 2014-08-20 00:00:00.000 |           5 |       20266.2 | Product5       | Cat2       |
| 2018-08-05 00:00:00.000 |           7 |       99603.2 | Product7       | Cat2       |
| 2016-12-24 00:00:00.000 |           7 |       73612   | Product7       | Cat2       |
| 2016-05-23 00:00:00.000 |           4 |       89645.6 | Product4       | Cat1       |
| 2019-12-09 00:00:00.000 |           1 |      228552   | Product1       | Cat1       |
| 2017-04-12 00:00:00.000 |           1 |       47201.7 | Product1       | Cat1       |
| 2016-07-09 00:00:00.000 |           5 |       74993.8 | Product5       | Cat2       |
| 2017-01-18 00:00:00.000 |          15 |       76319.4 | Product15      | Cat4       |
| 2019-04-19 00:00:00.000 |          14 |      137313   | Product14      | Cat4       |
| 2018-05-25 00:00:00.000 |          14 |      170404   | Product14      | Cat4       |
| 2019-08-27 00:00:00.000 |          15 |      215947   | Product15      | Cat4       |
| 2016-12-11 00:00:00.000 |           7 |      110990   | Product7       | Cat2       |
| 2014-10-16 00:00:00.000 |          15 |       25352.9 | Product15      | Cat4       |
| 2019-02-19 00:00:00.000 |           9 |      120008   | Product9       | Cat3       |
| 2018-02-25 00:00:00.000 |           7 |       99678.6 | Product7       | Cat2       |
| 2014-07-13 00:00:00.000 |          13 |       16296.4 | Product13      | Cat4       |
| 2016-08-05 00:00:00.000 |           8 |       90604.8 | Product8       | Cat3       |
| 2018-10-23 00:00:00.000 |          10 |      105946   | Product10      | Cat3       |
| 2020-06-18 00:00:00.000 |          12 |      141831   | Product12      | Cat3       |
| 2015-11-03 00:00:00.000 |           8 |       23908.8 | Product8       | Cat3       |
| 2014-05-15 00:00:00.000 |           9 |       28066.5 | Product9       | Cat3       |
| 2015-06-04 00:00:00.000 |           2 |       52768   | Product2       | Cat1       |
| 2016-04-25 00:00:00.000 |           3 |       51514   | Product3       | Cat1       |
| 2020-06-03 00:00:00.000 |           9 |      179516   | Product9       | Cat3       |
| 2019-07-15 00:00:00.000 |          10 |      160397   | Product10      | Cat3       |
| 2019-06-01 00:00:00.000 |           9 |      208282   | Product9       | Cat3       |
| 2020-08-12 00:00:00.000 |           2 |      273233   | Product2       | Cat1       |
| 2018-09-03 00:00:00.000 |           3 |      127214   | Product3       | Cat1       |
| 2019-07-02 00:00:00.000 |           4 |      202774   | Product4       | Cat1       |
| 2014-08-30 00:00:00.000 |           1 |       38524.4 | Product1       | Cat1       |
| 2014-12-11 00:00:00.000 |           1 |       14454   | Product1       | Cat1       |
| 2016-09-25 00:00:00.000 |          12 |       65611.6 | Product12      | Cat3       |
| 2018-04-16 00:00:00.000 |           5 |      167129   | Product5       | Cat2       |
| 2015-12-27 00:00:00.000 |           8 |       48344.8 | Product8       | Cat3       |
| 2017-06-06 00:00:00.000 |           5 |       65898.7 | Product5       | Cat2       |
| 2017-11-14 00:00:00.000 |           9 |      102504   | Product9       | Cat3       |



---

## Functional-Dependency__case_118

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|   TransferID |   PlayerID |   TransferFee |   TeamLeftID |   TeamJoinedID | Player               | Position           |   Age |   MarketValue |
|-------------:|-----------:|--------------:|-------------:|---------------:|:---------------------|:-------------------|------:|--------------:|
|          544 |      60394 |       2500000 |          127 |             79 | Philipp Klement      | Attacking Midfield |    27 |       2500000 |
|         1651 |     109436 |             0 |           30 |           2036 | Oliver Hüsing        | Centre-Back        |    26 |        500000 |
|          660 |     314295 |       2000000 |          379 |            167 | Reece Oxford         | Centre-Back        |    20 |       4000000 |
|          804 |     263431 |       1200000 |         1322 |             62 | David Hovorka        | Centre-Back        |    26 |       1250000 |
|         6984 |     283127 |         35000 |         1416 |           1095 | Oualid El Hajjam     | Right-Back         |    28 |       1000000 |
|          987 |     148344 |        670000 |          504 |           1053 | Lucas Andersen       | Second Striker     |    25 |       1500000 |
|         2785 |     282631 |             0 |         6418 |           2402 | Nicolás Maná         | Right Winger       |    25 |        450000 |
|         1253 |     324503 |        250000 |           80 |            403 | Vangelis Pavlidis    | Centre-Forward     |    20 |       1000000 |
|         2694 |      55911 |             0 |          830 |           2063 | Adrián Calello       | Defensive Midfield |    32 |        300000 |
|         1260 |     391742 |        250000 |           41 |            105 | Patric Pfeiffer      | Centre-Back        |    20 |        100000 |
|          472 |     203043 |       3000000 |          472 |           1533 | Pedro Bigas          | Centre-Back        |    29 |       3000000 |
|         1049 |     260846 |        500000 |          409 |              4 | Asger Sörensen       | Centre-Back        |    23 |        900000 |
|         3115 |      83430 |             0 |          405 |            703 | Albert Adomah        | Right Winger       |    31 |       3500000 |
|         1892 |      37152 |             0 |          405 |           1110 | Tommy Elphick        | Centre-Back        |    32 |       2000000 |
|          789 |     458537 |       1300000 |         1274 |            206 | Tobias Börkeeiet     | Defensive Midfield |    20 |        400000 |
|         3330 |      62064 |             0 |         6954 |           1283 | Tom Hiariej          | Defensive Midfield |    31 |        350000 |
|          227 |     126737 |       8000000 |          681 |            150 | Juanmi               | Right Winger       |    26 |       8000000 |
|           22 |     323704 |      40000000 |          131 |            964 | Malcom               | Right Winger       |    22 |      40000000 |
|         1046 |     182688 |        500000 |          605 |          11282 | Manolis Siopis       | Defensive Midfield |    25 |       1000000 |
|          603 |     428302 |       2200000 |          358 |            641 | Anfernee Dijksteel   | Right-Back         |    22 |             0 |
|         1769 |     122421 |             0 |         1090 |            200 | Adam Maher           | Central Midfield   |    26 |       4000000 |
|          105 |     525287 |      17000000 |         6195 |            294 | Carlos Vinícius      | Centre-Forward     |    24 |       7000000 |
|          344 |     392570 |       5000000 |           46 |           6574 | Marco Sala           | Left-Back          |    20 |        300000 |
|         3875 |      41581 |             0 |         2843 |           2844 | Maic Sema            | Right Midfield     |    30 |        700000 |
|           81 |     165895 |      20000000 |         6574 |             46 | Matteo Politano      | Right Winger       |    26 |      30000000 |
|          840 |      56830 |       1000000 |         1025 |            410 | Sebastien De Maio    | Centre-Back        |    32 |       1000000 |
|          563 |     456535 |       2500000 |         2696 |            415 | Agustín Rogel        | Centre-Back        |    22 |       1000000 |
|          933 |     164108 |        800000 |         4083 |             19 | Bruno Martella       | Left-Back          |    27 |       1800000 |
|         3493 |      74295 |             0 |          187 |            269 | Aleksandar Ignjovski | Defensive Midfield |    28 |        500000 |
|          609 |     308278 |       2000000 |           46 |           1532 | Rey Manaj            | Centre-Forward     |    22 |       1500000 |
|         3296 |     221986 |             0 |          648 |           2296 | Héctor Hernández     | Left-Back          |    28 |        300000 |
|         3248 |     182936 |             0 |          122 |           7179 | Filipe Ferreira      | Left-Back          |    29 |        350000 |
|         3537 |      55801 |             0 |         1038 |           4171 | Marco Sau            | Centre-Forward     |    31 |        400000 |
|          465 |     113036 |       3200000 |         1148 |            984 | Romaine Sawyers      | Attacking Midfield |    27 |       3000000 |
|         1127 |     243879 |        400000 |          504 |           1290 | Charles Pickel       | Defensive Midfield |    22 |        750000 |
|          256 |      84765 |       7500000 |          749 |           6574 | Francesco Caputo     | Centre-Forward     |    32 |       4000000 |
|         3397 |     324829 |             0 |          321 |          10004 | Anthony Maisonnial   | Goalkeeper         |    21 |        400000 |
|          615 |     140748 |       2000000 |          416 |            199 | Danilo Avelar        | Left-Back          |    30 |       1500000 |
|         4287 |     121686 |             0 |          371 |             80 | Cristian Gamboa      | Right-Back         |    29 |        750000 |
|         1074 |     248330 |        500000 |         3368 |            703 | Chema                | Centre-Back        |    27 |       2500000 |
|         1722 |       9594 |             0 |          281 |             58 | Vincent Kompany      | Centre-Back        |    33 |       8000000 |
|         3326 |     118375 |             0 |        12301 |          19806 | Dardo Miloc          | Central Midfield   |    29 |        400000 |
|         1726 |      53359 |             0 |         3008 |            221 | Evandro              | Attacking Midfield |    33 |       1500000 |
|         1056 |     146918 |        500000 |          964 |           1083 | Egor Baburin         | Goalkeeper         |    26 |        750000 |
|          876 |     223560 |       1000000 |         1244 |            210 | Luciano              | Centre-Forward     |    26 |       2000000 |
|         1858 |       5782 |             0 |         6890 |             36 | Emre Belözoglu       | Central Midfield   |    39 |        400000 |
|          571 |     368559 |       2500000 |         1025 |            698 | Ádám Nagy            | Defensive Midfield |    24 |       2000000 |
|         3211 |     333942 |             0 |           91 |           1557 | Lion Schweers        | Centre-Back        |    23 |        350000 |
|         2292 |     240497 |             0 |         2293 |          19789 | Moryké Fofana        | Left Winger        |    27 |       1200000 |
|         1077 |     268670 |        500000 |         1244 |          12321 | Gerard Gumbau        | Central Midfield   |    24 |       2500000 |



---

## Functional-Dependency__case_252

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Financial Statement Breakdown   | Entity   | Actual/Budget   | Date                    |            Value | Financial Statement List        | Category               | Main Category   |
|:--------------------------------|:---------|:----------------|:------------------------|-----------------:|:--------------------------------|:-----------------------|:----------------|
| SPU Training                    | Praxair  | Budget          | 2016-02-29 00:00:00.000 | 115442           | SPU Training                    | Other Expenses         | Expenses        |
| COS - Labor Burden              | Apotheca | Budget          | 2016-10-31 00:00:00.000 |  87208.4         | COS - Labor Burden              | COGS                   | Expenses        |
| Insurance-Workers Comp          | Holston  | Budget          | 2016-06-30 00:00:00.000 |  55933.7         | Insurance-Workers Comp          | Insurance              | Expenses        |
| Training Travel Expenses        | Holston  | Actual          | 2014-01-31 00:00:00.000 |  13237.1         | Training Travel Expenses        | Other Expenses         | Expenses        |
| Insurance - Liability/Umbrella  | Praxair  | Actual          | 2016-05-31 00:00:00.000 |  11198.3         | Insurance - Liability/Umbrella  | Insurance              | Expenses        |
| Telecommunications              | Apotheca | Actual          | 2015-01-31 00:00:00.000 |  14443.9         | Telecommunications              | Telecommunications     | Expenses        |
| Insurance - Liability/Umbrella  | Praxair  | Budget          | 2015-10-31 00:00:00.000 |   8538.99        | Insurance - Liability/Umbrella  | Insurance              | Expenses        |
| Inactive Job Costs              | Holston  | Budget          | 2014-11-30 00:00:00.000 | 241632           | Inactive Job Costs              | Other Expenses         | Expenses        |
| P/R - 401M Expense              | Praxair  | Budget          | 2016-01-31 00:00:00.000 |  15069.3         | P/R - 401M Expense              | Payroll                | Expenses        |
| COS - Commissions               | Praxair  | Budget          | 2014-07-31 00:00:00.000 | 472074           | COS - Commissions               | COGS                   | Expenses        |
| Health Insurance Const.Admin    | Holston  | Actual          | 2015-12-31 00:00:00.000 |  81298.8         | Health Insurance Const.Admin    | Payroll                | Expenses        |
| Workers Comp - Const.Admin      | Praxair  | Budget          | 2014-08-31 00:00:00.000 |   5674.82        | Workers Comp - Const.Admin      | Payroll                | Expenses        |
| Direct Advertising Expense      | Holston  | Budget          | 2015-05-31 00:00:00.000 | 643466           | Direct Advertising Expense      | Marketing              | Expenses        |
| Home Show Branch Directed       | Praxair  | Budget          | 2016-08-31 00:00:00.000 |  19297.8         | Home Show Branch Directed       | Marketing              | Expenses        |
| Home Show Branch Directed       | Holston  | Actual          | 2015-10-31 00:00:00.000 |   9327.02        | Home Show Branch Directed       | Marketing              | Expenses        |
| COS - Equipment                 | Holston  | Budget          | 2016-07-31 00:00:00.000 |  91497.6         | COS - Equipment                 | COGS                   | Expenses        |
| Office Security                 | Apotheca | Budget          | 2015-11-30 00:00:00.000 |   1566.09        | Office Security                 | Office Supplies        | Expenses        |
| Office Security                 | Praxair  | Actual          | 2016-03-31 00:00:00.000 |   2110.9         | Office Security                 | Office Supplies        | Expenses        |
| Utilities - Office              | Praxair  | Budget          | 2016-09-30 00:00:00.000 |  22084.3         | Utilities - Office              | Offices Utilities      | Expenses        |
| Rent - Office                   | Holston  | Budget          | 2015-01-31 00:00:00.000 | 105349           | Rent - Office                   | Renting Office Space   | Expenses        |
| Training Travel Expenses        | Apotheca | Actual          | 2016-02-29 00:00:00.000 |  35601.9         | Training Travel Expenses        | Other Expenses         | Expenses        |
| SPU Training                    | Holston  | Actual          | 2016-05-31 00:00:00.000 | 128612           | SPU Training                    | Other Expenses         | Expenses        |
| COS - Commissions               | Apotheca | Budget          | 2014-02-28 00:00:00.000 | 344876           | COS - Commissions               | COGS                   | Expenses        |
| Insurance - Liability/Umbrella  | Holston  | Actual          | 2014-09-30 00:00:00.000 |   3835.94        | Insurance - Liability/Umbrella  | Insurance              | Expenses        |
| COS - Commissions               | Apotheca | Budget          | 2015-03-31 00:00:00.000 | 838052           | COS - Commissions               | COGS                   | Expenses        |
| Workers Comp - Const.Admin      | Holston  | Budget          | 2015-06-30 00:00:00.000 |   9861.65        | Workers Comp - Const.Admin      | Payroll                | Expenses        |
| Revenue Installed               | Holston  | Budget          | 2016-06-30 00:00:00.000 |      1.45962e+07 | Revenue Installed               | Revenue                | Revenue         |
| COS - Repair Fund               | Apotheca | Budget          | 2014-04-30 00:00:00.000 |  39553.1         | COS - Repair Fund               | COGS                   | Expenses        |
| Revenue Installed-Lighting      | Apotheca | Actual          | 2016-09-30 00:00:00.000 | 632440           | Revenue Installed-Lighting      | Revenue                | Revenue         |
| Stone Discount Allocation       | Apotheca | Budget          | 2014-08-31 00:00:00.000 | -57661           | Stone Discount Allocation       | Other Expenses         | Expenses        |
| Training Travel Expenses        | Holston  | Actual          | 2016-10-31 00:00:00.000 |  51123.1         | Training Travel Expenses        | Other Expenses         | Expenses        |
| Fuel Expense - Const.Admin      | Holston  | Actual          | 2015-04-30 00:00:00.000 |  28067.9         | Fuel Expense - Const.Admin      | Fuel                   | Expenses        |
| P/R Taxes Sales/Admin           | Holston  | Budget          | 2016-09-30 00:00:00.000 |  45808           | P/R Taxes Sales/Admin           | Payroll                | Expenses        |
| Telecommunications              | Praxair  | Budget          | 2014-12-31 00:00:00.000 |  15632.9         | Telecommunications              | Telecommunications     | Expenses        |
| Extraordinary Income/Expense    | Apotheca | Budget          | 2014-12-31 00:00:00.000 | -52438.4         | Extraordinary Income/Expense    | General & Admin        | Expenses        |
| Depreciation Expense            | Holston  | Actual          | 2014-04-30 00:00:00.000 |  26203.5         | Depreciation Expense            | Depreciation Expense   | Expenses        |
| Sealer Material                 | Praxair  | Budget          | 2014-01-31 00:00:00.000 |   9636.54        | Sealer Material                 | Equipment              | Expenses        |
| Recruiting                      | Apotheca | Actual          | 2016-02-29 00:00:00.000 |  65005.1         | Recruiting                      | Recruitment            | Expenses        |
| T&E - Lodging                   | Praxair  | Actual          | 2016-02-29 00:00:00.000 |   6703.67        | T&E - Lodging                   | Travel & Entertainment | Expenses        |
| Revenue Installed-Turf          | Praxair  | Actual          | 2015-02-28 00:00:00.000 | 180902           | Revenue Installed-Turf          | Revenue                | Revenue         |
| P/R - 401M Expense              | Apotheca | Budget          | 2014-02-28 00:00:00.000 |   4374.45        | P/R - 401M Expense              | Payroll                | Expenses        |
| Professional Fees - Legal       | Praxair  | Actual          | 2015-02-28 00:00:00.000 |    508.215       | Professional Fees - Legal       | Professional Fees      | Expenses        |
| Revenue Adjust - Closed Jobs    | Apotheca | Actual          | 2014-03-31 00:00:00.000 | 155901           | Revenue Adjust - Closed Jobs    | Revenue                | Revenue         |
| P/R Taxes Sales/Admin           | Holston  | Budget          | 2014-12-31 00:00:00.000 |  14039.7         | P/R Taxes Sales/Admin           | Payroll                | Expenses        |
| Canvassing                      | Apotheca | Budget          | 2014-08-31 00:00:00.000 |  91085.1         | Canvassing                      | Marketing              | Expenses        |
| Home Show Branch Directed       | Apotheca | Budget          | 2015-03-31 00:00:00.000 |  10765.2         | Home Show Branch Directed       | Marketing              | Expenses        |
| Rental Yard/Storage             | Praxair  | Actual          | 2014-01-31 00:00:00.000 |    851.642       | Rental Yard/Storage             | Other Expenses         | Expenses        |
| Revenue Installed-Water Feature | Holston  | Actual          | 2014-09-30 00:00:00.000 |   9808.32        | Revenue Installed-Water Feature | Revenue                | Revenue         |
| Telecomm - Broadband            | Praxair  | Actual          | 2014-11-30 00:00:00.000 |   3675.38        | Telecomm - Broadband            | Telecommunications     | Expenses        |
| Revenue Adjust - Closed Jobs    | Holston  | Actual          | 2016-03-31 00:00:00.000 | 513399           | Revenue Adjust - Closed Jobs    | Revenue                | Revenue         |



---

## Functional-Dependency__case_249

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Order ID   | Product ID   | Location ID   | Sales Person ID   | Customer ID   | Purchase Date           |   Quantity | Customer Name       | Profit Groups   |   Average Sales | Sales Grouping   |
|:-----------|:-------------|:--------------|:------------------|:--------------|:------------------------|-----------:|:--------------------|:----------------|----------------:|:-----------------|
| AX15456    | ENX2090      | A105          | EMP1006           | C1667         | 2016-11-25 00:00:00.000 |          2 | Kevin Lopez         | Poor Clients    |        12932.3  | Mid Sales        |
| AX14817    | ENX2035      | A177          | EMP1014           | C1584         | 2017-12-26 00:00:00.000 |          1 | Howard Harrison     | Ok Client       |        12583    | Mid Sales        |
| AX24882    | ENX2029      | A188          | EMP1011           | C1395         | 2015-09-06 00:00:00.000 |          2 | Billy Reid          | Poor Clients    |        12224    | Mid Sales        |
| AX18918    | ENX2079      | A139          | EMP1003           | C1775         | 2017-05-11 00:00:00.000 |          1 | Kenneth Marshall    | Ok Client       |        17741.3  | High Sales       |
| AX10196    | ENX2083      | A110          | EMP1008           | C1141         | 2015-06-22 00:00:00.000 |          1 | Phillip Harvey      | Good Client     |        24737    | High Sales       |
| AX22160    | ENX2068      | A167          | EMP1037           | C1543         | 2016-11-26 00:00:00.000 |          1 | Brian Kim           | Ok Client       |        21600    | High Sales       |
| AX24319    | ENX2092      | A166          | EMP1044           | C1406         | 2016-06-26 00:00:00.000 |          1 | Paul Richardson     | Ok Client       |        13359.3  | Mid Sales        |
| AX17585    | ENX2057      | A142          | EMP1030           | C1246         | 2016-08-25 00:00:00.000 |          1 | Ronald Bradley      | Good Client     |        25576    | Very High Sales  |
| AX11899    | ENX2064      | A173          | EMP1012           | C1205         | 2017-05-13 00:00:00.000 |          1 | Eric Shaw           | Ok Client       |        16738    | High Sales       |
| AX16925    | ENX2057      | A126          | EMP1002           | C1047         | 2015-04-19 00:00:00.000 |          1 | Patrick Graham      | Ok Client       |        15021    | High Sales       |
| AX23507    | ENX2082      | A154          | EMP1023           | C1140         | 2016-01-20 00:00:00.000 |          1 | Henry Reyes         | Ok Client       |        16050.7  | High Sales       |
| AX23444    | ENX2056      | A118          | EMP1000           | C1216         | 2016-06-11 00:00:00.000 |          1 | Jimmy Harper        | Ok Client       |        12398.7  | Mid Sales        |
| AX21334    | ENX2032      | A168          | EMP1014           | C1326         | 2016-04-22 00:00:00.000 |          2 | Matthew Duncan      | Ok Client       |        17877.3  | High Sales       |
| AX14838    | ENX2025      | A119          | EMP1037           | C1463         | 2015-10-05 00:00:00.000 |          1 | Christopher Nguyen  | Ok Client       |        19992.3  | High Sales       |
| AX21981    | ENX2093      | A123          | EMP1037           | C1317         | 2015-07-20 00:00:00.000 |          1 | Mark Morales        | Good Client     |        18845.3  | High Sales       |
| AX19383    | ENX2061      | A180          | EMP1001           | C1125         | 2016-05-13 00:00:00.000 |          1 | Nicholas Williamson | Ok Client       |        18782    | High Sales       |
| AX19147    | ENX2021      | A105          | EMP1028           | C1191         | 2015-03-26 00:00:00.000 |          1 | Sean Vasquez        | Poor Clients    |         4768.33 | Low Sales        |
| AX18266    | ENX2094      | A196          | EMP1009           | C1638         | 2016-04-13 00:00:00.000 |          2 | Jack Lynch          | Poor Clients    |         6377.67 | Low Sales        |
| AX20023    | ENX2093      | A173          | EMP1037           | C1662         | 2015-11-27 00:00:00.000 |          2 | Jose Ellis          | Poor Clients    |        10862.7  | Mid Sales        |
| AX22388    | ENX2074      | A126          | EMP1038           | C1644         | 2015-08-25 00:00:00.000 |          1 | Terry Watson        | Ok Client       |        10734.3  | Mid Sales        |
| AX23089    | ENX2065      | A125          | EMP1002           | C1232         | 2015-07-11 00:00:00.000 |          1 | Justin Butler       | Ok Client       |        21822.7  | High Sales       |
| AX11496    | ENX2085      | A144          | EMP1032           | C1622         | 2015-08-30 00:00:00.000 |          1 | Joseph Warren       | Poor Clients    |        12514.7  | Mid Sales        |
| AX15912    | ENX2011      | A170          | EMP1005           | C1617         | 2017-02-24 00:00:00.000 |          1 | Albert Rice         | Ok Client       |        20023    | High Sales       |
| AX16013    | ENX2060      | A152          | EMP1016           | C1250         | 2016-05-08 00:00:00.000 |          3 | Christopher Ramos   | Poor Clients    |        11520    | Mid Sales        |
| AX23943    | ENX2079      | A103          | EMP1017           | C1584         | 2017-10-15 00:00:00.000 |          1 | Howard Harrison     | Ok Client       |        12583    | Mid Sales        |
| AX22644    | ENX2091      | A182          | EMP1021           | C1492         | 2016-04-18 00:00:00.000 |          1 | David Wilson        | Poor Clients    |         7392.33 | Low Sales        |
| AX19054    | ENX2043      | A157          | EMP1012           | C1633         | 2016-08-22 00:00:00.000 |          1 | Ryan Ruiz           | Ok Client       |        17823    | High Sales       |
| AX19428    | ENX2017      | A126          | EMP1010           | C1512         | 2017-06-17 00:00:00.000 |          1 | Shawn Ray           | Ok Client       |        19197    | High Sales       |
| AX14442    | ENX2099      | A123          | EMP1014           | C1517         | 2015-03-08 00:00:00.000 |          3 | Eric Alvarez        | Ok Client       |        16904    | High Sales       |
| AX11261    | ENX2077      | A125          | EMP1036           | C1274         | 2017-03-04 00:00:00.000 |          2 | Paul Henderson      | Ok Client       |        16029.7  | High Sales       |
| AX17870    | ENX2036      | A151          | EMP1039           | C1400         | 2016-06-12 00:00:00.000 |          1 | Ralph Elliott       | Ok Client       |        19995.7  | High Sales       |
| AX23715    | ENX2051      | A112          | EMP1035           | C1768         | 2015-07-29 00:00:00.000 |          1 | Stephen Greene      | Ok Client       |        17070    | High Sales       |
| AX10169    | ENX2020      | A180          | EMP1018           | C1215         | 2017-09-17 00:00:00.000 |          1 | Jonathan Freeman    | Ok Client       |        11523.3  | Mid Sales        |
| AX22115    | ENX2054      | A149          | EMP1009           | C1540         | 2017-08-02 00:00:00.000 |          3 | Victor Hughes       | Ok Client       |        15851.3  | High Sales       |
| AX12361    | ENX2044      | A141          | EMP1040           | C1014         | 2015-04-22 00:00:00.000 |          3 | Jason Duncan        | Ok Client       |        14544.3  | Mid Sales        |
| AX15107    | ENX2002      | A162          | EMP1009           | C1179         | 2016-01-03 00:00:00.000 |          3 | Juan Scott          | Ok Client       |        16789    | High Sales       |
| AX11250    | ENX2071      | A137          | EMP1003           | C1459         | 2017-07-28 00:00:00.000 |          1 | Charles Sims        | Ok Client       |        13662.7  | Mid Sales        |
| AX20655    | ENX2092      | A164          | EMP1031           | C1789         | 2015-10-12 00:00:00.000 |          1 | Steven Nichols      | Poor Clients    |         7662    | Low Sales        |
| AX18635    | ENX2038      | A181          | EMP1005           | C1426         | 2016-01-07 00:00:00.000 |          4 | Steven Hayes        | Ok Client       |        16256.7  | High Sales       |
| AX15771    | ENX2047      | A195          | EMP1025           | C1383         | 2017-04-22 00:00:00.000 |          1 | Gary Jones          | Poor Clients    |        11946.3  | Mid Sales        |
| AX22232    | ENX2067      | A154          | EMP1036           | C1438         | 2017-04-05 00:00:00.000 |          3 | George Thompson     | Ok Client       |        13874    | Mid Sales        |
| AX24507    | ENX2075      | A153          | EMP1019           | C1286         | 2017-07-16 00:00:00.000 |          1 | Alan Sims           | Poor Clients    |         8617.67 | Low Sales        |
| AX17939    | ENX2072      | A187          | EMP1031           | C1767         | 2015-12-15 00:00:00.000 |          2 | Donald Andrews      | Ok Client       |        17098.7  | High Sales       |
| AX18238    | ENX2025      | A107          | EMP1027           | C1796         | 2017-12-09 00:00:00.000 |          1 | Patrick Hall        | Ok Client       |        13187.7  | Mid Sales        |
| AX22651    | ENX2066      | A142          | EMP1029           | C1289         | 2015-10-05 00:00:00.000 |          2 | Ronald Anderson     | Ok Client       |        14603.7  | Mid Sales        |
| AX20784    | ENX2050      | A129          | EMP1000           | C1697         | 2016-08-24 00:00:00.000 |          4 | Justin Miller       | Ok Client       |        13200.7  | Mid Sales        |
| AX22410    | ENX2077      | A177          | EMP1017           | C1738         | 2016-01-06 00:00:00.000 |          1 | Shawn Owens         | Ok Client       |        16242.3  | High Sales       |
| AX10625    | ENX2003      | A102          | EMP1035           | C1435         | 2015-01-10 00:00:00.000 |          2 | Kevin Campbell      | Ok Client       |        13401    | Mid Sales        |
| AX10838    | ENX2100      | A132          | EMP1023           | C1229         | 2015-01-11 00:00:00.000 |          1 | Larry Ray           | Poor Clients    |         8155.67 | Low Sales        |
| AX16514    | ENX2098      | A150          | EMP1012           | C1408         | 2016-12-29 00:00:00.000 |          1 | Carl Reid           | Ok Client       |        13259    | Mid Sales        |



---

## Functional-Dependency__case_255

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Date                    |   EMP ID | Product ID   |   Unit Sold |   Revenue | EMP Name   | Supervisor   |
|:------------------------|---------:|:-------------|------------:|----------:|:-----------|:-------------|
| 2019-03-31 00:00:00.000 |    10013 | P10010       |         165 |      9075 | EMP-13     | Supervisor-3 |
| 2019-03-05 00:00:00.000 |    10011 | P10003       |         236 |      9204 | EMP-11     | Supervisor-3 |
| 2019-04-09 00:00:00.000 |    10006 | P10019       |         244 |     19276 | EMP-6      | Supervisor-1 |
| 2019-01-02 00:00:00.000 |    10006 | P10015       |         125 |     15250 | EMP-6      | Supervisor-1 |
| 2019-01-12 00:00:00.000 |    10001 | P10008       |         128 |      8704 | EMP-1      | Supervisor-1 |
| 2019-03-03 00:00:00.000 |    10012 | P10016       |         243 |     22356 | EMP-12     | Supervisor-3 |
| 2019-03-15 00:00:00.000 |    10014 | P10029       |         185 |     23865 | EMP-14     | Supervisor-3 |
| 2019-01-29 00:00:00.000 |    10008 | P10016       |         205 |     18860 | EMP-8      | Supervisor-2 |
| 2019-04-05 00:00:00.000 |    10011 | P10029       |          60 |      7740 | EMP-11     | Supervisor-3 |
| 2019-03-14 00:00:00.000 |    10018 | P10014       |          79 |     11850 | EMP-18     | Supervisor-4 |
| 2019-03-18 00:00:00.000 |    10009 | P10010       |          79 |      4345 | EMP-9      | Supervisor-2 |
| 2019-01-20 00:00:00.000 |    10012 | P10020       |         214 |     14980 | EMP-12     | Supervisor-3 |
| 2019-01-15 00:00:00.000 |    10006 | P10001       |         103 |      6180 | EMP-6      | Supervisor-1 |
| 2019-03-10 00:00:00.000 |    10009 | P10013       |         194 |     18818 | EMP-9      | Supervisor-2 |
| 2019-03-14 00:00:00.000 |    10009 | P10016       |          77 |      7084 | EMP-9      | Supervisor-2 |
| 2019-03-26 00:00:00.000 |    10010 | P10005       |         248 |     10912 | EMP-10     | Supervisor-2 |
| 2019-04-20 00:00:00.000 |    10015 | P10024       |         232 |     15776 | EMP-15     | Supervisor-3 |
| 2019-01-27 00:00:00.000 |    10018 | P10024       |         117 |      7956 | EMP-18     | Supervisor-4 |
| 2019-02-07 00:00:00.000 |    10005 | P10009       |         266 |     19418 | EMP-5      | Supervisor-1 |
| 2019-03-22 00:00:00.000 |    10001 | P10008       |         123 |      8364 | EMP-1      | Supervisor-1 |
| 2019-01-07 00:00:00.000 |    10013 | P10016       |         294 |     27048 | EMP-13     | Supervisor-3 |
| 2019-04-01 00:00:00.000 |    10014 | P10003       |         147 |      5733 | EMP-14     | Supervisor-3 |
| 2019-01-03 00:00:00.000 |    10006 | P10015       |         147 |     17934 | EMP-6      | Supervisor-1 |
| 2019-02-20 00:00:00.000 |    10017 | P10023       |          58 |      1334 | EMP-17     | Supervisor-4 |
| 2019-02-27 00:00:00.000 |    10015 | P10026       |         223 |     24530 | EMP-15     | Supervisor-3 |
| 2019-04-11 00:00:00.000 |    10012 | P10009       |          91 |      6643 | EMP-12     | Supervisor-3 |
| 2019-01-01 00:00:00.000 |    10007 | P10014       |         266 |     39900 | EMP-7      | Supervisor-2 |
| 2019-02-07 00:00:00.000 |    10001 | P10017       |         168 |     19488 | EMP-1      | Supervisor-1 |
| 2019-03-25 00:00:00.000 |    10009 | P10018       |         139 |      4031 | EMP-9      | Supervisor-2 |
| 2019-03-24 00:00:00.000 |    10018 | P10024       |         207 |     14076 | EMP-18     | Supervisor-4 |
| 2019-02-27 00:00:00.000 |    10007 | P10017       |          66 |      7656 | EMP-7      | Supervisor-2 |
| 2019-01-09 00:00:00.000 |    10004 | P10024       |         241 |     16388 | EMP-4      | Supervisor-1 |
| 2019-01-05 00:00:00.000 |    10007 | P10004       |         285 |     23940 | EMP-7      | Supervisor-2 |
| 2019-02-13 00:00:00.000 |    10007 | P10004       |         238 |     19992 | EMP-7      | Supervisor-2 |
| 2019-03-25 00:00:00.000 |    10001 | P10006       |         125 |     14125 | EMP-1      | Supervisor-1 |
| 2019-04-06 00:00:00.000 |    10020 | P10018       |          57 |      1653 | EMP-20     | Supervisor-4 |
| 2019-01-23 00:00:00.000 |    10018 | P10013       |         162 |     15714 | EMP-18     | Supervisor-4 |
| 2019-02-20 00:00:00.000 |    10013 | P10016       |          68 |      6256 | EMP-13     | Supervisor-3 |
| 2019-04-01 00:00:00.000 |    10005 | P10006       |         297 |     33561 | EMP-5      | Supervisor-1 |
| 2019-02-06 00:00:00.000 |    10001 | P10015       |         280 |     34160 | EMP-1      | Supervisor-1 |
| 2019-01-23 00:00:00.000 |    10005 | P10015       |          68 |      8296 | EMP-5      | Supervisor-1 |
| 2019-02-01 00:00:00.000 |    10009 | P10011       |         106 |      2438 | EMP-9      | Supervisor-2 |
| 2019-01-10 00:00:00.000 |    10012 | P10020       |         177 |     12390 | EMP-12     | Supervisor-3 |
| 2019-01-02 00:00:00.000 |    10013 | P10029       |         170 |     21930 | EMP-13     | Supervisor-3 |
| 2019-01-09 00:00:00.000 |    10009 | P10022       |         197 |     17139 | EMP-9      | Supervisor-2 |
| 2019-02-23 00:00:00.000 |    10001 | P10007       |         183 |     26535 | EMP-1      | Supervisor-1 |
| 2019-04-18 00:00:00.000 |    10008 | P10008       |         171 |     11628 | EMP-8      | Supervisor-2 |
| 2019-04-03 00:00:00.000 |    10019 | P10004       |         105 |      8820 | EMP-19     | Supervisor-4 |
| 2019-01-12 00:00:00.000 |    10005 | P10014       |         152 |     22800 | EMP-5      | Supervisor-1 |
| 2019-04-19 00:00:00.000 |    10002 | P10022       |         294 |     25578 | EMP-2      | Supervisor-1 |



---

## Functional-Dependency__case_69

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|   Id_many | CommonServiceName              | Services                                 | Sub-Service                                 | Interface                                                       | API   | Ansible   | Chef   | Packer   | Terraform   |   CloudNamesId |   ID.1_many | CloudNames.CloudName   |   Id | CloudName   |   ID.1 |
|----------:|:-------------------------------|:-----------------------------------------|:--------------------------------------------|:----------------------------------------------------------------|:------|:----------|:-------|:---------|:------------|---------------:|------------:|:-----------------------|-----:|:------------|-------:|
|       539 | Load Balancer                  | Server Load Balancer                     | Backend Server API                          | AddBackendServers                                               | Yes   | Yes       | No     | No       | No          |              3 |         539 | Alibaba                |    3 | Alibaba     |      3 |
|      2607 | Amazon Route 53                | Amazon Route 53                          | Amazon Route 53                             | GetDomainDetail                                                 | Yes   | Yes       | No     | No       | No          |              2 |        2607 | AWS                    |    2 | AWS         |      2 |
|       751 | Log Service                    | Log Service                              | LogStore related interfaces                 | ListShard                                                       | Yes   | No        | No     | No       | No          |              3 |         751 | Alibaba                |    3 | Alibaba     |      3 |
|      1126 | Storage Service                | Baidu Object Storage                     | Bucket API                                  | GetBucketStaticWebsite                                          | Yes   | No        | No     | No       | No          |              1 |        1126 | Baidu                  |    1 | Baidu       |      1 |
|      3231 | Simple Notification Service    | Amazon Simple Notification Service (SNS) | Amazon Simple Notification Service (SNS)    | Unsubscribe                                                     | Yes   | Yes       | No     | No       | Yes         |              2 |        3231 | AWS                    |    2 | AWS         |      2 |
|      4979 | Cloud eye                      | Cloud eye                                | Alarm Rule Management                       | Deleting an Alarm Rule                                          | Yes   | No        | No     | No       | No          |              7 |        4979 | Huawei                 |    7 | Huawei      |      7 |
|      3359 | IOT hub                        | AWS IoT                                  | AWS IoT                                     | ListPrincipalThings                                             | Yes   | No        | No     | No       | No          |              2 |        3359 | AWS                    |    2 | AWS         |      2 |
|      2086 | IAM                            | IAM                                      |                                             | CreateServiceSpecificCredential                                 | Yes   | No        | No     | No       | No          |              2 |        2086 | AWS                    |    2 | AWS         |      2 |
|      2621 | Amazon Route 53                | Amazon Route 53                          | Amazon Route 53                             | UpdateTagsForDomain                                             | Yes   | No        | No     | No       | No          |              2 |        2621 | AWS                    |    2 | AWS         |      2 |
|       730 | MapReduce                      | E-MapReduce                              | Job                                         | Modify a Job                                                    | Yes   | No        | No     | No       | No          |              3 |         730 | Alibaba                |    3 | Alibaba     |      3 |
|      1010 | Domain Name Service            | Alibaba Cloud DNS                        | Resolution Server Load Balancer Interface   | Enable/Disable Resolution SLB                                   | Yes   | No        | No     | No       | No          |              3 |        1010 | Alibaba                |    3 | Alibaba     |      3 |
|      5752 | Database MongoDB               | Cloud database MongoDB                   |                                             | createInstance                                                  | Yes   | No        | No     | No       | No          |              5 |        5752 | JD Cloud               |    5 | JD Cloud    |      5 |
|       232 | Container Service              | Cloud Container Engine                   | Cluster                                     | Cluster details                                                 | Yes   | No        | No     | No       | No          |              1 |         232 | Baidu                  |    1 | Baidu       |      1 |
|      2490 | Amazon Redshift                | Amazon Redshift                          | Amazon Redshift                             | DeleteSnapshotCopyGrant                                         | Yes   | No        | No     | No       | No          |              2 |        2490 | AWS                    |    2 | AWS         |      2 |
|      6031 | EIP                            | Network UNet                             |                                             | Application Firewall - GrantSecurityGroup (coming soon)         | Yes   | No        | No     | No       | No          |              6 |        6031 | U Cloud                |    6 | U Cloud     |      6 |
|      6152 | Content Delivery Network       | Cloud Distribution UCDN                  |                                             | Get Domain Prefetch Enable Status - GetUcdnDomainPrefetchEnable | Yes   | No        | No     | No       | No          |              6 |        6152 | U Cloud                |    6 | U Cloud     |      6 |
|      2146 | KMS                            | KMS                                      | KMS                                         | DescribeKey                                                     | Yes   | No        | No     | No       | No          |              2 |        2146 | AWS                    |    2 | AWS         |      2 |
|      3399 | Amazon Rekognition             | Amazon Rekognition                       |                                             |                                                                 | No    | No        | No     | No       | No          |              2 |        3399 | AWS                    |    2 | AWS         |      2 |
|      1534 | Timing Database                | Timing Database TSDB                     | Aggregate function                          | Sum                                                             | Yes   | No        | No     | No       | No          |              1 |        1534 | Baidu                  |    1 | Baidu       |      1 |
|      6182 | Distributed database           | Distributed database UDDB                |                                             | Delete Configuration -DeleteUDBParamGroup                       | Yes   | No        | No     | No       | No          |              6 |        6182 | U Cloud                |    6 | U Cloud     |      6 |
|      4573 | Volume backup service          | Volume backup service                    | Backup policy                               | Executing a Backup Policy At Once                               | Yes   | No        | No     | No       | No          |              7 |        4573 | Huawei                 |    7 | Huawei      |      7 |
|       834 | API Gateway                    | API Gateway                              | IP Access control                           | Query IP access control bound to AIP's                          | Yes   | No        | No     | No       | No          |              3 |         834 | Alibaba                |    3 | Alibaba     |      3 |
|      3528 | Physical server                | Blackstone physical server               | Load Balancing Related API                  | Modifying the Load Balanced Layer 7 Forwarding Path             | Yes   | No        | No     | No       | No          |              4 |        3528 | Tencent                |    4 | Tencent     |      4 |
|       180 | Relational Database RDS        | ApsaraDB for  RDS                        | Security Management                         | Modify the IP address whitelist of an RDS instance              | Yes   | No        | No     | No       | No          |              3 |         180 | Alibaba                |    3 | Alibaba     |      3 |
|      1480 | IOT device management          | IOT device management                    | Device list Management                      | Get device access details                                       | Yes   | No        | No     | No       | No          |              1 |        1480 | Baidu                  |    1 | Baidu       |      1 |
|      5306 | Relational Database Service    | Relational Database Service              | DB Instance Management                      | Obtaining Detailed Information of a Specified DB Instance       | Yes   | No        | No     | No       | Yes         |              7 |        5306 | Huawei                 |    7 | Huawei      |      7 |
|      6690 | Message Queue Ckafka           | Message Queue Ckafka                     | Ckafka API                                  | AddPartition                                                    | Yes   | No        | No     | No       | No          |              4 |        6690 | Tencent                |    4 | Tencent     |      4 |
|      3065 | AWS Directory Service          | AWS Directory Service                    | AWS Directory Service                       | GetDirectoryLimits                                              | Yes   | No        | No     | No       | No          |              2 |        3065 | AWS                    |    2 | AWS         |      2 |
|      2246 | Relational Database RDS        | RDS                                      | RDS                                         | DescribeDBSnapshots                                             | Yes   | Yes       | No     | No       | Yes         |              2 |        2246 | AWS                    |    2 | AWS         |      2 |
|      5529 | Text to Speech                 | Text to Speech                           | Service Management APIs                     | Enabling TTS                                                    | Yes   | No        | No     | No       | No          |              7 |        5529 | Huawei                 |    7 | Huawei      |      7 |
|      4660 | Scalable file service          | Scalable file service                    | File Sharing                                | Querying Export Locations of a Shared File System               | Yes   | No        | No     | No       | No          |              7 |        4660 | Huawei                 |    7 | Huawei      |      7 |
|      4276 | ECS                            | Elastic Cloud Server (ECS)               | Security Group Management Related Interface | Creating a Security Group                                       | Yes   | No        | No     | No       | No          |              7 |        4276 | Huawei                 |    7 | Huawei      |      7 |
|      4421 | Auto Scaling                   | Auto Scaling                             | AS Groups                                   | Modifying an AS Group                                           | Yes   | No        | No     | No       | No          |              7 |        4421 | Huawei                 |    7 | Huawei      |      7 |
|      6871 | Internet of Things suite       | Internet of Things suite                 | Rule engine management  related API         | Add rules                                                       | Yes   | No        | No     | No       | No          |              4 |        6871 | Tencent                |    4 | Tencent     |      4 |
|      1567 | face recognition               | Baidu face recognition                   | Face Bank management                        | Face registration                                               | No    | No        | No     | No       | No          |              1 |        1567 | Baidu                  |    1 | Baidu       |      1 |
|       306 | DB for MongoDB                 | ApsaraDB for MongoDB                     | Instance Management                         | Modify RDB instance maintain time                               | Yes   | No        | No     | No       | No          |              3 |         306 | Alibaba                |    3 | Alibaba     |      3 |
|      5045 | Identify and Access Management | Identify and Access Management           | OS-FEDERATION                               | Project                                                         | Yes   | No        | No     | No       | No          |              7 |        5045 | Huawei                 |    7 | Huawei      |      7 |
|      5966 | Physical cloud host            | Physical cloud host UPHost               |                                             | Start the physical machine - StartPHost                         | Yes   | No        | No     | No       | No          |              6 |        5966 | U Cloud                |    6 | U Cloud     |      6 |
|       351 | Storage Service                | Object Storage Service                   | Bucket Operations                           | Get Bucket Referer                                              | Yes   | No        | No     | No       | Yes         |              3 |         351 | Alibaba                |    3 | Alibaba     |      3 |
|      3328 | IOT hub                        | AWS IoT                                  | AWS IoT                                     | DeleteCACertificate                                             | Yes   | No        | No     | No       | No          |              2 |        3328 | AWS                    |    2 | AWS         |      2 |
|      6091 | VPN gateway IPSec VPN          | VPN gateway IPSec VPN                    |                                             |                                                                 | No    | No        | No     | No       | No          |              6 |        6091 | U Cloud                |    6 | U Cloud     |      6 |
|      5787 | Content Delivery Network       | CDN                                      |                                             | Query accelerated domain name                                   | No    | No        | No     | No       | No          |              5 |        5787 | JD Cloud               |    5 | JD Cloud    |      5 |
|      6937 | Channel partner                | Channel partner                          |                                             | Modify customer notes                                           | Yes   | No        | No     | No       | No          |              4 |        6937 | Tencent                |    4 | Tencent     |      4 |
|      6067 | Load Balancer                  | Load Balancing ULB                       |                                             | Create Load Balancing - CreateULB                               | Yes   | No        | No     | No       | No          |              6 |        6067 | U Cloud                |    6 | U Cloud     |      6 |
|      6651 | Storage Service                | Object Storage                           | Bucket related API                          | Get Bucket Lifecycle                                            | Yes   | No        | No     | No       | No          |              4 |        6651 | Tencent                |    4 | Tencent     |      4 |
|      5333 | Document Database Service      | Document Database Service                | DB Instance Monitoring                      | Monitoring DB Instances Using CES                               | No    | No        | No     | No       | No          |              7 |        5333 | Huawei                 |    7 | Huawei      |      7 |
|      1710 | Auto Scaling                   | Auto Scaling                             | Auto Scaling                                | Create Scaling Rules                                            | Yes   | Yes       | No     | No       | No          |              2 |        1710 | AWS                    |    2 | AWS         |      2 |
|      3109 | Amazon Cloud Directory         | Amazon Cloud Directory                   | Amazon Cloud Directory                      | ListAttachedIndices                                             | Yes   | No        | No     | No       | No          |              2 |        3109 | AWS                    |    2 | AWS         |      2 |
|      6174 | Distributed database           | Distributed database UDDB                |                                             | Get Backup Blacklist - DescribeUDBBackupBlacklist               | Yes   | No        | No     | No       | No          |              6 |        6174 | U Cloud                |    6 | U Cloud     |      6 |
|      1005 | Domain Name Service            | Alibaba Cloud DNS                        | Resolution Management Interface             | Retrieving Resolution Record Lists                              | Yes   | No        | No     | No       | No          |              3 |        1005 | Alibaba                |    3 | Alibaba     |      3 |



---

## Functional-Dependency__case_211

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| location                         |   population_many | date                    |   HighestInfectionCount_many |   PercentagePopulationInfected_many |   population |   HighestInfectionCount |   PercentagePopulationInfected |
|:---------------------------------|------------------:|:------------------------|-----------------------------:|------------------------------------:|-------------:|------------------------:|-------------------------------:|
| Germany                          |          83783945 | 2020-08-22 00:00:00.000 |                       233861 |                         0.279124    |     83783945 |                 3736959 |                     4.46023    |
| Oceania                          |          42677809 | 2021-06-09 00:00:00.000 |                        50417 |                         0.118134    |     42677809 |                   55408 |                     0.129829   |
| Italy                            |          60461828 | 2021-06-08 00:00:00.000 |                      4235592 |                         7.0054      |     60461828 |                 4260788 |                     7.04707    |
| Tajikistan                       |           9537642 | 2021-04-23 00:00:00.000 |                        13308 |                         0.139531    |      9537642 |                   13523 |                     0.141786   |
| Sao Tome and Principe            |            219161 | 2020-05-19 00:00:00.000 |                          251 |                         0.114528    |       219161 |                    2369 |                     1.08094    |
| Romania                          |          19237682 | 2021-05-20 00:00:00.000 |                      1074297 |                         5.58434     |     19237682 |                 1080823 |                     5.61826    |
| Monaco                           |             39244 | 2021-04-24 00:00:00.000 |                         2429 |                         6.18948     |        39244 |                    2580 |                     6.57425    |
| Cameroon                         |          26545864 | 2021-06-13 00:00:00.000 |                        80090 |                         0.301704    |     26545864 |                   80858 |                     0.304597   |
| Liechtenstein                    |             38137 | 2020-10-23 00:00:00.000 |                          324 |                         0.849569    |        38137 |                    3039 |                     7.96864    |
| Sudan                            |          43849269 | 2021-06-17 00:00:00.000 |                        36347 |                         0.0828908   |     43849269 |                   36658 |                     0.0836     |
| Malta                            |            441539 | 2020-09-06 00:00:00.000 |                         2039 |                         0.461794    |       441539 |                   30627 |                     6.93642    |
| Namibia                          |           2540916 | 2021-06-27 00:00:00.000 |                        84705 |                         3.33364     |      2540916 |                   91208 |                     3.58957    |
| Burkina Faso                     |          20903278 | 2020-03-23 00:00:00.000 |                           99 |                         0.00047361  |     20903278 |                   13485 |                     0.0645114  |
| Vietnam                          |          97338583 | 2020-12-15 00:00:00.000 |                         1405 |                         0.00144342  |     97338583 |                   17727 |                     0.0182117  |
| Eswatini                         |           1160164 | 2021-04-25 00:00:00.000 |                        18442 |                         1.5896      |      1160164 |                   19084 |                     1.64494    |
| Malaysia                         |          32365998 | 2021-03-06 00:00:00.000 |                       311777 |                         0.963286    |     32365998 |                  758967 |                     2.34495    |
| Senegal                          |          16743930 | 2020-07-25 00:00:00.000 |                         9552 |                         0.0570475   |     16743930 |                   43268 |                     0.25841    |
| Azerbaijan                       |          10139175 | 2021-03-17 00:00:00.000 |                       242491 |                         2.39162     |     10139175 |                  336122 |                     3.31508    |
| Lithuania                        |           2722291 | 2021-05-22 00:00:00.000 |                       270376 |                         9.93193     |      2722291 |                  278809 |                    10.2417     |
| Brazil                           |         212559409 | 2021-02-19 00:00:00.000 |                     10084208 |                         4.74418     |    212559409 |                18622304 |                     8.76099    |
| Ecuador                          |          17643060 | 2021-06-19 00:00:00.000 |                       445586 |                         2.52556     |     17643060 |                  459538 |                     2.60464    |
| El Salvador                      |           6486201 | 2021-04-04 00:00:00.000 |                        65337 |                         1.00732     |      6486201 |                   78766 |                     1.21436    |
| China                            |        1439323774 | 2020-08-18 00:00:00.000 |                        84934 |                         0.00590097  |   1439323774 |                   91864 |                     0.00638244 |
| Comoros                          |            869595 | 2020-07-16 00:00:00.000 |                          328 |                         0.0377187   |       869595 |                    3943 |                     0.453429   |
| Monaco                           |             39244 | 2021-06-28 00:00:00.000 |                         2575 |                         6.56151     |        39244 |                    2580 |                     6.57425    |
| Bolivia                          |          11673029 | 2020-06-09 00:00:00.000 |                        14644 |                         0.125452    |     11673029 |                  441286 |                     3.78039    |
| Hungary                          |           9660350 | 2020-09-22 00:00:00.000 |                        19499 |                         0.201846    |      9660350 |                  808160 |                     8.36574    |
| Madagascar                       |          27691019 | 2021-01-01 00:00:00.000 |                        17714 |                         0.0639702   |     27691019 |                   42247 |                     0.152566   |
| Djibouti                         |            988002 | 2021-05-20 00:00:00.000 |                        11485 |                         1.16245     |       988002 |                   11602 |                     1.17429    |
| Cameroon                         |          26545864 | 2020-06-14 00:00:00.000 |                         8681 |                         0.0327019   |     26545864 |                   80858 |                     0.304597   |
| Chile                            |          19116209 | 2020-03-25 00:00:00.000 |                         1197 |                         0.0062617   |     19116209 |                 1558557 |                     8.15307    |
| Saint Vincent and the Grenadines |            110947 | 2020-08-10 00:00:00.000 |                           57 |                         0.0513759   |       110947 |                    2227 |                     2.00726    |
| Mongolia                         |           3278292 | 2020-12-05 00:00:00.000 |                          849 |                         0.0258976   |      3278292 |                  120339 |                     3.67078    |
| Ukraine                          |          43733759 | 2021-04-12 00:00:00.000 |                      1913415 |                         4.37514     |     43733759 |                 2301221 |                     5.26189    |
| Montenegro                       |            628062 | 2020-07-14 00:00:00.000 |                         1287 |                         0.204916    |       628062 |                  100272 |                    15.9653     |
| Oceania                          |          42677809 | 2020-02-18 00:00:00.000 |                           15 |                         3.51471e-05 |     42677809 |                   55408 |                     0.129829   |
| Cambodia                         |          16718971 | 2020-07-30 00:00:00.000 |                          234 |                         0.00139961  |     16718971 |                   51384 |                     0.307339   |
| Australia                        |          25499881 | 2021-03-19 00:00:00.000 |                        29192 |                         0.114479    |     25499881 |                   30684 |                     0.12033    |
| Saudi Arabia                     |          34813867 | 2020-10-08 00:00:00.000 |                       338132 |                         0.971257    |     34813867 |                  486106 |                     1.3963     |
| Jordan                           |          10203140 | 2020-12-31 00:00:00.000 |                       294494 |                         2.88631     |     10203140 |                  751937 |                     7.36966    |
| Maldives                         |            540542 | 2020-06-09 00:00:00.000 |                         1942 |                         0.359269    |       540542 |                   73931 |                    13.6772     |
| Armenia                          |           2963234 | 2020-07-11 00:00:00.000 |                        31392 |                         1.05938     |      2963234 |                  225221 |                     7.60051    |
| Gabon                            |           2225728 | 2020-09-10 00:00:00.000 |                         8621 |                         0.387334    |      2225728 |                   25054 |                     1.12565    |
| Fiji                             |            896444 | 2021-04-25 00:00:00.000 |                           91 |                         0.0101512   |       896444 |                    4849 |                     0.540915   |
| Timor                            |           1318442 | 2021-05-31 00:00:00.000 |                         6994 |                         0.530475    |      1318442 |                    9278 |                     0.703709   |
| Turkey                           |          84339067 | 2020-08-29 00:00:00.000 |                       267064 |                         0.316655    |     84339067 |                 5430940 |                     6.43941    |
| Monaco                           |             39244 | 2021-01-22 00:00:00.000 |                         1311 |                         3.34064     |        39244 |                    2580 |                     6.57425    |
| Australia                        |          25499881 | 2020-11-24 00:00:00.000 |                        27853 |                         0.109228    |     25499881 |                   30684 |                     0.12033    |
| Mali                             |          20250834 | 2020-10-05 00:00:00.000 |                         3189 |                         0.0157475   |     20250834 |                   14428 |                     0.0712464  |
| Saint Lucia                      |            183629 | 2020-08-03 00:00:00.000 |                           25 |                         0.0136144   |       183629 |                    5302 |                     2.88734    |



---

## Functional-Dependency__case_218

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|   CustomerID | FirstName   | LastName       | Gender   | DateRegistered          |   CityID | City             | County                    | Region                    | Country          |
|-------------:|:------------|:---------------|:---------|:------------------------|---------:|:-----------------|:--------------------------|:--------------------------|:-----------------|
|        32074 | Claire      | Burnett        | F        | 2008-11-17 00:00:00.000 |      750 | Southampton      | Hampshire                 | South East England        | England          |
|        32102 | DEMELZA     | jones          | F        | 2005-03-04 00:00:00.000 |      852 | Watford          | Hertfordshire             | East of England           | England          |
|        21119 | Dana        | BANAT-RINZ     | F        | 2007-03-10 00:00:00.000 |      849 | Warwick          | Warwickshire              | West Midlands             | England          |
|          764 | Sarah       | Gilbert        | F        | 2007-10-03 00:00:00.000 |      112 | Bristol          | Gloucestershire           | South West England        | England          |
|        19942 | Elizabeth   | ENTWISTLE      | F        | 2006-08-05 00:00:00.000 |      802 | Tenterden        | Kent                      | South East England        | England          |
|        17649 | Sara        | Holliday       | F        | 2008-06-27 00:00:00.000 |     1401 | Newport          | Mayo                      | Connacht                  | Ireland          |
|        27457 | Fiona       | Davison        | F        | 2007-02-22 00:00:00.000 |     1025 | Caterham         | Surrey                    | South East England        | England          |
|        12798 | helen       | Ross           | F        | 2006-05-03 00:00:00.000 |     1332 | London           | London                    | London                    | England          |
|        19835 | Alastair    | Wyper          | M        | 2007-11-17 00:00:00.000 |     1125 | Edinburgh        | Midlothian/Edinburghshire | Scotland                  | Scotland         |
|         7689 | Pat         | Carberry       | F        | 2007-01-11 00:00:00.000 |      774 | Stockton-on-Tees | Durham                    | North East England        | England          |
|        26816 | Katharine   | edwards        | F        | 2007-11-20 00:00:00.000 |      826 | Truro            | Cornwall                  | South West England        | England          |
|        16546 | sherie      | ward           | F        | 2006-03-15 00:00:00.000 |       83 | Birmingham       | Warwickshire              | West Midlands             | England          |
|         6120 | Jeanette    | Read           | F        | 2005-05-16 00:00:00.000 |     1200 | Haverhill        | Suffolk                   | East of England           | England          |
|        22979 | ANGELA      | French         | F        | 2006-04-25 00:00:00.000 |      750 | Southampton      | Hampshire                 | South East England        | England          |
|         1055 | Lisa        | Forrest        | F        | 2007-06-19 00:00:00.000 |      497 | Leeds            | Yorkshire                 | Yorkshire and the Humber  | England          |
|        16875 | tabassum    | hussein        | F        | 2006-11-18 00:00:00.000 |      499 | Leicester        | Leicestershire            | East Midlands             | England          |
|        33713 | Melissa     | Freshwater     | F        | 2007-02-13 00:00:00.000 |      761 | St. Ives         | Huntingdonshire           | East of England           | England          |
|        15751 | Lisa        | Corke          | F        | 2005-10-09 00:00:00.000 |       16 | Andover          | Hampshire                 | South East England        | England          |
|        34224 | Jayne       | Gilpin         | F        | 2006-05-02 00:00:00.000 |      317 | Armagh           | Armagh                    | Ulster (Northern Ireland) | Northern Ireland |
|        22843 | Deborah     | dyson          | F        | 2007-10-03 00:00:00.000 |      673 | Portstewart      | Londonderry               | Ulster (Northern Ireland) | Northern Ireland |
|        31547 | Karen       | Duran          | F        | 2006-06-02 00:00:00.000 |      688 | Reading          | Berkshire                 | South East England        | England          |
|        15038 | Ashley      | Cochrane       | F        | 2006-12-01 00:00:00.000 |     1294 | Lasswade         | Midlothian/Edinburghshire | Scotland                  | Scotland         |
|        36052 | N           | Holt           | F        | 2008-04-26 00:00:00.000 |      336 | Bampton          | Oxfordshire               | South East England        | England          |
|        19605 | Kristen     | O'Connor       | F        | 2006-01-19 00:00:00.000 |      750 | Southampton      | Hampshire                 | South East England        | England          |
|        29627 | rupinder    | dhillon        | F        | 2006-11-07 00:00:00.000 |      139 | Camberley        | Surrey                    | South East England        | England          |
|        38817 | J L         | Trist          | F        | 2006-06-06 00:00:00.000 |      688 | Reading          | Berkshire                 | South East England        | England          |
|        14670 | c           | Lean           | F        | 2007-06-28 00:00:00.000 |     1549 | Southall         | Middlesex                 | London                    | England          |
|        16618 | donna       | Waddington     | F        | 2009-09-10 00:00:00.000 |      248 | Dunblane         | Perthshire                | Scotland                  | Scotland         |
|         3698 | Julie       | Wood           | F        | 2007-09-28 00:00:00.000 |     1157 | Gainsborough     | Lincolnshire              | East Midlands             | England          |
|        15409 | Alison      | Chambers       | F        | 2007-01-21 00:00:00.000 |     1002 | Bury St. Edmunds | Suffolk                   | East of England           | England          |
|        37740 | Catherine   | Murphy         | F        | 2005-08-28 00:00:00.000 |      293 | Abingdon         | Berkshire                 | South East England        | England          |
|        34067 | Julia       | Hume           | F        | 2006-12-07 00:00:00.000 |     1165 | Glenrothes       | Fife                      | Scotland                  | Scotland         |
|        29578 | kate        | Larvin         | F        | 2007-07-23 00:00:00.000 |     1263 | Kenilworth       | Warwickshire              | West Midlands             | England          |
|         6400 | ashleigh    | Meier          | F        | 2007-11-28 00:00:00.000 |      160 | Chelmsford       | Essex                     | East of England           | England          |
|        13069 | Shazia      | ali            | F        | 2009-06-19 00:00:00.000 |       99 | Bradford         | Yorkshire                 | Yorkshire and the Humber  | England          |
|        44163 | Salima      | Younis         | F        | 2006-02-05 00:00:00.000 |     1416 | Northolt         | Middlesex                 | London                    | England          |
|        40750 | SIOBAN      | GILMARTIN      | F        | 2006-04-02 00:00:00.000 |      928 | Bedford          | Bedfordshire              | East of England           | England          |
|         9982 | carol       | White          | F        | 2006-10-14 00:00:00.000 |      421 | Hindhead         | Surrey                    | South East England        | England          |
|         9908 | clare       | Parry          | F        | 2005-11-25 00:00:00.000 |     1703 | Wrexham          | Denbighshire/Sir Ddinbych | Wales                     | Wales            |
|        31884 | kellie      | hodges         | F        | 2007-01-10 00:00:00.000 |     1030 | Chatham          | Kent                      | South East England        | England          |
|        17475 | M           | Vence-Gunstane | F        | 2005-11-06 00:00:00.000 |     1554 | Southsea         | Hampshire                 | South East England        | England          |
|         1163 | Lorraine    | Miller         | F        | 2007-12-19 00:00:00.000 |     1108 | Dundee           | Angus/Forfarshire         | Scotland                  | Scotland         |
|        14844 | Linda       | DUFFY          | F        | 2007-03-02 00:00:00.000 |      334 | Ballymena        | Antrim                    | Ulster (Northern Ireland) | Northern Ireland |
|        23644 | Victoria    | Watson         | F        | 2007-05-25 00:00:00.000 |      761 | St. Ives         | Huntingdonshire           | East of England           | England          |
|         1308 | Jane        | Sargeson       | F        | 2006-01-27 00:00:00.000 |      196 | Cottingham       | Yorkshire                 | Yorkshire and the Humber  | England          |
|        30368 | Sarah       | Baker          | F        | 2006-11-25 00:00:00.000 |      707 | Ryde             | Isle of Wight             | South East England        | England          |
|        20485 | Tracy       | Hughes         | F        | 2006-12-14 00:00:00.000 |      879 | Wigan            | Lancashire                | North West England        | England          |
|        36541 | Diane       | Hopkins        | F        | 2007-12-20 00:00:00.000 |       98 | Bracknell        | Berkshire                 | South East England        | England          |
|         6471 | emma        | Bumford        | F        | 2009-05-09 00:00:00.000 |     1444 | Pentre           | Glamorgan/Morgannwg       | Wales                     | Wales            |
|         4077 | Alex        | Morris         | F        | 2006-10-09 00:00:00.000 |     1164 | Glasgow          | Lanarkshire               | Scotland                  | Scotland         |



---

## Functional-Dependency__case_372

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|   SalesOrderID |   SalesOrderDetailID |   OrderQty |   ProductID |   UnitPriceDiscount | Color_many   | Name                           | ProductNumber   | Color   |
|---------------:|---------------------:|-----------:|------------:|--------------------:|:-------------|:-------------------------------|:----------------|:--------|
|          53390 |                46594 |          1 |         979 |                   0 | Blue         | Touring-3000 Blue, 50          | BK-T18U-50      | Blue    |
|          63523 |                84373 |          1 |         867 |                   0 | Black        | Women's Mountain Shorts, S     | SH-W890-S       | Black   |
|          70027 |               106195 |          1 |         714 |                   0 | Multi        | Long-Sleeve Logo Jersey, M     | LJ-0192-M       | Multi   |
|          64968 |                87966 |          1 |         922 |                   0 | None         | Road Tire Tube                 | TT-R982         | None    |
|          49860 |                29973 |          2 |         823 |                   0 | Black        | LL Mountain Rear Wheel         | RW-M423         | Black   |
|          73371 |               117138 |          1 |         923 |                   0 | None         | Touring Tire Tube              | TT-T092         | None    |
|          66729 |                94005 |          1 |         929 |                   0 | None         | ML Mountain Tire               | TI-M602         | None    |
|          55294 |                55594 |          4 |         999 |                   0 | Black        | Road-750 Black, 52             | BK-R19B-52      | Black   |
|          59986 |                72780 |          1 |         870 |                   0 | None         | Water Bottle - 30 oz.          | WB-H098         | None    |
|          51832 |                42074 |         14 |         867 |                   0 | Black        | Women's Mountain Shorts, S     | SH-W890-S       | Black   |
|          43864 |                  680 |          1 |         748 |                   0 | Silver       | HL Mountain Frame - Silver, 38 | FR-M94S-38      | Silver  |
|          72506 |               114956 |          1 |         976 |                   0 | Yellow       | Road-350-W Yellow, 48          | BK-R79Y-48      | Yellow  |
|          72616 |               115246 |          1 |         871 |                   0 | None         | Mountain Bottle Cage           | BC-M005         | None    |
|          51690 |                39160 |          3 |         867 |                   0 | Black        | Women's Mountain Shorts, S     | SH-W890-S       | Black   |
|          74135 |               119075 |          1 |         708 |                   0 | Black        | Sport-100 Helmet, Black        | HL-U509         | Black   |
|          55270 |                55257 |          7 |         712 |                   0 | Multi        | AWC Logo Cap                   | CA-1098         | Multi   |
|          60487 |                74021 |          1 |         922 |                   0 | None         | Road Tire Tube                 | TT-R982         | None    |
|          65095 |                88281 |          1 |         974 |                   0 | Yellow       | Road-350-W Yellow, 42          | BK-R79Y-42      | Yellow  |
|          46344 |                 9896 |          1 |         754 |                   0 | Red          | Road-450 Red, 58               | BK-R68R-58      | Red     |
|          49068 |                26035 |          7 |         760 |                   0 | Red          | Road-650 Red, 60               | BK-R50R-60      | Red     |
|          69466 |               103596 |          2 |         998 |                   0 | Black        | Road-750 Black, 48             | BK-R19B-48      | Black   |
|          72656 |               115362 |          1 |         870 |                   0 | None         | Water Bottle - 30 oz.          | WB-H098         | None    |
|          44319 |                 2675 |          1 |         748 |                   0 | Silver       | HL Mountain Frame - Silver, 38 | FR-M94S-38      | Silver  |
|          53472 |                47366 |         11 |         858 |                   0 | Black        | Half-Finger Gloves, S          | GL-H102-S       | Black   |
|          71803 |               111261 |          2 |         868 |                   0 | Black        | Women's Mountain Shorts, M     | SH-W890-M       | Black   |
|          68624 |               100290 |          1 |         708 |                   0 | Black        | Sport-100 Helmet, Black        | HL-U509         | Black   |
|          54087 |                51609 |          1 |         870 |                   0 | None         | Water Bottle - 30 oz.          | WB-H098         | None    |
|          66921 |                94490 |          1 |         873 |                   0 | None         | Patch Kit/8 Patches            | PK-7098         | None    |
|          45813 |                 8068 |          8 |         765 |                   0 | Black        | Road-650 Black, 58             | BK-R50B-58      | Black   |
|          63763 |                84969 |          1 |         711 |                   0 | Blue         | Sport-100 Helmet, Blue         | HL-U509-B       | Blue    |
|          57154 |                62850 |          6 |         870 |                   0 | None         | Water Bottle - 30 oz.          | WB-H098         | None    |
|          71764 |               110541 |          1 |         872 |                   0 | None         | Road Bottle Cage               | BC-R205         | None    |
|          65154 |                88430 |         10 |         869 |                   0 | Black        | Women's Mountain Shorts, L     | SH-W890-L       | Black   |
|          53788 |                50888 |          1 |         860 |                   0 | Black        | Half-Finger Gloves, L          | GL-H102-L       | Black   |
|          58997 |                69388 |          7 |         715 |                   0 | Multi        | Long-Sleeve Logo Jersey, L     | LJ-0192-L       | Multi   |
|          51090 |                35782 |          3 |         907 |                   0 | Silver       | Rear Brakes                    | RB-9231         | Silver  |
|          67079 |                94865 |          1 |         797 |                   0 | Yellow       | Road-550-W Yellow, 38          | BK-R64Y-38      | Yellow  |
|          47721 |                19500 |          4 |         768 |                   0 | Black        | Road-650 Black, 44             | BK-R50B-44      | Black   |
|          60614 |                74335 |          1 |         880 |                   0 | Silver       | Hydration Pack - 70 oz.        | HY-1023-70      | Silver  |
|          48380 |                23841 |          2 |         825 |                   0 | Black        | HL Mountain Rear Wheel         | RW-M928         | Black   |
|          50297 |                32710 |          5 |         764 |                   0 | Red          | Road-650 Red, 52               | BK-R50R-52      | Red     |
|          48363 |                23605 |          2 |         761 |                   0 | Red          | Road-650 Red, 62               | BK-R50R-62      | Red     |
|          51776 |                41067 |          2 |         708 |                   0 | Black        | Sport-100 Helmet, Black        | HL-U509         | Black   |
|          53091 |                45856 |          1 |         922 |                   0 | None         | Road Tire Tube                 | TT-R982         | None    |
|          62318 |                79702 |          1 |         928 |                   0 | None         | LL Mountain Tire               | TI-M267         | None    |
|          49837 |                29580 |          1 |         767 |                   0 | Black        | Road-650 Black, 62             | BK-R50B-62      | Black   |
|          63180 |                82455 |          2 |         801 |                   0 | Yellow       | Road-550-W Yellow, 48          | BK-R64Y-48      | Yellow  |
|          53170 |                46048 |          1 |         784 |                   0 | Black        | Mountain-200 Black, 46         | BK-M68B-46      | Black   |
|          69557 |               104879 |          4 |         869 |                   0 | Black        | Women's Mountain Shorts, L     | SH-W890-L       | Black   |
|          73724 |               118047 |          1 |         712 |                   0 | Multi        | AWC Logo Cap                   | CA-1098         | Multi   |



---

## Functional-Dependency__case_207

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|   FinanceKey |   DateKey |   OrganizationKey |   DepartmentGroupKey |   ScenarioKey |   AccountKey | Date                    |   AccountCodeAlternateKey | AccountDescription                     | AccountType   | Operator   | CustomMembers   | ValueType   |
|-------------:|----------:|------------------:|---------------------:|--------------:|-------------:|:------------------------|--------------------------:|:---------------------------------------|:--------------|:-----------|:----------------|:------------|
|        10888 |  20110929 |                 6 |                    7 |             1 |           46 | 2011-09-29 00:00:00.000 |                      3550 | Current Retained Earnings              | Liabilities   | +          |                 | Currency    |
|        18545 |  20120430 |                12 |                    7 |             1 |           37 | 2012-04-30 00:00:00.000 |                      2410 | Long Term Obligations                  | Liabilities   | +          |                 | Currency    |
|        25557 |  20121128 |                12 |                    1 |             1 |           87 | 2012-11-28 00:00:00.000 |                      6920 | Rent                                   | Expenditures  | +          |                 | Currency    |
|        30204 |  20130330 |                13 |                    6 |             1 |           78 | 2013-03-30 00:00:00.000 |                      6700 | Other Expenses                         | Expenditures  | +          |                 | Currency    |
|         4214 |  20110331 |                 7 |                    6 |             1 |           52 | 2011-03-31 00:00:00.000 |                      4500 | Intercompany Sales                     | Revenue       | +          |                 | Currency    |
|        22596 |  20120928 |                 3 |                    1 |             1 |           71 | 2012-09-28 00:00:00.000 |                      6300 | Conferences                            | Expenditures  | +          |                 | Currency    |
|        13575 |  20111229 |                 3 |                    7 |             1 |           34 | 2011-12-29 00:00:00.000 |                      2340 | Intercompany Payables                  | Liabilities   | +          |                 | Currency    |
|         7446 |  20110701 |                 6 |                    6 |             1 |           53 | 2011-07-01 00:00:00.000 |                      4130 | Returns and Adjustments                | Expenditures  | -          |                 | Currency    |
|         2099 |  20110129 |                 8 |                    1 |             1 |           83 | 2011-01-29 00:00:00.000 |                      6840 | Furniture and Fixtures                 | Expenditures  | +          |                 | Currency    |
|        26236 |  20121228 |                 7 |                    6 |             1 |           73 | 2012-12-28 00:00:00.000 |                      6400 | Office Supplies                        | Expenditures  | +          |                 | Currency    |
|        14610 |  20120129 |                 3 |                    7 |             1 |           78 | 2012-01-29 00:00:00.000 |                      6700 | Other Expenses                         | Expenditures  | +          |                 | Currency    |
|        21077 |  20120731 |                 6 |                    6 |             1 |           96 | 2012-07-31 00:00:00.000 |                      9510 | Headcount                              | Balances      | ~          |                 | Units       |
|        28507 |  20130228 |                 7 |                    6 |             1 |           63 | 2013-02-28 00:00:00.000 |                      6100 | Commissions                            | Expenditures  | +          |                 | Currency    |
|         2045 |  20110129 |                 7 |                    7 |             1 |           19 | 2011-01-29 00:00:00.000 |                      1220 | Buildings & Improvements               | Assets        | +          |                 | Currency    |
|         4859 |  20110501 |                 5 |                    1 |             1 |           89 | 2011-05-01 00:00:00.000 |                      8000 | Interest Income                        | Revenue       | +          |                 | Currency    |
|        16617 |  20120330 |                 3 |                    7 |             1 |           73 | 2012-03-30 00:00:00.000 |                      6400 | Office Supplies                        | Expenditures  | +          |                 | Currency    |
|        28206 |  20130228 |                 5 |                    1 |             1 |           94 | 2013-02-28 00:00:00.000 |                      8500 | Taxes                                  | Expenditures  | -          |                 | Currency    |
|         6342 |  20110531 |                 6 |                    6 |             2 |           67 | 2011-05-31 00:00:00.000 |                      6220 | Meals                                  | Expenditures  | +          |                 | Currency    |
|        35260 |  20130829 |                 6 |                    7 |             1 |           23 | 2013-08-29 00:00:00.000 |                      1260 | Construction In Progress               | Assets        | +          |                 | Currency    |
|        38007 |  20131029 |                12 |                    1 |             1 |           85 | 2013-10-29 00:00:00.000 |                      6860 | Amortization of Goodwill               | Expenditures  | +          |                 | Currency    |
|        33221 |  20130630 |                11 |                    1 |             1 |           71 | 2013-06-30 00:00:00.000 |                      6300 | Conferences                            | Expenditures  | +          |                 | Currency    |
|        30899 |  20130430 |                 8 |                    6 |             1 |           52 | 2013-04-30 00:00:00.000 |                      4500 | Intercompany Sales                     | Revenue       | +          |                 | Currency    |
|         5056 |  20110501 |                 6 |                    3 |             1 |           60 | 2011-05-01 00:00:00.000 |                      6000 | Salaries                               | Expenditures  | +          |                 | Currency    |
|        11293 |  20111029 |                 3 |                    6 |             1 |           72 | 2011-10-29 00:00:00.000 |                      6310 | Marketing Collateral                   | Expenditures  | +          |                 | Currency    |
|        33949 |  20130731 |                 6 |                    1 |             1 |           89 | 2013-07-31 00:00:00.000 |                      8000 | Interest Income                        | Revenue       | +          |                 | Currency    |
|        11471 |  20111029 |                 4 |                    6 |             2 |           66 | 2011-10-29 00:00:00.000 |                      6210 | Travel Lodging                         | Expenditures  | +          |                 | Currency    |
|          159 |  20101229 |                 3 |                    7 |             1 |           73 | 2010-12-29 00:00:00.000 |                      6400 | Office Supplies                        | Expenditures  | +          |                 | Currency    |
|        37085 |  20131029 |                 3 |                    1 |             1 |           77 | 2013-10-29 00:00:00.000 |                      6620 | Utilities                              | Expenditures  | +          |                 | Currency    |
|        12342 |  20111029 |                 8 |                    7 |             1 |          100 | 2011-10-29 00:00:00.000 |                      2220 | Current Installments of Long-term Debt | Liabilities   | +          |                 | Currency    |
|        12988 |  20111129 |                 6 |                    4 |             2 |           82 | 2011-11-29 00:00:00.000 |                      6830 | Equipment                              | Expenditures  | +          |                 | Currency    |
|        26590 |  20121228 |                11 |                    7 |             1 |           20 | 2012-12-28 00:00:00.000 |                      1230 | Machinery & Equipment                  | Assets        | +          |                 | Currency    |
|        39338 |  20131129 |                13 |                    6 |             1 |           84 | 2013-11-29 00:00:00.000 |                      6850 | Other Assets                           | Expenditures  | +          |                 | Currency    |
|        13271 |  20111129 |                 7 |                    7 |             1 |           28 | 2011-11-29 00:00:00.000 |                      2210 | Notes Payable                          | Liabilities   | +          |                 | Currency    |
|        26447 |  20121228 |                11 |                    2 |             1 |           76 | 2012-12-28 00:00:00.000 |                      6610 | Telephone                              | Expenditures  | +          |                 | Currency    |
|        35509 |  20130829 |                11 |                    1 |             1 |           87 | 2013-08-29 00:00:00.000 |                      6920 | Rent                                   | Expenditures  | +          |                 | Currency    |
|        30341 |  20130430 |                 3 |                    7 |             1 |           61 | 2013-04-30 00:00:00.000 |                      6020 | Payroll Taxes                          | Expenditures  | +          |                 | Currency    |
|         6493 |  20110531 |                 7 |                    6 |             1 |           74 | 2011-05-31 00:00:00.000 |                      6500 | Professional Services                  | Expenditures  | +          |                 | Currency    |
|        27842 |  20130128 |                12 |                    7 |             1 |           33 | 2013-01-28 00:00:00.000 |                      2330 | Warranties                             | Liabilities   | +          |                 | Currency    |
|        34330 |  20130731 |                 8 |                    7 |             1 |           38 | 2013-07-31 00:00:00.000 |                      2420 | Pension Liability                      | Liabilities   | +          |                 | Currency    |
|        13550 |  20111229 |                 3 |                    6 |             1 |           92 | 2011-12-29 00:00:00.000 |                      8030 | Other Income                           | Revenue       | +          |                 | Currency    |
|        32631 |  20130630 |                 4 |                    1 |             1 |           78 | 2013-06-30 00:00:00.000 |                      6700 | Other Expenses                         | Expenditures  | +          |                 | Currency    |
|        11901 |  20111029 |                 6 |                    5 |             1 |           78 | 2011-10-29 00:00:00.000 |                      6700 | Other Expenses                         | Expenditures  | +          |                 | Currency    |
|        11799 |  20111029 |                 6 |                    3 |             2 |           73 | 2011-10-29 00:00:00.000 |                      6400 | Office Supplies                        | Expenditures  | +          |                 | Currency    |
|        17566 |  20120430 |                 3 |                    1 |             1 |           84 | 2012-04-30 00:00:00.000 |                      6850 | Other Assets                           | Expenditures  | +          |                 | Currency    |
|        24450 |  20121028 |                11 |                    6 |             1 |           65 | 2012-10-28 00:00:00.000 |                      6200 | Travel Transportation                  | Expenditures  | +          |                 | Currency    |
|         8044 |  20110801 |                 3 |                    7 |             1 |           94 | 2011-08-01 00:00:00.000 |                      8500 | Taxes                                  | Expenditures  | -          |                 | Currency    |
|        14583 |  20120129 |                 3 |                    7 |             1 |           24 | 2012-01-29 00:00:00.000 |                      1300 | Other Assets                           | Assets        | +          |                 | Currency    |
|        17049 |  20120330 |                 7 |                    6 |             1 |           54 | 2012-03-30 00:00:00.000 |                      4140 | Discounts                              | Expenditures  | -          |                 | Currency    |
|          157 |  20101229 |                 3 |                    7 |             2 |           71 | 2010-12-29 00:00:00.000 |                      6300 | Conferences                            | Expenditures  | +          |                 | Currency    |
|         1177 |  20110129 |                 3 |                    1 |             1 |           96 | 2011-01-29 00:00:00.000 |                      9510 | Headcount                              | Balances      | ~          |                 | Units       |



---

## Functional-Dependency__case_192

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Date                    |   product |   customer |   sales | CUSTOMER-id   | CUSTOMER-NAME   |
|:------------------------|----------:|-----------:|--------:|:--------------|:----------------|
| 2020-07-15 00:00:00.000 |         8 |          6 |     797 | 6             | CUSTOMER F      |
| 2020-01-02 00:00:00.000 |         6 |          4 |     713 | 4             | CUSTOMER D      |
| 2020-08-31 00:00:00.000 |         2 |          5 |     297 | 5             | CUSTOMER E      |
| 2021-01-04 00:00:00.000 |         8 |          4 |     898 | 4             | CUSTOMER D      |
| 2020-08-11 00:00:00.000 |         7 |          4 |     674 | 4             | CUSTOMER D      |
| 2020-02-28 00:00:00.000 |         9 |          5 |     324 | 5             | CUSTOMER E      |
| 2020-08-24 00:00:00.000 |         9 |          9 |     140 | 9             | CUSTOMER I      |
| 2020-02-03 00:00:00.000 |         2 |          8 |     272 | 8             | CUSTOMER H      |
| 2021-02-26 00:00:00.000 |         3 |          7 |     901 | 7             | CUSTOMER G      |
| 2020-09-29 00:00:00.000 |         5 |          1 |    3188 | 1             | CUSTOMER A      |
| 2020-08-03 00:00:00.000 |         1 |          6 |     728 | 6             | CUSTOMER F      |
| 2020-10-12 00:00:00.000 |         9 |          3 |    1876 | 3             | CUSTOMER C      |
| 2020-08-25 00:00:00.000 |         2 |          6 |     451 | 6             | CUSTOMER F      |
| 2020-09-30 00:00:00.000 |         8 |          3 |    1496 | 3             | CUSTOMER C      |
| 2020-07-27 00:00:00.000 |         1 |          3 |    1242 | 3             | CUSTOMER C      |
| 2020-12-23 00:00:00.000 |         7 |          1 |    4874 | 1             | CUSTOMER A      |
| 2021-01-08 00:00:00.000 |        10 |          7 |     997 | 7             | CUSTOMER G      |
| 2020-05-22 00:00:00.000 |         4 |          7 |     484 | 7             | CUSTOMER G      |
| 2020-03-19 00:00:00.000 |         7 |          1 |    2562 | 1             | CUSTOMER A      |
| 2020-05-07 00:00:00.000 |         1 |          4 |     960 | 4             | CUSTOMER D      |
| 2020-03-24 00:00:00.000 |         1 |          8 |     566 | 8             | CUSTOMER H      |
| 2021-03-08 00:00:00.000 |         4 |         10 |     115 |               |                 |
| 2020-05-25 00:00:00.000 |         5 |          9 |     405 | 9             | CUSTOMER I      |
| 2021-02-10 00:00:00.000 |         3 |         10 |     571 |               |                 |
| 2020-03-05 00:00:00.000 |         6 |          6 |     430 | 6             | CUSTOMER F      |
| 2020-10-20 00:00:00.000 |         2 |          6 |     141 | 6             | CUSTOMER F      |
| 2020-03-26 00:00:00.000 |         5 |          3 |    1024 | 3             | CUSTOMER C      |
| 2021-03-10 00:00:00.000 |         9 |          3 |    1335 | 3             | CUSTOMER C      |
| 2020-05-20 00:00:00.000 |         7 |          4 |     361 | 4             | CUSTOMER D      |
| 2020-02-26 00:00:00.000 |         8 |          4 |     758 | 4             | CUSTOMER D      |
| 2021-02-12 00:00:00.000 |         2 |          2 |    2791 | 2             | CUSTOMER B      |
| 2020-04-03 00:00:00.000 |         5 |          8 |     759 | 8             | CUSTOMER H      |
| 2021-03-11 00:00:00.000 |         7 |          7 |     852 | 7             | CUSTOMER G      |
| 2020-06-22 00:00:00.000 |         2 |          5 |     597 | 5             | CUSTOMER E      |
| 2020-01-29 00:00:00.000 |         2 |          9 |     572 | 9             | CUSTOMER I      |
| 2020-03-09 00:00:00.000 |         5 |          3 |    1622 | 3             | CUSTOMER C      |
| 2020-03-12 00:00:00.000 |         2 |          6 |     563 | 6             | CUSTOMER F      |
| 2020-01-30 00:00:00.000 |         5 |          3 |    1724 | 3             | CUSTOMER C      |
| 2020-04-08 00:00:00.000 |         4 |          8 |     795 | 8             | CUSTOMER H      |
| 2021-02-17 00:00:00.000 |         1 |          4 |     782 | 4             | CUSTOMER D      |
| 2021-01-06 00:00:00.000 |         5 |          6 |     303 | 6             | CUSTOMER F      |
| 2020-02-11 00:00:00.000 |        10 |          7 |     792 | 7             | CUSTOMER G      |
| 2020-11-10 00:00:00.000 |        10 |          5 |     735 | 5             | CUSTOMER E      |
| 2020-09-22 00:00:00.000 |         4 |          5 |     472 | 5             | CUSTOMER E      |
| 2021-01-20 00:00:00.000 |         8 |          3 |    1623 | 3             | CUSTOMER C      |
| 2020-06-19 00:00:00.000 |        10 |          2 |    2719 | 2             | CUSTOMER B      |
| 2020-05-13 00:00:00.000 |         7 |          3 |    1313 | 3             | CUSTOMER C      |
| 2020-01-15 00:00:00.000 |         4 |          9 |     405 | 9             | CUSTOMER I      |
| 2021-03-17 00:00:00.000 |         8 |          7 |     515 | 7             | CUSTOMER G      |
| 2020-08-18 00:00:00.000 |         8 |          1 |    2752 | 1             | CUSTOMER A      |



---

## Functional-Dependency__case_104

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Countries   | Event Date   | Event Description                                                                                                                                                                                                                 |   Event year | Country     | Image                                        |
|:------------|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------|:---------------------------------------------|
| Jordan      | 1970-09-07   | Popular Front for the Liberation of Palestine hijacks 4 planes and forces them to land at Dawson's Field, Jordan                                                                                                                  |         1970 | Jordan      | https://flagpedia.net/data/flags/h160/jo.png |
| Cuba        | 1960-09-17   | Cuba nationalizes US banks                                                                                                                                                                                                        |         1960 | Cuba        | https://flagpedia.net/data/flags/h160/cu.png |
| Finland     | 1835-02-28   | Dr Elias Lnnrot publishes Finnish poem Kalevala                                                                                                                                                                                   |         1835 | Finland     | https://flagpedia.net/data/flags/h160/fi.png |
| Albania     | 1913-07-29   | Independence of the Principality of Albania recognized by the Conference of London                                                                                                                                                |         1913 | Albania     | https://flagpedia.net/data/flags/h160/al.png |
| Bulgaria    | 1908-09-22   | Bulgaria declares independence from Ottoman Empire (Turkey)                                                                                                                                                                       |         1908 | Bulgaria    | https://flagpedia.net/data/flags/h160/bg.png |
| Panama      | 1911-01-31   | Congress names San Francisco as Panama Canal opening celebration site                                                                                                                                                             |         1911 | Panama      | https://flagpedia.net/data/flags/h160/pa.png |
| Palau       | 1981-01-01   | Palau (Trust Territory of Pacific Is) becomes self-governing                                                                                                                                                                      |         1981 | Palau       | https://flagpedia.net/data/flags/h160/pw.png |
| Indonesia   | 1959-07-05   | Indonesia restores constitution                                                                                                                                                                                                   |         1959 | Indonesia   | https://flagpedia.net/data/flags/h160/id.png |
| Afghanistan | 2003-08-11   | NATO takes over command of the peacekeeping force in Afghanistan, marking its first major operation outside Europe in its 54-year-history.                                                                                        |         2003 | Afghanistan | https://flagpedia.net/data/flags/h160/af.png |
| Estonia     | 1920-02-02   | Tarto/Dorpat peace treaty: USSR recognizes Estonian independence                                                                                                                                                                  |         1920 | Estonia     | https://flagpedia.net/data/flags/h160/er.png |
| France      | 1070-06-04   | Roquefort cheese created in a cave near Roquefort, France                                                                                                                                                                         |         1070 | France      | https://flagpedia.net/data/flags/h160/fr.png |
| Portugal    | 1654-01-26   | Portuguese troops conquer last Dutch base on Recife                                                                                                                                                                               |         1654 | Portugal    | https://flagpedia.net/data/flags/h160/pt.png |
| Denmark     | 1564-05-30   | (-31st) The first battle of Öland (between the islands of Gotland and Öland): Lübeck & Denmark beat Sweden                                                                                                                        |         1564 | Denmark     | https://flagpedia.net/data/flags/h160/dk.png |
| Mexico      | 1845-03-28   | Mexico drops diplomatic relations with US                                                                                                                                                                                         |         1845 | Mexico      | https://flagpedia.net/data/flags/h160/mx.png |
| Canada      | 1813-06-06   | US invasion of Canada halted at Stoney Creek (Ontario)                                                                                                                                                                            |         1813 | Canada      | https://flagpedia.net/data/flags/h160/cv.png |
| Morocco     | 1972-08-16   | Morocco King Hassan II's B727 shot during failed coup attempt by General Mohamed Oufkir. Reportedly, King Hassan grabbed the radio and told the rebel pilots Stop firing! The tyrant is dead!, fooling pilots to break off attack |         1972 | Morocco     | https://flagpedia.net/data/flags/h160/ma.png |
| Croatia     | 2016-08-16   | Croatian discus thrower Sandra Perković retains her Olympic title with a distance of 69.21m at the Rio de Janeiro Games                                                                                                           |         2016 | Croatia     | https://flagpedia.net/data/flags/h160/hr.png |
| Colombia    | 1538-08-06   | Bogotá, Colombia, is founded by Gonzalo Jiménez de Quesada                                                                                                                                                                        |         1538 | Colombia    | https://flagpedia.net/data/flags/h160/co.png |
| Egypt       | 1945-03-22   | Arab League forms with adoption of a charter in Cairo Egypt                                                                                                                                                                       |         1945 | Egypt       | https://flagpedia.net/data/flags/h160/ec.png |
| Greece      | 1827-10-08   | Sea battle at Navarino (Greece freed of Ottoman occupation)                                                                                                                                                                       |         1827 | Greece      | https://flagpedia.net/data/flags/h160/gr.png |
| Lithuania   | 1941-06-22   | The Lithuanian 1941 independence begins.                                                                                                                                                                                          |         1941 | Lithuania   | https://flagpedia.net/data/flags/h160/lt.png |
| Italy       | 0218-12-18   | BC Second Punic War: Battle of the Trebia - Hannibal's Carthaginian army heavily defeat Roman forces on Italian soil                                                                                                              |          218 | Italy       | https://flagpedia.net/data/flags/h160/it.png |
| Ukraine     | 2014-03-02   | President Vladimir Putin receives unanimous approval from Russia's parliament to send troops to the Ukraine                                                                                                                       |         2014 | Ukraine     | https://flagpedia.net/data/flags/h160/ua.png |
| Bulgaria    | 1913-03-26   | Bulgaria captures Adrianople, ending the 1st Balkan War                                                                                                                                                                           |         1913 | Bulgaria    | https://flagpedia.net/data/flags/h160/bg.png |
| Belarus     | 2011-10-30   | Czech tennis star Petra Kvitová beats Victoria Azarenka of Belarus 7–5, 4–6, 6–3 in the WTA Championship decider in Istanbul, Turkey                                                                                              |         2011 | Belarus     | https://flagpedia.net/data/flags/h160/by.png |
| China       | 1789-02-01   | Chinese troops driven out of Vietnam capital Thang Long                                                                                                                                                                           |         1789 | China       | https://flagpedia.net/data/flags/h160/ch.png |
| Austria     | 2005-10-22   | Austria's finance minister Karl-Heinz Grasser (36) weds Fiona Swarovski in Weissenkirchen, Austria                                                                                                                                |         2005 | Austria     | https://flagpedia.net/data/flags/h160/at.png |
| Tunisia     | 1984-01-02   | Riot in Tunis kills over 100                                                                                                                                                                                                      |         1984 | Tunisia     | https://flagpedia.net/data/flags/h160/tn.png |
| Peru        | 1992-04-05   | Peruvian President Alberto Fujimori suspends the constitution and dissolves Congress                                                                                                                                              |         1992 | Peru        | https://flagpedia.net/data/flags/h160/pe.png |
| Japan       | 1872-03-11   | The Meiji Japanese government officially annexes the Ryukyu Kingdom into what would become the Okinawa prefecture                                                                                                                 |         1872 | Japan       | https://flagpedia.net/data/flags/h160/jp.png |
| Togo        | 1965-12-06   | 2 trucks crashed into a crowd of dancers in Sotouboua Togo, kills 125                                                                                                                                                             |         1965 | Togo        | https://flagpedia.net/data/flags/h160/tg.png |
| Austria     | 1984-09-22   | Brussels Princess Astrid marries Archduke Lorenz of Austrian-Este at Church of Our Lady of De Zavel                                                                                                                               |         1984 | Austria     | https://flagpedia.net/data/flags/h160/at.png |
| Singapore   | 2000-10-31   | A Singapore Airlines Boeing 747-400 operating as Flight 006 collides with construction equipment upon takeoff in Taipei, Taiwan killing 79 passengers and four crew members                                                       |         2000 | Singapore   | https://flagpedia.net/data/flags/h160/sg.png |
| Vietnam     | 1962-01-18   | US begins spraying foliage in Vietnam to reveal Viet Cong guerrillas                                                                                                                                                              |         1962 | Vietnam     | https://flagpedia.net/data/flags/h160/vn.png |
| China       | 2012-08-18   | Former Martin and Everybody Hates Chris actress Tichina Arnold (43) weds Rico Hines in Honolulu, Hawaii                                                                                                                           |         2012 | China       | https://flagpedia.net/data/flags/h160/ch.png |
| Belgium     | 1907-04-12   | Belgium government of De Stain de Naeyer resigns                                                                                                                                                                                  |         1907 | Belgium     | https://flagpedia.net/data/flags/h160/be.png |
| Switzerland | 1915-09-05   | Anti-war conference in Zimmerwald, Switzerland                                                                                                                                                                                    |         1915 | Switzerland | https://flagpedia.net/data/flags/h160/se.png |
| Suriname    | 1908-05-09   | Dirk Fock becomes governor of Suriname                                                                                                                                                                                            |         1908 | Suriname    | https://flagpedia.net/data/flags/h160/sr.png |
| Pakistan    | 1960-06-11   | House packed with wedding celebrants collapses killing 30 (Pakistan)                                                                                                                                                              |         1960 | Pakistan    | https://flagpedia.net/data/flags/h160/pk.png |
| Nicaragua   | 1895-06-20   | Nicaragua, El Salvador and Honduras form a short-lived confederation                                                                                                                                                              |         1895 | Nicaragua   | https://flagpedia.net/data/flags/h160/ni.png |
| Mauritius   | 1968-03-12   | Mauritius gains independence from Britain (National Day)                                                                                                                                                                          |         1968 | Mauritius   | https://flagpedia.net/data/flags/h160/mu.png |
| Hungary     | 1526-11-09   | Jews are expelled from Pressburg (Bratislava), Hungary, by Maria of Hapsburg                                                                                                                                                      |         1526 | Hungary     | https://flagpedia.net/data/flags/h160/hu.png |
| Estonia     | 1920-02-24   | Peace treaty gives Estonia independence                                                                                                                                                                                           |         1920 | Estonia     | https://flagpedia.net/data/flags/h160/er.png |
| Norway      | 0793-06-08   | Vikings in long ships from modern-day Norway plunder St Cuthbert's monastery on Lindisfarne Island, off the northeast coast of England                                                                                            |          793 | Norway      | https://flagpedia.net/data/flags/h160/no.png |
| Peru        | 1978-05-23   | General strike in Peru                                                                                                                                                                                                            |         1978 | Peru        | https://flagpedia.net/data/flags/h160/pe.png |
| Ethiopia    | 1975-03-21   | Ethiopia abolishes its monarchy after 3,000 years                                                                                                                                                                                 |         1975 | Ethiopia    | https://flagpedia.net/data/flags/h160/et.png |
| Senegal     | 2012-03-26   | Macky Sall elected as President of Senegal                                                                                                                                                                                        |         2012 | Senegal     | https://flagpedia.net/data/flags/h160/sn.png |
| Mauritania  | 1994-07-01   | Fokker's-28 crashes at Tidjikja, Mauritania (94 killed)                                                                                                                                                                           |         1994 | Mauritania  | https://flagpedia.net/data/flags/h160/mr.png |
| Netherlands | 1655-02-16   | Dutch Grand Pensionary advisor Johan de Witt marries Wendela Bicker                                                                                                                                                               |         1655 | Netherlands | https://flagpedia.net/data/flags/h160/nl.png |
| Argentina   | 1816-07-09   | Argentina declares independence from Spain                                                                                                                                                                                        |         1816 | Argentina   | https://flagpedia.net/data/flags/h160/ar.png |



---

## Functional-Dependency__case_302

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|   UserKey |   StudentKey | UserEmail                | LastModifiedDate        |
|----------:|-------------:|:-------------------------|:------------------------|
|    207244 |       605753 |                          |                         |
|    207267 |       605447 | AlisaCameron@edfi.org    | 2021-11-05 19:02:30.703 |
|    207242 |       605143 |                          |                         |
|    207241 |       605228 |                          |                         |
|    207272 |       604849 | RussellGomez@edfi.org    | 2021-11-05 19:02:31.030 |
|    207244 |       604967 |                          |                         |
|    207270 |       605272 |                          |                         |
|    207267 |       605314 | AlisaCameron@edfi.org    | 2021-11-05 19:02:30.703 |
|    207264 |       605687 | MarjorieMontoya@edfi.org | 2021-11-05 19:02:30.620 |
|    207275 |       605659 |                          |                         |
|    207253 |       605220 | EstherGallegos@edfi.org  | 2021-11-05 19:02:30.936 |
|    207270 |       604881 |                          |                         |
|    207278 |       605339 |                          |                         |
|    207270 |       605728 |                          |                         |
|    207267 |       605273 | AlisaCameron@edfi.org    | 2021-11-05 19:02:30.703 |
|    207260 |       604828 |                          |                         |
|    207264 |       605077 | MarjorieMontoya@edfi.org | 2021-11-05 19:02:30.620 |
|    207258 |       605049 |                          |                         |
|    207253 |       605413 | EstherGallegos@edfi.org  | 2021-11-05 19:02:30.936 |
|    207285 |       604953 | DavidWilson@edfi.org     | 2021-11-05 19:02:30.693 |
|    207241 |       605219 |                          |                         |
|    207245 |       604833 |                          |                         |
|    207285 |       605700 | DavidWilson@edfi.org     | 2021-11-05 19:02:30.693 |
|    207253 |       605759 | EstherGallegos@edfi.org  | 2021-11-05 19:02:30.936 |
|    207243 |       605689 |                          |                         |
|    207285 |       605129 | DavidWilson@edfi.org     | 2021-11-05 19:02:30.693 |
|    207267 |       605401 | AlisaCameron@edfi.org    | 2021-11-05 19:02:30.703 |
|    207224 |       605166 |                          |                         |
|    207277 |       605223 |                          |                         |
|    207259 |       604930 |                          |                         |
|    207252 |       604852 |                          |                         |
|    207282 |       605749 |                          |                         |
|    207257 |       605315 |                          |                         |
|    207269 |       605464 |                          |                         |
|    207272 |       605752 | RussellGomez@edfi.org    | 2021-11-05 19:02:31.030 |
|    207262 |       605498 |                          |                         |
|    207255 |       605733 |                          |                         |
|    207267 |       605235 | AlisaCameron@edfi.org    | 2021-11-05 19:02:30.703 |
|    207243 |       605159 |                          |                         |
|    207225 |       605404 |                          |                         |
|    207259 |       605618 |                          |                         |
|    207258 |       605354 |                          |                         |
|    207285 |       605556 | DavidWilson@edfi.org     | 2021-11-05 19:02:30.693 |
|    207252 |       605419 |                          |                         |
|    207285 |       605072 | DavidWilson@edfi.org     | 2021-11-05 19:02:30.693 |
|    207245 |       605406 |                          |                         |
|    207278 |       605411 |                          |                         |
|    207285 |       604882 | DavidWilson@edfi.org     | 2021-11-05 19:02:30.693 |
|    207245 |       604846 |                          |                         |
|    207275 |       605528 |                          |                         |



---

## Functional-Dependency__case_159

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|     id |   campaign_id |   coupon_id |   customer_id | Redemption_status   | campaign_type   | start_date              | end_date                |   Intervel |
|-------:|--------------:|------------:|--------------:|:--------------------|:----------------|:------------------------|:------------------------|-----------:|
| 108400 |            11 |         971 |           709 | NO REDEM            | Y               | 2013-04-22 00:00:00.000 | 2013-06-07 00:00:00.000 |         46 |
|  17293 |             8 |         271 |           697 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
|  97164 |            11 |         669 |          1115 | NO REDEM            | Y               | 2013-04-22 00:00:00.000 | 2013-06-07 00:00:00.000 |         46 |
|  85822 |            13 |         142 |           304 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|  69116 |            13 |         796 |           905 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|  94307 |            10 |         662 |          1368 | NO REDEM            | Y               | 2013-04-08 00:00:00.000 | 2013-05-10 00:00:00.000 |         32 |
|  47712 |             8 |          79 |          1509 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
|   7719 |            30 |         666 |           588 | NO REDEM            | X               | 2012-11-19 00:00:00.000 | 2013-01-04 00:00:00.000 |         46 |
|  33891 |             8 |          56 |           519 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
|  52759 |            13 |         147 |           679 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|   2843 |             8 |         424 |           743 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
| 102920 |            30 |        1001 |            91 | NO REDEM            | X               | 2012-11-19 00:00:00.000 | 2013-01-04 00:00:00.000 |         46 |
| 122779 |             8 |         623 |          1390 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
|   3700 |            13 |         155 |          1104 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|  41219 |            12 |         783 |           100 | NO REDEM            | Y               | 2013-04-22 00:00:00.000 | 2013-05-24 00:00:00.000 |         32 |
|  22591 |            13 |        1114 |           947 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|  11762 |            13 |         601 |           202 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|  31924 |            13 |         516 |          1490 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|  23608 |             9 |         788 |           457 | NO REDEM            | Y               | 2013-03-11 00:00:00.000 | 2013-04-12 00:00:00.000 |         32 |
|  29384 |             8 |          50 |          1215 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
| 104682 |             8 |          91 |           901 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
|  14667 |             8 |         754 |          1202 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
| 103410 |            13 |        1108 |           737 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|  81296 |            13 |         159 |           702 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|  48494 |            13 |         142 |          1134 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|  87810 |            13 |          21 |           742 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|  40330 |             8 |         247 |           732 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
|  37381 |             9 |         520 |          1333 | NO REDEM            | Y               | 2013-03-11 00:00:00.000 | 2013-04-12 00:00:00.000 |         32 |
|  62298 |            13 |         116 |           754 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
|  12698 |            12 |         705 |           484 | NO REDEM            | Y               | 2013-04-22 00:00:00.000 | 2013-05-24 00:00:00.000 |         32 |
| 105879 |            13 |         129 |           332 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
| 108815 |            13 |         766 |           169 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
| 123490 |            30 |         486 |             9 | NO REDEM            | X               | 2012-11-19 00:00:00.000 | 2013-01-04 00:00:00.000 |         46 |
|   1156 |             2 |         744 |           679 | NO REDEM            | Y               | 2012-12-17 00:00:00.000 | 2013-01-18 00:00:00.000 |         32 |
|  24183 |            11 |        1012 |           446 | NO REDEM            | Y               | 2013-04-22 00:00:00.000 | 2013-06-07 00:00:00.000 |         46 |
|  59704 |            29 |         674 |          1099 | NO REDEM            | Y               | 2012-10-08 00:00:00.000 | 2012-11-30 00:00:00.000 |         53 |
|  15944 |             8 |          54 |          1104 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
|  93984 |            26 |         361 |           269 | NO REDEM            | X               | 2012-08-12 00:00:00.000 | 2012-09-21 00:00:00.000 |         40 |
|  25473 |             8 |         271 |           188 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
| 127221 |             8 |           7 |          1314 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
|  75861 |            26 |         660 |           225 | NO REDEM            | X               | 2012-08-12 00:00:00.000 | 2012-09-21 00:00:00.000 |         40 |
|  62842 |            13 |         130 |           740 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
| 120101 |            26 |         352 |           131 | NO REDEM            | X               | 2012-08-12 00:00:00.000 | 2012-09-21 00:00:00.000 |         40 |
| 105755 |             8 |          58 |          1305 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
|  24246 |            13 |         154 |           543 | NO REDEM            | X               | 2013-05-19 00:00:00.000 | 2013-07-05 00:00:00.000 |         47 |
| 122169 |             8 |         383 |          1098 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
|  51869 |             8 |          46 |            28 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
| 107935 |             5 |         431 |          1014 | NO REDEM            | Y               | 2013-01-12 00:00:00.000 | 2013-02-15 00:00:00.000 |         34 |
|  41828 |             8 |         296 |           301 | NO REDEM            | X               | 2013-02-16 00:00:00.000 | 2013-04-05 00:00:00.000 |         48 |
|  44256 |            30 |         933 |          1296 | NO REDEM            | X               | 2012-11-19 00:00:00.000 | 2013-01-04 00:00:00.000 |         46 |



---

## Functional-Dependency__case_148

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Date                    | IT Dep.               | CostElement          | Country        |   Budget | Cost Element         | Cost Element Group   | Business Area   |
|:------------------------|:----------------------|:---------------------|:---------------|---------:|:---------------------|:---------------------|:----------------|
| 2020-08-01 00:00:00.000 | R1                    | Recognition          | Canada         |       33 | Recognition          | Other                | BU              |
| 2020-09-01 00:00:00.000 | Productivity          | Hardware             | Netherlands    |     5901 | Hardware             | Hardware & Software  | R&D             |
| 2020-05-01 00:00:00.000 | Help Desk             | Telecomm             | USA            |     4645 | Telecomm             | Other                | R&D             |
| 2020-07-01 00:00:00.000 | Core Infrastructure   | Vehicles             | Canada         |       23 | Vehicles             | Other                | R&D             |
| 2020-12-01 00:00:00.000 | Productivity          | Travel               | United Kingdom |     2514 | Travel               | Other                | BU              |
| 2020-10-01 00:00:00.000 | Data Centers          | Software Maintenance | United Kingdom |    11743 | Software Maintenance | Hardware & Software  | R&D             |
| 2020-09-01 00:00:00.000 | Networking            | Administrative       | USA            |  -316925 | Administrative       | Administrative       | R&D             |
| 2020-05-01 00:00:00.000 | Core Infrastructure   | Supplies             | USA            |      423 | Supplies             | Other                | R&D             |
| 2020-02-01 00:00:00.000 | Manufacturing         | Hardware             | Ireland        |       34 | Hardware             | Hardware & Software  | R&D             |
| 2020-04-01 00:00:00.000 | Manufacturing         | Other                | United Kingdom |      162 | Other                | Other                | BU              |
| 2020-10-01 00:00:00.000 | Manufacturing         | Software Maintenance | United Kingdom |       81 | Software Maintenance | Hardware & Software  | R&D             |
| 2020-10-01 00:00:00.000 | EIM                   | Hardware Maintenance | USA            |      125 | Hardware Maintenance | Hardware & Software  | R&D             |
| 2020-02-01 00:00:00.000 | Distribution          | Telecomm             | Germany        |      144 | Telecomm             | Other                | R&D             |
| 2020-07-01 00:00:00.000 | Core Infrastructure   | Hardware Maintenance | Canada         |     4578 | Hardware Maintenance | Hardware & Software  | R&D             |
| 2020-06-01 00:00:00.000 | Development           | Travel               | United Kingdom |      875 | Travel               | Other                | BU              |
| 2020-03-01 00:00:00.000 | Manufacturing         | Employee Performance | USA            |     1276 | Employee Performance | Other                | BU              |
| 2020-01-01 00:00:00.000 | Manufacturing         | Training             | Spain          |      232 | Training             | Other                | BU              |
| 2020-07-01 00:00:00.000 | Six Sigma             | Administrative       | USA            |    -2609 | Administrative       | Administrative       | R&D             |
| 2020-08-01 00:00:00.000 | Vendor Management     | Telecomm             | USA            |     2400 | Telecomm             | Other                | R&D             |
| 2020-09-01 00:00:00.000 | Distribution          | Internal Labor       | Belgium        |     7183 | Internal Labor       | Labor                | BU              |
| 2020-03-01 00:00:00.000 | Core                  | Employee Performance | USA            |       29 | Employee Performance | Other                | BU              |
| 2020-12-01 00:00:00.000 | Six Sigma             | Training             | USA            |     1577 | Training             | Other                | BU              |
| 2020-06-01 00:00:00.000 | SSO                   | Employee Performance | USA            |      160 | Employee Performance | Other                | BU              |
| 2020-03-01 00:00:00.000 | R2                    | Internal Labor       | Italy          |     3999 | Internal Labor       | Labor                | BU              |
| 2020-06-01 00:00:00.000 | Core Infrastructure   | Depreciation         | Mexico         |     4616 | Depreciation         | Depr & Amort         | R&D             |
| 2020-01-01 00:00:00.000 | Distribution          | Travel               | Canada         |      561 | Travel               | Other                | BU              |
| 2020-09-01 00:00:00.000 | Data Centers          | External Labor       | USA            |   299663 | External Labor       | Labor                | BU              |
| 2020-01-01 00:00:00.000 | Productivity          | Travel               | United Kingdom |     2514 | Travel               | Other                | BU              |
| 2020-03-01 00:00:00.000 | Emerging              | Training             | Mexico         |      858 | Training             | Other                | BU              |
| 2020-04-01 00:00:00.000 | Vendor Management     | Software             | USA            |      200 | Software             | Hardware & Software  | R&D             |
| 2020-08-01 00:00:00.000 | Emerging              | Supplies             | Mexico         |       24 | Supplies             | Other                | R&D             |
| 2020-08-01 00:00:00.000 | R2                    | Internal Labor       | United Kingdom |    98587 | Internal Labor       | Labor                | BU              |
| 2020-01-01 00:00:00.000 | Productivity          | Travel               | Belgium        |      272 | Travel               | Other                | BU              |
| 2020-05-01 00:00:00.000 | Productivity          | Supplies             | Ireland        |      313 | Supplies             | Other                | R&D             |
| 2020-05-01 00:00:00.000 | Productivity          | External Labor       | Ireland        |    19277 | External Labor       | Labor                | BU              |
| 2020-03-01 00:00:00.000 | R1                    | Hardware             | Canada         |      116 | Hardware             | Hardware & Software  | R&D             |
| 2020-12-01 00:00:00.000 | Manufacturing         | Training             | Puerto Rico    |      320 | Training             | Other                | BU              |
| 2020-06-01 00:00:00.000 | Business Intelligence | Internal Labor       | USA            |    61026 | Internal Labor       | Labor                | BU              |
| 2020-02-01 00:00:00.000 | Productivity          | Depreciation         | Netherlands    |      511 | Depreciation         | Depr & Amort         | R&D             |
| 2020-04-01 00:00:00.000 | Innovation            | Internal Labor       | USA            |    17659 | Internal Labor       | Labor                | BU              |
| 2020-06-01 00:00:00.000 | Networking            | Amortization         | USA            |     1025 | Amortization         | Depr & Amort         | R&D             |
| 2020-04-01 00:00:00.000 | Core Infrastructure   | Hardware             | USA            |       51 | Hardware             | Hardware & Software  | R&D             |
| 2020-10-01 00:00:00.000 | Manufacturing         | Hardware             | Spain          |      864 | Hardware             | Hardware & Software  | R&D             |
| 2020-12-01 00:00:00.000 | Manufacturing         | Supplies             | France         |      408 | Supplies             | Other                | R&D             |
| 2020-07-01 00:00:00.000 | Manufacturing         | Telecomm             | Brazil         |       25 | Telecomm             | Other                | R&D             |
| 2020-09-01 00:00:00.000 | Productivity          | Telecomm             | France         |     2720 | Telecomm             | Other                | R&D             |
| 2020-01-01 00:00:00.000 | Networking            | External Labor       | USA            |   242943 | External Labor       | Labor                | BU              |
| 2020-04-01 00:00:00.000 | Document Management   | Telecomm             | USA            |     2820 | Telecomm             | Other                | R&D             |
| 2020-02-01 00:00:00.000 | Distribution          | Internal Labor       | Italy          |     7183 | Internal Labor       | Labor                | BU              |
| 2020-12-01 00:00:00.000 | Document Management   | Internal Labor       | USA            |   193712 | Internal Labor       | Labor                | BU              |



---

## Functional-Dependency__case_327

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| associate_id       | forecast_starting_date   | SF Assignment_V.Credited Utilization   | scheduled_hours_final   | Associate ID   | SF Contact         | Associates    | Team   |
|:-------------------|:-------------------------|:---------------------------------------|:------------------------|:---------------|:-------------------|:--------------|:-------|
| 0037000001Zs04GAAR | 2021-01-31 00:00:00.000  | Credited                               | 10.0                    | 2448           | 0037000001Zs04GAAR | Associate 29  | Team 1 |
| 00370000023WxCmAAK |                          |                                        |                         |                |                    |               |        |
| 0030g00002A3RG2AAN | 2021-01-10 00:00:00.000  | Credited                               | 0.2                     | 5487           | 0030g00002A3RG2AAN | Associate 97  | Team 2 |
| 0037000000wXuvQAAS | 2021-09-12 00:00:00.000  | Credited                               | 5.0                     | 1000           | 0037000000wXuvQAAS | Associate 1   | Team 1 |
| 00370000025WWBWAA4 | 2021-01-31 00:00:00.000  | Credited                               | 5.0                     | 5573           | 00370000025WWBWAA4 | Associate 109 | Team 1 |
| 0034u00002VUwZ9AAL | 2021-05-23 00:00:00.000  | Credited                               | 1.14                    | 7093           | 0034u00002VUwZ9AAL | Associate 236 | Team 2 |
| 0030g00002Ry6XEAAZ | 2021-01-24 00:00:00.000  | Credited                               | 0.25                    | 6257           | 0030g00002Ry6XEAAZ | Associate 137 | Team 2 |
| 003700000249tUCAAY | 2021-12-12 00:00:00.000  | Credited                               | 10.0                    | 5541           | 003700000249tUCAAY | Associate 102 | Team 1 |
| 0030g00002PFLbXAAX | 2021-05-23 00:00:00.000  | Credited                               | 4.0                     | 7081           | 0030g00002PFLbXAAX | Associate 233 | Team 2 |
| 0037000000tZRFmAAO | 2022-01-02 00:00:00.000  | Credited                               | 1.0                     | 905            | 0037000000tZRFmAAO | Associate 309 | Team 1 |
| 0030g00002DrALrAAN | 2021-03-07 00:00:00.000  | Credited                               | 2.63                    |                |                    |               |        |
| 0030g00002PFL7MAAX | 2021-01-03 00:00:00.000  | Credited                               | 2.0                     |                |                    |               |        |
| 0030g00002RZGlvAAH | 2021-09-19 00:00:00.000  | Credited                               | 15.0                    | 7261           | 0030g00002RZGlvAAH | Associate 261 | Team 1 |
| 00370000025WdiqAAC | 2021-09-12 00:00:00.000  | Credited                               | 0.5                     | 5278           | 00370000025WdiqAAC | Associate 86  | Team 1 |
| 0030g00002MZmhXAAT | 2021-09-19 00:00:00.000  | Credited                               | 0.29                    | 6549           | 0030g00002MZmhXAAT | Associate 164 | Team 1 |
| 0030g00002PUpamAAD |                          |                                        |                         |                |                    |               |        |
| 00370000014S3OcAAK | 2021-03-21 00:00:00.000  | Credited                               | 2.5                     | 2096           | 00370000014S3OcAAK | Associate 15  | Team 2 |
| 0030g00002JcVL8AAN | 2021-07-25 00:00:00.000  | Credited                               | 35.13                   | 6406           | 0030g00002JcVL8AAN | Associate 147 | Team 1 |
| 0030g00002ScCaOAAV | 2021-03-07 00:00:00.000  | Credited                               | 0.5                     |                |                    |               |        |
| 0030g00002MZmTLAA1 | 2021-04-25 00:00:00.000  | Credited                               | 0.45                    | 6941           | 0030g00002MZmTLAA1 | Associate 219 | Team 1 |
| 0030g00002MHd7gAAD | 2021-08-08 00:00:00.000  | Credited                               | 0.5                     |                |                    |               |        |
| 0030g00002RZGlvAAH | 2021-04-18 00:00:00.000  | Credited                               | 3.03                    | 7261           | 0030g00002RZGlvAAH | Associate 261 | Team 1 |
| 0030g00002UmwbkAAB | 2020-12-27 00:00:00.000  | Credited                               | 2.0                     |                |                    |               |        |
| 00370000024A11UAAS | 2021-03-14 00:00:00.000  | Credited                               | 1.09                    | 5555           | 00370000024A11UAAS | Associate 107 | Team 1 |
| 00370000022eV8bAAE | 2021-01-03 00:00:00.000  | Credited                               | 2.0                     | 5379           | 00370000022eV8bAAE | Associate 88  | Team 1 |
| 00370000025WdiqAAC | 2021-05-23 00:00:00.000  | Credited                               | 3.14                    | 5278           | 00370000025WdiqAAC | Associate 86  | Team 1 |
| 0030g00002ScCaOAAV | 2020-12-20 00:00:00.000  | Credited                               | 0.5                     |                |                    |               |        |
| 0030g00002Lmy96AAB | 2021-01-31 00:00:00.000  | Credited                               | 1.25                    | 6502           | 0030g00002Lmy96AAB | Associate 157 | Team 2 |
| 0030g00002PUpamAAD | 2021-06-13 00:00:00.000  | Credited                               | 0.1                     |                |                    |               |        |
| 0030g00002JcVL8AAN | 2021-06-06 00:00:00.000  | Credited                               | 4.0                     | 6406           | 0030g00002JcVL8AAN | Associate 147 | Team 1 |
| 0030g00002PUtGgAAL | 2021-09-26 00:00:00.000  | Credited                               | 0.5                     |                |                    |               |        |
| 0037000001Au4MUAAZ | 2021-09-05 00:00:00.000  | Credited                               | 0.11                    | 2372           | 0037000001Au4MUAAZ | Associate 27  | Team 2 |
| 0030g00002PUpamAAD | 2021-05-23 00:00:00.000  | Credited                               | 0.18                    |                |                    |               |        |
| 0030g00002PUpT7AAL | 2021-05-30 00:00:00.000  | Credited                               | 2.0                     | 7103           | 0030g00002PUpT7AAL | Associate 237 | Team 2 |
| 0030g00002A3RG2AAN | 2021-01-31 00:00:00.000  | Credited                               | 1.0                     | 5487           | 0030g00002A3RG2AAN | Associate 97  | Team 2 |
| 0037000001fLNt2AAG | 2021-06-27 00:00:00.000  | Credited                               | 0.44                    | 2775           | 0037000001fLNt2AAG | Associate 48  | Team 1 |
| 0030g00002MHdC8AAL | 2021-10-10 00:00:00.000  | Credited                               | 1.05                    |                |                    |               |        |
| 0030g00002MZmhXAAT | 2022-03-06 00:00:00.000  | Credited                               | 7.65                    | 6549           | 0030g00002MZmhXAAT | Associate 164 | Team 1 |
| 00370000017gqxfAAA | 2021-01-24 00:00:00.000  | Credited                               | 1.2                     | 2246           | 00370000017gqxfAAA | Associate 24  | Team 1 |
| 0030g00002PUpamAAD | 2021-05-09 00:00:00.000  | Credited                               | 1.0                     |                |                    |               |        |
| 00370000023fgUCAAY | 2021-03-28 00:00:00.000  | Credited                               | 3.0                     | 5512           | 00370000023fgUCAAY | Associate 99  | Team 1 |
| 0037000001z3RaDAAU | 2021-03-28 00:00:00.000  | Credited                               | 0.39                    | 5236           | 0037000001z3RaDAAU | Associate 82  | Team 2 |
| 0030g000027FoaSAAS | 2021-07-11 00:00:00.000  | Credited                               | 7.5                     | 5740           | 0030g000027FoaSAAS | Associate 117 | Team 1 |
| 0030g00002MZmjJAAT | 2021-01-31 00:00:00.000  | Credited                               | 4.8                     | 6551           | 0030g00002MZmjJAAT | Associate 165 | Team 1 |
| 0030g00002PUpT7AAL |                          |                                        |                         | 7103           | 0030g00002PUpT7AAL | Associate 237 | Team 2 |
| 0037000000wXuvQAAS | 2021-06-20 00:00:00.000  | Credited                               | 1.5                     | 1000           | 0037000000wXuvQAAS | Associate 1   | Team 1 |
| 0030g00002PUtGgAAL | 2021-10-24 00:00:00.000  | Credited                               | 0.75                    |                |                    |               |        |
| 0030g00002MZmhXAAT | 2021-04-25 00:00:00.000  | Credited                               | 5.96                    | 6549           | 0030g00002MZmhXAAT | Associate 164 | Team 1 |
| 0030g00002PUpT7AAL | 2021-07-11 00:00:00.000  | Credited                               | 1.6                     | 7103           | 0030g00002PUpT7AAL | Associate 237 | Team 2 |
| 00370000024A11UAAS | 2021-05-16 00:00:00.000  | Credited                               | 1.26                    | 5555           | 00370000024A11UAAS | Associate 107 | Team 1 |



---

## Functional-Dependency__case_301

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| movie_title                            | release_date_many       | genre               | MPAA_rating   |   gross_with_inflation |     gross |   ReleaseYear |   FilmAge | release_date            | hero                    | villian             | song                  |
|:---------------------------------------|:------------------------|:--------------------|:--------------|-----------------------:|----------:|--------------:|----------:|:------------------------|:------------------------|:--------------------|:----------------------|
| Pooh's Heffalump Movie                 | 2005-02-11 00:00:00.000 | Adventure           | G             |               23801835 |  18098433 |          2005 |        17 |                         |                         |                     |                       |
| Signs                                  | 2002-08-02 00:00:00.000 | Thriller/Suspense   | PG-13         |              330754439 | 227965690 |          2002 |        20 |                         |                         |                     |                       |
| African Cats                           | 2011-04-22 00:00:00.000 | Documentary         | G             |               16401551 |  15428747 |          2011 |        11 |                         |                         |                     |                       |
| Guilty as Sin                          | 1993-06-04 00:00:00.000 | Thriller/Suspense   | R             |               46064723 |  22622537 |          1993 |        29 |                         |                         |                     |                       |
| Nixon                                  | 1995-12-20 00:00:00.000 | Drama               | R             |               26302005 |  13668249 |          1995 |        27 |                         |                         |                     |                       |
| The Marrying Man                       | 1991-04-05 00:00:00.000 | Romantic Comedy     | R             |               24939118 |  12454768 |          1991 |        31 |                         |                         |                     |                       |
| The Lookout                            | 2007-03-30 00:00:00.000 | Drama               | R             |                5637048 |   4600585 |          2007 |        15 |                         |                         |                     |                       |
| My Science Project                     | 1985-08-09 00:00:00.000 | Comedy              |               |                9736051 |   4100000 |          1985 |        37 |                         |                         |                     |                       |
| Secretariat                            | 2010-10-08 00:00:00.000 | Drama               | PG            |               63781920 |  59699513 |          2010 |        12 |                         |                         |                     |                       |
| You Again                              | 2010-09-24 00:00:00.000 | Comedy              | PG            |               27461121 |  25702053 |          2010 |        12 |                         |                         |                     |                       |
| The Ladykillers                        | 2004-03-26 00:00:00.000 | Comedy              | R             |               53881593 |  39692139 |          2004 |        18 |                         |                         |                     |                       |
| Jack                                   | 1996-08-09 00:00:00.000 | Drama               | PG-13         |              111792852 |  58617334 |          1996 |        26 |                         |                         |                     |                       |
| High Heels and Low Lifes               | 2001-10-26 00:00:00.000 |                     | R             |                 337782 |    226792 |          2001 |        21 |                         |                         |                     |                       |
| Phenomenon                             | 1996-07-05 00:00:00.000 | Drama               | PG            |              199559799 | 104636382 |          1996 |        26 |                         |                         |                     |                       |
| Up                                     | 2009-05-29 00:00:00.000 | Adventure           | PG            |              329336681 | 293004164 |          2009 |        13 |                         |                         |                     |                       |
| Roving Mars                            | 2006-01-27 00:00:00.000 | Documentary         | G             |               12948025 |  10407978 |          2006 |        16 |                         |                         |                     |                       |
| Return to Oz                           | 1985-06-21 00:00:00.000 | Adventure           |               |               25215934 |  10618813 |          1985 |        37 |                         |                         |                     |                       |
| Toy Story 3                            | 2010-06-18 00:00:00.000 | Adventure           | G             |              443408255 | 415004880 |          2010 |        12 |                         |                         |                     |                       |
| Jonas Brothers: The 3D Concert Experi… | 2009-02-27 00:00:00.000 | Concert/Performance | G             |               38174685 |  38174685 |          2009 |        13 |                         |                         |                     |                       |
| Duets                                  | 2000-09-15 00:00:00.000 | Drama               | R             |                7404372 |   4734235 |          2000 |        22 |                         |                         |                     |                       |
| Super Mario Bros.                      | 1993-05-28 00:00:00.000 | Action              | PG            |               42445058 |  20844907 |          1993 |        29 |                         |                         |                     |                       |
| Mr. 3000                               | 2004-09-17 00:00:00.000 | Comedy              | PG-13         |               29593641 |  21800302 |          2004 |        18 |                         |                         |                     |                       |
| Tarzan                                 | 1999-06-16 00:00:00.000 | Adventure           | G             |              283900254 | 171091819 |          1999 |        23 | 1999-06-18 00:00:00.000 | Tarzan                  | Clayton             | You'll Be in My Heart |
| D.O.A.                                 | 1988-03-18 00:00:00.000 | Thriller/Suspense   |               |               26062188 |  12706478 |          1988 |        34 |                         |                         |                     |                       |
| Houseguest                             | 1995-01-06 00:00:00.000 | Comedy              | PG            |               51016522 |  26325256 |          1995 |        27 |                         |                         |                     |                       |
| Peter Pan: Return to Neverland         | 2002-02-15 00:00:00.000 | Adventure           | G             |               70269715 |  48430258 |          2002 |        20 |                         |                         |                     |                       |
| Homeward Bound II: Lost in San Franc…  | 1996-03-08 00:00:00.000 | Adventure           | G             |               62384706 |  32709423 |          1996 |        26 |                         |                         |                     |                       |
| The Boatniks                           | 1970-07-01 00:00:00.000 | Comedy              |               |              101200742 |  18607492 |          1970 |        52 |                         |                         |                     |                       |
| The Distinguished Gentleman            | 1992-12-04 00:00:00.000 | Comedy              | R             |               94349900 |  46434570 |          1992 |        30 |                         |                         |                     |                       |
| America's Heart and Soul               | 2004-07-02 00:00:00.000 | Documentary         | Not Rated     |                 426246 |    314000 |          2004 |        18 |                         |                         |                     |                       |
| Big Business                           | 1988-06-10 00:00:00.000 | Comedy              | PG            |               82352451 |  40150487 |          1988 |        34 |                         |                         |                     |                       |
| Alexander and the Terrible, Horrible,… | 2014-10-10 00:00:00.000 | Comedy              | PG            |               69055550 |  66954149 |          2014 |         8 |                         |                         |                     |                       |
| Moana                                  | 2016-11-23 00:00:00.000 | Adventure           | PG            |              246082029 | 246082029 |          2016 |         6 | 2016-11-23 00:00:00.000 | Moana                   |                     | How Far I'll Go       |
| The Odd Life of Timothy Green          | 2012-08-15 00:00:00.000 | Drama               | PG            |               54914942 |  51853450 |          2012 |        10 |                         |                         |                     |                       |
| Déjà Vu                                | 2006-11-22 00:00:00.000 | Thriller/Suspense   | PG-13         |               82267038 |  64038616 |          2006 |        16 |                         |                         |                     |                       |
| Monsters, Inc.                         | 2001-11-02 00:00:00.000 | Adventure           | G             |              416073179 | 289423425 |          2001 |        21 |                         |                         |                     |                       |
| The Rescuers Down Under                | 1990-11-16 00:00:00.000 | Adventure           | G             |               55796728 |  27931461 |          1990 |        32 | 1990-11-16 00:00:00.000 | Bernard and Miss Bianca | Percival C. McLeach |                       |
| Bubble Boy                             | 2001-08-24 00:00:00.000 | Comedy              | PG-13         |                7450434 |   5002310 |          2001 |        21 |                         |                         |                     |                       |
| What About Bob?                        | 1991-05-17 00:00:00.000 | Comedy              | PG            |              127571325 |  63710000 |          1991 |        31 |                         |                         |                     |                       |
| The Apple Dumpling Gang                | 1975-07-01 00:00:00.000 | Comedy              |               |              131246872 |  31916500 |          1975 |        47 |                         |                         |                     |                       |
| Ernest Goes to Jail                    | 1990-04-06 00:00:00.000 | Comedy              | PG            |               49999822 |  25029569 |          1990 |        32 |                         |                         |                     |                       |
| ESPN's Ultimate X - The Movie          | 2002-05-10 00:00:00.000 | Documentary         | PG            |                6089874 |   4197175 |          2002 |        20 |                         |                         |                     |                       |
| The Joy Luck Club                      | 1993-09-08 00:00:00.000 | Drama               | R             |               66768171 |  32790064 |          1993 |        29 |                         |                         |                     |                       |
| Snow Dogs                              | 2002-01-18 00:00:00.000 | Comedy              | PG            |              117745317 |  81150692 |          2002 |        20 |                         |                         |                     |                       |
| Mad Love                               | 1995-05-26 00:00:00.000 | Drama               | PG-13         |               29934306 |  15446532 |          1995 |        27 |                         |                         |                     |                       |
| Ratatouille                            | 2007-06-29 00:00:00.000 | Comedy              | G             |              252955933 | 206445654 |          2007 |        15 |                         |                         |                     |                       |
| Wild Hogs                              | 2007-03-02 00:00:00.000 | Comedy              | PG-13         |              206110533 | 168213584 |          2007 |        15 |                         |                         |                     |                       |
| Meet the Robinsons                     | 2007-03-30 00:00:00.000 | Adventure           | G             |              119860589 |  97822171 |          2007 |        15 | 2007-03-30 00:00:00.000 | Lewis                   | Doris               | Little Wonders        |
| Under the Tuscan Sun                   | 2003-09-26 00:00:00.000 | Comedy              | PG-13         |               60944053 |  43601508 |          2003 |        19 |                         |                         |                     |                       |
| The Other Sister                       | 1999-02-26 00:00:00.000 | Romantic Comedy     | PG-13         |               46145331 |  27807627 |          1999 |        23 |                         |                         |                     |                       |



---

## Functional-Dependency__case_208

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| Date                    |   ProductID |   BusinessUnitID |   SalespersonID | BusinessUnit   | Division      | Group     |
|:------------------------|------------:|-----------------:|----------------:|:---------------|:--------------|:----------|
| 2018-03-21 00:00:00.000 |        3319 |               27 |             130 | Wearables      | Electronics   | Wearable  |
| 2016-12-30 00:00:00.000 |        3516 |                4 |              34 | Hair Care BU   | Personal care | Hair Care |
| 2017-02-23 00:00:00.000 |        2892 |               27 |             101 | Wearables      | Electronics   | Wearable  |
| 2018-12-22 00:00:00.000 |        8622 |               22 |               5 | Smartphones    | Electronics   | Mobile    |
| 2018-07-27 00:00:00.000 |        2892 |               27 |              33 | Wearables      | Electronics   | Wearable  |
| 2017-04-18 00:00:00.000 |        3516 |               27 |              24 | Wearables      | Electronics   | Wearable  |
| 2018-09-20 00:00:00.000 |        1837 |                1 |             140 | Baby Care BU   | Personal care | Baby Care |
| 2017-04-01 00:00:00.000 |        3721 |               27 |              79 | Wearables      | Electronics   | Wearable  |
| 2018-07-09 00:00:00.000 |        3526 |               27 |              74 | Wearables      | Electronics   | Wearable  |
| 2018-12-18 00:00:00.000 |        8622 |               22 |               9 | Smartphones    | Electronics   | Mobile    |
| 2018-10-09 00:00:00.000 |        3526 |               27 |             115 | Wearables      | Electronics   | Wearable  |
| 2016-07-28 00:00:00.000 |        2892 |                4 |             100 | Hair Care BU   | Personal care | Hair Care |
| 2017-05-31 00:00:00.000 |        5466 |                6 |              63 | Skin Care BU   | Personal care | Skin Care |
| 2018-11-12 00:00:00.000 |        8622 |               22 |              59 | Smartphones    | Electronics   | Mobile    |
| 2017-12-21 00:00:00.000 |        2892 |               27 |             136 | Wearables      | Electronics   | Wearable  |
| 2016-08-25 00:00:00.000 |        2892 |               27 |              47 | Wearables      | Electronics   | Wearable  |
| 2016-05-31 00:00:00.000 |        3526 |                4 |             156 | Hair Care BU   | Personal care | Hair Care |
| 2018-06-29 00:00:00.000 |        3221 |               27 |             101 | Wearables      | Electronics   | Wearable  |
| 2016-03-21 00:00:00.000 |        8631 |               22 |              13 | Smartphones    | Electronics   | Mobile    |
| 2018-06-26 00:00:00.000 |        7995 |               21 |               9 | Tablets        | Electronics   | Mobile    |
| 2017-12-21 00:00:00.000 |        2892 |               27 |             120 | Wearables      | Electronics   | Wearable  |
| 2017-10-30 00:00:00.000 |        6028 |                7 |              27 | Accessories    | Electronics   | Comp      |
| 2018-06-12 00:00:00.000 |        3415 |                4 |              51 | Hair Care BU   | Personal care | Hair Care |
| 2016-11-30 00:00:00.000 |        3933 |                1 |             140 | Baby Care BU   | Personal care | Baby Care |
| 2018-10-25 00:00:00.000 |        2868 |                4 |             143 | Hair Care BU   | Personal care | Hair Care |
| 2018-04-11 00:00:00.000 |        6765 |               21 |             118 | Tablets        | Electronics   | Mobile    |
| 2018-12-17 00:00:00.000 |        7683 |               28 |             106 | Speakers       | Electronics   | Audio     |
| 2017-10-05 00:00:00.000 |        3333 |               27 |             101 | Wearables      | Electronics   | Wearable  |
| 2016-12-12 00:00:00.000 |        8406 |               21 |             146 | Tablets        | Electronics   | Mobile    |
| 2018-08-31 00:00:00.000 |        7751 |               28 |              70 | Speakers       | Electronics   | Audio     |
| 2017-03-01 00:00:00.000 |        3721 |               27 |             164 | Wearables      | Electronics   | Wearable  |
| 2018-01-29 00:00:00.000 |        2892 |               27 |              96 | Wearables      | Electronics   | Wearable  |
| 2016-04-19 00:00:00.000 |        3415 |                4 |              46 | Hair Care BU   | Personal care | Hair Care |
| 2017-10-20 00:00:00.000 |        2146 |                1 |              76 | Baby Care BU   | Personal care | Baby Care |
| 2017-01-11 00:00:00.000 |        3308 |               27 |              24 | Wearables      | Electronics   | Wearable  |
| 2017-11-28 00:00:00.000 |        3300 |               27 |               8 | Wearables      | Electronics   | Wearable  |
| 2016-09-30 00:00:00.000 |        9785 |               22 |              81 | Smartphones    | Electronics   | Mobile    |
| 2018-03-12 00:00:00.000 |        2127 |                1 |             115 | Baby Care BU   | Personal care | Baby Care |
| 2018-09-20 00:00:00.000 |        3539 |               27 |             104 | Wearables      | Electronics   | Wearable  |
| 2017-09-29 00:00:00.000 |        3305 |               27 |              32 | Wearables      | Electronics   | Wearable  |
| 2018-06-15 00:00:00.000 |        2564 |                1 |             104 | Baby Care BU   | Personal care | Baby Care |
| 2016-11-25 00:00:00.000 |        2877 |               20 |              50 | Recorders      | Electronics   | Video     |
| 2016-08-16 00:00:00.000 |        3333 |               27 |             145 | Wearables      | Electronics   | Wearable  |
| 2018-05-29 00:00:00.000 |        8618 |               22 |              39 | Smartphones    | Electronics   | Mobile    |
| 2018-10-25 00:00:00.000 |        3319 |               27 |              40 | Wearables      | Electronics   | Wearable  |
| 2016-01-21 00:00:00.000 |        7686 |               28 |              72 | Speakers       | Electronics   | Audio     |
| 2018-01-28 00:00:00.000 |        3679 |               19 |             132 | Lighting       | Electronics   | Video     |
| 2016-10-10 00:00:00.000 |        6765 |               21 |             112 | Tablets        | Electronics   | Mobile    |
| 2018-03-14 00:00:00.000 |         966 |                1 |               1 | Baby Care BU   | Personal care | Baby Care |
| 2017-01-31 00:00:00.000 |        3526 |               27 |              99 | Wearables      | Electronics   | Wearable  |



---

## Functional-Dependency__case_105

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
|   cart_id |   customer_id |   order_id |   invoice_id |   stage_id |   source_id | Stage Name       | Sorted Stage       |
|----------:|--------------:|-----------:|-------------:|-----------:|------------:|:-----------------|:-------------------|
|       550 |            80 |       1139 |          293 |          1 |           5 | Shopping         | 1 Shopping         |
|        64 |           577 |        700 |          202 |          3 |           4 | Add Address      | 3 Add Address      |
|        96 |           250 |       1045 |         1757 |          3 |           7 | Add Address      | 3 Add Address      |
|       595 |           175 |       1156 |         1615 |          2 |           3 | Start Checkout   | 2 Start Checkout   |
|        49 |           880 |       1098 |         1444 |          1 |           6 | Shopping         | 1 Shopping         |
|       669 |           630 |       1603 |          621 |          2 |           3 | Start Checkout   | 2 Start Checkout   |
|       432 |           274 |       1380 |          919 |          2 |           2 | Start Checkout   | 2 Start Checkout   |
|       440 |           705 |       1591 |         1505 |          1 |           5 | Shopping         | 1 Shopping         |
|       357 |           997 |       1497 |          840 |          4 |           5 | Add Payment      | 4 Add Payment      |
|       489 |            13 |       1701 |         1727 |          1 |           3 | Shopping         | 1 Shopping         |
|       779 |           921 |        882 |          735 |          3 |           5 | Add Address      | 3 Add Address      |
|       872 |           647 |        651 |         1161 |          1 |           7 | Shopping         | 1 Shopping         |
|       494 |           648 |        448 |          913 |          2 |           2 | Start Checkout   | 2 Start Checkout   |
|       748 |           586 |        822 |          116 |          7 |           7 | Shipped          | 7 Shipped          |
|       235 |           186 |         12 |         1633 |          7 |           4 | Shipped          | 7 Shipped          |
|       874 |           547 |        583 |         1756 |          4 |           4 | Add Payment      | 4 Add Payment      |
|       379 |           383 |       1983 |         1439 |          1 |           1 | Shopping         | 1 Shopping         |
|       675 |           431 |        891 |         1991 |          4 |           4 | Add Payment      | 4 Add Payment      |
|       299 |           473 |       1926 |          125 |          3 |           1 | Add Address      | 3 Add Address      |
|       805 |           281 |       1653 |          119 |          1 |           1 | Shopping         | 1 Shopping         |
|       945 |           356 |       1637 |         1005 |          1 |           5 | Shopping         | 1 Shopping         |
|       981 |           540 |       1793 |         1785 |          1 |           3 | Shopping         | 1 Shopping         |
|       526 |           405 |        162 |         1956 |          1 |           4 | Shopping         | 1 Shopping         |
|       678 |           680 |       1123 |          900 |          1 |           5 | Shopping         | 1 Shopping         |
|       430 |           545 |        709 |          808 |          1 |           2 | Shopping         | 1 Shopping         |
|       743 |           821 |       1670 |         1381 |          1 |           2 | Shopping         | 1 Shopping         |
|       163 |           433 |       1626 |         1232 |          1 |           3 | Shopping         | 1 Shopping         |
|       884 |           984 |       1963 |          786 |          5 |           3 | Order Created    | 5 Order Created    |
|       899 |           863 |       1157 |          377 |          4 |           5 | Add Payment      | 4 Add Payment      |
|       358 |           533 |       1735 |          974 |          6 |           6 | Order Processing | 6 Order Processing |
|       159 |           258 |        786 |          629 |          1 |           4 | Shopping         | 1 Shopping         |
|       556 |           764 |       1548 |          916 |          1 |           3 | Shopping         | 1 Shopping         |
|       407 |            38 |        126 |          170 |          2 |           4 | Start Checkout   | 2 Start Checkout   |
|       290 |           366 |        570 |          544 |          1 |           5 | Shopping         | 1 Shopping         |
|       523 |           803 |       1371 |         1784 |          1 |           4 | Shopping         | 1 Shopping         |
|       314 |           693 |        149 |          565 |          1 |           2 | Shopping         | 1 Shopping         |
|       721 |           903 |       1271 |          484 |          2 |           1 | Start Checkout   | 2 Start Checkout   |
|       179 |           848 |       1235 |         1252 |          2 |           6 | Start Checkout   | 2 Start Checkout   |
|       895 |            32 |       1564 |          997 |          4 |           6 | Add Payment      | 4 Add Payment      |
|       700 |           698 |        885 |         1491 |          1 |           7 | Shopping         | 1 Shopping         |
|       936 |            28 |        272 |         1616 |          1 |           1 | Shopping         | 1 Shopping         |
|       118 |           924 |        236 |         1690 |          1 |           3 | Shopping         | 1 Shopping         |
|       711 |           670 |       1650 |          443 |          1 |           1 | Shopping         | 1 Shopping         |
|       761 |           921 |        625 |          827 |          7 |           2 | Shipped          | 7 Shipped          |
|       585 |           913 |       1930 |          659 |          1 |           1 | Shopping         | 1 Shopping         |
|       318 |           263 |        435 |         1092 |          1 |           1 | Shopping         | 1 Shopping         |
|       122 |           477 |        585 |         1271 |          5 |           4 | Order Created    | 5 Order Created    |
|       285 |            13 |        651 |         1402 |          2 |           1 | Start Checkout   | 2 Start Checkout   |
|       389 |           419 |       1277 |          897 |          1 |           6 | Shopping         | 1 Shopping         |
|        48 |           951 |         34 |         1716 |          4 |           4 | Add Payment      | 4 Add Payment      |



---

## Functional-Dependency__case_67

**Task:** Functional-Dependency

**Input:**

Given a table represented shown below, your task is to determine functional dependencies that exist in the table. Recall that a functional dependency is a relationship where the value of one attribute (or a set of attributes), known as the determinant columns, can uniquely determines the value of another attribute, known as the dependent columns (e.g., student-ID => student-Name, car-model => car-make, employee-ID => department, etc.).

Instructions:
Analyze the provided table below, identify all functional dependencies that should semantically hold in the table. Do not produce spurious relationships that not semantically meaningful.

No explanation, format the output as a JSON object:{"Functional-Dependency": <list of functional dependencies>}. Each functional dependency should be represented as [<determinant column>, <dependent column>]

Input Table:
| product_code   | customer_code   | market_code   | order_date              |   sales_qty |   sales_amount | currency   |   norm_sales_amount | custmer_name             | customer_type   |
|:---------------|:----------------|:--------------|:------------------------|------------:|---------------:|:-----------|--------------------:|:-------------------------|:----------------|
| Prod120        | Cus010          | Mark003       | 2019-05-10 00:00:00.000 |           1 |            245 | INR        |                 245 | Atlas Stores             | Brick & Mortar  |
| Prod113        | Cus018          | Mark011       | 2019-04-05 00:00:00.000 |           1 |            324 | INR        |                 324 | Electricalslance Stores  | Brick & Mortar  |
| Prod049        | Cus002          | Mark007       | 2019-02-05 00:00:00.000 |           1 |            907 | INR        |                 907 | Nomad Stores             | Brick & Mortar  |
| Prod057        | Cus019          | Mark011       | 2018-12-11 00:00:00.000 |           3 |           1847 | INR        |                1847 | Electricalsopedia Stores | Brick & Mortar  |
| Prod294        | Cus020          | Mark011       | 2019-08-05 00:00:00.000 |           1 |            102 | INR        |                 102 | Nixon                    | E-Commerce      |
| Prod260        | Cus022          | Mark011       | 2018-08-08 00:00:00.000 |          53 |           4074 | INR        |                4074 | Electricalslytical       | E-Commerce      |
| Prod116        | Cus018          | Mark011       | 2019-01-09 00:00:00.000 |           2 |            500 | INR        |                 500 | Electricalslance Stores  | Brick & Mortar  |
| Prod309        | Cus006          | Mark004       | 2019-02-26 00:00:00.000 |           1 |            509 | INR        |                 509 | Electricalsara Stores    | Brick & Mortar  |
| Prod300        | Cus024          | Mark011       | 2019-01-23 00:00:00.000 |           1 |             37 | INR        |                  37 | Power                    | E-Commerce      |
| Prod269        | Cus005          | Mark004       | 2018-04-26 00:00:00.000 |           1 |            185 | INR        |                 185 | Premium Stores           | Brick & Mortar  |
| Prod129        | Cus033          | Mark005       | 2017-10-27 00:00:00.000 |           3 |           1417 | INR        |                1417 | All-Out                  | E-Commerce      |
| Prod318        | Cus010          | Mark003       | 2020-05-19 00:00:00.000 |           2 |           2630 | INR        |                2630 | Atlas Stores             | Brick & Mortar  |
| Prod206        | Cus016          | Mark002       | 2020-05-14 00:00:00.000 |           3 |           2347 | INR        |                2347 | Logic Stores             | Brick & Mortar  |
| Prod206        | Cus016          | Mark002       | 2019-07-22 00:00:00.000 |           1 |            565 | INR        |                 565 | Logic Stores             | Brick & Mortar  |
| Prod296        | Cus020          | Mark004       | 2018-03-08 00:00:00.000 |           1 |            329 | INR        |                 329 | Nixon                    | E-Commerce      |
| Prod326        | Cus013          | Mark003       | 2018-09-28 00:00:00.000 |           7 |          14704 | INR        |               14704 | Unity Stores             | Brick & Mortar  |
| Prod123        | Cus031          | Mark005       | 2017-11-24 00:00:00.000 |           1 |             83 | INR        |                  83 | Zone                     | E-Commerce      |
| Prod250        | Cus023          | Mark011       | 2019-06-12 00:00:00.000 |          28 |           2722 | INR        |                2722 | Sound                    | E-Commerce      |
| Prod298        | Cus008          | Mark005       | 2019-10-30 00:00:00.000 |           5 |          11731 | INR        |               11731 | Acclaimed Stores         | Brick & Mortar  |
| Prod250        | Cus019          | Mark011       | 2019-10-24 00:00:00.000 |           1 |            111 | INR        |                 111 | Electricalsopedia Stores | Brick & Mortar  |
| Prod129        | Cus008          | Mark005       | 2017-12-11 00:00:00.000 |           1 |            157 | INR        |                 157 | Acclaimed Stores         | Brick & Mortar  |
| Prod334        | Cus010          | Mark003       | 2018-10-31 00:00:00.000 |           1 |            861 | INR        |                 861 | Atlas Stores             | Brick & Mortar  |
| Prod334        | Cus037          | Mark007       | 2018-02-14 00:00:00.000 |           1 |            444 | INR        |                 444 | Propel                   | E-Commerce      |
| Prod246        | Cus007          | Mark004       | 2018-11-27 00:00:00.000 |         160 |          13778 | INR        |               13778 | Info Stores              | Brick & Mortar  |
| Prod292        | Cus005          | Mark004       | 2019-04-10 00:00:00.000 |           1 |            106 | INR        |                 106 | Premium Stores           | Brick & Mortar  |
| Prod232        | Cus010          | Mark002       | 2018-04-12 00:00:00.000 |          33 |           2713 | INR        |                2713 | Atlas Stores             | Brick & Mortar  |
| Prod280        | Cus005          | Mark004       | 2018-01-30 00:00:00.000 |           1 |             65 | INR        |                  65 | Premium Stores           | Brick & Mortar  |
| Prod290        | Cus021          | Mark011       | 2020-06-11 00:00:00.000 |           1 |            356 | INR        |                 356 | Modular                  | E-Commerce      |
| Prod297        | Cus019          | Mark011       | 2017-10-24 00:00:00.000 |           1 |            347 | INR        |                 347 | Electricalsopedia Stores | Brick & Mortar  |
| Prod334        | Cus010          | Mark003       | 2019-06-20 00:00:00.000 |           2 |           2074 | INR        |                2074 | Atlas Stores             | Brick & Mortar  |
| Prod290        | Cus018          | Mark011       | 2018-06-22 00:00:00.000 |           1 |             83 | INR        |                  83 | Electricalslance Stores  | Brick & Mortar  |
| Prod216        | Cus016          | Mark002       | 2020-04-28 00:00:00.000 |           3 |           1505 | INR        |                1505 | Logic Stores             | Brick & Mortar  |
| Prod316        | Cus006          | Mark004       | 2020-05-11 00:00:00.000 |         120 |         129491 | INR        |              129491 | Electricalsara Stores    | Brick & Mortar  |
| Prod297        | Cus005          | Mark004       | 2017-11-15 00:00:00.000 |           1 |            287 | INR        |                 287 | Premium Stores           | Brick & Mortar  |
| Prod129        | Cus007          | Mark004       | 2019-09-06 00:00:00.000 |           1 |            106 | INR        |                 106 | Info Stores              | Brick & Mortar  |
| Prod123        | Cus018          | Mark011       | 2019-09-19 00:00:00.000 |           1 |            296 | INR        |                 296 | Electricalslance Stores  | Brick & Mortar  |
| Prod239        | Cus020          | Mark004       | 2018-10-24 00:00:00.000 |           2 |            181 | INR        |                 181 | Nixon                    | E-Commerce      |
| Prod060        | Cus010          | Mark003       | 2018-10-22 00:00:00.000 |           3 |           1181 | INR        |                1181 | Atlas Stores             | Brick & Mortar  |
| Prod177        | Cus005          | Mark004       | 2017-12-04 00:00:00.000 |           3 |           2954 | INR        |                2954 | Premium Stores           | Brick & Mortar  |
| Prod280        | Cus024          | Mark011       | 2018-03-15 00:00:00.000 |           1 |             56 | INR        |                  56 | Power                    | E-Commerce      |
| Prod057        | Cus017          | Mark011       | 2018-03-23 00:00:00.000 |           3 |           2014 | INR        |                2014 | Epic Stores              | Brick & Mortar  |
| Prod110        | Cus007          | Mark004       | 2018-06-12 00:00:00.000 |          19 |          27167 | INR        |               27167 | Info Stores              | Brick & Mortar  |
| Prod188        | Cus003          | Mark003       | 2017-11-29 00:00:00.000 |           5 |           6454 | INR        |                6454 | Excel Stores             | Brick & Mortar  |
| Prod040        | Cus005          | Mark004       | 2018-06-29 00:00:00.000 |           1 |            431 | INR        |                 431 | Premium Stores           | Brick & Mortar  |
| Prod288        | Cus021          | Mark011       | 2018-04-06 00:00:00.000 |           2 |            435 | INR        |                 435 | Modular                  | E-Commerce      |
| Prod261        | Cus024          | Mark002       | 2019-10-07 00:00:00.000 |           1 |             74 | INR        |                  74 | Power                    | E-Commerce      |
| Prod135        | Cus006          | Mark004       | 2017-12-08 00:00:00.000 |           3 |            620 | INR        |                 620 | Electricalsara Stores    | Brick & Mortar  |
| Prod103        | Cus003          | Mark003       | 2018-06-28 00:00:00.000 |           1 |            435 | INR        |                 435 | Excel Stores             | Brick & Mortar  |
| Prod166        | Cus035          | Mark007       | 2019-02-05 00:00:00.000 |           1 |            269 | INR        |                 269 | Relief                   | E-Commerce      |
| Prod271        | Cus016          | Mark002       | 2020-04-16 00:00:00.000 |           1 |            167 | INR        |                 167 | Logic Stores             | Brick & Mortar  |



---

## String-Relationship__case_7867

**Task:** String-Relationship

**Input:**

You are given a table below, where some of the columns may be derived from other columns using string-based transformations (e.g., string split, concatenation, formatting, substring extraction, and pattern matching, etc.). 

Your task is to identify string transformation relationships between the columns, by determining if any column, henceforce referred to as a TargetColumn, can be derived from other columns, referred to as SourceColumns, using the string-based transformations. Please only return relationships that are semantically meaningful and truly hold, and do not return any relationships that are spurious. 

No explanation is needed, return all the detected relationships in the following JSON format: 
{
  "String-Relationship": [
    [["SourceColumn1", "SourceColumn2", ...], "TargetColumn"],
    ...
  ]
}

Input Table:
| Foreign_0   |   Foreign_1 |   Foreign_2 |   Foreign_3 |   Foreign_4 | Foreign_5   | Foreign_6                                                                          | Foreign_7   |   Foreign_8 |   Foreign_9 |   Foreign_10 |   Foreign_11 | Foreign_12   |       Foreign_13 | Foreign_14                          |   Foreign_15 | Foreign_16           |   Foreign_17 |   Foreign_18 | Foreign_19      |   Foreign_20 |   Foreign_21 |   Foreign_22 |   Foreign_23 |   Foreign_24 |   Foreign_25 |   Foreign_26 | Foreign_27        | Foreign_28   |   Foreign_29 |   A | B                                           | C      | D         |   E | F                                                                                                                                                                      |   G |   H |
|:------------|------------:|------------:|------------:|------------:|:------------|:-----------------------------------------------------------------------------------|:------------|------------:|------------:|-------------:|-------------:|:-------------|-----------------:|:------------------------------------|-------------:|:---------------------|-------------:|-------------:|:----------------|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|-------------:|:------------------|:-------------|-------------:|----:|:--------------------------------------------|:-------|:----------|----:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----:|----:|
| 5           |         168 |   161467    |          30 |        3    | 53          | Coolant spin on filter/conditioner                                                 | CHPC        |        0.7  |         194 |        42100 |      1315813 |              |      2.20861e+06 | RENFE ALTA VELOCITAT (AVE)          |           93 | Belfast LGD          |      102.9   |            4 |                 |           74 |      10.8818 |           11 |        15000 |      166.851 |         1661 |        102.4 | Jeroen Sercu      | CLM          |       180000 |   1 | RECORD TYPE CODE                            | 1-5    | X(5)      |   5 | "TPALT"                                                                                                                                                                |   1 |   5 |
| 5           |          18 |   180529    |           0 |        3    |             | Davco 382 fuel/water separator, non heated                                         |             |        0.6  |         150 |        42100 |       473925 |              | 614110           | RENFE RODALIES                      |           21 | Northern Ireland     |      100.8   |           14 | Big Dog Classic |           32 |    4240.69   |           41 |         1625 |      166.851 |         2317 |        102.4 | Arthur Janssens   | LM           |        37000 |   2 | REPORT YEAR                                 | 6-9    | 9(4)      |   4 | This is the calendar year that this report is being sent by the TPA.                                                                                                   |   6 |   9 |
|             |             |             |             |             |             |                                                                                    |             |             |             |              |              |              |                  |                                     |              |                      |              |              |                 |              |              |              |              |              |              |              |                   |              |              |     |                                             |        |           |     | Format is: "YYYY".                                                                                                                                                     |     |     |
| 5           |         296 |    48004.5  |          30 |        1.68 | 31          | Davco 382 fuel/water separator, non heated                                         |             |        0.6  |          98 |        42100 |     12228064 |              | 344982           | RENFE AVANT                         |           93 | Belfast LGD          |      100.8   |           23 |                 |           12 |       0      |           30 |         1625 |     2586.19  |         7722 |        102.4 | Glenn Vlamynck    | LM           |        37000 |   3 | SEQUENCE NO                                 | 10-16  | 9(7)      |   7 | An incrementing batch sequence number that starts at 0000001.                                                                                                          |  10 |  16 |
| 5           |          16 |   180529    |           0 |        3.25 | 51          | Oil fill and dipstick EZ access                                                    |             |        0.8  |         154 |        42100 |      2714217 |              |  74944.1         | RENFE MITJANA DISTÀNCIA (REGIONALS) |           45 | Northern Ireland     |      108.481 |           38 |                 |           12 |       0      |           41 |         1625 |     2669.61  |         2317 |        102.4 | Anthony Denoyel   | LM           |       180000 |   4 | BENEFIT YEAR                                | 17-20  | 9(4)      |   4 | The benefit year for which invoice cycle has ended.                                                                                                                    |  17 |  20 |
|             |             |             |             |             |             |                                                                                    |             |             |             |              |              |              |                  |                                     |              |                      |              |              |                 |              |              |              |              |              |              |              |                   |              |              |     |                                             |        |           |     | Format is: "YYYY".                                                                                                                                                     |     |     |
| 5           |          18 |    34312.6  |           0 |        4.98 | 45          | Front engine powered take off adapter and radiator cut out                         |             |        0.7  |         191 |        42100 |      1986482 |              | 461540           | RENFE AVANT                         |           93 | Belfast LGD Deprived |      100     |            3 |                 |           34 |    4240.69   |           30 |        15000 |     2669.61  |         7722 |        102.4 | Anthony Denoyel   | LM           |        37000 |   5 | DDPS SYSTEM DATE                            | 21-28  | 9(8)      |   8 | ‘CCYYMMDD’ = DDPS File creation date.                                                                                                                                  |  21 |  28 |
| 5           |          28 |   125608    |         146 |       20.97 | 58          | Coolant spin on filter/conditioner                                                 |             |        0.7  |         181 |        34500 |     58343439 |              | 791192           | METRO                               |           96 | Northern Ireland     |      100.8   |            1 |                 |           34 |       0      |           58 |        15000 |     2586.19  |         4655 |        102.4 | Diego De Soete    | LM           |       180000 |   6 | DDPS SYSTEM TIME                            | 29-34  | 9(6)      |   6 | ‘HHMMSS’ = DDPS File creation time.                                                                                                                                    |  29 |  34 |
| 3           |          73 |    62202.7  |           0 |        4.98 | 61          | Fuel/water separator/heated/ Thermostatically controlled, Racor 400 series (Brand) |             |        0.9  |          93 |        42100 |      1827841 |              |      2.40876e+06 | METRO                               |           96 | Belfast LGD          |      105.8   |           42 |                 |           18 |       0      |           58 |        15000 |     4504.97  |         4655 |         89.6 | Arthur Janssens   | LM           |        18200 |   7 | FILE ID                                     | 35-39  | X(5)      |   5 | 12UMD - Manufacturer Reimbursement Detail.                                                                                                                             |  35 |  39 |
| 3           |          70 |     8838.98 |           0 |        4.97 | 18          | Delco 24 SI Alternator, 145 AMP                                                    |             |        0.4  |         214 |        34500 |    219478307 |              |      2.20861e+06 | TRAMVIA                             |           69 | Belfast LGD Deprived |      108.481 |           14 |                 |          208 |       0      |           66 |         1625 |     1334.81  |         7215 |         57.6 | Adiel De Waele    | LM           |       180000 |   8 | LABELER CODE                                | 40-44  | X(5)      |   5 | Labeler Code is the first 5 positions of the NDC.  Format is MMMMM.                                                                                                    |  40 |  44 |
| 5           |          27 |    62202.7  |           0 |        3.25 | 16          | Dual element air cleaner                                                           |             |        0.4  |          93 |        34500 |      2714217 |              |      1.17769e+06 | FGC                                 |           93 | Northern Ireland     |      102.9   |            3 |                 |           74 |       0      |           66 |         1625 |     2669.61  |         1661 |        102.4 | Pieter Maelegheer | LM           |        90000 |   9 | DETAIL RECORD COUNT                         | 45-55  | 9(11)     |  11 | The number of DETMD records for this Labeler.                                                                                                                          |  45 |  55 |
| 3           |          75 |   239974    |           0 |        6.48 |             | Delco 24 SI Alternator, 130 AMP                                                    |             |        0.8  |          93 |        42100 |      1154102 |              | 105459           | RENFE ALTA VELOCITAT (AVE)          |           69 | Northern Ireland     |      100     |            8 |                 |           18 |       0      |           30 |         1625 |     2586.19  |         7215 |        102.4 | Glenn Vlamynck    | LM           |       180000 |  10 | TOTAL REPORTED GAP DISCOUNT PREVIOUS AMOUNT | 56-69  | S9(12)V99 |  14 | The Total Reported Gap Discount amounts that were reported on the most recent invoices related to the upheld disputes.                                                 |  56 |  69 |
| 5           |         237 |   143168    |          30 |        1    | 53          | Oil fill and dipstick EZ access                                                    |             |        0.8  |          40 |        34500 |     58343439 |              |      3.71906e+06 | RENFE ALTA VELOCITAT (AVE)          |           33 | Northern Ireland     |      100.8   |            8 |                 |           12 |       0      |           50 |        15000 |     2586.19  |         6617 |        102.4 | Tom Geldhof       | CLM          |       180000 |  11 | TOTAL REPORTED GAP DISCOUNT CURRENT AMOUNT  | 70-83  | S9(12)V99 |  14 | The Total Gap Discount amounts as of the creation of this Reimbursement Report.                                                                                        |  70 |  83 |
| 5           |          46 |   180529    |          30 |       17.84 |             | Delco 24 SI Alternator, 130 AMP                                                    |             |        0.4  |         207 |        42100 |    219478307 |              | 351416           | RENFE AVANT                         |           96 | Belfast LGD Deprived |      102.9   |            4 | Record Breakers |           74 |     301.064  |           16 |        15000 |     1334.81  |          222 |         57.6 | Arthur Janssens   | CLM          |       180000 |  12 | TOTAL UPHELD DISPUTE REIMBURSEMENT AMOUNT   | 84-97  | S9(12)V99 |  14 | Total net payment amount calculated as the "Total Reported Gap Discount Current Amount" minus the "Total Reported Gap Discount Previous Amount."                       |  84 |  97 |
|             |             |             |             |             |             |                                                                                    |             |             |             |              |              |              |                  |                                     |              |                      |              |              |                 |              |              |              |              |              |              |              |                   |              |              |     |                                             |        |           |     |                                                                                                                                                                        |     |     |
|             |             |             |             |             |             |                                                                                    |             |             |             |              |              |              |                  |                                     |              |                      |              |              |                 |              |              |              |              |              |              |              |                   |              |              |     |                                             |        |           |     | The net payment amount that needs to be paid (reimbursed) by the contracts to the manufacturers.  This will be displayed as a negative amount in the reporting output. |     |     |
|             |          25 |   200379    |           0 |        3.76 | 60          | Dual element air cleaner                                                           |             |        0.95 |          32 |        42100 |    219478307 |              | 194732           | FGC                                 |           45 | Belfast LGD Deprived |      104.973 |           14 |                 |           34 |       0      |            6 |         1625 |     1334.81  |         2317 |        102.4 | Arthur Janssens   | CLM          |        37000 |  13 | FILLER                                      | 98-200 | X(103)    | 103 | Spaces                                                                                                                                                                 |  98 | 200 |



---

## String-Relationship__case_6407

**Task:** String-Relationship

**Input:**

You are given a table below, where some of the columns may be derived from other columns using string-based transformations (e.g., string split, concatenation, formatting, substring extraction, and pattern matching, etc.). 

Your task is to identify string transformation relationships between the columns, by determining if any column, henceforce referred to as a TargetColumn, can be derived from other columns, referred to as SourceColumns, using the string-based transformations. Please only return relationships that are semantically meaningful and truly hold, and do not return any relationships that are spurious. 

No explanation is needed, return all the detected relationships in the following JSON format: 
{
  "String-Relationship": [
    [["SourceColumn1", "SourceColumn2", ...], "TargetColumn"],
    ...
  ]
}

Input Table:
| Foreign_0   | Foreign_1                      |   Foreign_2 |   Foreign_3 |   Foreign_4 |   Foreign_5 |   Foreign_6 | Foreign_7            | Foreign_8                       |       Foreign_9 | Foreign_10                               | Foreign_11   | Foreign_12                                          |   Foreign_13 | Foreign_14             |   Foreign_15 |   Foreign_16 | Foreign_17   |   Foreign_18 |   Foreign_19 |   Foreign_20 |   Foreign_21 |   Foreign_22 | Foreign_23             |   Foreign_24 | Foreign_25   |   Foreign_26 |   Foreign_27 |   Foreign_28 |   Foreign_29 | C   |   D | E   | F   | G   | H   | I   | J   | K     | L     |
|:------------|:-------------------------------|------------:|------------:|------------:|------------:|------------:|:---------------------|:--------------------------------|----------------:|:-----------------------------------------|:-------------|:----------------------------------------------------|-------------:|:-----------------------|-------------:|-------------:|:-------------|-------------:|-------------:|-------------:|-------------:|-------------:|:-----------------------|-------------:|:-------------|-------------:|-------------:|-------------:|-------------:|:----|----:|:----|:----|:----|:----|:----|:----|:------|:------|
|             | Field equipment rental from NP | 1581.38     |        23   |         351 |          75 |       10    | 4DE♦R12M  (4DE♦♦100) | User can add devices on the fly | 212547          | Operations and Maintenance Planning      | OCS-A 0486   | 2.      Feasibility study                           |           10 | Belfast Trust          |     0.569262 |    454219550 | 22           |     132139   |            0 |     629.337  |       167906 |            0 |                        |         2087 |              |            0 |      1.72414 |        64.02 |      81169.3 | a   |   1 | p   |     |     |     |     |     | a1p   | False |
|             | Consumables                    |  307.675    |        14   |           0 |          60 |       18.25 | 4DB♦R20M  (4DB♦♦220) |                                 |      0          | Operational Readiness Review and Go-Live | OCS-A 0521   | 4.      Detailed project design/development         |            4 | Belfast Trust Deprived |     0.741342 |    208043701 | 22           |      96262.8 |           15 |     197.244  |       167906 |            0 |                        |          545 |              |            0 |     77.5862  |       159.88 |      79352.2 | b   |   2 | o   |     |     |     |     |     | b2o   | False |
|             | Field equipment rental from NP |    0.784592 |         8   |           0 |          75 |       28.25 | 4DH♦S16M             |                                 | 918761          | Operations and Maintenance Planning      | OCS-A 0501   | 4.      Detailed project design/development         |           10 | Belfast Trust          |     0.970903 |    454219550 | 26           |      94315.6 |            0 |     345.314  |       167906 |          801 |                        |        12545 |              |            0 |      3.44828 |       139.3  |      77575.7 | c   |   3 | i   |     |     |     |     |     | c3i   | False |
| 0           | Fuel for scooter               |  916.73     |         2.3 |           0 |          45 |       10    | 4DA♦S13M             | to these bottom 5 rows          |      0          | Design Documents - To Be and As Built    | OCS-A 0508   | 2.      Feasibility study                           |            4 | Belfast Trust Deprived |     0.597592 |    176838322 | 23           |      94315.6 |            0 |     389.54   |       167906 |            0 |                        |         1042 |              |            0 |      1.72414 |       237.99 |      74141.2 | d   |   4 | u   |     |     |     |     |     | d4u   | False |
| 0           | Field equipment rental from NP | 1935.81     |        23   |           0 |          75 |       80    | 4DA♦R18M  (4DA♦♦200) |                                 |      4.202e+06  |                                          | OCS-A 0487   | 1.    Energy Masterplanning/Local Area Energy Plans |            7 | Belfast Trust Deprived |     1.14749  |     38705925 | 19           |     107519   |            3 |     652.55   |        90786 |          801 | Variable Interest Rate |         2087 |              |            0 |      1.72414 |       104.06 |      77575.7 | e   |   5 | y   |     |     |     |     |     | e5y   | False |
|             | Consumables                    | 1935.81     |         8   |      163132 |          60 |       80    | 4DK♦F63K  (4DP♦♦150) |                                 |  12324          | Operational Readiness Review and Go-Live | OCS-A 0498   | 4.      Detailed project design/development         |            3 | Belfast Trust Deprived |     0.652132 |   1113209462 | 21           |      98209.2 |            7 |     143.294  |        90786 |            0 |                        |          545 |              |            0 |      1.72414 |        73.9  |      79352.2 | f   |   6 | t   |     |     |     |     |     | f6t   | False |
|             | Fuel for scooter               | 1935.81     |        23   |         351 |           0 |       16.25 | 4DJ♦R19M  (4DJ♦♦200) |                                 | 498710          | Operational Readiness Review and Go-Live | OCS-A 0487   | 1.    Energy Masterplanning/Local Area Energy Plans |           10 | Belfast Trust Deprived |     0.966372 |    454219550 |              |     132139   |            0 |      84.1375 |       167906 |         1223 |                        |         1042 | 79900        |            0 |     17.2414  |       213.45 |      74141.2 | g   |   7 | r   |     |     |     |     |     | g7r   | False |
|             | Accomodation Longyearbyen      |  605.544    |         2.3 |         220 |          45 |       18.25 | 4DR♦F76K  (4DS♦♦220) |                                 |      8.6326e+07 | Operational Readiness Checklist          | OCS-A 0486   | 3.      Business planning                           |            9 | Belfast Trust          |     0.686368 |     38705925 | 25           |     102759   |            0 |     652.55   |       167906 |            0 | Variable Interest Rate |        12545 | 22115000     |            0 |     17.2414  |       111.47 |      79352.2 | h   |   8 | e   |     |     |     |     |     | h8e   | False |
|             | Food in field                  | 3093.61     |         8   |        2933 |          60 |      116    | 4DR♦F76K  (4DS♦♦220) |                                 |      3.73e+07   | Design Documents - To Be and As Built    | OCS-A 0490   | 1.    Energy Masterplanning/Local Area Energy Plans |            2 | Belfast Trust          |     0.622765 |    729194525 | 20           |     112500   |            0 |     949.566  |       167906 |            0 |                        |         1042 |              |            0 |      1.72414 |       106.53 |      72481.3 | i   |   9 | s   |     |     |     |     |     | i9s   | False |
|             | Fuel for scooter               | 2305.64     |         8   |           0 |          75 |       28.25 | 4DE♦R18M  (4DE♦♦200) |                                 |  73516.6        | Plans                                    | OCS-A 499    | 1.    Energy Masterplanning/Local Area Energy Plans |            7 | Belfast Trust Deprived |     0.970903 |   1102883778 | 24           |      96262.8 |            7 |     566.534  |       167906 |          801 |                        |          897 | 22115000     |            0 |     17.2414  |       100.6  |      69272.3 | j   |  10 | w   |     |     |     |     |     | j10w  | False |
|             | Flights                        | 2691.39     |        14   |           0 |          45 |      116    | 4DB♦F54K             |                                 | 211568          |                                          | OCS-A 0483   | 1.    Energy Masterplanning/Local Area Energy Plans |            4 | Belfast Trust Deprived |     0.674627 |    454219550 | 21           |      96262.8 |            3 |     566.534  |        90786 |            0 | Variable Interest Rate |          545 |              |            0 |     17.2414  |       142.12 |      72481.3 | w   |  13 | w   |     |     |     |     |     | w13w  | True  |
|             | Consumables                    | 2691.39     |         2.3 |           0 |          10 |       40    | 4DJ♦R28M  (4DJ♦♦270) |                                 |      3.73e+07   |                                          | OCS-A 0500   | 4.      Detailed project design/development         |            9 | Belfast Trust          |     0.569262 |    176838322 | 23           |     102759   |            0 |     106.513  |        90786 |            0 |                        |         1042 | 79900        |           26 |     17.2414  |       164.36 |      77575.7 | w   |  13 | w   |     |     |     |     |     | w13w  | True  |
|             | Food in field                  | 1241.85     |        23   |           0 |          45 |      116    | 4DK♦R16M  (4DK♦♦150) |                                 |  37000          | Operational Readiness Checklist          | OCS-A 0501   | 6.      Commercialisation support                   |            8 | Belfast Trust Deprived |     0.686368 |    176838322 | 26           |     102759   |            0 |     265.248  |       167906 |            0 | Variable Interest Rate |         2087 |              |            0 |     77.5862  |       111.47 |      75839   | w   |  13 | w   | q   |     |     |     |     | w13wq | False |



---

## String-Relationship__case_8004

**Task:** String-Relationship

**Input:**

You are given a table below, where some of the columns may be derived from other columns using string-based transformations (e.g., string split, concatenation, formatting, substring extraction, and pattern matching, etc.). 

Your task is to identify string transformation relationships between the columns, by determining if any column, henceforce referred to as a TargetColumn, can be derived from other columns, referred to as SourceColumns, using the string-based transformations. Please only return relationships that are semantically meaningful and truly hold, and do not return any relationships that are spurious. 

No explanation is needed, return all the detected relationships in the following JSON format: 
{
  "String-Relationship": [
    [["SourceColumn1", "SourceColumn2", ...], "TargetColumn"],
    ...
  ]
}

Input Table:
|   Foreign_0 |   Foreign_1 | Foreign_2          | Foreign_3   |   Foreign_4 |   Foreign_5 |   Foreign_6 |   Foreign_7 |        Foreign_8 | Foreign_9    |   Foreign_10 |   Foreign_11 |   Foreign_12 | Foreign_13         |   Foreign_14 | Foreign_15   | Foreign_16        |   Foreign_17 | Foreign_18   | Foreign_19           |   Foreign_20 | Foreign_21   |   Foreign_22 |   Foreign_23 |   Foreign_24 |   Foreign_25 | Foreign_26   | Foreign_27        |   Foreign_28 | Foreign_29   | C   |   D | E   | F   | G   | H   | I   | J   | K     | L     |
|------------:|------------:|:-------------------|:------------|------------:|------------:|------------:|------------:|-----------------:|:-------------|-------------:|-------------:|-------------:|:-------------------|-------------:|:-------------|:------------------|-------------:|:-------------|:---------------------|-------------:|:-------------|-------------:|-------------:|-------------:|-------------:|:-------------|:------------------|-------------:|:-------------|:----|----:|:----|:----|:----|:----|:----|:----|:------|:------|
|         -36 |     6.45002 | 72.426256356728828 |             |      1847.3 |        1    |          93 |     1902.3  |      0           | SITC QINGDAO |        43964 |            1 |      0       | 3781.95158227302   |      68433.1 | DNB          |                   |    0.0355275 | i.           |                      |   0.00257339 | NO0010815376 |      859.677 |          0.5 |        426.8 |            0 | x 13 units = | CHF / …           |            8 | N L          | a   |   1 | p   |     |     |     |     |     | a1p   | False |
|       -1029 |     6.54658 | 27.57307918516873  |             |      2914.9 |        1    |          33 |     1902.3  |   8498.28        | SITC KOBE    |        43978 |            5 |      0       | 3350.6634289128206 |      68433.1 |              |                   |    0.0588357 | ii.          |                      |   0.0249714  | NO0010685704 |      537.097 |          0.6 |        375.5 |            0 | x 13 units = | CHF / …           |            8 | D M          | b   |   2 | o   |     |     |     |     |     | b2o   | False |
|          -1 |     6.45002 | 72.426256356728828 |             |      2648   |        0.5  |         164 |     3957.51 |      0           | SITC DALIAN  |        43964 |            5 |      0       | 788.84294244119576 |      32623.7 |              | Subtotal Salaries |   -0.0198092 | iii.         | Coach and/or Captain |   0.0249714  | NO0010669922 |     1020.97  |          0.8 |        588.1 |            0 | x 93 units = | CHF / …           |            2 | N L          | c   |   3 | i   |     |     |     |     |     | c3i   | False |
|          11 |     6.53622 |                    |             |      1663.8 |        0.5  |          19 |     3957.51 | 460786           | SITC DALIAN  |        43978 |            3 |      0       | 788.84294244119576 |      37802   | WWW 2        |                   |    0.0355275 | ii.          |                      |   0.0249714  | NO0010863178 |     1020.97  |          0   |        295.7 |            0 | x 24 units = | CHF / …           |            7 | M P          | d   |   4 | u   |     |     |     |     |     | d4u   | False |
|       -1029 |     6.53622 | 27.57307918516873  |             |      1560.7 |        1    |          33 |     3957.51 |      0           | SITC QINGDAO |        43964 |            2 |      0       | 1794.1097839978556 |      32623.7 | DNB          |                   |   -0.0198092 | iv.          |                      |   0.00257339 | NO0010732258 |      537.097 |          0.3 |        292.6 |            0 | x 93 units = | CHF / …           |            9 | A B          | e   |   5 | y   |     |     |     |     |     | e5y   | False |
|        -205 |     6.45002 | 72.426256356728828 | 1           |      1548.9 |        1    |          45 |     2226.68 |      0           | SITC DALIAN  |        43964 |            5 |      0       |                    |      68433.1 |              |                   |    0.0343151 | iii.         |                      |   0.0249714  | NO0010815376 |     1020.97  |          0   |        379.3 |          250 | x 0 units =  | CHF / …           |            4 | M P          | f   |   6 | t   |     |     |     |     |     | f6t   | False |
|         -29 |     6.53622 | 72.426256356728828 |             |      2883.9 |        1    |          19 |     1300.89 |      1.20455e+06 | SITC DALIAN  |        43978 |            2 |     34.2967  | 2159.0528212369486 |      37802   | WWW 2        |                   |   -0.0198092 | iii.         |                      |   0.00257339 | NO0010881162 |     1020.97  |          0.6 |        425.1 |            0 | x 93 units = | CHF / …           |            3 | C V          | g   |   7 | r   |     |     |     |     |     | g7r   | False |
|          -1 |     6.54658 |                    |             |      1514.6 |        0.5  |          33 |    13761.8  |      0           | SITC DALIAN  |        43964 |            2 |     34.2967  | 3350.6634289128206 |      32623.7 |              |                   |    0.0343151 | iv.          |                      |   0.0249714  | NO0010687023 |     1020.97  |          0.2 |        317.9 |            0 | x 24 units = | CHF / Concentrato |            2 | A P          | h   |   8 | e   |     |     |     |     |     | h8e   | False |
|       -1029 |     6.53622 | 27.57307918516873  |             |      1501.5 |        0.75 |          45 |    12201    |      1.20455e+06 | SITC KOBE    |        43964 |            4 |      3.79134 | 1566.3711854466101 |      37802   | DNB          |                   |    0.0343151 | iv.          |                      |   0.0249714  | NO0010780687 |     1020.97  |          0.6 |        292.8 |            0 | x 0 units =  | CHF / …           |            2 | N L          | i   |   9 | s   |     |     |     |     |     | i9s   | False |
|        -604 |     6.54658 |                    |             |      2648   |        1    |         164 |     2276    |      0           | SITC DALIAN  |        43964 |            4 |      0       | 4231.2356116483597 |      51651   |              |                   |    0.0588357 | iv.          |                      |   0.0249714  | NO0010763022 |     1020.97  |          0   |        396.4 |            0 | x 0 units =  | CHF / Min         |            2 | T B          | j   |  10 | w   |     |     |     |     |     | j10w  | False |
|          11 |     6.45002 |                    |             |      1547.4 |        1    |          19 |    13761.8  |      0           | SITC QINGDAO |        43964 |            1 |      0       | 50.699869100112743 |      68433.1 |              |                   |    0.0355275 | ii.          |                      |   0.00257339 | NO0010821192 |      859.677 |          0   |        393.1 |            0 | x 93 units = | CHF / …           |            2 | D M          | w   |  13 | w   |     |     |     |     |     | w13w  | True  |
|         -36 |     6.50347 |                    |             |      1511.6 |        1    |          45 |    12201    |  40203.4         | SITC QINGDAO |        43964 |            2 |      3.79134 | 3350.6634289128206 |      51651   |              |                   |    0.0343151 | i.           |                      |   0.0249714  | NO0010794308 |     1020.97  |          0.3 |        318.3 |            0 | x 24 units = | CHF / …           |            9 | T B          | w   |  13 | w   |     |     |     |     |     | w13w  | True  |
|       -1029 |     6.53622 | 72.426256356728828 |             |      2464.9 |        0.5  |          93 |     1902.3  | 414373           | SITC DALIAN  |        43978 |            2 |      0       | 3350.6634289128206 |      51651   |              |                   |   -0.0198092 | ii.          |                      |   0.00257339 | NO0010821192 |      537.097 |          0.7 |        300   |            0 | x 13 units = | CHF / h           |            8 | N L          | w   |  13 | w   | q   |     |     |     |     | w13wq | False |



---

## String-Relationship__case_8802

**Task:** String-Relationship

**Input:**

You are given a table below, where some of the columns may be derived from other columns using string-based transformations (e.g., string split, concatenation, formatting, substring extraction, and pattern matching, etc.). 

Your task is to identify string transformation relationships between the columns, by determining if any column, henceforce referred to as a TargetColumn, can be derived from other columns, referred to as SourceColumns, using the string-based transformations. Please only return relationships that are semantically meaningful and truly hold, and do not return any relationships that are spurious. 

No explanation is needed, return all the detected relationships in the following JSON format: 
{
  "String-Relationship": [
    [["SourceColumn1", "SourceColumn2", ...], "TargetColumn"],
    ...
  ]
}

Input Table:
|   Foreign_0 |   Foreign_1 |   Foreign_2 | Foreign_3   | Foreign_4    | Foreign_5   | Foreign_6                                                                         | Foreign_7   |   Foreign_8 | Foreign_9      | Foreign_10   | Foreign_11   |   Foreign_12 | Foreign_13   |   Foreign_14 |   Foreign_15 |   Foreign_16 | Foreign_17   | Foreign_18   | Foreign_19   | Foreign_20   |   Foreign_21 |   Foreign_22 |   Foreign_23 | Foreign_24   |   Foreign_25 | Foreign_26   |   Foreign_27 | Foreign_28   |   Foreign_29 | Foreign_30   | Foreign_31   | Foreign_32   | Foreign_33   |   Foreign_34 |   Foreign_35 | Foreign_36   |   Foreign_37 | Foreign_38      | Foreign_39   | Foreign_40   |   Foreign_41 | Foreign_42   | Foreign_43   |   Foreign_44 |   Foreign_45 | Foreign_46                | Foreign_47   |   Foreign_48 |   Foreign_49 |   Foreign_50 | Foreign_51   |   Foreign_52 | Foreign_53   |   Foreign_54 | Foreign_55   |   Foreign_56 |   Foreign_57 | Foreign_58         |   Foreign_59 | Foreign_60   |   Foreign_61 |   Foreign_62 | Foreign_63           | Foreign_64   |   Foreign_65 | Foreign_66   |   Foreign_67 | Foreign_68   |   Foreign_69 |   Foreign_70 | Foreign_71   | Foreign_72   |   Foreign_73 | Foreign_74   | Foreign_75            |   Foreign_76 | Foreign_77   | Foreign_78   | Foreign_79   | Foreign_80   |   Foreign_81 |   Foreign_82 | Foreign_83    |   Foreign_84 | Foreign_85   |   Foreign_86 | Foreign_87         |   Foreign_88 | Foreign_89   |   Foreign_90 |   Foreign_91 |   Foreign_92 | Foreign_93   |   Foreign_94 | Foreign_95   | Foreign_96   |   Foreign_97 |   Foreign_98 |   Foreign_99 | A                          | B   |   C |   D | E       | F       | G   |
|------------:|------------:|------------:|:------------|:-------------|:------------|:----------------------------------------------------------------------------------|:------------|------------:|:---------------|:-------------|:-------------|-------------:|:-------------|-------------:|-------------:|-------------:|:-------------|:-------------|:-------------|:-------------|-------------:|-------------:|-------------:|:-------------|-------------:|:-------------|-------------:|:-------------|-------------:|:-------------|:-------------|:-------------|:-------------|-------------:|-------------:|:-------------|-------------:|:----------------|:-------------|:-------------|-------------:|:-------------|:-------------|-------------:|-------------:|:--------------------------|:-------------|-------------:|-------------:|-------------:|:-------------|-------------:|:-------------|-------------:|:-------------|-------------:|-------------:|:-------------------|-------------:|:-------------|-------------:|-------------:|:---------------------|:-------------|-------------:|:-------------|-------------:|:-------------|-------------:|-------------:|:-------------|:-------------|-------------:|:-------------|:----------------------|-------------:|:-------------|:-------------|:-------------|:-------------|-------------:|-------------:|:--------------|-------------:|:-------------|-------------:|:-------------------|-------------:|:-------------|-------------:|-------------:|-------------:|:-------------|-------------:|:-------------|:-------------|-------------:|-------------:|-------------:|:---------------------------|:----|----:|----:|:--------|:--------|:----|
|    14988754 |           0 |     6.33695 | Yes         | MF-2004 Code |             | ESMAI shower set                                                                  | Apr         |        68   | 6005BGB00      | Trasferte    |              |            0 |              |         2023 |         2015 |      46.5522 | #REF!        |              | A8TEXT       | No Change    |        49.6  |     0.81951  |            7 |              |            1 |              |          0.1 |              |            0 |              | #REF!        | 575.77       | Pct 65+      |        44583 |   -0.0427791 |              |            0 | 50              | Nitrogen     |              |            7 | #DIV/0!      |              |            0 |           22 | Web Developer             |              |          2   |            0 |         2041 |              |            0 |              |            0 |              |      43427.8 |        96293 | $35,000 to $49,999 |     0.198743 |              |       905000 |        43010 | T. meses operativos: | Pct Und 18   |         2034 |              |     0.32824  | Wales        |         1000 |    0.0195896 |              |              |      205.052 |              | Total energy consumed |        44505 | 91306-       | HVAC-1a      |              | Friday       |           81 |          510 | Rod McGowan   |     17525.2  |              |        358.7 | -                  |           59 |              |        44226 |            0 |   -0.0333064 | 7            |         8200 |              |              |        52312 |  4.27245e+06 |       69.178 | II: Personal hygiene       | INC |   7 |   7 | INC / 7 | #VALUE! |     |
|    14988754 |          53 |     6.30655 | No          | MF-2004 Code |             | ESMAI external element for in wall bath-shower instalation  RocaBox               | Apr         |        66.7 | *--            | Trasferte    |              |            0 |              |         2024 |         2015 |      46.5522 | #REF!        |              | A8TEXT       | No Change    |         7.86 |     0.967556 |           79 |              |            1 |              |          0.1 |              |            0 | 6            | #REF!        | 487.74       | Pct Und 18   |        44583 |   -0.0427791 |              |            0 |                 | Phosphorus   |              |            5 | #DIV/0!      |              |            0 |           22 | Assoc Dir Acad Advising   |              |         30   |            0 |         2041 |              |            0 |              |            0 |              |      43391.6 |        96293 | $35,000 to $49,999 |     0.462072 |              |       905000 |        43010 | T. meses operativos: | Pct Und 18   |         2030 |              |     0.32824  | N Ireland    |         1000 |    0.0195896 |              | 381          |      240.651 |              | Standard energy       |        44505 | 91306-       | HVAC-1a      |              | Thursday     |           93 |          510 | Don Ainscough |      1433.71 |              |        376.2 | 552.85399990336157 |           34 |              |        44226 |            0 |   -0.315516  |              |         8200 |              |              |        52312 |  4.43218e+06 |      232.136 | III: Bathing / dressing    | INC |   7 |   7 | INC / 7 | #VALUE! |     |
|    14988754 |           0 |     6.33695 | Yes         | MF-2004 Code |             | ESMAI bidet with pop up waste                                                     | Apr         |        81   | 12V-8AH        | Trasferte    |              |            0 |              |         2032 |         2014 |      46.5522 | #REF!        |              | A8TEXT       | No Change    |        17.5  |     0.893148 |           43 |              |            1 |              |          0.1 |              |            0 |              | #REF!        | 605.54       | Pct 65+      |        44583 |   -0.0427791 |              |            0 | 100ea/1BOX      | Nitrogen     |              |            6 | #DIV/0!      |              |            0 |           22 | Professor 9 Mo FT         |              |         12   |            0 |         2041 |              |       340238 |              |            0 |              |      43388.5 |       107072 | $35,000 to $49,999 |     0.307807 |              |       905000 |        43010 | T. meses operativos: | Pct Und 18   |         2033 |              |     0.158364 | UK           |         1000 |    0.0195896 |              |              |      180.671 |              | AUC                   |        44505 | 91306-       | HVAC-1a      |              | Saturday     |            9 |          510 | Simon Mayes   |      2152.79 |              |        370   | 552.85399990336157 |           59 |              |        44226 |            0 |   -0.239243  |              |         8200 |              |              |        52312 |  4.27245e+06 |     1676.21  | IV: Food preparation       | INC |   8 |   8 | INC / 8 | #VALUE! |     |
|    14988754 |           0 |     6.41058 | No          | MF-2004 Code |             | ESMAI Combo Pack: tap washbasin with pop up waste, tap bath- shower, handle 70 cm | Apr         |        65.1 | Wire+Profusion | Trasferte    |              |            0 |              |         2032 |         2015 |      46.5522 | #REF!        |              | A7TEXT       | No Change    |        64.56 |     0.864457 |           31 |              |            1 |              |          0.1 |              |            0 | 6            | #REF!        | 605.54       | Pct Und 18   |        44583 |   -0.0427791 |              |            0 | 10ea/50set/1box | Nitrogen     |              |            7 | #DIV/0!      |              |            0 |           22 | Director Plant Operations |              |          6.3 |            0 |         2041 |              |         5440 |              |            0 |              |      43374.5 |        93703 | $20,000 to $34,999 |     0.359331 |              |       905000 |        43010 | T. meses operativos: | Pct 65+      |         2042 |              |     0.158364 | N Ireland    |         1000 |    0.0832458 |              | 70           |      250.132 |              | NMD/UC kVA            |        44505 | 91306-       | HVAC-1a      |              | Sunday       |           69 |          510 | David Styring |      1026.87 |              |        474.8 | -                  |           59 |              |        44226 |            0 |   -0.315516  | 7            |         8200 |              |              |        52312 |  4.3968e+06  |     1185.97  | V: Shopping                | INC |   5 |   5 | INC / 5 | #VALUE! |     |
|    14988754 |           0 |     6.37502 | No          | MF-2004 Code |             | ESMAI shower set                                                                  | Apr         |        82.2 | S2-MNP         | Trasferte    |              |            0 |              |         2035 |         2015 |      46.5522 | #REF!        |              | A7TEXT       | No Change    |        35    |     0.87046  |           55 |              |            1 |              |          0.1 |              |            0 | 6            | #REF!        |              | Pct 65+      |        44583 |   -0.0427791 |              |            0 | 50              | Limestone    |              |           14 | #DIV/0!      |              |            0 |           22 | Administrative Secretary  |              |          5   |            0 |         2041 |              |       340238 |              |            0 |              |      43447.5 |       117222 | $75,000 or more    |     0.394002 |              |       905000 |        43010 | T. meses operativos: | Pct Und 18   |         2035 |              |     0.32824  | Scotland     |         1000 |    0.0195896 |              | 70           |      238.466 |              | Chargeable demand     |        44505 | 91306-       | HVAC-1b      |              | Thursday     |          141 |          510 | Andy Wilford  |      5930.44 |              |        419   | -                  |           34 |              |        44226 |            0 |   -0.315516  |              |         8200 |              |              |        52312 |  4.43218e+06 |       20.89  | VII: Health, safety & meds | INC |   7 |   9 | INC / 9 | #VALUE! |     |



---

## semantic-transform__CountryToThreeLettersISOCode

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source   |
|:---------|
| Bhutan   |
| Anguilla |
| Iceland  |
| Kiribati |
| Japan    |

Eample Output Column:
| target   |
|:---------|
| BTN      |
| AIA      |
| ISL      |
| KIR      |
| JPN      |

Test Input Column:
| source              |
|:--------------------|
| Afghanistan         |
| Albania             |
| Algeria             |
| American Samoa      |
| Andorra             |
| Angola              |
| Antarctica          |
| Antigua and Barbuda |
| Argentina           |
| Armenia             |



---

## semantic-transform__Driver2Champioships

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source             |
|:-------------------|
| Alain Prost        |
| Jim Clark          |
| Alain Prost        |
| Fernando Alonso    |
| Juan Manuel Fangio |

Eample Output Column:
|   target |
|---------:|
|     1989 |
|     1965 |
|     1986 |
|     2006 |
|     1956 |

Test Input Column:
| source             |
|:-------------------|
| Michael Schumacher |
| Juan Manuel Fangio |
| Alain Prost        |
| Sebastian Vettel   |
| Jack Brabham       |
| Jackie Stewart     |
| Niki Lauda         |
| Nelson Piquet      |
| Ayrton Senna       |
| Alberto Ascari     |



---

## semantic-transform__Case26

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source                                |
|:--------------------------------------|
| Amsterdam Airport Schiphol            |
| Shanghai Pudong International Airport |
| Narita International Airport          |
| Melbourne Airport                     |
| Suvarnabhumi Airport                  |

Eample Output Column:
| target   |
|:---------|
| EHAM     |
| ZSPD     |
| RJAA     |
| YMML     |
| VTBS     |

Test Input Column:
| source                                           |
|:-------------------------------------------------|
| Hartsfield-Jackson Atlanta International Airport |
| O'Hare International Airport                     |
| London Heathrow Airport                          |
| Tokyo International Airport                      |
| Paris Charles de Gaulle Airport                  |
| Los Angeles International Airport                |
| Dallas-Fort Worth International Airport          |
| Beijing Capital International Airport            |
| Frankfurt Airport                                |
| Denver International Airport                     |



---

## semantic-transform__bankToCountryDistinct

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source                                   |
|:-----------------------------------------|
| BANCA CRED.COOPER.VICENTINO POJANA MAGG. |
| AS DNB NORD BANKA                        |
| DANSKE BANK A/SLATVIJA BRANCH            |
| OKASAN SECURITIES CO. LTD.               |
| LYXOR ASSET MANAGEMENT                   |

Eample Output Column:
| target   |
|:---------|
| ITALY    |
| LATVIA   |
| LATVIA   |
| JAPAN    |
| FRANCE   |

Test Input Column:
| source                                 |
|:---------------------------------------|
| BANKE MILLIE AFGHAN                    |
| DA AFGHANISTAN BANK                    |
| BRAC AFGHANISTAN BANK                  |
| NATIONAL BANK OF PAKISTAN KABUL BRANCH |
| MAIWAND BANK                           |
| GHAZANFAR BANK                         |
| PASHTANY BANK                          |
| BAKHTAR BANK                           |
| AFGHANISTAN INTERNATIONAL BANK         |
| FIRST MICROFINANCE BANK LTD. THE       |



---

## semantic-transform__SymbolToCompanyName

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source   |
|:---------|
| MSFT     |
| GOOGL    |
| GM       |
| AMZN     |
| AAPL     |

Eample Output Column:
| target                 |
|:-----------------------|
| Microsoft Corporation  |
| Google Inc             |
| General Motors Company |
| Amazon.com Inc.        |
| Apple Inc              |

Test Input Column:
| source   |
|:---------|
| IBM      |
| BAC      |
| GE       |
| CMCSA    |
| SAP      |



---

## semantic-transform__TeamToManager

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source                 |
|:-----------------------|
| Dallas Mavericks       |
| Golden State Warriors  |
| Sacramento Kings       |
| Minnesota Timberwolves |
| San Antonio Spurs      |

Eample Output Column:
| target        |
|:--------------|
| Donnie Nelson |
| Bob Myers     |
| Geoff Petrie  |
| David Kahn    |
| R.C. Buford   |

Test Input Column:
| source             |
|:-------------------|
| Boston Celtics     |
| Los Angeles Lakers |
| Memphis Grizzlies  |
| Houston Rockets    |
| Chicago Bulls      |
| Detroit Pistons    |



---

## semantic-transform__GregorianToHijri

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source   |
|:---------|
| 4/20/13  |
| 4/1/15   |
| 5/8/15   |
| 1/1/15   |
| 8/8/15   |

Eample Output Column:
| target     |
|:-----------|
| 06/09/1434 |
| 06/11/1436 |
| 07/19/1436 |
| 03/10/1436 |
| 10/01/1434 |

Test Input Column:
| source   |
|:---------|
| 6/1/15   |
| 12/1/15  |
| 12/8/15  |
| 8/8/15   |
| 11/20/11 |



---

## semantic-transform__shoesizeUSEUR

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

|   source |
|---------:|
|     10.5 |
|     11.5 |
|      6   |
|     12.5 |
|      8.5 |

Eample Output Column:
|   target |
|---------:|
|     44   |
|     45   |
|     38   |
|     46.5 |
|     41   |

Test Input Column:
|   source |
|---------:|
|      6.5 |
|      7   |
|      7.5 |
|      8   |
|      9   |
|      9.5 |
|     10   |
|     11   |
|     12   |
|     13   |



---

## semantic-transform__CountryToCurrencies

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source           |
|:-----------------|
| Germany          |
| Marshall Islands |
| Bangladesh       |
| Peru             |
| Saudi Arabia     |

Eample Output Column:
| target               |
|:---------------------|
| Euro                 |
| United States dollar |
| Bangladeshi taka     |
| Peruvian nuevo sol   |
| Saudi riyal          |

Test Input Column:
| source                |
|:----------------------|
| Afghanistan           |
| Akrotiri and Dhekelia |
| Albania               |
| Algeria               |
| Andorra               |
| Angola                |
| Anguilla              |
| Antigua and Barbuda   |
| Argentina             |
| Armenia               |



---

## semantic-transform__Case50

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source         |
|:---------------|
| Sam Bradford   |
| Earl Campbell  |
| Carson Palmer  |
| Jameis Winston |
| Gary Beban     |

Eample Output Column:
| target              |
|:--------------------|
| Oklahoma            |
| Texas               |
| Southern California |
| Florida State       |
| UCLA                |

Test Input Column:
| source             |
|:-------------------|
| Robert Griffin III |
| Cameron Newton     |
| Mark Ingram        |
| Tim Tebow          |
| Troy Smith         |
| Reggie Bush        |
| Matt Leinart       |
| Jason White        |
| Eric Crouch        |
| Chris Weinke       |



---

## semantic-transform__Case34

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source                                     |
|:-------------------------------------------|
| BMW                                        |
| Hunan Jiangnan Automobile Manufacturing Co |
| JAC                                        |
| Xiamen King Long                           |
| Dongfeng Motor                             |

Eample Output Column:
| target   |
|:---------|
| Germany  |
| China    |
| China    |
| China    |
| China    |

Test Input Column:
| source     |
|:-----------|
| Toyota     |
| GM         |
| Volkswagen |
| Hyundai    |
| Ford       |
| Nissan     |
| Honda      |
| PSA        |
| Suzuki     |
| Renault    |



---

## semantic-transform__ISSNToTitle

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source    |
|:----------|
| 0036-8075 |
| 0824-3298 |
| 0976-2280 |
| 1066-8888 |
| 0362-5915 |

Eample Output Column:
| target                                             |
|:---------------------------------------------------|
| Science Magazine                                   |
| Man and Nature                                     |
| International journal of Web & Semantic Technology |
| The VLDB Journal                                   |
| TODS                                               |

Test Input Column:
| source    |
|:----------|
| 1806-2636 |
| 2326-5744 |
| 0893-6080 |
| 1350-1917 |
| 2320-2890 |



---

## semantic-transform__AsciiToUnicode

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source   |
|:---------|
| {        |
| (        |
| 2        |
| #        |
| +        |

Eample Output Column:
|   target |
|---------:|
|      123 |
|       40 |
|       50 |
|       35 |
|       43 |

Test Input Column:
| source   |
|:---------|
| 3        |
| C        |
| L        |
| x        |



---

## semantic-transform__AirportcodeToCity

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source   |
|:---------|
| pei      |
| cle      |
| crv      |
| rez      |
| rgl      |

Eample Output Column:
| target       |
|:-------------|
| pereira      |
| cleveland    |
| crotone      |
| resende rj   |
| rio gallegos |

Test Input Column:
| source   |
|:---------|
| het      |
| ctg      |
| gbe      |
| boi      |
| kif      |
| lci      |
| esf      |
| aex      |
| jej      |
| lle      |



---

## semantic-transform__RGBToColor

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source      |
|:------------|
| 47;79;47    |
| 211;211;211 |
| 240;255;255 |
| 84;84;84    |
| 165;42;42   |

Eample Output Column:
| target     |
|:-----------|
| Dark Green |
| LightGrey  |
| Azure      |
| Grey       |
| Brown      |

Test Input Column:
| source      |
|:------------|
| 255;255;255 |
| 138;43;226  |
| 173;216;230 |
| 0;255;255   |
| 255;165;0   |



---

## semantic-transform__ISBNToTitle

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source            |
|:------------------|
| 978-0451476807    |
| 1501260049        |
| 9.78055E+12       |
| 0-553-10354-7     |
| 978-3-642-29575-1 |

Eample Output Column:
| target                    |
|:--------------------------|
| Eye of the needle         |
| The innovator's dilemma   |
| The google Story          |
| A Game of thrones         |
| In-Memory Data Management |

Test Input Column:
| source            |
|:------------------|
| 0-688-03036-X     |
| 978-0374275631    |
| 033036426X        |
| 978-1-118-12938-8 |
| 978-0312427986    |



---

## semantic-transform__BankToCity

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source                                                 |
|:-------------------------------------------------------|
| PHAROS SECURITIES                                      |
| GDF SUEZ                                               |
| BANK OF ALEXANDRIA S A E                               |
| BELTONE SECURITIES BROKERAGE S.A.E                     |
| PRINCIPAL BANK FOR DEVELOPMENT AND AGRICULTURAL CREDIT |

Eample Output Column:
| target   |
|:---------|
| CAIRO    |
| PARIS    |
| CAIRO    |
| CAIRO    |
| CAIRO    |

Test Input Column:
| source                                                   |
|:---------------------------------------------------------|
| COMMERCIAL BANK -LANTA-BANK'                             |
| GENERAL ELECTRIC COMPANY                                 |
| THE 77 BANKLTD.                                          |
| MIZUHO CORPORATE BANK LTD. PARIS BRANCH                  |
| LA BANQUE POSTALE                                        |
| BANQUE D'ESCOMPTE                                        |
| ALWATANY BANK OF EGYPT                                   |
| NATIONAL BANK OF KUWAIT (INTERNATIONAL) PLC PARIS BRANCH |
| GALLIARD CAPITAL MANAGEMENT INC                          |
| SUEZ CANAL BANK                                          |



---

## semantic-transform__Case27

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source                                  |
|:----------------------------------------|
| Mario Tennis Open                       |
| Dragon Warrior VII                      |
| Super Mario 3D Land                     |
| Luigi's Mansion: Dark Moon              |
| The Legend of Zelda: Ocarina of Time 3D |

Eample Output Column:
| target      |
|:------------|
| Nintendo    |
| Square Enix |
| Nintendo    |
| Nintendo    |
| Nintendo    |

Test Input Column:
| source                              |
|:------------------------------------|
| Mario Kart 7                        |
| New Super Mario Bros. 2             |
| Animal Crossing: New Leaf           |
| Nintendogs + Cats                   |
| Paper Mario: Sticker Star           |
| Monster Hunter 3 Ultimate           |
| Kid Icarus: Uprising                |
| Super Street Fighter IV: 3D Edition |



---

## semantic-transform__Case42

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source     |
|:-----------|
| Iran       |
| Maldives   |
| England    |
| Malaysia   |
| Bangladesh |

Eample Output Column:
| target           |
|:-----------------|
| Tulip            |
| Pink Rose        |
| Tudor rose       |
| Chinese hibiscus |
| Shapla           |

Test Input Column:
| source      |
|:------------|
| Nepal       |
| Sikkim      |
| Sri Lanka   |
| Afghanistan |
| Bhutan      |
| China       |
| India       |
| Kashmir     |
| Singapore   |



---

## semantic-transform__Case25

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source                                |
|:--------------------------------------|
| Amsterdam Airport Schiphol            |
| Shanghai Pudong International Airport |
| Narita International Airport          |
| Melbourne Airport                     |
| Suvarnabhumi Airport                  |

Eample Output Column:
| target   |
|:---------|
| AMS      |
| PVG      |
| NRT      |
| MEL      |
| BKK      |

Test Input Column:
| source                                           |
|:-------------------------------------------------|
| Hartsfield-Jackson Atlanta International Airport |
| O'Hare International Airport                     |
| London Heathrow Airport                          |
| Tokyo International Airport                      |
| Paris Charles de Gaulle Airport                  |
| Los Angeles International Airport                |
| Dallas-Fort Worth International Airport          |
| Beijing Capital International Airport            |
| Frankfurt Airport                                |
| Denver International Airport                     |



---

## semantic-transform__Case40

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source        |
|:--------------|
| Winston–Salem |
| Richmond      |
| Minneapolis   |
| Mesquite      |
| Vancouver     |

Eample Output Column:
| target         |
|:---------------|
| North Carolina |
| California     |
| Minnesota      |
| Texas          |
| Washington     |

Test Input Column:
| source       |
|:-------------|
| New York     |
| Los Angeles  |
| Chicago      |
| Houston      |
| Philadelphia |
| Phoenix      |
| San Antonio  |
| San Diego    |
| Dallas       |
| San Jose     |



---

## semantic-transform__MountainsOver7k2Range

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source           |
|:-----------------|
| Gangkhar Puensum |
| Makalu           |
| Mamostong Kangri |
| Changtse         |
| Gasherbrum I     |

Eample Output Column:
| target    |
|:----------|
| Himalayas |
| Himalayas |
| Karakoram |
| Himalayas |
| Karakoram |

Test Input Column:
| source        |
|:--------------|
| Mount Everest |
| K2            |
| Kangchenjunga |
| Lhotse        |
| Cho Oyu       |
| Dhaulagiri    |
| Manaslu       |
| Nanga Parbat  |
| Annapurna     |
| Broad Peak    |



---

## semantic-transform__ElementToSymbol

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source   |
|:---------|
| Ra       |
| Be       |
| Ar       |
| Rn       |
| Ni       |

Eample Output Column:
| target    |
|:----------|
| Radium    |
| Beryllium |
| Argon     |
| Radon     |
| Nickel    |

Test Input Column:
| source   |
|:---------|
| Ac       |
| Ag       |
| Al       |
| Am       |
| As       |
| At       |
| Au       |
| B        |
| Ba       |
| Bh       |



---

## semantic-transform__ZipToCity

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

|   source |
|---------:|
|    61743 |
|    39737 |
|    61933 |
|    96112 |
|    68058 |

Eample Output Column:
| target        |
|:--------------|
| GRAYMONT      |
| BELLEFONTAINE |
| Kansas        |
| Fort Bidwell  |
| SOUTH BEND    |

Test Input Column:
|   source |
|---------:|
|    90638 |
|    10997 |
|    90639 |
|    10998 |
|    22526 |
|     2108 |
|    90637 |
|     2109 |
|    10990 |
|    10992 |



---

## semantic-transform__WorldRecordToAthlete

**Task:** semantic-transform

**Input:**

Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source        |
|:--------------|
| Kenya         |
| Kenya         |
| Ethiopia      |
| Jamaica       |
| United States |

Eample Output Column:
| target          |
|:----------------|
| Silas Kiplagat  |
| William Yiampoy |
| Abera Kuma      |
| Yohan Blake     |
| Ben Blankenship |

Test Input Column:
| source        |
|:--------------|
| United States |
| United States |
| Kenya         |
| United States |
| Mexico        |
| United States |
| United States |
| United States |
| Kenya         |
| Kenya         |



---

