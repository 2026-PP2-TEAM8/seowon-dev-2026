
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
