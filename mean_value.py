# Medelvärde

def main():
    input_string = input("Ange tal separerade med kommatecken: ")
    numbers = [float(num.strip()) for num in input_string.split(',')]
    average = sum(numbers) / len(numbers)
    print(round(average, 1))

if __name__ == "__main__":
    main()
