import json
import csv
class Calls:
    def __init__ (self,Time=float,Src =int,Dest=int,Status=int,ElevIndex=int,allocatedelevator=int):
        self.Time=Time;
        self.Src=Src;
        self.Dest=Dest;
        self.Status=Status;
        self.ElevIndex=ElevIndex;
        self.allocatedelevator=allocatedelevator;
    def load_from_file(self, file_name):
        allcalls = []
        f = open (file_name, "r")
        reader = csv.reader(f)
        for row in reader:
            call = Calls()
            call.Time = row[1]
            call.Src = row[2]
            call.Dest = row[3]
            call.Status = row[4]
            call.ElevIndex = row[5]
            allcalls.append(call)
        return allcalls

    def __str__(self):
        return str(self.Time)+","+str(self.Src)+","+str(self.Dest)+","+str(self.Status)+","+str(self.ElevIndex)+","\
               +str(self.allocatedelevator)

"""""
if __name__ == '__main__':
    call = Calls()
    test = call.load_from_file("C:/Users/omer/PycharmProjects/Ex1/data/Ex1_input/Ex1_Calls/Calls_a.csv")
    print(type(test))
    print(test)
    print(type(test[0].Dest))
    print(test[0].Dest)
    print(type(test[0].Src))
    print(test[0].Src)
    a = int(test[0].Dest)
    print(a)
    print(type(a))
"""