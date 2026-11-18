from datetime import date


def calc_dday(pay_day):
    today = date.today()
    pay_date = date(today.year, today.month, pay_day)

    if pay_date < today:
        if today.month == 12:
            pay_date = date(today.year + 1, 1, pay_day)
        else:
            pay_date = date(today.year, today.month + 1, pay_day)

    return (pay_date - today).days


def sort_by_dday(subs):
    result = []
    for s in subs:
        result.append((calc_dday(s["pay_day"]), s["name"], s["price"]))
    result.sort()
    return result


def filter_imminent(sorted_list, days=3):
    result = []
    for item in sorted_list:
        if item[0] <= days:
            result.append(item)
    return result