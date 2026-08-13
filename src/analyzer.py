import csv
data = []
with open('../data/matches.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
    #     data.append(row)
    # this is the slow method.
    data = list(reader)

def parse_matches(data):
    return len(data)

def total_goals(data):
    total = 0
    for row in data:
        total = total + int(row['home_goals']) + int(row['away_goals'])
    return total

def avg_goals(data):
    total_matches = parse_matches(data)
    if total_matches == 0.0:
        return 0.0
    return total_goals(data)/total_matches
def calculate_points(data):
    points = {}
    for row in data:
        home_team = row['home_team']
        away_team = row['away_team']
        home_goals = int(row['home_goals'])
        away_goals = int(row['away_goals'])
        if home_team not in points:
            points[home_team] = 0
        if away_team not in points:
            points[away_team] = 0
        if(home_goals>away_goals):
            points[home_team]+=3
        elif(home_goals<away_goals):
            points[away_team]+=3
        else:
            points[home_team]+=1
            points[away_team]+=1
    return points

# Pretty printing the table
def print_table(points_dict):
    print("\n--- TEAM POINTS TABLE ---")

    sorted_teams = sorted(points_dict.items(),key=lambda item: item[1],reverse=True)
    for team, pts in sorted_teams:
        print(f"{team:<20} | {pts} pts")
if __name__ == '__main__':
    print(avg_goals(data))
    print(calculate_points(data))
    print_table(calculate_points(data))
