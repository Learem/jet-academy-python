available_formatters = ["plain", "bold", "italic", "link", "inline-code", "header", "ordered-list", "unordered-list", "line-break"]
result_string = []


def print_text():
    for line in result_string:
        print(line, end="")
    print()


def formatter_plain():
    string = input("- Text: ")
    return string


def formatter_bold():
    string = input("- Text: ")
    return "**" + string + "**"


def formatter_italic():
    string = input("- Text: ")
    return "*" + string + "*"


def formatter_inline_code():
    string = input("- Text: ")
    return "`" + string + "`"


def formatter_link():
    string_1 = input("- Label: ")
    string_2 = input("- URL: ")
    return "[" + string_1 + "](" + string_2 + ")"


def formatter_header():
    while True:
        level_num = int(input("- Level: "))
        if 0 < level_num < 7:
            break
        else:
            print("The level should be within the range of 1 to 6")
    string = input("- Text: ")
    return "#" * level_num + " " + string + "\n"


def formatter_line_break():
    return "\n"


def formatter_list(ordered):
    string = ""
    while True:
        rows_num = int(input("- Number of rows: "))
        if rows_num > 0:
            break
        else:
            print("The number of rows should be greater than zero")
    for num in range(rows_num):
        row = input(f"- Row #{num + 1}: ")
        if ordered:
            string += str(num + 1) + ". " + row + "\n"
        else:
            string += "* " + row + "\n"
    return string


while True:
    formatter = input("- Choose a formatter: ")
    if formatter == "!done":
        with open("output.md", "w") as md_file:
            md_file.writelines(result_string)
        break
    if formatter == "!help":
        print("Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break")
        print("Special commands: !help !done")
    elif formatter in available_formatters:
        if formatter == "plain":
            result_string.append(formatter_plain())
        elif formatter == "bold":
            result_string.append(formatter_bold())
        elif formatter == "italic":
            result_string.append(formatter_italic())
        elif formatter == "inline-code":
            result_string.append(formatter_inline_code())
        elif formatter == "link":
            result_string.append(formatter_link())
        elif formatter == "header":
            result_string.append(formatter_header())
        elif formatter == "line-break":
            result_string.append(formatter_line_break())
        elif formatter == "ordered-list":
            result_string.append(formatter_list(True))
        elif formatter == "unordered-list":
            result_string.append(formatter_list(False))
        print_text()
    else:
        print("Unknown formatter or command. Please try again")
