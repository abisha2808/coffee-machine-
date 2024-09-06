from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


things = MenuItem(water=300,coffee=100,milk=200,cost=2.5,name="espresso")
item = Menu()
product = CoffeeMaker()
money = MoneyMachine()
should_off = False
while not should_off:
    choice = input(f"What would you like? ({item.get_items()}):")
    if choice == "off":
        should_off = True
    elif choice == "report":
         product.report()
         money.report()
    else:
        menu_item = item.find_drink(choice)
        print(menu_item)
        result = product.is_resource_sufficient(menu_item)
        if result:
            #cost = money.process_coins()
            make_payment = money.make_payment(menu_item.cost)
            if make_payment:
                product.make_coffee(menu_item)
