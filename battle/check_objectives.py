import instruction.asm as asm
from memory.space import Bank, Write


class CheckObjectives(asm.JSR):
    def __init__(self):
        import data.dialogs as dialogs
        import objectives

        src = [
            asm.PHP(),
            asm.AXY8(),
        ]
        for objective in objectives:
            src += [
                objective.check_complete.battle(),
                asm.CMP(0x00, asm.IMM8),
                asm.BEQ("AFTER_DIALOG" + str(objective.id)),            # if not complete, go to next objective

                asm.LDA(dialogs.BATTLE_OBJECTIVES[objective.id], asm.IMM8),
                asm.JSR(0x5fd4, asm.ABS),                               # display objective complete message

                "AFTER_DIALOG" + str(objective.id),
            ]
        src += [
            "RETURN",
            asm.PLP(),
            asm.RTS(),
        ]

        space = Write(Bank.C2, src, "battle check objectives")
        CheckObjectives.__init__ = lambda self : super().__init__(space.start_address, asm.ABS)
        self.__init__()
