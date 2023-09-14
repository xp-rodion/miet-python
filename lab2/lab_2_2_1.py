def get_address_net(ip: str, mask: str) -> str:
    list_mask = list(map(int, mask.split(".")))
    list_ip = list(map(int, ip.split(".")))
    address = ".".join([bin_and(*nums) for nums in zip(list_mask, list_ip)])
    return address


def bin_and(first: int, second: int):
    result = eval(bin(first & second))
    return str(result)


def create_addresses(input_file: str, mask: str):
    with open(input_file, "r") as file:
        lst_addresses = [get_address_net(ip, mask) for ip in file.readlines()]
        return lst_addresses


def write_addresses(output_file: str, addresses: list):
    with open(output_file, "w") as file:
        for address in addresses:
            file.write(f"{address}\n")


addresses = create_addresses("info.log", mask=input())
write_addresses("ip_solve.log", addresses)
