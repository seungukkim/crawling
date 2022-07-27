# -*- coding: cp949 -*-


# class Comments:
#     title                = "#### %s 레스토랑에 오신걸 환영합니다. ####"
#     product_description  = "%s:%s(%s원)"
#     insert_price         = "\n요금을 넣어 주세요. : "
#     insufficient_price    = "%s 요금이 부족합니다. 거스름돈은 %s원 입니다."
#     select_menu          = "원하시는 메뉴를 선택하세요."
#     select_error         = "잘못 입력하셨습니다."
#     finish_sale          = "선택하신 %s 입니다. 거스름돈은 %s원 입니다.\n감사합니다."
#     terminate_sale       = "주문을 종료합니다."

# class Menus:
#     food_names  = []
#     food_prices = []
from restaurant import Comments,Menus

all_menus = [
    {"menu":"김밥","price":1500},
    {"menu":"떡볶이","price":2000},
    {"menu":"우동","price":3000},
    {"menu":"라면","price":2500},    
]

class Order(Menus):
    _data = all_menus
    _name ="김밥천국"
    _status = True

    def __init__(self):
        print(Comments.title % self._name)

    def set_products(self):
        Menus.food_names=[]
        Menus.food_prices=[]
        for food in self._data:
            Menus.food_names.append(food["menu"])
            Menus.food_prices.append(food["price"])

    def run(self):
        self.set_products()
        while self._status:
            try:
                inputMoney = int(input(Comments.insert_price))
        
            except ValueError:
                print(Comments.select_error)
        
            else:
                self.selectMenu(inputMoney)

    def selectMenu(self,money):
        print(Comments.select_menu)


        for idx, name in enumerate(Menus.food_names):
            price = Menus.food_prices[idx]
            print(Comments.product_description%(str(idx),name,price))

        inputFood = int(input(Comments.select_menu))
        self.payment(money,inputFood)

    def payment(self,money,idx):
        name = Menus.food_names[idx]
        price = Menus.food_prices[idx]

        if money >= price:
            balance = money-price
            print(Comments.finish_sale%(name,str(balance)))

        else:
            print(Comments.insufficient_price%(name,str(money)))

if __name__ =="__main__":
    order = Order()

    try:
        order.run()
    except KeyboardInterrupt:
        order._status=False
        print(Comments.terminate_sale)