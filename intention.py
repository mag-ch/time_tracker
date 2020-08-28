class Task:
    duration = 0

    def __init__(self, name, startTime, tasktype):
        self.name = name
        self.startTime = startTime
        self.endTime = None
        self.date = None
        self.weekday = None
        self.type = tasktype
        self.ongoing = False

    def getDur(self):
        if self.endTime is not None:
            self.duration = abs(string_to_int(self.startTime) - string_to_int(self.endTime))
            return self.duration

def string_to_int(s):
    timef = s.split(":")
    hour = int(timef[0])
    minute = int(timef[1])
    return minute + 60 * hour

def get_dur(t1, t2):
    return abs(string_to_int(t1) - string_to_int(t2))

def get_time(t1, dur):
    mins = string_to_int(t1) + dur
    return str(int(mins/60)) + ":" + "%02d" % ((mins % 60),)

class Schedule:
    def __init__(self, day):
        self.day = day
        self.tasks = []

    def add(self, *tasks):
        for y in tasks:
            self.tasks.append(y)

    def printlist(self):
        for x in self.tasks:
            print(x._name)


# print(get_time("3:34", 1343))
# monday = Schedule("monday")
# monday.add(read, write)
# monday.printlist()