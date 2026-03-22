# semantic-transform: All Questions (9 total)

**Model:** Qwen2.5-7B-Instruct

---

## Question 1: ISSNToTitle (DataXFormer)

**Dataset:** DataXFormer  
**Test case:** ISSNToTitle  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
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


````

### Model Response

```
{"output": ["Computer Speech & Language", "Journal of Computer Science and Technology", "Computers & Education", "Journal of Systems and Software", "Neurocomputing"]}
```

### Correct Answer

```
[
  "Acta Scientiarum Animal Sciences",
  "Advances in Chemical Science",
  "Neural Networks",
  "Information Systems Journal",
  "Biomedical Journal"
]
```


---

## Question 2: Case24 (SEMA-join)

**Dataset:** SEMA-join  
**Test case:** Case24  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source       |
|:-------------|
| Kannada      |
| Polish       |
| Byelorussian |
| Faeroese     |
| Mongolian    |

Eample Output Column:
| target   |
|:---------|
| KN       |
| PL       |
| BE       |
| FO       |
| MN       |

Test Input Column:
| source      |
|:------------|
| Abkhazian   |
| Afar        |
| Afrikaans   |
| Albanian    |
| Amharic     |
| Arabic      |
| Armenian    |
| Assamese    |
| Aymara      |
| Azerbaijani |


````

### Model Response

```
{"output": ["AB", "AA", "AF", "AL", "AM", "AR", "AV", "AS", "AY", "AZ"]}
```

### Correct Answer

```
[
  "AB",
  "AA",
  "AF",
  "SQ",
  "AM",
  "AR",
  "HY",
  "AS",
  "AY",
  "AZ"
]
```


---

## Question 3: BankToCity (DataXFormer)

**Dataset:** DataXFormer  
**Test case:** BankToCity  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
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


````

### Model Response

```
{"output": ["CAIRO", "NEW YORK", "CAIRO", "PARIS", "PARIS", "PARIS", "CAIRO", "PARIS", "UNKNOWN", "PARIS"]}
```

### Correct Answer

```
[
  "MOSCOW",
  "STAMFORDCT",
  "SENDAI",
  "PARIS",
  "CHALONS EN CHAMPAGNE",
  "PARIS",
  "EL MANSOURA",
  "PARIS",
  "MINNEAPOLISMN",
  "6TH OF OCTOBER"
]
```


---

## Question 4: Case22 (SEMA-join)

**Dataset:** SEMA-join  
**Test case:** Case22  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
Your task is to perform semantic data transformation on a given column of input values. You will first be shown a pair of example input/output columns, to learn the desired semantic transformations as demonstrated by the input/output columns. Then you will be given a new input column, where the goal is to generate output values corresponding to each value in the new input column, following the same transformation relationship demonstrated in the example input/output columns. 

No explanation is needed, and do not generate code. Simply return your answer in JSON format: {"output": [<output column>]}.

Eample Input Column:

| source                       |
|:-----------------------------|
| Ghost                        |
| Michael Jackson's This Is It |
| The Mummy                    |
| Taxi Driver                  |
| The Deer Hunter              |

Eample Output Column:
| target             |
|:-------------------|
| Paramount Pictures |
| Columbia Pictures  |
| Universal Studios  |
| Columbia Pictures  |
| Universal Studios  |

Test Input Column:
| source                             |
|:-----------------------------------|
| All the King's Men                 |
| To Sir, with Love                  |
| Guess Who's Coming to Dinner       |
| Close Encounters of the Third Kind |
| Ghostbusters                       |
| The Karate Kid                     |
| Spider-Man                         |
| Men in Black                       |
| Bad Boys                           |
| James Bond series                  |


````

### Model Response

```
{"output": ["Paramount Pictures", "Columbia Pictures", "Universal Studios", "Universal Studios", "Columbia Pictures", "Columbia Pictures", "Sony Pictures", "Sony Pictures", "Columbia Pictures", "Metro-Goldwyn-Mayer"]}
```

