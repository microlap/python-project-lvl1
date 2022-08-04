#!/usr/bin/env python3
import random
import prompt


print('Welcome to the Brain Games!')

name = prompt.string('May I have your name? ')
print('Hello,', name)

print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even():
    count = 0
    ans_pos = 'yes'
    ans_neg = 'no'
    while count != 3:
        n = round(random.random() * 100)
        print('Question:', n)
        answer = input('Your answer: ')
        if (n % 2 == 0 and answer == ans_pos) or (n % 2 != 0 and answer == ans_neg):
            print('Correct')
            count += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'. \n Let's try again, Bill!")
            count = 0
    print('Congratulations,', name, '!')


is_even()