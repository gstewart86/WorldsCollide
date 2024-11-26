from data.item_names import name_id as item_name_id
from objectives.results._objective_result import *


class Field(field_result.Result):
    def src(self):
        return [
            field.AddItem(item_name_id["Ribbon"]),
        ]

class Battle(battle_result.Result):
    def src(self):
        return [
            battle_result.AddItem(item_name_id["Ribbon"]),
        ]

class Result(ObjectiveResult):
    NAME = "Ribbon"
    def __init__(self):
        super().__init__(Field, Battle)
