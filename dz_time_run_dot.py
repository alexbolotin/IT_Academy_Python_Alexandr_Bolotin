import datetime
import time
import dz_time_module_numbers as nu
import os

def genetator(mig):
     for i in range(10000):
        mig += 1
        yield mig  

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def if_else(x_in,mig):
    if x_in == '0':
        x_out = nu.a_0
    elif x_in == '1':
        x_out = nu.a_1
    elif x_in == '2':
        x_out = nu.a_2
    elif x_in == '3':
        x_out = nu.a_3
    elif x_in == '4':
        x_out = nu.a_4
    elif x_in == '5':
        x_out = nu.a_5
    elif x_in == '6':
        x_out = nu.a_6
    elif x_in == '7':
        x_out = nu.a_7
    elif x_in == '8':
        x_out = nu.a_8
    elif x_in == '9':
        x_out = nu.a_9
    elif x_in == ':':
        if str(mig)[-1] == '0' or str(mig)[-1] == '5':
            x_out = nu.a_dot_0
        elif str(mig)[-1] == '1' or str(mig)[-1] == '6':
            x_out = nu.a_dot_1
        elif str(mig)[-1] == '2' or str(mig)[-1] == '7':
            x_out = nu.a_dot_2
        elif str(mig)[-1] == '3' or str(mig)[-1] == '8':
            x_out = nu.a_dot_3
        elif str(mig)[-1] == '4' or str(mig)[-1] == '9':
            x_out = nu.a_dot_4
    return x_out
    
mig = 0 
m = genetator(mig)
number_column = nu.number_column_1

while True:
    time.sleep(0.1)
    cls()
    clock = datetime.datetime.now()
    time_str = clock.strftime("%H:%M:%S")
    len_time = len(time_str)

    time_dict = {}
    for i in range(len(time_str)):
        time_dict[i] = time_str[i]

    time_dict_paint_numers = {}
    for i in range(0,len_time):
        time_dict_paint_numers[i] = if_else(time_dict[i],mig)

    finish = ''
    for j in range(0,number_column):
        for i in range(0,len_time):
            finish += nu.a + time_dict_paint_numers[i][j] + nu.a
        print(finish)
        finish = ''
    mig = next(m)