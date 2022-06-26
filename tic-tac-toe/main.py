import os


the_board = [i for i in range(1,10)]
the_board_2 = [i for i in range(1,10)]
menu_answers = {'1':'statistic','2':'playgame'}
is_the_user_x = True
is_the_user_0 = False
player_number_x_or_0 = {True: 'X', False: '0'}
move = False
statistic_game = {'X':0, '0':0}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def change_player(move):
    change_move = not move
    return change_move

def get_answer(wrong = 0):
    if wrong != 0:
        print('Pls pick the right option:')
    answer = input('Your choice: ')
    return menu_answers.get(answer)

def show_menu():
    print('__MENU__')
    print('1. SHOW STATISTIC')
    print('2. PLAY THE GAME\n')

def player_choice():
    show_menu()
    answer = get_answer()
    while not answer:
        wrong = 1
        cls()
        show_menu()
        answer = get_answer(wrong)
    return answer

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

def get_user_turn():
    while True:
        try:
            result = win_check()
            if result == 'next':
                global move
                move = change_player(move)

                turn = input(f'User {player_number_x_or_0.get(move)} turn (1-9):')
                while not int(turn) in the_board_2:
                    print('Enter a free value')
                    turn = input(f'User {player_number_x_or_0.get(move)} turn (1-9):')

                print('OK')
                the_board_2.remove(int(turn))
                the_board[int(turn)-1] = player_number_x_or_0[move]
                return turn

            elif result == 'draw':
                print('End the game\n')
                print('Its a DRAW!')
                turn = 'finish'
                return turn

            elif result == 'finish':
                print('End the game\n')
                print(f'Winner is Player {player_number_x_or_0.get(move)}!')
                statistic_game[player_number_x_or_0.get(move)] += 1
                turn = 'finish'
                return turn
        except:
            print('Enter correct value')
            move = change_player(move) 

  
def show_statistic():
    print('Showing statistic:')
    print(statistic_game)
    input('Lets continue? :)\nPush any buttom\n')
    main()

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
    answer = player_choice()
    if answer == 'statistic':
        show_statistic()
    else: 
        play_the_game()
        input('One more time? :)\nPush any buttom\n')
        main()
    pass

if __name__ == '__main__':
    main()

