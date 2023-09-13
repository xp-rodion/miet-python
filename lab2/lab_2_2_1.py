def get_address_net(ip: str, mask: str) -> str:
    list_mask = list(map(int, mask.split(".")))
    list_ip = ip.split(".")
    first_num = bin(int(list_ip[2]))[:-1] + bin(list_mask[2])[-1]
    second_num = list_mask[-1]
    address = f"{list_ip[0]}.{list_ip[1]}.{eval(first_num)}.{second_num}\n"
    return address


def create_addresses(input_file: str, mask: str):
    with open(input_file, "r") as file:
        lst_addresses = [get_address_net(ip, mask) for ip in file.readlines()]
        return lst_addresses


def write_addresses(output_file: str, addresses: list):
    with open(output_file, "w") as file:
        for address in addresses:
            file.write(address)


addresses = create_addresses("info.log", mask=input())
write_addresses("ip_solve.log", addresses)
