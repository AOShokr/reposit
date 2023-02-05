def main():
    amount = input("How much? ")
    print(gauge(int(convert(amount).removesuffix("%"))))


def convert(fraction):
    x,z,y = fraction.partition("/")
    return f"{int(x)/int(y):.0%}"


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



if __name__ == "__main__":
    main()
    
