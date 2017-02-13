# Demo Project to use High Chart using Python and Django Application

1. Automatic download data from Yahoo finance excel data (daily at a certain time) for SP500 stocks. For example, download AAPL data from 
http://chart.finance.yahoo.com/table.csv?s=AAPL&a=0&b=13&c=2017&d=1&e=13&f=2017&g=d&ignore=.csv

2. Load data, cleansing data, Plot the interactive chart using Python, Store the data in MySQL

3. Process the data with moving average for user selected duration (for example, 5 days, 3 months, 12 months). Overlap the curves produced with the raw data curve. 

UI can be similar the Finance yahoo's interactive chart, for example:

http://finance.yahoo.com/chart/AAPL#eyJtdWx0aUNvbG9yTGluZSI6ZmFsc2UsImJvbGxpbmdlclVwcGVyQ29sb3IiOiIjZTIwMDgxIiwiYm9sbGluZ2VyTG93ZXJDb2xvciI6IiM5NTUyZmYiLCJtZmlMaW5lQ29sb3IiOiIjNDVlM2ZmIiwibWFjZERpdmVyZ2VuY2VDb2xvciI6IiNmZjdiMTIiLCJtYWNkTWFjZENvbG9yIjoiIzc4N2Q4MiIsIm1hY2RTaWduYWxDb2xvciI6IiMwMDAwMDAiLCJyc2lMaW5lQ29sb3IiOiIjZmZiNzAwIiwic3RvY2hLTGluZUNvbG9yIjoiI2ZmYjcwMCIsInN0b2NoRExpbmVDb2xvciI6IiM0NWUzZmYiLCJyYW5nZSI6IjF5In0%3D

4. Process the data with Bollinger band

5. Add a search bar for users to search which stock to display. The search bar will always stay on top of all the pages.

Add a drop down menu that users can choose which stock to display. 

6. Upload the code to my server and test it.