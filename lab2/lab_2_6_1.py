def get_count_symbols(file: str) -> dict[[str, int]]:
    symbs, kirill_letters = {}, "йцукенгшщзхъфывапролджэячсмитьбю"
    with open(file, "r") as file:
        for line in file.readlines():
            for symbol in line:
                symbol = symbol.lower()
                if symbol not in kirill_letters:
                    continue

                if symbol in symbs.keys():
                    symbs[symbol] += 1
                else:
                    symbs[symbol] = 1

        return symbs


def beauty_output(symbols: dict) -> None:
    for symbol, count in symbols.items():
        print(f"{symbol}: {count}")


path_to_file = input("Текстовый документ: ")
symbols = get_count_symbols(path_to_file)
beauty_output(symbols)