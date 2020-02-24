###########################################
# Extract audio features for each track
###########################################

import pandas as pd
import glob
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data

# spotify authorization
client_id = 'f59f6a84e2584cc7bfa24f0b65eecca7'
client_secret = 'a1bc278e92054ffe9c2248c5320179e3'

# read all data find all spotify_ids
def get_tids():
    tids = set()
    for filename in glob.glob('./data/*.csv'):
        path = os.path.abspath(filename)
        data = pd.read_csv(path)
        spotify_ids = set(data['spotify_id'])
        tids = tids.union(spotify_ids)
    tids = list(tids)[1:]  # remove nan
    return tids

# extract audio features
def audio_features(tids):
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    columns = sp.audio_features(tids[0])[0].keys()
    df = pd.DataFrame(columns=columns)

    for tid in tids:
        features = sp.audio_features(tid)
        df.append(features[0], ignore_index=True)

    df.to_csv('audio_features.csv')

if __name__ == '__main__':
    tids = get_tids()
    audio_features(tids)