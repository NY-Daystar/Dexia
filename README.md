0. creation du venv
   `python -m venv env`
   `source env/Scripts/activate`

1. Installation de scrapy: `pip install requests beautifulsoup4`

2. Generation du modele: scrapy genspider f1_spider https://f1i.autojournal.fr/calendrier-f1-2023-dates-horaires-grands-prix/#item=1

3. Execution du scrapper : scrapy crawl imdb_spider -o imdb_movies.csv
