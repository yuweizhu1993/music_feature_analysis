############################################
# Convert original data to total rank data
############################################

# for each region, use the total occurance in top 200 songs as ranking criterion
# and create a new dataframe

import pandas as pd
import glob
import os

def rank_df(input_path, output_path):
    data = pd.read_csv(input_path)
    # drop redundent rows
    data.drop(data[data['Track Name'] == 'Track Name'].index, inplace = True)
    data.drop(data[data['Position'] == 'position'].index, inplace = True)
    data.drop(data[data['Position'].isnull()].index, inplace=True)
    # change columns data type
    data['Position'] = data['Position'].astype('int32')

    rank_data = data.groupby(['Track Name', 'Artist'], sort=False) \
                    .agg({'region': 'count',
                         'Streams': 'max',
                         'Position': 'min',
                         'spotify_id': 'min'}) \
                    .reset_index() \
                    .sort_values(['region'], ascending=False) \
                    .reset_index()

    # change column name and drop redundant columns
    rank_data = rank_data.drop(columns=['index'])
    rank_data = rank_data.rename(columns={'region': 'Count'})
    rank_data.to_csv(output_path)

def read_files():
    for filename in glob.glob('./data/*.csv'):
        input_path = os.path.abspath(filename)
        output_path = './total_rank_data/' + str(os.path.basename(filename))
        print(input_path)
        rank_df(input_path, output_path)

if __name__ == '__main__':
    read_files()