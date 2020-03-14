class Student:
    def __init__(self, name, math, chi, eng, bio):
        self.name = name
        self.math = math
        self.chi = chi
        self.eng = eng
        self.bio = bio
    def info(self):
        return '{:<10}{:<10}{:<10}{:<10}{:<10}'. format(self.name, self.math, self.chi, self.eng, self.bio)

def get_math_avg(sts):
    return sum([st.math for st in sts])/ len (sts)
def get_chi_avg(sts):
    return sum([st.chi for st in sts])/ len (sts)
def get_eng_avg(sts):
    return sum([st.eng for st in sts])/ len (sts)
def get_bio_avg(sts):
    return sum([st.bio for st in sts])/ len (sts)

def pr_sts(sts):
    for st in sts:
        print(st.info())

def select_math_larger(sts, score):
    chosen = []
    for st in sts:
        if st.math > score:
            chozen.append(st)
    return chosen

def read_scores():
    with open('students.txt') as f:
        sts = []
        line = f.readline()
        print(line)
        for line in f:
            ts = line.strip().split()
            print(ts)
            st = Student(ts[0], float(ts[1]), float(ts[2]), float(ts[3]), float(ts[4]))
            sts.append(st)
            print(st.info())


    math_avg = get_math_avg(sts)
    chi_avg = get_chi_avg(sts)
    eng_avg = get_eng_avg(sts)
    bio_avg = get_bio_avg(sts)
    fmt = '{:<10}{:<10}{:<10}{:<10}{:<10}'
    print(fmt.format('Avg:', math_avg, chi_avg, eng_avg, bio_avg))

    print('-' * 69)
    lst1 = select_math_larger(sts, 70)
    pr_sts(lst1)

read_scores()