#housinganalysis.py
import requests
import pandas as pd


def pulldata( year, url ):
    """Get annual housing price data from html table in url."""

    statusOk = False

    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    filename = 'housingData' + year + '.csv' 
    df.to_csv( filename )

    print(filename)

    statusOk = True

    return statusOk 