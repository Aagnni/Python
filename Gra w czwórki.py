ROWS = 6
COLUMNS = 7

def main():



    board = [["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"]]

    printBoard(board)
    
    playerName1 = inputPlayerName()
    playerName2 = inputPlayerName()
    playerToken1 = "C"
    playerToken2 = "Z"

    gameOver = False
    turn = 0
    while gameOver == False:
        if turn == 0:
            col = chooseCol(board, playerName1)
            row = checkAvailableRow(board, col)
            insertToken(board, col, row, playerToken1)
            printBoard(board)
            if reverseMove(board, col, row):
                turn -= 1
            if checkGameOver(board, playerToken1):
                gameOver = True
                print(f'Koniec gry, wygral gracz {playerName1}')
                saveGameResult(board, playerName1)
        else:
            col = chooseCol(board, playerName2)
            row = checkAvailableRow(board, col)
            insertToken(board, col, row, playerToken2)
            printBoard(board)
            if reverseMove(board, col, row):
                turn -= 1
            if checkGameOver(board, playerToken2):
                gameOver = True
                print(f'Koniec gry, wygral gracz {playerName2}')
                saveGameResult(board, playerName2)

        if checkTie(board):
            gameOver = True
            print(f'Koniec gry, remis!')
            saveGameResult(board, None)
        
        
        turn += 1
        turn %= 2



def inputPlayerName():
    playerName = input("Imię pierwszego gracza: ")
    print(f'Witaj {playerName}')
    return playerName

def printBoard(board):
    print("1 2 3 4 5 6 7")
    for row in range(ROWS):
        for column in range(COLUMNS):
          print(board[row][column],end=" ")
        print("")

def chooseCol(board, playerName):
    col = inputCol(playerName)
    while checkCol(board, col) == False:
        print(f'Kolumna {col+1} jest pelna, wybierz inna kolumne')
        col = inputCol(playerName)
    return col

def inputCol(playerName):
    col = int(0)
    while (col < 1 or col > 7):
        col = int(input(f'{playerName} podaj numer kolumny [1-7] do której chcesz wrzucić krążek: '))
    print(f'Wybrana kolumna: {col}')
    return col-1

def checkCol(board, col):
    return board[0][col] == "-"

def checkAvailableRow(board, col):
    row = len(board) - 1
    available = False
    while(available == False):
        if board[row][col] != "-":
            row -= 1
        else:
            available = True
    return row

def insertToken(board, col, row, token):
    board[row][col] = token


def checkGameOver(board, token):
    if checkColWin(board, token) or checkRowWin(board, token) or checkDiagWin(board, token):
        return True

def checkTie(board):
    fullColumns = 0
    for column in range(COLUMNS):
        if not checkCol(board, column):
            fullColumns += 1
    if fullColumns == COLUMNS:
        return True

def checkColWin(board, token):
    for row in range(ROWS-3):
        for column in range(COLUMNS):
            if token == board[row][column] == board[row+1][column] == board[row+2][column] == board[row+3][column]:
                return True

def checkRowWin(board, token):
    for row in range(ROWS):
        for column in range(COLUMNS-3):
            if token == board[row][column] == board[row][column+1] == board[row][column+2] == board[row][column+3]:
                return True

def checkDiagWin(board, token):
    for row in range(ROWS-3):
        for column in range(COLUMNS-3):
            if token == board[row][column] == board[row+1][column+1] == board[row+2][column+2] == board[row+3][column+3]:
                return True
    for row in range(ROWS-3):
        for column in range(3, COLUMNS):
            if token == board[row][column] == board[row+1][column-1] == board[row+2][column-2] == board[row+3][column-3]:
                return True

def reverseMove(board, col, row):
    answer = input("Czy chcesz cofnac swój ruch?[T/N] ")
    if answer.lower() == "t" or answer.lower() == "tak" or answer.lower() == "true":
        board[row][col] = "-"
        print("Ruch cofnięty.")
        printBoard(board)
        return True

def saveGameResult(board, playerName):
    file = open("result.txt",'w')

    file.write("1 2 3 4 5 6 7" + "\n")
    for row in range(ROWS):
        fileRow = ""
        for column in range(COLUMNS):
            fileRow += (board[row][column] + " ")
        file.write(fileRow + "\n")
    if playerName:
        file.write(f'Koniec gry, wygral gracz {playerName}')
    else:
        file.write(f'Koniec gry, remis!')
    
    file.close()


main()