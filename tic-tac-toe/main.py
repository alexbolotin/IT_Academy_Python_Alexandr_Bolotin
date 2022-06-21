import os

the_board = [i for i in range(1,10)]


menu_answers = {'1':'statistic','2':'playgame'}
is_the_user_x = True
is_the_user_0 = False
TURNS = {True: 'X', False: '0'}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_answer():
    answer = input('Your choice: ')
    return menu_answers.get(answer)

def show_the_board():
    cls()
    print(f'{the_board[0]}  |  {the_board[1]}  |  {the_board[2]}')
    print(f'-- | --- | --')
    print(f'{the_board[3]}  |  {the_board[4]}  |  {the_board[5]}')
    print(f'-- | --- | --')
    print(f'{the_board[6]}  |  {the_board[7]}  |  {the_board[8]}')

def show_menu():
    print('__MENU__')
    print('1. SHOW STATISTIC')
    print('1. PLAY THE GAME\n')

    answer = get_answer()

    while not answer:
        print('Pls pick the right option:')
        answer = get_answer()
        cls()
    return answer


def get_user_turn():
    while True:
        try:
            turn = input(f'User {TURNS.get(is_the_user_x)} turn (1-9):')
            if int(turn) in range(1,10):
                print('OK')
                return turn #X or 0
            else:
                print('Enter correct value')
        except:
            print('Enter correct value') 

                  
def show_statistic():
    print('Showing statistic')

def play_the_game():
    print('Playing  the game')
    show_the_board()
    while True:
        turn = get_user_turn()

def main():
    cls()
    answer = show_menu()
    if answer == 'statistic':
        show_statistic()
    else: 
        play_the_game()
    pass






if __name__ == '__main__':
    main()

