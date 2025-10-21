import time
import random

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

attempts = [
    "Mmm... w-was it... *Lemurs*?",
    "No no... focus, focus...",
    "Ahem—by the moons of Mirkwood!",
    "Come on... you can do this...",
    "Alright... one last try..."
]

def to_decimal(number_string, original_base):
    if original_base == 10:
        return int(number_string)
    total_value = 0
    power = 0
    for char in number_string[::-1]:
        char_value = digits.index(char)
        total_value += (char_value * (original_base ** power))
        power += 1
    return total_value

def from_decimal(decimal_number, target_base):
    if decimal_number == 0:
        return "0"
    result = ""
    while decimal_number > 0:
        remainder = decimal_number % target_base
        decimal_number //= target_base
        char_to_add = digits[remainder]
        result = char_to_add + result
    return result

def initiate():
    print("Welcome to the GRAND base converter! Where math meets magic!")
    currentBase = input("What base of math do you possess? (2-36) ")
    number = input("What number do you hold in your minds eyes? ").upper()
    desiredBase = input("From the deepest crevasses of your heart and mind what base do you desire? (2-36) ")

    for line in attempts:
        print(line)
        time.sleep(2)

    base10_value = to_decimal(number, int(currentBase))
    converted_value = from_decimal(base10_value, int(desiredBase))

    spell = f"ABRACADABRA {number} in base {currentBase} is {converted_value} in base {desiredBase}"
    for c in f"{spell.upper()}!!!":
        print(c, end='', flush=True)
        time.sleep(0.1)

if __name__ == "__main__":
    initiate()