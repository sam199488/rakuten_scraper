# rakuten_scraper

An API that enables extracting information concerning the
items that are sold on [Rakuten](http://rakuten.co.jp).

![Python-Version](https://img.shields.io/badge/Python-3.6.1-blue.svg)

## Setup
1. Install python3 from https://www.python.org/downloads/


1. Install dependancies:

    ```Python
    pip install -r requirements.txt
    ```

1. Start the server:

    ```Python
    python main.py
    ```
##  Usage
you can use the API by using HTTP GET requests : 
```
http://127.0.0.1:5000/items?nb=3&q=luxury
```
there are 2 GET parameters 
  1.  nb :
        the number of search pages
  1.  q :
        the title of the item
      
    
