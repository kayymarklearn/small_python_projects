from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
machine_on = True
menu_items = Menu()
available_items = menu_items.get_items()

while machine_on:
    order = input(f"Would you like? ({available_items}): ").lower()
    if order == "report":
        coffee_machine.report()
        money_machine.report()
    elif order == "off":
        machine_on = False
    else:
        order_available = menu_items.find_drink(order)
        if order_available:
            resources_available = coffee_machine.is_resource_sufficient(order_available)
            if resources_available:
                money_paid = money_machine.make_payment(order_available.cost)
                if money_paid:
                    coffee_machine.make_coffee(order_available)
