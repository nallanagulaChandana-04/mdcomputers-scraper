# MDComputers Product Information Extractor

## Project Description

This project is a Python-based web scraping application that extracts
product information from the MDComputers website based on a search term
provided by the user.

The application extracts:

- Product Name
- Selling Price

The search term is entered dynamically, so the user can search for
different products without changing the source code.

## Technologies Used

- Python
- Selenium
- BeautifulSoup
- Requests
- HTML
- Git
- GitHub

## Features

- Accepts a search term from the user
- Dynamically creates the MDComputers search URL
- Retrieves the search results page
- Parses the webpage
- Extracts product names
- Extracts selling prices
- Displays results in a readable format
- Handles empty search terms
- Handles request/browser errors
- Avoids duplicate products

## Project Structure

```text
mdcomputers-scraper/
│
├── scraper.py
├── requirements.txt
├── README.md
└── .gitignore

