from xmlrpc.client import boolean
import numpy as np
import pandas as pd

import json
from pathlib import Path

def get_data(pre:boolean) -> pd.DataFrame:
    if pre:
        data_path = 'data/data_pre'
    else:
        data_path = 'data'
    
    pathlist = Path(data_path).glob('**/*.json')
    df_sclices = []

    for path in pathlist:
        data = json.load(open(path))
        df_sclices.append(pd.DataFrame(data['playlists']))

    df = pd.concat(df_sclices, ignore_index=True)
    return df