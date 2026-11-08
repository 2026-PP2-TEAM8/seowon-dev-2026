
"""
[목표]
    1. 이번 달 총 지출을 자동으로 계산해준다.
    2. 총 지출 중 카테고리별 비중을 계산해준다.
"""

class Subscription :

    def __init__(self, name: str, price: int, day: int, category: str):
        self.name = name
        self.price = price
        self.day = day
        self.category = category

    def __repr__(self):
        return f"<Subscription: {self.name} ({self.category}) - {self.price}원, 매월 {self.day}일>"

class Subscriptions :

    keymaping = {1 : "여가", 2 : "음악", 3 : "쇼핑", 4 : "생산성", 5 : "기타"}

    def __init__(self):
        self.sub_list = []

    def add_register(self, name, price, day, category) :
        self.sub_list.append(Subscription(name, price, day, self.keymaping[category]))

def total_sum(Subscriptions) :
    total = 0

    for Subscription in Subscriptions.sub_list :
        total += Subscription.price

    return total

def category_sum (Subscriptions) :
    category_price = {"여가" : 0, "음악" : 0, "쇼핑" : 0, "생산성" : 0, "기타" : 0}

    for Subscription in Subscriptions.sub_list :
        category_price[Subscription.category] += Subscription.price

    return category_price


def cal_percent (category_price) :
    total = sum(category_price.values())
    category_percent = {"여가" : 0, "음악" : 0, "쇼핑" : 0, "생산성" : 0, "기타" : 0}

    for category in category_price :
        category_percent[category] = category_price[category] / total

    return category_percent