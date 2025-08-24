def calculate_area_triangle(base, height):
    area = (base * height) / 2
    return area

print('Exercise 1:', calculate_area_triangle(10, 5))


def simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

print('Exercise 2:', simple_interest(1000, 5, 2))


def apply_discount(price, discount):
    discounted_price = price - (price * discount / 100)
    return discounted_price

print('Exercise 3:', apply_discount(100, 25))


def convert_temperature(temp, unit):
    if unit == 'C':
        return temp * 9 / 5 + 32
    elif unit == 'F':
        return (temp - 32) * 5 / 9

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


def sum_to(n):
    total = sum(range(n + 1))
    return total

print('Exercise 5:', sum_to(10))


def largest(num1, num2, num3):
    return max(num1, num2, num3)

print('Exercise 6:', largest(1, 2, 3))


def calculate_tip(bill, tip):
    tip_amount = bill * tip / 100
    return tip_amount

print('Exercise 7:', calculate_tip(50, 20))


def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print('Exercise 8:', product(2, 5, 5))


def basic_calculator(num1, num2, operation):
    if operation == "subtract":
        return num1 - num2
    elif operation == "add":
        return num1 + num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2

print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
