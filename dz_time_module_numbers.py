import colorama
from colorama import Fore, Back, Style
colorama.init()


def sum_number(x1, x2, x3, x4, x5):
    return x1+x2+x3+x4+x5


def number_dict(x, n):
    x_dict = {}
    s = 0
    for i in range(5):
        x_dict[i] = x[s:s+n]
        s += n
    return x_dict


# количество столбцов в нарисованнх цифрах
number_column_1 = 5

a_0_0 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_0_1 = '\u2B1C\u2B1B\u2B1B\u2B1C'
a_0_2 = '\u2B1C\u2B1B\u2B1B\u2B1C'
a_0_3 = '\u2B1C\u2B1B\u2B1B\u2B1C'
a_0_4 = '\u2B1C\u2B1C\u2B1C\u2B1C'
n_0 = 4
a_0 = number_dict(sum_number(a_0_0, a_0_1, a_0_2, a_0_3, a_0_4), n_0)

a_1_0 = '\u2B1B\u2B1B\u2B1C\u2B1B'
a_1_1 = '\u2B1B\u2B1C\u2B1C\u2B1B'
a_1_2 = '\u2B1B\u2B1B\u2B1C\u2B1B'
a_1_3 = '\u2B1B\u2B1B\u2B1C\u2B1B'
a_1_4 = '\u2B1B\u2B1C\u2B1C\u2B1C'
n_1 = 4
a_1 = number_dict(sum_number(a_1_0, a_1_1, a_1_2, a_1_3, a_1_4), n_1)

a_2_0 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_2_1 = '\u2B1B\u2B1B\u2B1B\u2B1C'
a_2_2 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_2_3 = '\u2B1C\u2B1B\u2B1B\u2B1B'
a_2_4 = '\u2B1C\u2B1C\u2B1C\u2B1C'
n_2 = 4
a_2 = number_dict(sum_number(a_2_0, a_2_1, a_2_2, a_2_3, a_2_4), n_2)

a_3_0 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_3_1 = '\u2B1B\u2B1B\u2B1B\u2B1C'
a_3_2 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_3_3 = '\u2B1B\u2B1B\u2B1B\u2B1C'
a_3_4 = '\u2B1C\u2B1C\u2B1C\u2B1C'
n_3 = 4
a_3 = number_dict(sum_number(a_3_0, a_3_1, a_3_2, a_3_3, a_3_4), n_3)

a_4_0 = '\u2B1C\u2B1B\u2B1B\u2B1C'
a_4_1 = '\u2B1C\u2B1B\u2B1B\u2B1C'
a_4_2 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_4_3 = '\u2B1B\u2B1B\u2B1B\u2B1C'
a_4_4 = '\u2B1B\u2B1B\u2B1B\u2B1C'
n_4 = 4
a_4 = number_dict(sum_number(a_4_0, a_4_1, a_4_2, a_4_3, a_4_4), n_4)

a_5_0 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_5_1 = '\u2B1C\u2B1B\u2B1B\u2B1B'
a_5_2 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_5_3 = '\u2B1B\u2B1B\u2B1B\u2B1C'
a_5_4 = '\u2B1C\u2B1C\u2B1C\u2B1C'
n_5 = 4
a_5 = number_dict(sum_number(a_5_0, a_5_1, a_5_2, a_5_3, a_5_4), n_5)

a_6_0 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_6_1 = '\u2B1C\u2B1B\u2B1B\u2B1B'
a_6_2 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_6_3 = '\u2B1C\u2B1B\u2B1B\u2B1C'
a_6_4 = '\u2B1C\u2B1C\u2B1C\u2B1C'
n_6 = 4
a_6 = number_dict(sum_number(a_6_0, a_6_1, a_6_2, a_6_3, a_6_4), n_6)

a_7_0 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_7_1 = '\u2B1B\u2B1B\u2B1B\u2B1C'
a_7_2 = '\u2B1B\u2B1B\u2B1C\u2B1B'
a_7_3 = '\u2B1B\u2B1C\u2B1B\u2B1B'
a_7_4 = '\u2B1B\u2B1C\u2B1B\u2B1B'
n_7 = 4
a_7 = number_dict(sum_number(a_7_0, a_7_1, a_7_2, a_7_3, a_7_4), n_7)

