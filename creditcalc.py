import math
import argparse


def round_down(arg1, arg2):
    if arg1 - round(arg1 / arg2) * (arg2 - 1) > round(arg1 / arg2):
        return round(arg1 / arg2) + 1
    else:
        return round(arg1 / arg2)


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")
args = parser.parse_args()
if args.type not in ("diff", "annuity") or (args.payment is not None and args.type == "diff"):
    print("Incorrect parameters")
else:
    params = "apni"
    monthly_payment = 0
    loan_principal = 0
    number_months = 0
    loan_interest = 0.0
    overpayment = 0
    if args.payment is not None:
        monthly_payment = int(args.payment)
        params = params.replace("a", "")
    if args.principal is not None:
        loan_principal = int(args.principal)
        params = params.replace("p", "")
    if args.periods is not None:
        number_months = int(args.periods)
        params = params.replace("n", "")
    if args.interest is not None:
        loan_interest = float(args.interest)
        params = params.replace("i", "")
    if len(params) != 1:
        print("Incorrect parameters")
    else:
        if args.type == "annuity":
            if params == "n":
                nominal_interest = loan_interest / 12 / 100
                number = math.log(monthly_payment / (monthly_payment - nominal_interest * loan_principal), 1 + nominal_interest)
                number_months = math.ceil(number)
                res = 'It will take '
                number_y = number_months // 12
                if number_y > 1:
                    res = res + f'{number_y} years'
                elif number_y == 1:
                    res = res + '1 year'
                number_m = number_months % 12
                if number_m > 0 and number_y > 0:
                    res = res + ' and '
                if number_m > 1:
                    res = res + f'{number_m} months'
                elif number_m == 1:
                    res = res + '1 month'
                res = res + ' to repay this loan!'
                print(res)
            if params == "a":
                nominal_interest = loan_interest / 12 / 100
                temp = math.pow(1 + nominal_interest, number_months)
                monthly_payment = math.ceil(loan_principal * nominal_interest * temp / (temp - 1))
                print(f'Your monthly payment = {monthly_payment}!')
                print(f'Overpayment = {monthly_payment*number_months-loan_principal}')
            if params == "p":
                nominal_interest = loan_interest / 12 / 100
                temp = math.pow(1 + nominal_interest, number_months)
                loan_principal = math.floor(monthly_payment * (temp - 1) / nominal_interest / temp)
                print(f'Your loan principal = {loan_principal}!')
            print(f'Overpayment = {monthly_payment*number_months-loan_principal}')
        elif args.type == "diff":
            nominal_interest = loan_interest / 12 / 100
            overpayment = 0
            temp_payment = 0
            for m in range(number_months):
                temp_payment = math.ceil(loan_principal / number_months + nominal_interest * (loan_principal - loan_principal * m / number_months))
                overpayment += temp_payment
                print(f'Month {m+1}: payment is {temp_payment}')
            print()
            print(f'Overpayment = {overpayment-loan_principal}')
