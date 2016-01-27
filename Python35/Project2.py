# Dmitriy Gutnik 77099786 and
import connectfour

def print_board(board:list):
    for i in range(-1,connectfour.BOARD_ROWS):
        temp = ''
        for x in range(0,connectfour.BOARD_COLUMNS):
            if (i == -1):
                temp += str(x+1) + ' '
            else:
                if (board[x][i] == connectfour.NONE):
                    temp += '. '
                elif(board[x][i] == connectfour.RED):
                    temp += 'R '
                else:
                    temp += 'Y '
        print(temp)

def main():
    game = connectfour.new_game()
    while connectfour.winner(game)==connectfour.NONE:
        print_board(game[0])
        temp = ''
        if (game.turn == 1):
            temp = 'RED'
        else:
            temp = "YELLOW"
        user = input('It is ' + temp + "'s turn. What would you like to do (Syntax : 'MANEVUER COLUMN'):")
        print(len(str.split(user)))
        while  len(str.split(user)) !=2 and (str.split(user)[0] == 'pop' or str.split(user)[0] == 'drop') == False or (int(str.split(user)[1]) > 7 or int(str.split(user)[1]) < 1):
            user = input('It is ' + temp + "'s turn. What would you like to do (Syntax : 'MANEVUER COLUMN'):")
        if (str.split(user)[0] == 'pop'):
            game = connectfour.pop(game,int(str.split(user)[1])-1)
        else:
            game = connectfour.drop(game,int(str.split(user)[1])-1)
    print_board(game[0])
    print('THE WINNNER IS PLAYER ' + str(connectfour.winner(game)))

if __name__ == "__main__":
    main()
