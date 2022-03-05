"""
    housinganalysis
    ---------------

    This module contains utilities used in the boston housing market analysis. 

"""

import os 
import requests
import pandas as pd


def pulldata( year, url, path_to_data=None ):
    """Get annual housing price data from html table in url."""

    statusOk = False

    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    
    filename = 'housingData' + year + '.csv' 
    if path_to_data:
        filename = os.path.join(path_to_data, filename)
    df.to_csv( filename )
    print(filename)

    statusOk = True

    return statusOk 