import pandas as pd

read_file = pd.read_excel (r'C:\Kulon Progo Sentiment Analysis Using KNN\Selenium Instagram\Puncak Saka.xlsx')
read_file.to_csv (r'C:\Kulon Progo Sentiment Analysis Using KNN\Selenium Instagram\comments.csv', index = None, header=True)