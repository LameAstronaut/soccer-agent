import pandas as pd
import numpy as np

def goal_difference(df):
    home_goals = df['home_goals']
    away_goals = df['away_goals']

    # df.insert(0,"away_goal_diff",away_goals - home_goals)
    # df.insert(0,"home_goal_diff",home_goals - away_goals)
    df['home_goal_diff'] = home_goals- away_goals
    df['away_goal_diff'] = away_goals - home_goals

    return df


def calculate_features(df):
    home_df = df[['match_id','home_team','home_goals']]
    home_df = home_df.rename(columns = {'home_team': 'team','home_goals':'goals'})

    away_df= df[['match_id','away_team','away_goals']]
    away_df = away_df.rename(columns = {'away_team': 'team','away_goals':'goals'})


    combined = pd.concat([home_df,away_df]).sort_values(by=['team','match_id'])
    
    combined['goals_before_match'] = combined.groupby('team')['goals'].transform(lambda x: x.cumsum().shift(1)).fillna(0)

    combined['rolling_avg_goals'] = combined.groupby('team')['goals'].transform(lambda x: x.shift(1).rolling(window=3,min_periods=1).mean()).fillna(0).round(2)

    

    return combined



if __name__ ==  '__main__':
    df = pd.read_csv('../data/matches.csv')

    print(goal_difference(df))
    print(calculate_features(df))
