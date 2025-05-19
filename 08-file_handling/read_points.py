def read_points(results=None):
    result = []
    try:
        with open('statistics.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if ':' not in line or '-' not in line:
                    continue

                team_info = line.split(':')
                team_name = team_info[0]
                stats = team_info[1].split('-')

                try:
                    wins = int(stats[0])
                    losses = int(stats[1])
                    ties = int(stats[2])
                except ValueError:
                    raise ValueError(f"Invalid format in the file: {line}")

                points = wins * 3 + ties * 1
                result.append((team_name, points))

    except FileNotFoundError:
        print("The file 'statistics.txt' was not found.")
    return results


if __name__ == "__main__":
    try:
        points_list = read_points()
        print(points_list)
    except ValueError as e:
        print(e)