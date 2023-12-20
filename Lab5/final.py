# Assignment 5
# Implement Minimax algorithm with Alpha-Beta Pruning to solve the Tic-Tac-Toe Problem.

# Group Members:
# Md. Sajid Anam Ifti
# Md. Hasibur Rahman


answer = None

class Solution:
    def isValid(self, board):
        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    return True
        return False

    def result(self, board):
        for row in range(3):
            if (board[row][0] == 'o' and board[row][1] == 'o' and board[row][2] == 'o'):
                return -10
            if (board[row][0] == 'x' and board[row][1] == 'x' and board[row][2] == 'x'):
                return 10

        for col in range(3):
            if (board[0][col] == 'o' and board[1][col] == 'o' and board[2][col] == 'o'):
                return -10
            if (board[0][col] == 'x' and board[1][col] == 'x' and board[2][col] == 'x'):
                return 10

        # Diagonal
        if (board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o'):
            return -10
        if (board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o'):
            return -10

        if (board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x'):
            return 10
        if (board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x'):
            return 10

        return 0

    def minimax(self, board, depth, alpha, beta, isMax):
        global answer
        score = self.result(board)

        if (score != 0):
            return score

        if (self.isValid(board) == False):
            return 0

        if (isMax): #max_a_b_p
            best = float("-inf")
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == '_'):
                        board[i][j] = 'x'
                        value = self.minimax(
                            board, depth + 1, alpha, beta, not isMax)
                        best = max(best, value)
                        alpha = max(alpha, value)
                        board[i][j] = '_'
                        if beta <= alpha:
                            answer = best
                            break
            return best
        else: #min_a_b_p
            best = float("inf")
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == '_'):
                        board[i][j] = 'o'
                        value = self.minimax(
                            board, depth + 1, alpha, beta, not isMax)
                        best = min(best, value)
                        beta = min(beta, value)
                        board[i][j] = '_'
                        if beta <= alpha:
                            answer = best
                            break
            print("Next board can be")
            for i in board:
                print(' '.join(map(str, i)))
            return best

    def findBestMove(self, board, player):
        bestVal = -1000
        bestMove = (-1, -1)
        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    board[i][j] = player
                    moveVal = self.minimax(
                        board, 0, float("-inf"), float("inf"), False)
                    board[i][j] = '_'
                    if (moveVal > bestVal):
                        bestMove = (i, j)
                        bestVal = moveVal
        return (str(bestMove[0]), str(bestMove[1]))


if __name__ == '__main__':
    print('Board = ')

    state = []

    for i in range(0, 3):
        temp = input().split(' ')
        state.append(temp)

    p = str(input('Player = ')).lower()

    if p == 'min':
        player = 'o'
    elif p == 'max':
        player = 'x'

    pos = Solution().findBestMove(state, player)

    if answer == 10:
        print("Draw")
    else:
        x = int(pos[0])
        y = int(pos[1])
        state[x][y] = player
        
        if answer == 0:
            print("Winner is Min.")
        elif answer == -10:
            print("Winner is Max")
        else:
            print("Invalid")

        print("Next board can be")
        for i in state:
            print(' '.join(map(str, i)))