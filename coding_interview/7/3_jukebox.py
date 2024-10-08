# Customer -> choose song -> see price -> pay -> get_change ??? -> listen

# 1 Jukebox (songs, state)
# 2 Song (name, author, album, duration)
# 3 CashMachine (current_sum, denomination)

# Assumptions
# Jukebox works with only one denomination coin
# Search engine out of scope


from dataclasses import dataclass
from typing import Optional


@dataclass
class Song:

    name: str
    author: str
    album: str
    duration_sec: int

    def play(self):
        pass

    def stop(self):
        pass

    def pause(self):
        pass


class CashMachine:

    _paid: bool = False
    _sum: int = 0

    def is_paid(self):
        return self._paid

    def pay(self):
        self._paid = True

    def confirm(self):
        self._sum += 1
        self._paid = False

    def clear(self):
        self._sum = 0

    def show_sum(self):
        return self._sum


class JukeBox:

    songs: list[Song]
    recommended: list[Song]
    selected: Optional[Song]
    cash_machine: "CashMachine" = CashMachine()

    def search(self) -> list[Song]:
        pass

    def select(self, song):
        self.selected = song

    def pay(self):
        self.cash_machine.pay()

    def play(self):

        if not self.cash_machine.is_paid():
            raise PermissionError("Pay")

        if self.selected is None:
            raise PermissionError("Select song")

        self.cash_machine.confirm()
        self.selected.play()
        self.selected = None
