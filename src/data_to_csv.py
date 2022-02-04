import numpy as np
import pandas as pd
from src.get_data import get_data

def playlist_level(df):
    df = df.drop(columns=['tracks'])
    df = df.sort_values(by=['pid'])
    df = df.reset_index().drop(columns=['index'])
    return df

def track_level(df):
    df = df.drop(columns=['name','collaborative', 'modified_at', 'num_tracks', 'num_albums',
                          'num_followers', 'num_edits', 'duration_ms', 'num_artists', 'description'])
    df['tracks'] = df['tracks'].apply(lambda x: pd.DataFrame(x))
    
    tracks_list = []
    playlist_ids = []
    
    for _, row in df.iterrows():
        sub_df = row['tracks']
        tracks_num = len(sub_df)
        tracks_list.append(sub_df)
        playlist_ids.append(np.repeat(row['pid'], tracks_num))
    
    df = pd.concat(tracks_list)
    df['pid'] = np.concatenate(playlist_ids).flatten()
    df = df.sort_values(by=['pid', 'pos'])
    df = df.reset_index().drop(columns=['index'])
    return df

def data_to_csv(track: bool) -> str:
    df = get_data(pre=True)
    size = f'{int(df.shape[0]/1000)}k'
    print()
    if track:
        track_df = track_level(df)
        track_df.to_csv(f'data/csv_data/track_df_{size}.csv')
    else:
        playlist_df = playlist_level(df)
        playlist_df.to_csv(f'data/csv_data/playlist_df_{size}.csv')
    return size