from abc import ABC, abstractmethod


class Orders(ABC):
    @abstractmethod
    def get_info_order(self, origin: int, destination: int) -> dict:
        pass

    @abstractmethod
    def get_cost(self, origin: int, destination: int) -> float:
        pass

    @abstractmethod
    def get_duration(self, origin: int, destination: int) -> float:
        pass

class OrderSend(Orders):
    def get_info_order(self, origin: int, destination: int) -> dict:
        return {"start_address": origin, "end_address": destination, "order": "Send the package"}

    def get_cost(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.1, 2)

    def get_duration(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.5, 2)

class OrderUponDelivery(Orders):
    def get_info_order(self, origin: int, destination: int) -> dict:
        return {"start_address": origin, "end_address": destination, "order": "Upon delivery"}

    def get_cost(self, origin: int, destination: int) -> float:
        return 0

    def get_duration(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 2, 2)

class OrderVirtual(Orders):
    def get_info_order(self, origin: int, destination: int) -> dict:
        return {"start_address": origin, "end_address": destination, "order": "Virtual order"}

    def get_cost(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.05, 2)

    def get_duration(self, origin: int, destination: int) -> float:
        return round((destination - origin) * 0.25, 2)