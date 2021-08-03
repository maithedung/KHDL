import requests
from bs4 import BeautifulSoup
import pandas as pd
import random


def crawl_sentence():
    url = 'https://sentence.yourdictionary.com/'

    word_search = input('Enter word search: ')

    source_code = requests.get(url + word_search).text
    soup = BeautifulSoup(source_code, 'html.parser')

    content_list = []

    for each_text in soup.findAll('span', {'class': 'sentence-item__text'}):
        content = each_text.text
        content_list.append(content)

    # Create a Pandas dataframe from the data.
    df = pd.DataFrame({'Data': content_list})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(
        f'./Data/{word_search}.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name=f'{word_search}')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()

    print(f'Crawled {len(content_list)} sentences!')


crawl_sentence()
