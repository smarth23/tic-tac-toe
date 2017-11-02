#Display Board
def board_print(dict):
    print('--------------')
    print('Board location reference:')
    print('')
    print(' ', dict['l1'], ' | ', dict['l2'],' | ', dict['l3'], ' ')
    print('--------------------------')
    print(' ', dict['l4'], ' | ', dict['l5'],' | ', dict['l6'], ' ')
    print('--------------------------')
    print(' ', dict['l7'], ' | ', dict['l8'],' | ', dict['l9'], ' ')
    print('')

def update_board(mv,ch):
    if ch == 'x':
        di={mv:'x'}
        return di
    elif ch == 'o':
        di={mv:'o'}
        return di



def print_turn(n,dict):
    print('Move:Player',n+1)
    print('--------------')
    print('')
    if n == 0:
        mv = input('enter location for "x" :')
        dict[mv]='x'
        return dict
        #di = update_board(mv, 'x',)
    elif n == 1:
        mv = input('enter location for "o" :')
        #di = update_board(mv, 'o')
        dict[mv]='o'
        return dict



#New_Dict
def create_new_dict():
    my_dict={'l1':' ','l2':' ','l3':' ','l4':' ','l5':' ','l6':' ','l7':' ','l8':' ','l9':' '}
    #my_dict=dict.fromkeys(['1':'a', '2', 'l3', 'l4','l5','l6','l7','l8','l9'])
    #my_dict_2={}
    return my_dict

def win(dict):
    if 'x'== dict['l1'] == dict['l2']== dict['l3'] or 'o'== dict['l1'] == dict['l2']== dict['l3']:
        return True
    elif 'x'== dict['l4'] == dict['l5']== dict['l6'] or 'o'== dict['l4'] == dict['l5']== dict['l6']:
        return True
    elif 'x'== dict['l7'] == dict['l8']== dict['l9'] or 'o'== dict['l7'] == dict['l8']== dict['l9']:
        return True
    elif 'x'== dict['l1'] == dict['l4']== dict['l7'] or 'o'== dict['l1'] == dict['l4']== dict['l7']:
        return True
    elif 'x'== dict['l2'] == dict['l5']== dict['l8'] or 'o'== dict['l2'] == dict['l5']== dict['l8']:
        return True
    elif 'x'== dict['l3'] == dict['l6']== dict['l9'] or 'o'== dict['l3'] == dict['l6']== dict['l9']:
        return True
    elif 'x'== dict['l1'] == dict['l5']== dict['l9'] or 'x'== dict['l1'] == dict['l5']== dict['l9']:
        return True
    elif 'x'== dict['l3'] == dict['l5']== dict['l7'] or 'x'== dict['l3'] == dict['l5']== dict['l7']:
        return True


def Begin():
    print('Please follow the reference board for player moves')
    board_start=create_new_dict()
    board_print(board_start)
    n = 1
    count=0
    while count<9:
        n=1-n
        updated_board=print_turn(n,board_start)
        #print(updated_board)
        board_print(updated_board)
        check=win(updated_board)
        if check == True:
            print('You Won')
            break
    count +=1



print('Welcome to the game of Tic Tac Toe')
print('Player 1 is "X" and Player 2 is "Y"')
main_in=input('To start the game press y: ')
if main_in == 'y':
    Begin()

