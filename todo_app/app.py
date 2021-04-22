from todo_app.trello_client import get_cards, add_card, move_card

from flask import Flask, render_template, redirect, request

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    cards = get_cards()
    return render_template('index.html', items=cards)

@app.route('/add-item', methods=['POST'])
def create_item():
    item = request.form.get('item')
    add_card(item)
    return redirect('/')

@app.route('/move-item', methods=['POST'])
def move_item():
    cardId = request.form.get('cardId')
    move_card(cardId)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


