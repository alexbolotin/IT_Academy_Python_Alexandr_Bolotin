import os

the_board = [i for i in range(1,10)]
the_board_2 = [i for i in range(1,10)]
menu_answers = {'1':'statistic','2':'playgame'}
is_the_user_x = True
is_the_user_0 = False
player_number_x_or_0 = {True: 'X', False: '0'}
move = False

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def generator_player():
    while True:
        for i in range(0,2):
            yield int(i)

def change_player(move):
    change_move = not move
    return change_move

def get_answer(wrong = 0):
    if wrong > 1:
        print('Pls pick the right option:')
    answer = input('Your choice: ')
    return menu_answers.get(answer)

def win_check():
    if (the_board[0] == the_board[1] == the_board[2]) or (the_board[3] == the_board[4] == the_board[5]) or (the_board[6] == the_board[7] == the_board[8]) \
or (the_board[0] == the_board[3] == the_board[6]) or (the_board[1] == the_board[4] == the_board[7]) or (the_board[5] == the_board[5] == the_board[8]) \
or (the_board[0] == the_board[4] == the_board[8]) or (the_board[2] == the_board[4] == the_board[6]):
        result = 'finish'
    elif not the_board_2:
        result = 'draw'
    else :
        result = 'next'
        
    return result
    
    

def show_the_board():
    cls()
    print('    GAME    \n')  
    print(f'{the_board[0]}  |  {the_board[1]}  |  {the_board[2]}')
    print(f'-- | --- | --')
    print(f'{the_board[3]}  |  {the_board[4]}  |  {the_board[5]}')
    print(f'-- | --- | --')
    print(f'{the_board[6]}  |  {the_board[7]}  |  {the_board[8]}\n')

def show_menu(wrong = 0):
    print('__MENU__')
    print('1. SHOW STATISTIC')
    print('2. PLAY THE GAME\n')
    answer = get_answer(wrong)
    while not answer:
        wrong = 2
        cls()
        show_menu(wrong)
        answer = get_answer()
    return answer

def get_user_turn():
    while True:
        try:
            result = win_check()
            if result == 'next':
                global move
                move = change_player(move)
                
                turn = input(f'User {player_number_x_or_0.get(move)} turn (1-9):')
                if int(turn) in the_board_2:
                    print('OK')
                    the_board_2.remove(int(turn))
                    the_board[int(turn)-1] = player_number_x_or_0[move]
                    return turn
                else:
                    print('Enter correct value')

            elif result == 'draw':
                print('End the game\n')
                print('Its a DRAW!')
                turn = 'finish'
                return turn

            elif result == 'finish':
                print('End the game\n')
                print(f'Winner is Player {player_number_x_or_0.get(move)}!')
                turn = 'finish'
                return turn
        except:
            print('Enter correct value') 

                  
def show_statistic():
    print('Showing statistic')

def play_the_game():
    show_the_board()
    while True:
        turn = get_user_turn()
        if turn == 'finish':
            global the_board
            global the_board_2
            the_board_2 = [i for i in range(1,10)]
            the_board = [i for i in range(1,10)]
            break
        else:
            show_the_board()
        


def main():
    cls()
    answer = show_menu()
    if answer == 'statistic':
        show_statistic()
    else: 
        play_the_game()
        input('One more time? :)\nPush any buttom\n')
        main()
    pass


if __name__ == '__main__':
    main()

