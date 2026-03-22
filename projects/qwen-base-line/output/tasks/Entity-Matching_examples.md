# Entity-Matching: All Questions (9 total)

**Model:** Qwen2.5-7B-Instruct

---

## Question 1: test_29 (Fodors-Zagats)

**Dataset:** Fodors-Zagats  
**Test case:** test_29  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
You are given two data records from two datasets that may refer to the same real-world entity. Each record consists of multiple attributes, such as name, address, and other identifying details. Your goal is to determine whether pairs of records refer to the same entity (match) or different entities (non-match).

No explanation and return the final answer as a JSON object, {"label": "<LABEL>"}, where "<LABEL>" is either "match" or "non-match".

Entity A:
| name              | addr                       | city          | phone         | type                  |   class |
|:------------------|:---------------------------|:--------------|:--------------|:----------------------|--------:|
| ` the bacchanal ' | ' 3570 las vegas blvd. s ' | ` las vegas ' | 702/731 -7525 | ` only in las vegas ' |     449 |

Entity B:
| name                           | addr                        | city          | phone        | type        |   class |
|:-------------------------------|:----------------------------|:--------------|:-------------|:------------|--------:|
| ` michael \ 's ( las vegas ) ' | ' 3595 las vegas blvd. s. ' | ` las vegas ' | 702-737-7111 | continental |     664 |


````

### Model Response

```
{"label": "non-match"}
```

### Correct Answer

```
{"label": "non-match"}  (label=0)
```


---

## Question 2: test_400 (DBLP-ACM)

**Dataset:** DBLP-ACM  
**Test case:** test_400  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
You are given two data records from two datasets that may refer to the same real-world entity. Each record consists of multiple attributes, such as name, address, and other identifying details. Your goal is to determine whether pairs of records refer to the same entity (match) or different entities (non-match).

No explanation and return the final answer as a JSON object, {"label": "<LABEL>"}, where "<LABEL>" is either "match" or "non-match".

Entity A:
| title                                | authors                                           | venue             |   year |
|:-------------------------------------|:--------------------------------------------------|:------------------|-------:|
| vqbd : exploring semistructured data | jihwang yeo , sudarshan s. chawathe , thomas baby | sigmod conference |   2001 |

Entity B:
| title                                                       | authors                                                                      | venue             |   year |
|:------------------------------------------------------------|:-----------------------------------------------------------------------------|:------------------|-------:|
| lore : a database management system for semistructured data | jason mchugh , serge abiteboul , roy goldman , dallas quass , jennifer widom | acm sigmod record |   1997 |


````

### Model Response

```
{"label": "non-match"}
```

### Correct Answer

```
{"label": "non-match"}  (label=0)
```


---

## Question 3: test_435 (DBLP-Scholar)

**Dataset:** DBLP-Scholar  
**Test case:** test_435  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
You are given two data records from two datasets that may refer to the same real-world entity. Each record consists of multiple attributes, such as name, address, and other identifying details. Your goal is to determine whether pairs of records refer to the same entity (match) or different entities (non-match).

No explanation and return the final answer as a JSON object, {"label": "<LABEL>"}, where "<LABEL>" is either "match" or "non-match".

Entity A:
| title                                                                                                         | authors                                                  | venue         |   year |
|:--------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------|:--------------|-------:|
| research activities in database management and information retrieval at the university of illinois at chicago | i cruz , a khokhar , b liu , a sistla , o wolfson , c yu | sigmod record |   2002 |

Entity B:
| title                                                               | authors                                               | venue           |   year |
|:--------------------------------------------------------------------|:------------------------------------------------------|:----------------|-------:|
| database research at the university of illinois at urbana-champaign | m winslett , kcc chang , ah doan , j han , c zhai , y | sigmod record , |   2002 |


````

### Model Response

```
{"label": "non-match"}
```

### Correct Answer

```
{"label": "non-match"}  (label=0)
```


---

## Question 4: test_573 (DBLP-Scholar)

**Dataset:** DBLP-Scholar  
**Test case:** test_573  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
You are given two data records from two datasets that may refer to the same real-world entity. Each record consists of multiple attributes, such as name, address, and other identifying details. Your goal is to determine whether pairs of records refer to the same entity (match) or different entities (non-match).

No explanation and return the final answer as a JSON object, {"label": "<LABEL>"}, where "<LABEL>" is either "match" or "non-match".

Entity A:
| title                                            | authors                                       | venue   |   year |
|:-------------------------------------------------|:----------------------------------------------|:--------|-------:|
| scalable techniques for mining causal structures | c silverstein , s brin , r motwani , j ullman | vldb    |   1998 |

Entity B:
| title                                                                 | authors   | venue   | year   |
|:----------------------------------------------------------------------|:----------|:--------|:-------|
| scalable distributed data structures : a survey of current techniques | d beck    |         |        |


````

### Model Response

```
{"label": "non-match"}
```

### Correct Answer

```
{"label": "non-match"}  (label=0)
```


---

## Question 5: test_920 (Walmart-Amazon)

**Dataset:** Walmart-Amazon  
**Test case:** test_920  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
You are given two data records from two datasets that may refer to the same real-world entity. Each record consists of multiple attributes, such as name, address, and other identifying details. Your goal is to determine whether pairs of records refer to the same entity (match) or different entities (non-match).