a_8_0 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_8_1 = '\u2B1C\u2B1B\u2B1B\u2B1C'
a_8_2 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_8_3 = '\u2B1C\u2B1B\u2B1B\u2B1C'
a_8_4 = '\u2B1C\u2B1C\u2B1C\u2B1C'
n_8 = 4
a_8 = number_dict(sum_number(a_8_0, a_8_1, a_8_2, a_8_3, a_8_4), n_8)

a_9_0 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_9_1 = '\u2B1C\u2B1B\u2B1B\u2B1C'
a_9_2 = '\u2B1C\u2B1C\u2B1C\u2B1C'
a_9_3 = '\u2B1B\u2B1B\u2B1B\u2B1C'
a_9_4 = '\u2B1C\u2B1C\u2B1C\u2B1C'
n_9 = 4
a_9 = number_dict(sum_number(a_9_0, a_9_1, a_9_2, a_9_3, a_9_4), n_9)

# nothing
a = '\u2B1B'

# dot
a_point_0 = '\u2B1B'
a_point_1 = '\u2B1B'
a_point_2 = '\u2B1C'
a_point_3 = '\u2B1B'
a_point_4 = '\u2B1B'
n_point = 1
a_point = number_dict(sum_number(a_point_0, a_point_1,
                      a_point_2, a_point_3, a_point_4), n_point)


# :
a_zero_0 = '\u2B1B'
a_zero_1 = '\u2B1C'
a_zero_2 = '\u2B1B'
a_zero_3 = '\u2B1C'
a_zero_4 = '\u2B1B'
n_zero = 1
a_zero = number_dict(sum_number(a_zero_0, a_zero_1,
                     a_zero_2, a_zero_3, a_zero_4), n_zero)

# dot_position_0
a_dot_0_0 = u"\U0001F7E5"
a_dot_0_1 = '\u2B1B'
a_dot_0_2 = '\u2B1B'
a_dot_0_3 = '\u2B1B'
a_dot_0_4 = '\u2B1B'
n_dot_0 = 1
a_dot_0 = number_dict(sum_number(a_dot_0_0, a_dot_0_1,
                      a_dot_0_2, a_dot_0_3, a_dot_0_4), n_dot_0)

# dot_position_1
a_dot_1_0 = '\u2B1B'
a_dot_1_1 = u"\U0001F7E7"
a_dot_1_2 = '\u2B1B'
a_dot_1_3 = '\u2B1B'
a_dot_1_4 = '\u2B1B'
n_dot_1 = 1
a_dot_1 = number_dict(sum_number(a_dot_1_0, a_dot_1_1,
                      a_dot_1_2, a_dot_1_3, a_dot_1_4), n_dot_1)

# dot_position_2
a_dot_2_0 = '\u2B1B'
a_dot_2_1 = '\u2B1B'
a_dot_2_2 = u"\U0001F7EA"
a_dot_2_3 = '\u2B1B'
a_dot_2_4 = '\u2B1B'
n_dot_2 = 1
a_dot_2 = number_dict(sum_number(a_dot_2_0, a_dot_2_1,
                      a_dot_2_2, a_dot_2_3, a_dot_2_4), n_dot_2)

# dot_position_3
a_dot_3_0 = '\u2B1B'
a_dot_3_1 = '\u2B1B'
a_dot_3_2 = '\u2B1B'
a_dot_3_3 = u"\U0001F7E8"
a_dot_3_4 = '\u2B1B'
n_dot_3 = 1
a_dot_3 = number_dict(sum_number(a_dot_3_0, a_dot_3_1,
                      a_dot_3_2, a_dot_3_3, a_dot_3_4), n_dot_3)

# dot_position_4
a_dot_4_0 = '\u2B1B'
a_dot_4_1 = '\u2B1B'
a_dot_4_2 = '\u2B1B'
a_dot_4_3 = '\u2B1B'
a_dot_4_4 = u"\U0001F7E9"
n_dot_4 = 1
a_dot_4 = number_dict(sum_number(a_dot_4_0, a_dot_4_1,
                      a_dot_4_2, a_dot_4_3, a_dot_4_4), n_dot_4)
