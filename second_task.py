import random

def get_numbers_ticket(min:int, max:int, quantity:int):
    try:
        if min < 1:
            empty_list = []
            return empty_list
        elif max > 1000:
            empty_list = []
            return empty_list
        else:
            numbers = list(range(min, max))
            number_list = random.sample(numbers, quantity)
            number_list.sort()
            return number_list
    except:
        empty_list = []
        return empty_list
    
        
        

print("Ваші лотерейні числа:", get_numbers_ticket(1000,1200, 10))