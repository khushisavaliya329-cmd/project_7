
import datetime as dt
import time as tm
import math as mth
import random as rnd
import uuid as uid


def get_number(message):
    while True:
        try:
            value = float(input(message))
            if mth.isfinite(value):
                return value
            print("Please enter a finite number!")
        except ValueError:
            print("Please enter a valid number!")


def get_choice(message, minimum, maximum):
    while True:
        try:
            choice = int(input(message))
            if minimum <= choice <= maximum:
                return choice
            print("Enter a number between", minimum, "and", maximum)
        except ValueError:
            print("Please enter numbers only!")


def date_time():
    now = dt.datetime.now()
    print("Current Date:", now.strftime("%d-%m-%Y"))
    print("Current Time:", now.strftime("%H:%M:%S"))


def date_difference():
    try:
        d1 = dt.datetime.strptime(input("Enter first date (YYYY-MM-DD): "), "%Y-%m-%d")
        d2 = dt.datetime.strptime(input("Enter second date (YYYY-MM-DD): "), "%Y-%m-%d")
        print("Difference:", abs((d2 - d1).days), "days")
    except ValueError:
        print("Invalid date format!")


def stopwatch():
    input("Press Enter to start")
    start = tm.time()
    input("Press Enter to stop")
    print("Time:", round(tm.time() - start, 2), "seconds")


def countdown():
    n = get_number("Enter seconds: ")

    if n < 1 or n != int(n):
        print("Enter a positive whole number!")
        return

    n = int(n)

    while n > 0:
        print(n)
        tm.sleep(1)
        n -= 1

    print("Time's up!")


def calculations():
    print("1. Factorial")
    print("2. Square Root")
    print("3. Logarithm")
    print("4. Sine")

    c = get_choice("Choose: ", 1, 4)
    n = get_number("Enter number: ")

    if c == 1:
        if n >= 0 and n == int(n):
            print("Factorial:", mth.factorial(int(n)))
        else:
            print("Enter a non-negative whole number!")

    elif c == 2:
        if n >= 0:
            print("Square Root:", mth.sqrt(n))
        else:
            print("Cannot calculate square root of a negative number!")

    elif c == 3:
        if n > 0:
            print("Logarithm:", mth.log(n))
        else:
            print("Enter a number greater than zero!")

    elif c == 4:
        print("Sine:", mth.sin(mth.radians(n)))


def area():
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    c = get_choice("Choose: ", 1, 3)

    if c == 1:
        r = get_number("Enter radius: ")
        if r >= 0:
            print("Area:", mth.pi * r * r)
        else:
            print("Radius cannot be negative!")

    elif c == 2:
        l = get_number("Enter length: ")
        b = get_number("Enter breadth: ")

        if l >= 0 and b >= 0:
            print("Area:", l * b)
        else:
            print("Dimensions cannot be negative!")

    elif c == 3:
        b = get_number("Enter base: ")
        h = get_number("Enter height: ")

        if b >= 0 and h >= 0:
            print("Area:", 0.5 * b * h)
        else:
            print("Dimensions cannot be negative!")


def compound_interest():
    p = get_number("Enter principal: ")
    r = get_number("Enter rate: ")
    t = get_number("Enter years: ")

    if p >= 0 and r >= 0 and t >= 0:
        amount = p * (1 + r / 100) ** t
        print("Compound Interest:", round(amount - p, 2))
        print("Total Amount:", round(amount, 2))
    else:
        print("Enter non-negative values!")


def random_operations():
    print("1. Random Number")
    print("2. Random List Item")
    print("3. Random Password")
    print("4. Random OTP")
    print("5. Random Sampling")
    print("6. UUID Generation")
    print("7. Game Simulation")

    c = get_choice("Choose: ", 1, 7)

    if c == 1:
        print("Random Number:", rnd.randint(1, 100))

    elif c == 2:
        items = ["Python", "Java", "C++", "HTML"]
        print("Random Item:", rnd.choice(items))

    elif c == 3:
        password = ''.join(rnd.choices(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))
        print("Random Password:", password)

    elif c == 4:
        print("OTP:", rnd.randint(100000, 999999))

    elif c == 5:
        data = ["Book", "Pen", "Laptop", "Phone", "Table"]
        print("Sample:", rnd.sample(data, 3))

    elif c == 6:
        print("Unique ID:", uid.uuid4())

    elif c == 7:
        print("Dice Result:", rnd.randint(1, 6))


def file_operation():
    message = input("Enter message to save: ")

    with open("toolkit_log.txt", "a", encoding="utf-8") as f:
        f.write(message + "\n")

    print("Data saved successfully!")


def read_file():
    try:
        with open("toolkit_log.txt", "r", encoding="utf-8") as f:
            content = f.read()

            if content:
                print(content)
            else:
                print("File is empty!")

    except FileNotFoundError:
        print("File not found! Write some data first.")


def update_file():
    message = input("Enter new information: ")

    with open("toolkit_log.txt", "w", encoding="utf-8") as f:
        f.write(message + "\n")

    print("File updated successfully!")


def unit_conversion():
    n = get_number("Enter kilometres: ")

    if n >= 0:
        print("Metres:", n * 1000)
        print("Miles:", n * 0.621371)
    else:
        print("Distance cannot be negative!")


def explore():
    print("1. datetime")
    print("2. math")
    print("3. random")
    print("4. time")
    print("5. uuid")

    c = get_choice("Choose module: ", 1, 5)

    if c == 1:
        print(dir(dt))
    elif c == 2:
        print(dir(mth))
    elif c == 3:
        print(dir(rnd))
    elif c == 4:
        print(dir(tm))
    elif c == 5:
        print(dir(uid))


def main():
    while True:
        print("\n===== MODULAR TOOLKIT =====")
        print("1. Current Date and Time")
        print("2. Date Difference")
        print("3. Stopwatch")
        print("4. Countdown Timer")
        print("5. Mathematical Calculations")
        print("6. Area Calculation")
        print("7. Compound Interest")
        print("8. Random Operations")
        print("9. File Operations")
        print("10. Unit Conversion")
        print("11. Explore Modules")
        print("12. Exit")

        choice = get_choice("Enter your choice: ", 1, 12)

        if choice == 1:
            date_time()
        elif choice == 2:
            date_difference()
        elif choice == 3:
            stopwatch()
        elif choice == 4:
            countdown()
        elif choice == 5:
            calculations()
        elif choice == 6:
            area()
        elif choice == 7:
            compound_interest()
        elif choice == 8:
            random_operations()
        elif choice == 9:
            print("1. Write")
            print("2. Read")
            print("3. Update")

            c = get_choice("Choose: ", 1, 3)

            if c == 1:
                file_operation()
            elif c == 2:
                read_file()
            elif c == 3:
                update_file()

        elif choice == 10:
            unit_conversion()
        elif choice == 11:
            explore()
        elif choice == 12:
            print("Thank you for using Modular Toolkit!")
            break


if __name__ == "__main__":
    main()
