from datetime import datetime
from intention import *
from flask import *
from models import *
#export FLASK_APP=hello.py
app = Flask(__name__)


@app.route('/')
def start():
    return render_template("index.html")


@app.route('/tracker')
def day():
    return render_template("start_page.html")


@app.route('/tracker/<day>', methods=['GET', 'POST'])
def track(day):
    # Instantiates days of the week
    week = {
        "0": "Monday",
        "1": "Tuesday",
        "2": "Wednesday",
        "3": "Thursday",
        "4": "Friday",
        "5": "Saturday",
        "6": "Sunday"
    }
    weekday = request.form.get("weekday")
    index = datetime.strptime(weekday, '%Y-%m-%d').weekday()
    var = week[str(index)]

    if request.method == 'GET':
        # display the stuff onto the schedule
        tasks = get_tasks_by_date()
        pass

    if request.method == 'PUT':
        # create task and store it to the database
        task = Task(request.form.get('task'))
        store_task(task)

    # Displays the tasks on a schedule
    today = Schedule
    return render_template("track_day.html", day=weekday, day_of_the_week=var, tasks=tasks)
