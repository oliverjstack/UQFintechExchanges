from datetime import datetime


class OrderInfo:
    price: float
    shares: int
    timestamp: datetime
    isLimit: bool
    limit: int

    def __init__(self, price, shares, timestamp, isLimit, limit=0):
        self.price = price
        self.shares = shares
        self.timestamp = datetime.fromtimestamp(timestamp)
        self.isLimit = isLimit
        if isLimit:
            self.limit = limit


class Order:
    orderId: str
    info: OrderInfo

    def __init__(self, orderId, orderType, info):
        self.orderId = orderId
        self.orderType = orderType
        self.info = info

    def get_price(self):
        return self.info.price

    def get_type(self):
        return self.orderType

    def get_id(self):
        return self.orderId

    def get_shares(self):
        return self.info.shares

    def __str__(self):
        return f"<{self.orderId}> {self.orderType} order for {self.info.price} placed at {self.info.timestamp}"

    def __repr__(self):
        return f"{self.info.shares} at {self.info.price}"
