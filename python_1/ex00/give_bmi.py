import numpy as py
from ft_filter import ft_filter


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    imc = [weight[i] / (height[i] ** 2) for i in range(len(height))]
    return imc


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    print("-------------")
    return (list(crea(lambda x: x > limit, bmi)))