No explanation and return the final answer as a JSON object, {"label": "<LABEL>"}, where "<LABEL>" is either "match" or "non-match".

Entity A:
| title                                               | category   | brand     | modelno   |   price |
|:----------------------------------------------------|:-----------|:----------|:----------|--------:|
| gear head 2.4 ghz wireless optical nano mouse black | mice       | gear head | mp2800blk |   15.82 |

Entity B:
| title                                        | category   | brand   | modelno   |   price |
|:---------------------------------------------|:-----------|:--------|:----------|--------:|
| kingwin 2.4 ghz wireless optical mouse kw-06 | mice       | kingwin | kw-06     |    9.99 |


````

### Model Response

```
{"label": "non-match"}
```

### Correct Answer

```
{"label": "non-match"}  (label=0)
```


---

## Question 6: test_39 (Fodors-Zagats)

**Dataset:** Fodors-Zagats  
**Test case:** test_39  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
You are given two data records from two datasets that may refer to the same real-world entity. Each record consists of multiple attributes, such as name, address, and other identifying details. Your goal is to determine whether pairs of records refer to the same entity (match) or different entities (non-match).

No explanation and return the final answer as a JSON object, {"label": "<LABEL>"}, where "<LABEL>" is either "match" or "non-match".

Entity A:
| name        | addr                   | city    | phone         | type        |   class |
|:------------|:-----------------------|:--------|:--------------|:------------|--------:|
| ` luna si ' | ' 1931 peachtree rd. ' | atlanta | 404/355 -5993 | continental |     405 |

Entity B:
| name                              | addr                  | city    | phone        | type                 |   class |
|:----------------------------------|:----------------------|:--------|:-------------|:---------------------|--------:|
| ` ritz-carlton cafe ( atlanta ) ' | ' 181 peachtree st. ' | atlanta | 404-659-0400 | ` american ( new ) ' |     711 |


````

### Model Response

```
{"label": "non-match"}
```

### Correct Answer

```
{"label": "non-match"}  (label=0)
```


---

## Question 7: test_288 (DBLP-Scholar)

**Dataset:** DBLP-Scholar  
**Test case:** test_288  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
You are given two data records from two datasets that may refer to the same real-world entity. Each record consists of multiple attributes, such as name, address, and other identifying details. Your goal is to determine whether pairs of records refer to the same entity (match) or different entities (non-match).

No explanation and return the final answer as a JSON object, {"label": "<LABEL>"}, where "<LABEL>" is either "match" or "non-match".

Entity A:
| title                                             | authors                                   | venue         |   year |
|:--------------------------------------------------|:------------------------------------------|:--------------|-------:|
| implementation aspects of an object-oriented dbms | a dogac , m altinel , c ozkan , i durusoy | sigmod record |   1995 |

Entity B:
| title                              | authors       | venue   |   year |
|:-----------------------------------|:--------------|:--------|-------:|
| improving object-oriented analysis | g eckertâ ? ¦ |         |   1994 |


````

### Model Response

```
{"label": "non-match"}
```

### Correct Answer

```
{"label": "non-match"}  (label=0)
```


---

## Question 8: test_202 (Walmart-Amazon)

**Dataset:** Walmart-Amazon  
**Test case:** test_202  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
You are given two data records from two datasets that may refer to the same real-world entity. Each record consists of multiple attributes, such as name, address, and other identifying details. Your goal is to determine whether pairs of records refer to the same entity (match) or different entities (non-match).

No explanation and return the final answer as a JSON object, {"label": "<LABEL>"}, where "<LABEL>" is either "match" or "non-match".

Entity A:
| title                       | category   | brand    |   modelno |   price |
|:----------------------------|:-----------|:---------|----------:|--------:|
| logitech corded mouse black | mice       | logitech | 910001830 |   17.82 |

Entity B:
| title                           | category   | brand    | modelno    |   price |
|:--------------------------------|:-----------|:---------|:-----------|--------:|
| logitech corded mouse m125 blue | mice       | logitech | 910-001831 |   11.48 |


````

### Model Response

```
{"label": "non-match"}
```

### Correct Answer

```
{"label": "non-match"}  (label=0)
```


---

## Question 9: test_469 (DBLP-Scholar)

**Dataset:** DBLP-Scholar  
**Test case:** test_469  
**Version:** 1.0_sample1000_markdown  

### Prompt

````
You are given two data records from two datasets that may refer to the same real-world entity. Each record consists of multiple attributes, such as name, address, and other identifying details. Your goal is to determine whether pairs of records refer to the same entity (match) or different entities (non-match).

No explanation and return the final answer as a JSON object, {"label": "<LABEL>"}, where "<LABEL>" is either "match" or "non-match".

Entity A:
| title                                                                  | authors               | venue                       |   year |
|:-----------------------------------------------------------------------|:----------------------|:----------------------------|-------:|
| searching in metric spaces with user-defined and approximate distances | p ciaccia , m patella | acm trans . database syst . |   2002 |

Entity B:
| title                                        | authors   | venue   |   year |
|:---------------------------------------------|:----------|:--------|-------:|
| truth and approximate truth in metric spaces | ce ortiz  |         |   1997 |


````

### Model Response

```
{"label": "non-match"}
```

### Correct Answer

```
{"label": "non-match"}  (label=0)
```

