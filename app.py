from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# List to store the to-do items
todos = []

@app.route('/')
def home():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    # Get the to-do item from the form
    todo_item = request.form.get('todo')
    
    # Add the item to the list
    if todo_item:
        todos.append(todo_item)
    
    # Redirect back to the homepage
    return redirect(url_for('home'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    # Remove the item from the list by its index
    if 0 <= todo_id < len(todos):
        todos.pop(todo_id)
    
    # Redirect back to the homepage
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
