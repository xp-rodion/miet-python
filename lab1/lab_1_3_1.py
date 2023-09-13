def cinema_system(n_tickets: int) -> dict:
    information_about_persons = {}
    for _ in range(n_tickets):
        data = input().split()
        data_place = data[0], data[1]
        price = data[2]
        if data_place not in information_about_persons.keys():
            information_about_persons[data_place] = {price}
        else:
            information_about_persons[data_place].add(price)

    return information_about_persons


def create_output_data(information: dict):
    for key, value in information.items():
        print(*key, f"- {len(value)}")


create_output_data(cinema_system(int(input())))