import random

def get_numbers_ticket(min_value:int, max_value:int, quantity:int):
    try:
        if min_value<1 or max_value>1000:
            print([])
            return []
        lottery_numbers=sorted(random.sample(range(min_value,max_value),quantity))
        print(lottery_numbers)
        return lottery_numbers
    except (TypeError, ValueError):
        print([])
        return []

get_numbers_ticket(10,14,6)