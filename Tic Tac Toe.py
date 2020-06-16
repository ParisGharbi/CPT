#Two Player Tic-Tac-Toe game 

Board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in Board:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#Main function which has all gameplay functionality
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(Board)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        #Win/Lose
        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != ' ': # across the top
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif Board['4'] == Board['5'] == Board['6'] != ' ': # across the middle
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['2'] == Board['3'] != ' ': # across the bottom
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ': # down the left side
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ': # down the middle
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['3'] == Board['6'] == Board['9'] != ' ': # down the right side
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif Board['7'] == Board['5'] == Board['3'] != ' ': # diagonal
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['5'] == Board['9'] != ' ': # diagonal
                printBoard(Board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        #Tie
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        #Change player every move
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    #Restart game or not
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            Board[key] = " "

        game()

if __name__ == "__main__":
    game()