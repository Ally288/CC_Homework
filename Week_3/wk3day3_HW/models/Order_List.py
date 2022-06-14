from models.CustomerOrder import *

customer_order_1 = CustomerOrder(
    "Bob the Builder", "18/05/22", 10, "Screwdrivers", 5.00
)
customer_order_2 = CustomerOrder("Mario", "15/05/22", 5, "Plunger", 2.00)
customer_order_3 = CustomerOrder("Link", "13/05/22", 10, "Bow Arrows", 500.00)
customer_order_4 = CustomerOrder("Harry Potter", "12/05/22", 1, "Magic Wand", 1000.00)


orders = [customer_order_1, customer_order_2, customer_order_3, customer_order_4]
