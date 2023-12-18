print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15



def check_input(number):
  if number.isdigit() and int(number) > 0:
    return True
  else:
    return False

def input_parameters():
  while True:
    number = input("Введите число: ")
    if check_input(number):
      return int(number)
    else:
      print(f"Ошибка ввода: {number}. Попробуйте еще раз.")

def summa_n(number):
  sum = 0
  for count in range(1, number + 1):
    sum += count
  print(sum)
  return sum
  
def main():
  number = input_parameters()
  summ = summa_n(number)
  print(f'Сумма чисел от 1 до {number} равна {summ}.')


main()