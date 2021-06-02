#Программааааааа а Питончике версияя 1.0
print("Привет! Это калькулятор!")
number1 = input(float("Введи левый операнд "))
number2 = input(float("Введи правый операнд"))
operator = input("Ведите операцию (+, -, *, /, **): ") 
if (operator == "+"):
   print("Сумма значений = ", (number1 + number2)
elif (operator == "-"):
   print("Разность значений = ",  (number1 - number2)
elif (operator == "*"):
   print("Произведение значений = ",  (number1 * number2)
elif (operator == "/"):
   if (number2 == 0):
      print("На ноль делить нельзя!")
   else:
