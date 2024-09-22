import re
from typing import Callable
from decimal import Decimal

text = "Загальний дохід працівника складається з декількох частин: "\
     "1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 3254.00 доларів."

def generator_numbers(text: str):
    pattern = r"\d+\.\d+"
    matches = re.findall(pattern, text)
    
    for i in matches:
        yield i


# print(generator_numbers(text))
def sum_profit(text: str, func: Callable[[str],float]):
    income = Decimal("0")
    for i in generator_numbers(text):
        i = Decimal(i)
        income += i
    return income 
    
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
