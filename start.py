def parse_args(txt):
    lines = txt.splitlines()
    xy_grid = [int(num) for num in lines[0].split(" ")]
    dev_count = int(lines[xy_grid[1] + 1])
    manager_count = int(lines[xy_grid[1] + dev_count + 2])

    lines.pop(0)
    game_grid = ''
    count = 0
    for line in lines:
        if count == xy_grid[1]:
            break
        game_grid = game_grid + line + "\n"
        count += 1

    developers_list = lines[(count + 1):dev_count]
    managers_list = lines[(count + dev_count + 2):]

    developers = []
    managers = []

    for developer in developers_list:
        temp_arr = developer.split(' ')
        dev = {
            "company": temp_arr[0],
            "bonus": temp_arr[1],
            "skill_count": temp_arr[2],
            "skills": temp_arr[3:]
        }
        developers.append(dev)

    for manager in managers_list:
        temp_arr = manager.split(' ')
        man = {
            "company": temp_arr[0],
            "bonus": temp_arr[1],
        }
        managers.append(man)

    obj = {
        "xy_grid": xy_grid,
        "dev_count": dev_count,
        "manager_count": manager_count,
        "developers": developers,
        "managers": managers,
        "game_grid": game_grid
    }
    return obj


def optimise(game_obj):
    pass


if __name__ == '__main__':
    path = './inputs/' + input('Choose file: ') + '.txt'
    with open(path, 'r') as str_file:
        obj = parse_args(str_file.read())
        str_file.close()
    print(obj)
    optimise(obj)
