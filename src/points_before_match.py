import pandas as pd
import numpy as np

def points_before_match(df):
    home_pts = pd.Series(0,index=df.index)
    away_pts = pd.Series(0,index=df.index)

    home_win= df['home_goals'] > df['away_goals']
    away_win = df['home_goals'] < df['away_goals']
    draw = df['home_goals'] == df['away_goals']

    # home_pts[home_win] = 3
    # home_pts[away_win] = 0
    # home_pts[draw] = 1
    # away_pts[home_win] = 0
    # away_pts[away_win] = 3
    # away_pts[draw] = 1

    # df1 = pd.DataFrame({'match_id':df['match_id'],'team':df['home_team'],'pts':home_pts})
    # df2 = pd.DataFrame({'match_id':df['match_id'],'team':df['away_team'],'pts':away_pts})
    
    df['home_pts'] = np.select([home_win,draw,away_win],[3,1,0])
    df['away_pts'] = np.select([away_win,draw,home_win],[3,1,0])


    df1 = df[['match_id','home_team','home_pts']].rename(columns={'home_team':'team','home_pts':'pts'})

    df2 = df[['match_id','away_team','away_pts']].rename(columns={'away_team':'team','away_pts':'pts'})
    df3 = pd.concat([df1,df2]).sort_values(by=['team','match_id'])
    df3['points_before_match'] = df3.groupby('team')['pts'].transform(lambda x: x.cumsum().shift(1)).fillna(0)
    return df3







if __name__ == '__main__':
    df = pd.read_csv('../data/matches.csv')
    print(points_before_match(df))











