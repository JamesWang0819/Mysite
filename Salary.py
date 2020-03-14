class SalaryRecord:
    name = 'unknown'
    work_hours = None
    wage = 0
    def __init__(self, name):
        self.name = name
        self.work_hours = [0 for i in range()]
    def workHour(self, day, hour):
        self.work_hours[days] = hour
    def setWage(self, wage):
        self.wage = wage
    def weekWage(self):
        total_hours = sum(self.work_hours)
        return self.wage * total_hours

def read_file():
    with open('Salary.txt') as f:
        first = f.readline()
        for line in f:
            line = line.strip()
            tokens = line.split()
            wr = SalaryRecord(tokens[0])
            for i in range(1,7):
                wr.workHour(i, float(tokens[i]))
                wr.setWage(float(tokens[-1]))
            print(wr.name, wr.weekWage())



read_file()



























