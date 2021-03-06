"""
3.1
"""

def right_justify(s):
    '''
    Function adds so many empty spaces so that string ends in line 70
    '''
    spaces_str = ' ' * (70 - len(s))
    print(spaces_str + s)

####

"""
3.2
"""
def do_twice(f, value):
    f(value)
    f(value)


def print_spam(value):
    print(f"spam: {value}")


def print_twice(bruce):
    print(bruce)
    print(bruce)


def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)


"""
3.3
"""
def draw_grid(rows=1, columns=1):
    for i in range(rows):
        row_length = (('+' + ' -' * 4 + ' ') * columns) + '+'
        print(row_length)
        for i in range(4):
            middle_string = ('|' + ' ' * 9) * (columns + 1)
            print(middle_string)
    row_length = (('+' + ' -' * 4 + ' ') * columns) + '+'
    print(row_length)


if __name__ == '__main__':
    # 3.1
    right_justify('adam')
    right_justify('Bemski')

    # 3.2
    do_twice(print_spam, 15)
    do_twice(print_twice, "spam")
    do_four(print_spam, 555)

    # 3.3
    draw_grid()
    print()
    draw_grid(2,1)
    print()
    draw_grid(2,3)
    draw_grid(6,5)
