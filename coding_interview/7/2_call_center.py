# Employee -> Respondent -> Manager -> Director
# CallCenter

from dataclasses import dataclass
from enum import Enum


class Roles(Enum):
    respondent = 'Respondent'
    manager = 'Manager'
    director = 'Director'


@dataclass
class Employee:

    available: bool
    role: "Roles"

    def is_available(self):
        return self.available

    def start_call(self):
        self.available = False

    def finish_call(self):
        self.available = True


@dataclass
class Hierarchy:

    respondent: list["Employee"]
    manager: "Employee"
    director: "Employee"

    def get_next(self) -> "Employee":
        pass

    def add(self, employee: "Employee"):
        pass


class Call:
    pass


@dataclass
class CallCenter:

    hierarchy: "Hierarchy"
    queue: list["Call"]

    def dispatch_call(self):
        employee = self.hierarchy.get_next()
        employee.start_call()