### Correct Answer

```
[
  "Columbia Pictures",
  "Columbia Pictures",
  "Columbia Pictures",
  "Columbia Pictures",
  "Columbia Pictures",
  "Columbia Pictures",
  "Columbia Pictures",
  "Columbia Pictures",
  "Columbia Pictures",
  "Eon Productions"
]
```


---

## Question 5: ISBNToAuthor (DataXFormer)

**Dataset:** DataXFormer  
**Test case:** ISBNToAuthor  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
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
| target                             |
|:-----------------------------------|
| Ken Follet                         |
| CLAYTON M. CHRISTENSEN             |
| David A. Vise and Mark Malseed     |
| George R. R. Martin                |
| Hasso Plattner and Alexander Zeier |

Test Input Column:
| source            |
|:------------------|
| 0-688-03036-X     |
| 978-0374275631    |
| 033036426X        |
| 978-1-118-12938-8 |
| 978-0312427986    |


````

### Model Response

```
{"output": ["Stephen King", "John Green", "Iain M. Banks", "James Patterson", "Alfred Bester"]}
```

### Correct Answer

```
[
  "John Irving",
  "Daniel Kehlmann",
  "Markus Zusak",
  "Abraham Silberschatz and Peter B. Galvin and Greg Gagne",
  "Mario Vargas Llosa"
]
```


---

## Question 6: CountryToThreeLettersISOCode (DataXFormer)

**Dataset:** DataXFormer  
**Test case:** CountryToThreeLettersISOCode  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
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


````

### Model Response

```
{"output": ["AFG", "ALB", "DZA", "ASM", "AND", "AGO", "ATA", "ATG", "ARG", "ARM"]}
```

### Correct Answer

```
[
  "AFG",
  "ALB",
  "DZA",
  "ASM",
  "AND",
  "AGO",
  "ATA",
  "ATG",
  "ARG",
  "ARM"
]
```


---

## Question 7: Driver2Champioships (DataXFormer)

**Dataset:** DataXFormer  
**Test case:** Driver2Champioships  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
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


````

### Model Response

```
{"output": [1995, 1956, 1989, 2010, 1960, 1968, 1978, 1979, 1988, 1954]}
```

### Correct Answer

```
[
  1994,
  1951,
  1985,
  2010,
  1959,
  1969,
  1975,
  1981,
  1988,
  1952
]
```


---

## Question 8: Case26 (SEMA-join)

**Dataset:** SEMA-join  
**Test case:** Case26  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
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


````

### Model Response

```
{"output": ["KATL", "KORD", "EGKK", "RJAA", "LFPG", "KLAX", "KDFW", "ZBAA", "EDDF", "KDEN"]}
```

### Correct Answer

```
[
  "KATL",
  "KORD",
  "EGLL",
  "RJTT",
  "LFPG",
  "KLAX",
  "KDFW",
  "ZBAA",
  "EDDF",
  "KDEN"
]
```


---

## Question 9: bankToCountryDistinct (DataXFormer)

**Dataset:** DataXFormer  
**Test case:** bankToCountryDistinct  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
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


````

### Model Response

```
{"output": ["AFGHANISTAN", "AFGHANISTAN", "AFGHANISTAN", "PAKISTAN", "AFGHANISTAN", "AFGHANISTAN", "AFGHANISTAN", "AFGHANISTAN", "AFGHANISTAN", "AFGHANISTAN"]}
```

### Correct Answer

```
[
  "AFGHANISTAN",
  "AFGHANISTAN",
  "AFGHANISTAN",
  "AFGHANISTAN",
  "AFGHANISTAN",
  "AFGHANISTAN",
  "AFGHANISTAN",
  "AFGHANISTAN",
  "AFGHANISTAN",
  "AFGHANISTAN"
]
```

