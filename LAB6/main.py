def check(player):
    for i in range(len(player)):
        for j in range(i + 1, len(player)):
            for l in range(j + 1, len(player)):
                if player[i] + player[j] + player[l] == 15:
                    return True
    return False

def final(A, B, numbers):
    if check(A):
        return 1
    elif check(B):
        return 2
    elif len(numbers) == 0:
        return 0
    else:
        return None

def diff_heuristic(current_player, A, B):
    if current_player == 1:
        return -(15 - sum(A))
    else:
        return -(15 - sum(B))

def minimax(A, B, numbers, depth, player):
    if depth == 0 or final(A, B, numbers):
        return diff_heuristic(player, A, B)

    if player == 2:
        max_eval = float('-inf')
        for move in numbers.copy():
            if move not in A + B:
                numbers.remove(move)
                B.append(move)
                eval = minimax(A, B, numbers, depth - 1, 1)
                numbers.append(move)
                B.remove(move)
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in numbers.copy():
            if move not in A + B:
                numbers.remove(move)
                A.append(move)
                eval = minimax(A, B, numbers, depth - 1, 2)
                numbers.append(move)
                A.remove(move)
                min_eval = min(min_eval, eval)
        return min_eval

def ai(current_player, A, B, numbers):
    best_val = float('-inf')
    best_move = None

    for move in numbers.copy():
        if move not in A + B:
            numbers.remove(move)
            B.append(move)
            move_val = minimax(A, B, numbers, 2, 1)
            numbers.append(move)
            B.remove(move)

            if move_val > best_val:
                best_val = move_val
                best_move = move

    numbers.remove(best_move)
    B.append(best_move)
    return 1, B, numbers

A = []
B = []
current_player = 1
winner = None
numbers = [i for i in range(1, 10)]

while True:
    if final(A, B, numbers) is not None:
        winner = final(A, B, numbers)
        print("Winner:", "Player A" if winner == 1 else "Player B" if winner == 2 else "Draw")
        break

    if current_player == 1:
        number_move = int(input("(Player A) Enter a number: "))
        while number_move not in numbers:
            number_move = int(input("(Player A) Again: "))

        numbers.remove(number_move)
        A.append(number_move)
        current_player = 2
    else:
        current_player, B, numbers = ai(current_player, A, B, numbers)
        print("(Player B) AI chooses:", B[-1])