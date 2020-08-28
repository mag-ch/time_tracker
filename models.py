import sqlite3
from datetime import date, time
import intention
import datetime as DT
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

current_day = date.today().strftime("%m-%d-%y")

conn = sqlite3.connect(':memory:')

cur = conn.cursor()

cur.execute(""" CREATE TABLE tasks (name text, date text, start_time text, end_time text, type text) """)

cur.execute("INSERT INTO tasks VALUES ('write', '09-20-20', '1:30', '3:30', null)")


# STORING METHODS
def store_task(task):
    with conn:
        cur.execute('insert into tasks values(?, ?, ?, ?, ?)',
                    (task.name, current_day, task.startTime, task.endTime, task.type))


def store_all_tasks(list_tasks):
    for t in list_tasks:
        store_task(t)


# RETRIEVAL METHODS
def get_tasks_by_date(date):
    cur.execute('select * from tasks WHERE date == ?', (date,))
    tasks = cur.fetchall()
    return tasks

def get_dur(task):
    cur.execute('SELECT start_time, end_time FROM tasks WHERE name = ?', (task, ))
    times = cur.fetchone()
    return intention.get_dur(times[0], times[1])

def get_times():
    cur.execute('SELECT start_time, end_time FROM tasks')
    return cur.fetchall()

def get_categories():
    cur.execute('SELECT type FROM tasks')
    return cur.fetchall()


# DELETE RECORDS
def del_task(taskname):
    with conn:
        cur.execute('DELETE from tasks WHERE name == ?', (taskname,))


# UPDATE EXISTING RECORDS
def update_time(task_name, endTime):
    with conn:
        cur.execute('UPDATE tasks SET end_time = ? WHERE name = ?', (endTime, task_name))


def update_time_from_dur(task, duration):
    update_time(task.name, intention.get_time(task.startTime, duration))


def set_all_dates(list_tasks, date):
    for t in list_tasks:
        t.date = date
        with conn:
            cur.execute('UPDATE tasks SET date = ? WHERE name = ?', (date, t.name))



t1 = intention.Task("yeah", "3:30", "prod")
t2 = intention.Task("this", "3:00", "fun")
t3 = intention.Task("is", "1:00", "work")
t4 = intention.Task("pretty", "16:45", "food")
t5 = intention.Task("cool", "12:00", "work")

list_tasks = [t1, t2, t3, t4, t5]

store_all_tasks(list_tasks)
set_all_dates(list_tasks, "09-27-2020")
for t in list_tasks:
    update_time_from_dur(t, 30)

print(get_tasks_by_date('09-27-2020'))
print(get_times())

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
# ax.bar(get_categories(),
#        [x.duration for x in list_tasks],
#        color='purple')
# ax.xticks = ([0, 1, 2, 3], get_categories())
#
# # Set title and labels for axes
# ax.set(xlabel="Date",
#        ylabel="Precipitation (inches)",
#        title="Daily Total Precipitation\nJune - Aug 2005 for Boulder Creek")
#
# plt.show()