from collections import deque


var_dict = {}
operator = deque()
postfix = deque()


def check_cmd(exp):
    if exp == "/exit":
        print("Bye!")
        return "exit"
    elif exp == "/help":
        print("The program calculates expression: \nsupported variables, addition, subtraction, multiplication, division and power")
        return "help"
    else:
        print("Unknown command")
        return "no command"


def is_variable(var):
    for ch in var:
        if ch in "0123456789 =":
            return False
    return True


def make_assign(asgn):
    lexs = [var.strip() for var in asgn.split("=", 1)]
    if not is_variable(lexs[0]):
        print("Invalid identifier")
    else:
        try:
            var_dict[lexs[0]] = int(lexs[1])
        except ValueError:
            if not lexs[1]:
                print("Invalid assignment")
            elif not is_variable(lexs[1]):
                print("Invalid assignment")
            elif var_dict.get(lexs[1]) is None:
                print("Unknown variable")
            else:
                var_dict[lexs[0]] = var_dict[lexs[1]]
        except IndexError:
            print("Invalid assignment")


def higher_top(exp):
    if len(operator) > 0:
        if exp in "-+":
            return False
        top = operator[-1]
        if exp in "*/":
            return top in "-+"
        if exp in "^":
            return top in "-+*/"
        if exp in "()":
            return True
    else:
        return True


def infix_to_postfix(exp):
    if exp not in "-+*/()^":
        postfix.append(exp)
    else:
        if len(operator) == 0 or operator[-1] == "(":
            operator.append(exp)
        elif exp not in "()" and higher_top(exp):
            operator.append(exp)
        elif exp not in "()":
            while len(operator) > 0 and not higher_top(exp) and operator[-1] != "(":
                postfix.append(operator.pop())
            operator.append(exp)
        elif exp == "(":
            operator.append(exp)
        elif exp == ")":
            while len(operator) > 0 and operator[-1] != "(":
                postfix.append(operator.pop())
            operator.pop()


def error_syntax(expr):
    while "++" in expr:
        expr = expr.replace("++", "+")
    while "---" in expr:
        expr = expr.replace("---", "-")
    while "--" in expr:
        expr = expr.replace("--", "+")
    res = ""
    for char in expr:
        if char in "-+*/()^":
            res += " " + char + " "
        else:
            res += char
    lexems = res.split()
    operators = []
    brackets = []
    for oper in lexems:
        if len(operators) == 0:
            operators.append(oper)
            if oper == "(":
                brackets.append(oper)
            if oper == ")":
                if len(brackets) > 0:
                    brackets.pop()
                else:
                    operators = []
                    break
        elif oper in "+*/^":
            if operators[-1] in "-+*/^(":
                operators = []
                break
            else:
                operators.append(oper)
        elif oper == "-":
            if operators[-1] in "-+*/^":
                operators = []
                break
            else:
                operators.append(oper)
        elif oper == "(":
            if operators[-1] not in "-+*/^(":
                operators = []
                break
            else:
                operators.append(oper)
                brackets.append(oper)
        elif oper == ")":
            if operators[-1] in "-+*/^(":
                operators = []
                break
            else:
                operators.append(oper)
                if len(brackets) > 0:
                    brackets.pop()
                else:
                    operators = []
                    break
        else:
            if operators[-1] not in "-+*/^(":
                operators = []
                break
            else:
                if operators[-1] == "-":
                    if len(operators) == 1:
                        oper = "-" + oper
                        del operators[-1]
                    else:
                        if operators[-2] == "(":
                            oper = "-" + oper
                            del operators[-1]
                operators.append(oper)
    if len(brackets) > 0:
        operators = []
    return operators


def calc_num(arg):
    try:
        return int(arg)
    except ValueError:
        if is_variable(arg):
            return var_dict.get(arg)
        else:
            return ""


def calculate_postfix():
    operators = []
    try:
        while len(postfix) > 0:
            item = postfix.popleft()
            if item in "-+*/^":
                value_1 = operators.pop()
                value_2 = operators.pop()
                if item == "-":
                    operators.append(value_2 - value_1)
                elif item == "+":
                    operators.append(value_2 + value_1)
                elif item == "*":
                    operators.append(value_2 * value_1)
                elif item == "/":
                    operators.append(value_2 // value_1)
                elif item == "^":
                    operators.append(value_2 ** value_1)
            else:
                value = calc_num(item)
                if value is None:
                    print("Unknown variable")
                    break
                elif value == "":
                    print("Invalid identifier")
                    break
                else:
                    operators.append(value)
    except IndexError:
        print("Invalid expression")
    else:
        if len(operators) == 1:
            print(operators[0])


while True:
    user_input = input()
    if user_input == "":
        continue
    if user_input.startswith("/"):
        if check_cmd(user_input) == "exit":
            break
        else:
            continue
    if "=" in user_input:
        make_assign(user_input)
        continue
    exprs = error_syntax(user_input)
    if len(exprs) == 0:
        print("Invalid expression")
        continue
    postfix.clear()
    operator.clear()
    for lex in exprs:
        infix_to_postfix(lex)
    for _ in range(len(operator)):
        postfix.append(operator.pop())
    calculate_postfix()
