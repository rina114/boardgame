from flask import Flask, render_template, request
import re
from game import winner

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=["GET", "POST"])
def game():

    if request.method == "GET":
        # 盤面をリセット
        new_board = [i for i in range(1, 10)] 
        win = 0

    elif request.method == "POST":
        # どのマスが押されたか
        i = int(request.form["row"])
        j = int(request.form["col"])
        board = request.form["board"]
        
        # 文字列としてリストを受け取っているため、リストに戻す
        new_board = re.sub("[\[\]']", "",  board)
        new_board = new_board.split(', ')
        
        if (board.count('○') + board.count('×'))%2 == 0:
            # 先攻の番
            new_board[i*3+j] = '○'
        else:
            # 後攻の番
            new_board[i*3+j] = '×'
        
        win = winner(new_board)
            
    return render_template('game.html', board=new_board, winner=win)

if __name__ == "__main__":
    app.run(debug=True)