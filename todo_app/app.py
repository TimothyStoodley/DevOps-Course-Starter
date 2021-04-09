from flask import Flask, render_template, redirect, request

from todo_app.data.session_items import get_item, get_items, add_item, save_item

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

@app.route('/add-item', methods=['POST'])
def create_item():
    item = request.form.get('item')
    add_item(item)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
