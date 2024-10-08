from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from uuid import uuid4


@dataclass
class Place:
    id: int
    car: "Car"
    # additional
    type: str
    level: int

    @property
    def is_free(self):
        return bool(self.car)


@dataclass
class Car:

    def __init__(self):
        self.id: str = uuid4()
        self.enter_time = None
        self.exit_time = None
        self.payment_sum: int = 0  # support only one concurrency
        self.payment_time = None
        self.timeout_min = 15

    @property
    def is_paid(self) -> bool:
        return datetime.now() - self.payment_time < self.timeout_min

    def enter(self):
        self.enter_time = datetime.now()

    def park(self, place: Place):
        self.place = place

    def pay(self, sum: int):
        self.payment_sum += sum

    def exit(self):
        self.exit_time = datetime.now()
        self.payment_sum = 0


class GateState(Enum):
    opened = 1
    closed = 2


@dataclass
class Gate:

    state: "GateState" = GateState.closed
    close_period_sec: int = 30

    def open(self):
        self.state = GateState.opened
        self._wait()
        self.state = GateState.closed

    def _wait(self):
        pass


class Parking:

    places: list["Place"] = []
    income: int = 0
    cars: list["Car"] = []
    gate = Gate()

    def count_free(self) -> int:
        return sum([1 for p in self.places if p.is_free])

    def handle_new_car(self):
        car = Car()
        car.enter()
        self.add_car(car)
        self.gate.open()

    def park(self, car, place_id):
        place = [p for p in self.places if p.id == place_id]
        place.car = car

    def pay(self, car_id, amount):
        car = self.get_car(car_id)
        car.pay(amount)
        self.income += amount

    def exit(self, car_id):
        car = self.get_car(car_id)
        if car.is_paid:
            car.exit()
            self.remove_car(car)
            self.gate.open()

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        self.cars.remove(car)

    def get_car(self, car_id):
        car = [c for c in self.cars if c.id == car_id][0]
        return car















