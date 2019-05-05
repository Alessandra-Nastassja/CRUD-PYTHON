from flask import Flask

app = Flask(__name__) 

# Routes of direcition for URL  

@app.route('/')
def Index():
    return 'Hello World'

@app.route('/add_contact')
def add_contact():
    return 'add contact'

@app.route('/edit')
def edit_contact():
    return 'edit_contact'

@app.route('/delete')
def delete_contact():
    return 'delete_contact'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)