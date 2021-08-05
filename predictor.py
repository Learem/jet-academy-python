import itertools
import random


def next_symbol(prob_0, prob_1):
    if prob_0 > prob_1:
        return "0"
    elif prob_0 < prob_1:
        return "1"
    else:
        return random.choice("01")


max_len = 100
user_cash = 1000

my_list = []
my_triads = [''.join(triad) for triad in itertools.product('01', repeat=3)]
random.seed()
print('Please give AI some data to learn...')
print('The current data length is 0, 100 symbols left')
while True:
    print('Print a random string containing 0 or 1:\n')
    my_str = input()
    my_list += [ch for ch in my_str if ch in '01']
    if len(my_list) > max_len - 1:
        my_str = ''.join(my_list)
        print('\nFinal data string:', my_str, sep='\n')
        break
    print(f'Current data length is {len(my_list)}, {max_len - len(my_list)} symbols left')
zero_triads = {triad: 0 for triad in my_triads}
ones_triads = zero_triads.copy()
for k in range(0, len(my_str) - 3):
    if my_str[k+3] == '1':
        ones_triads[my_str[k:k + 3]] += 1
    else:
        zero_triads[my_str[k:k + 3]] += 1
triad_weights = [zero_triads[val] + ones_triads[val] for val in zero_triads.keys()]
# print(gen_triad(triad_weights))
# for item in zero_triads.keys():
#    print(f'{item} : {zero_triads[item]},{ones_triads[item]}')
print('\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.')
print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!')
while True:
    print('\nPrint a random string containing 0 or 1:')
    my_str = input()
    if my_str == "enough":
        break
    else:
        my_str = "".join([ch for ch in my_str if ch in '01'])
    predict_str = random.choices(my_triads, weights=triad_weights)[0]
    if len(my_str) > 3:
        #    predict_str = my_str[:3]
        print('prediction:')
        predict_guess = 0
        len_test_string = len(my_str) - 3
        for k in range(len_test_string):
            #        print(predict_str[-3:], zero_triads[predict_str[-3:]], ones_triads[predict_str[-3:]])
            pr_symbol = next_symbol(zero_triads[my_str[k:k+3]], ones_triads[my_str[k:k+3]])
            #        pr_symbol = next_symbol(zero_triads[predict_str[-3:]], ones_triads[predict_str[-3:]])
            if pr_symbol == my_str[k+3]:
                predict_guess += 1
            predict_str += pr_symbol
        print(predict_str)
        user_cash += len_test_string - 2 * predict_guess
        print(f'\nComputer guessed right {predict_guess} out of {len_test_string} symbols ({predict_guess * 100 / len_test_string:00.2f} %)')
        print(f'Your capital is now ${user_cash}')
print("Game over!")
