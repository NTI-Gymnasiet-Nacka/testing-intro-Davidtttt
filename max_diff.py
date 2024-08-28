# Största skillnad

import numbers


def main():
    input_string = input("Ange tal separererade med kommatecken")
    numbers = [int(num.strip()) for num in input_string.split(',')]
    print(max(numbers) - min(numbers))

if __name__ == "__main__":
    main()
