from constants.objectives.condition_bits import check_bit
from objectives.conditions._objective_condition import *


class Condition(ObjectiveCondition):
    NAME = "Check"
    def __init__(self, check):
        self.check = check
        super().__init__(ConditionType.EventBit, check_bit[self.check].bit)

    def __str__(self):
        return super().__str__(self.check)
