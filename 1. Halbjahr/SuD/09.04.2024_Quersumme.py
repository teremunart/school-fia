# Einheit: Rekursive Methoden/Funktionen

def main():
    numberToCalculate = int(input())
    print(addToQuersumme(numberToCalculate))


def addToQuersumme(s):
    if (s % 10) == 0:
        return s % 10
    else:
        return s % 10 + addToQuersumme(s // 10)


if __name__ == "__main__":
    main()
