import random

def get_number_ticket(min:int, max:int, quantity:int):
    if quantity > (max - min):
        return("Вибачте, помилка, кількість номерів більше за заданий діапазон")
    elif max < min:
        return("Вибачте, помилка, Ваше максимальне значення менше за мінімільне")
    else:
        numbers = list(range(min, max))
        number_list = random.sample(numbers, quantity)
        number_list.sort()
        return number_list
    
        
        

print(get_number_ticket(1,100, 6))