
def winner(gameBoard):
    # 勝ち手を列挙
    lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    # forで勝ち手を1パターンずつ見ていく
    for i in range(0, len(lines)):
        [a, b, c] = lines[i]
        # 勝ち手の場所に同じ記号が入っていないかを確認
        if gameBoard[a] and gameBoard[a] == gameBoard[b] and gameBoard[a] == gameBoard[c]: 
            # 同じ記号が入っていたら、入っている記号を返す
            return gameBoard[a]
    # どちらも勝っていない場合はNoneを返す
    return None