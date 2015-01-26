import csv, datetime
from datetime import date
global today
global number

from flask import Flask, render_template
app = Flask(__name__)

csv_path = './static/deaths2014.csv'
csv_obj = csv.DictReader(open(csv_path, 'r'))
csv_list = list(csv_obj)
csv_dict = dict([[o['id'], o] for o in csv_list])


@app.route('/<today>')
def today():
    today=date.today()
    return today 
@app.route('/<number>')
def number():
    y = date.today()
    x = date(2014, y.month, y.day)
    if x >= date(2014, 12, 1): 
        number=25
    elif x>= date(2014, 10, 18):
        number=24
    elif x>= date(2014, 10, 11):
        number=23
    elif x>= date(2014, 9, 16):
        number=22
    elif x>= date(2014, 9, 5):
        number=21
    elif x>= date(2014, 8, 27):
        number=20
    elif x>= date(2014, 8, 21):
        number=19
    elif x>= date(2014, 8, 20):
        number=18
    elif x>= date(2014, 7, 30):
        number=17
    elif x>= date(2014, 7, 29):
        number=16
    elif x>= date(2014, 7, 8):
        number=15
    elif x>= date(2014, 6, 28):
        number=14
    elif x>= date(2014, 6, 26):
        number=13
    elif x>= date(2014, 4, 24):
        number=11
    elif x>= date(2014, 3, 19):
        number=10
    elif x>= date(2014, 3, 15):
        number=9
    elif x>= date(2014, 3, 12):
        number=8
    elif x>= date(2014, 3, 9):
        number=7
    elif x>= date(2014, 3, 4):
        number=6
    elif x>= date(2014, 2, 26):
        number=5
    elif x>= date(2014, 2, 15):
        number=4
    elif x>= date(2014, 2, 13):
        number=3
    elif x>= date(2014, 2, 4):
        number=2
    elif x>= date(2014, 1, 3):
        number=1		
    return number
@app.route("/")
def index():
    return render_template('index.html',today=today,number=number,
        object_list=csv_list,
    )
if __name__ == '__main__':

    app.run(
        host="0.0.0.0",
        port=8000,
        use_reloader=True,
        debug=True,
    )