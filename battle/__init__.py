from battle.animations import Animations
from battle.multipliers import Multipliers

__all__ = ["Battle"]
class Battle:
    def __init__(self):
        self.multipliers = Multipliers()
        self.animations = Animations()
