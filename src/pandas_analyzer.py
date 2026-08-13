import pandas as pd

def match_count(df):
    return len(df)

def total_goals(df):
    return (df['home_goals']+df['away_goals']).sum()

def avg_goals(df):
    if match_count(df) == 0:
        return 0
    else:
        return total_goals(df)/match_count(df)

def calculate_points(df):
    home_pts = pd.Series(0,index=df.index)
    away_pts = pd.Series(0,index=df.index)

    home_win = df['home_goals'] > df['away_goals']
    away_win = df['home_goals'] < df['away_goals']
    draw = df['home_goals'] == df['away_goals']
    
    home_pts[home_win] = 3
    home_pts[draw] = 1
    home_pts[away_win] = 0
    away_pts[home_win] = 0
    away_pts[draw] = 1
    away_pts[away_win] = 3

    df1 = pd.DataFrame({'team':df['home_team'],'pts':home_pts})
    df2 = pd.DataFrame({'team':df['away_team'],'pts':away_pts})

    df3 = pd.concat([df1,df2]).groupby('team')['pts'].sum().sort_values(ascending=False)

    return df3

def print_summary(df):
    print(match_count(df))
    print(total_goals(df))
    print(avg_goals(df))


if __name__ == '__main__':
    df = pd.read_csv("../data/matches.csv")
    print_summary(df)
    print(calculate_points(df))
