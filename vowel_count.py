# Vokalräkning

def main():
    string = input()
    vokal = "aeiouyåäöAEIOUYÅÄÖ"
    print(sum(1 for char in string if char in vokal))
    pass

if __name__ == "__main__":
    main()
