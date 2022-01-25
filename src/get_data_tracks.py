from operator import ge
from xmlrpc.client import boolean
import numpy as np
import pandas as pd

import json
from pathlib import Path
from src.get_data import get_data

def get_data_tracks(pre:boolean) -> pd.DataFrame:
    df = get_data(pre)

    tracks_list = []

    #by Linus
    df['tracks'] = df['tracks'].apply(lambda x: pd.DataFrame(x))

    df.reset_index().drop(columns='index')

    playlist_ids = []
    playlist_names = []
    playlist_tracks_nums = []
    playlist_albums_nums = []
    playlist_followers_nums = []
    playlist_artists_nums = []

    for _, row in df.iterrows():
        tracks_sub_df = row['tracks']
        tracks_list.append(tracks_sub_df)
        
        tracks_num = len(tracks_sub_df)
        playlist_ids.append(np.repeat(row['pid'], tracks_num))
        playlist_names.append(np.repeat(row['name'], tracks_num))
        playlist_tracks_nums.append(np.repeat(row['num_tracks'], tracks_num))
        playlist_albums_nums.append(np.repeat(row['num_albums'], tracks_num))
        playlist_followers_nums.append(np.repeat(row['num_followers'], tracks_num))
        playlist_artists_nums.append(np.repeat(row['num_artists'], tracks_num))
    
    tracks_df = pd.concat(tracks_list)
    tracks_df['pid'] = np.concatenate(playlist_ids).flatten()
    tracks_df['name'] = np.concatenate(playlist_names).flatten()
    tracks_df['num_tracks'] = np.concatenate(playlist_tracks_nums).flatten()
    tracks_df['num_albums'] = np.concatenate(playlist_albums_nums).flatten()
    tracks_df['num_followers'] = np.concatenate(playlist_followers_nums).flatten()
    tracks_df['num_artists'] = np.concatenate(playlist_artists_nums).flatten()

    tracks_df_pid = tracks_df.set_index(['pid', 'name', 'num_tracks', 'num_albums', 'num_followers', 'num_artists','pos'])

    return tracks_df_pid
