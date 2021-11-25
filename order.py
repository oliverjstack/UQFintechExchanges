from enum import Enum
from time import time
from datetime import datetime


class OrderInfo:
    shares: int
    timestamp: datetime
    isLimit: bool
    limit: int

    def __init__(self, shares, timestamp, isLimit, limit=0):
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

    def get_shares(self):
        return self.info.shares

    def get_type(self):
        return self.orderType

    def get_id(self):
        return self.orderId

    def __str__(self):
        return f"<{self.orderId}> {self.orderType} order for {self.info.shares} shares placed at {self.info.timestamp}"
