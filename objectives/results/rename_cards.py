from data.item_names import name_id as item_name_id
from objectives.results._objective_result import *

RENAME_CARD_COUNT = 14

class Field(field_result.Result):
    def src(self):
        src = []
        for _ in range(RENAME_CARD_COUNT):
            src += [
                field.AddItem(item_name_id["Rename Card"]),
            ]
        return src

class Battle(battle_result.Result):
    def src(self):
        src = []
        for _ in range(RENAME_CARD_COUNT):
            src += [
                battle_result.AddItem(item_name_id["Rename Card"]),
            ]
        return src

class Result(ObjectiveResult):
    NAME = "Rename Cards"
    def __init__(self):
        super().__init__(Field, Battle)
