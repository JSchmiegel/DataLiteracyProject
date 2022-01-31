from xmlrpc.client import boolean
import pandas as pd

import json
from pathlib import Path

def get_data(pre:boolean) -> pd.DataFrame:
    if pre:
        data_path = 'data/data_pre'
    else:
        data_path = 'data'
    
    pathlist = Path(data_path).glob('**/*.json')
    df_slices = []

    for path in pathlist:
        data = json.load(open(path))
        df_slices.append(pd.DataFrame(data['playlists']))

    df = pd.concat(df_slices, ignore_index=True)
    return df