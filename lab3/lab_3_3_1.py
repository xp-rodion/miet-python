def get_correct_format_for_date(date: str) -> dict:
    new_date = list(map(int, date.split(".")))
    return {
        "day": new_date[0],
        "month": new_date[1],
        "year": new_date[2],
    }


def compare_years(first_year: dict, second_year: dict) -> dict:

    if first_year["year"] > second_year["year"]:
        return first_year

    if second_year["year"] > first_year["year"]:
        return second_year

    if first_year["month"] > second_year["month"]:
        return first_year

    if second_year["month"] > first_year["month"]:
        return second_year

    if first_year["day"] > second_year["day"]:
        return first_year

    return second_year


def nearest_date(*args) -> str:
    now_date = get_correct_format_for_date("05.09.2023")
    near_date = {
        "day": 0,
        "month": 0,
        "year": 0
    }
    for date in args:
        correct_date = get_correct_format_for_date(date)

        if abs(now_date["year"] - correct_date["year"]) > abs(now_date["year"] - near_date["year"]):
            continue

        if abs(now_date["year"] - correct_date["year"]) < abs(now_date["year"] - near_date["year"]):
            near_date = correct_date
            near_date["origin"] = date
            continue

        if abs(now_date["month"] - correct_date["month"]) > abs(now_date["month"] - near_date["month"]):
            continue

        if abs(now_date["month"] - correct_date["month"]) < abs(now_date["month"] - near_date["month"]):
            near_date = correct_date
            near_date["origin"] = date
            continue

        if abs(now_date["day"] - correct_date["day"]) > abs(now_date["day"] - near_date["day"]):
            continue

        if abs(now_date["day"] - correct_date["day"]) < abs(now_date["day"] - near_date["day"]):
            near_date = correct_date
            near_date["origin"] = date
            continue

        near_date = compare_years(correct_date, near_date)
        near_date["origin"] = date

    return near_date["origin"]


data = input().split()
print(nearest_date(*data))