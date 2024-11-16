# 1st program
print(9 ** 0.5 * 5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
result_no_priority = 2 * 2 + 2
result_with_priority = 2 * (2 + 2)
comparison_result = result_no_priority == result_with_priority
print("Без приоритета:", result_no_priority)
print("С приоритетом:", result_with_priority)
print("Результаты равны?", comparison_result)

# 4th program
s = '123.456'
num = float(s)
num_shifted = num * 10
num_int = int(num_shifted)
first_after_decimal = num_int % 10
print(first_after_decimal)
