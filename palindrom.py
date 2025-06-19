def is_palindrome(s):
    return s == s[::-1]

input_strings = [
    'kasurrusak',
    '12321',
    'abc12321cba',
    '123abc321',
    'a1b2b1a',
    'notapalindrome'
]

for i in input_strings:
    print(f'{is_palindrome(i)}\t{i}')