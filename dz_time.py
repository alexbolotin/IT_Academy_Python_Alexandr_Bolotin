import datetime
import dz_time_module_numbers as nu
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

def if_else(x_in,i):
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
        x_out = nu.a_point
    return x_out

x = datetime.datetime.now()
x1 = x.strftime("%H:%M:%S")
# print(x1) 
x3 = {}
for i in range(len(x1)):
    x3[i] = x1[i]
# print(x3)

x4 = {}
for i in range(0,8):
    x4[i] = if_else(x3[i],i)

finish = ''
for j in range(0,5):
    for i in range(0,8):
        finish += nu.a + x4[i][j] + nu.a
    print(finish)
    finish = ''
 