# get two integer parameters
# return sum
def plus(x, y):
    return x+y
def mi(x,y):
    return x-y
def re(x,y):
    return x*y
def re2(x,y):
    return x/y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus, 2: minus, 3:times, 4:divied ")
        check = int(input())
        if check == 1:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", plus(x,y))
        elif check > 4:
            print("Unsupported")
        else:
            print("Thank you")

        if check == 2:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", mi(x,y))
        elif check > 4:
            print("Unsupported")

        if check == 3:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", re(x,y))
        elif check > 4:
            print("Unsupported")


        if check == 4:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", re2(x,y))
        elif check > 4:
            print("Unsupported")


if __name__ == "__main__":
    main()
