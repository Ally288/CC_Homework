class CustomerOrder:
    def __init__(
        self,
        client_name,
        order_date,
        quantity,
        product_description,
        price_per_unit,
    ):
        self.customer_name = client_name
        self.order_date = order_date
        self.quantity = quantity
        self.product_description = product_description
        self.price_per_unit = price_per_unit
