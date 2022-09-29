# declare global variables
memory = 0
x = 0
y = 0
operator = ""


# take and check user input
def take_input():
    global x, y, operator, memory
    msg_0 = 'Enter an equation'
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

    while True:
        print(msg_0)
        calc = input()
        x, operator, y = calc.split(" ")
        try:
            x = memory if x.lower() == "m" else float(x)
            y = memory if y.lower() == "m" else float(y)
            if operator in "+-/*":
                prompt_check(x, operator, y)
                break
            else:
                print(msg_2)
        except ValueError:
            print(msg_1)


def is_one_digit(n):
    try:
        num = int(n)
        return -10 < num < 10 and n == num
    except ValueError:
        return False


def prompt_check(m, oper, n):
    msg = ""
    if is_one_digit(m) and is_one_digit(n):
        msg += " ... lazy"
    if (m == 1 or n == 1) and oper == "*":
        msg += " ... very lazy"
    if (m == 0 or n == 0) and (oper in "*+-"):
        msg += " ... very, very lazy"
    if msg != "":
        print(f"You are{msg}")


def calculate():
    global x, y, operator
    while True:
        take_input()
        if operator == "+":
            res = x + y
            break
        elif operator == "-":
            res = x - y
            break
        elif operator == "*":
            res = x * y
            break
        elif operator == "/":
            try:
                res = x / y
                break
            except ZeroDivisionError:
                print("Yeah... division by zero. Smart move...")
    print(res)
    return res


def store_memory(result):
    global memory
    print("Do you want to store the result? (y / n):")
    answer = input().lower()
    if answer == "y":
        if is_one_digit(result):
            print("Are you sure? It is only one digit! (y / n)")
            answer2 = input().lower()
            if answer2 == "y":
                print("Don't be silly! It's just one number! Add to the memory? (y / n)")
                answer3 = input().lower()
                if answer3 == "y":
                    print("Last chance! Do you really want to embarrass yourself? (y / n)")
                    answer4 = input().lower()
                    memory = result if answer4 == "y" else 0
        else:
            memory = result
    else:
        memory = 0


def main():
    global memory
    running = True

    while running:
        result = calculate()
        store_memory(result)
        print("Do you want to continue calculations? (y / n):")
        answer = input().lower()
        running = True if answer == "y" else False


if __name__ == '__main__':
    main()