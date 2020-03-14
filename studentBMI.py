class Student:
    sid = 'unknown'
    name = 'unknown'
    gender = 'unknown'
    height = 0
    weight = 0
    def __init__(self,sid,name,gender):
        self.sid = sid
        self.name = name
        self.gender = gender
    def set_height(self, h):
        self.height = h
    def set_weight(self, w):
        self.weight = w
    def info(self):
        fmt = '{:10}{:10}{:10}{:10}{:10}'
        return fmt.format(self.sid, self.name, 
            self.gender, self.height, self.weight)

class BMIReport:
    name = 'unknown'
    students = None
    def find(self, sid):
        for st in self.students:
            if st.sid == sid:
                return st
            return None
    def __init__(self, name):
        self.name = name
        self.students = []
    def add(self, st):
        self.students.append(st)
    def remove(self, sid):
        for st in self.students:
            if st:
                self.students.remove(st)
    def update(self, sid, opts={}):
        st = self.find(sid)
            if st:
                if opts.get('name'):
                    st.name = opts.get('name')
                if opts.get('gender'):
                    st.gender = opts.get('gender')
                if opts.get('height'):
                    st.gender = opts.get('height')
                if opts.get('weight'):
                    st.gender = opts.get('weight')
    def pr_report(self):
        for st in self.students:
            print(st.info())
    def save_file(self, filename):
        with open(filename,'w') as f:
            f.write(self.name + '\n')
            for st in self.students:
                f.write(st.info() + '\n')
    def read_file(self, filename):
        with open(filename) as f:
            name = f.readline().strip()
            self.name = name
            for line in f:
                line = line.strip()
                ts = line.split(',')
                st = Student(ts[0], ts[1], ts[2])
                st.set_height(float(ts[3]))
                st.set_weight(float(ts[4]))
                self.add(st)


def test():
    report = BMIReport('Dummy')
    report.read_file('studentBMI.txt')
    report.remove('A03')
    report.update('A02', {'height': 269, 'weight': 99})
    report.pr_report()

    '''report.save_file('test.txt')'''

test()

