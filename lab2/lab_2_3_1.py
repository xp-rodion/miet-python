import csv


def convert_data(data: list[str]) -> list | None:
    uncorrected_data = data[0].split(";")
    try:
        player_data = [uncorrected_data[0]] + list(map(int, uncorrected_data[1:]))
        return player_data
    except ValueError:
        return


def reader_csv(file: str) -> list[list]:
    with open(file, "r", newline="") as csv_file:
        data = csv.reader(csv_file)
        plrs = [convert_data(player) for player in data if convert_data(player)]
        return plrs


def sorted_players(plrs: list[list]):
    std_players = list(sorted(plrs, key=lambda x: x[1]))
    return std_players[::-1]


def write_csv(file: str, plrs: list[list]):
    with open(file, "w", newline="") as csv_file:
        columns = ["Спортсмен", "Место"]
        writer = csv.DictWriter(csv_file, fieldnames=columns)
        writer.writeheader()
        results = []
        for index, player in enumerate(plrs):
            ex_player = plrs[index - 1]
            place = index + 1 if (player[1], player[2]) != (ex_player[1], ex_player[2]) else results[index - 1]["Место"]
            results.append({"Спортсмен": player[0], "Место": place})
        writer.writerows(results)


input_file = input("Входные данные: ")
output_file = input("Выходные данные: ")

players = reader_csv(input_file)
sort_players = sorted_players(players)
write_csv(file=output_file, plrs=sort_players)