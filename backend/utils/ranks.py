import re

def cc_rank(complexity: int) -> str:
    if complexity < 5:
        return "A"
    elif complexity < 10:
        return "B"
    elif complexity < 20:
        return "C"
    elif complexity < 30:
        return "D"
    elif complexity < 40:
        return "E"
    else:
        return "F"

def mi_rank(score: float) -> str:
    if score >= 85:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 55:
        return "C"
    elif score >= 40:
        return "D"
    elif score >= 25:
        return "E"
    else:
        return "F"
