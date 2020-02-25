from flask import Flask, render_template, request, redirect, url_for
import task3_kutsil

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('account_search.html')

    if request.method == 'POST':
        if not request.form.get("acct"):
            return render_template('empty.html')
        result = task3_kutsil.fmain(request.form['acct'])
        if result == 'OK':
            return redirect(url_for('maps'))
        elif result == 'There is no user with such name':
            return render_template('noname.html')
        elif result == 'This user has no friends':
            return render_template('nofriends.html')

@app.route('/map')
def maps():
    return render_template("Friends.html")

@app.route('/error_empty', methods=['GET'])
def empty():
    render_template('empty.html')


@app.route('/error_nofriends', methods=['GET'])
def nofriends():
    render_template('nofriends.html')


@app.route('/error_noname', methods=['GET'])
def noname():
    render_template('noname.html')
