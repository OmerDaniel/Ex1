from Building import Building
from Elevator import Elevator
from Calls import Calls

class MyElevAlgo:
    def __init__(self, building =Building):
        self.building =building;


    def calctime(self,elev:Elevator):
        time = 0
        if len(elev.listofcalls) == 0:
            return time
        for i in range(len(elev.listofcalls)):
            a=int(elev.listofcalls[i].Src)
            b=int(elev.listofcalls[i].Dest)
            time += 2*elev.stoptime + 2*elev.starttime + 2*elev.closetime + 2*elev.opentime + elev.speed * (abs(a-b))
        return time


    def allocateAnElevator (self, a:Calls):
        elevlist = self.building.Elevators
        if len(elevlist) == 1:
            if type(elevlist[0])==type:
                elevlist[0].createlist
            elevlist[0].listofcalls.append(a)
            a.allocatedelevator = 0
            return 0
        if (type(elevlist[0].listofcalls) == type):
            for i in range(len(elevlist)):
                elevlist[i].createlist()

        chosenelevindex = 0
        for i in range(len(elevlist)):
            if i > 0:
                if self.calctime(elevlist[i]) < self.calctime(elevlist[chosenelevindex]):
                    chosenelevindex = i
        elevlist[chosenelevindex].listofcalls.append(a)
        a.allocatedelevator = chosenelevindex
        return chosenelevindex





if __name__ == '__main__':
    print("enter your building json file path in the line below:")
    s=input()
    print("enter your calls csv file path in the line below:")
    s1=input()
    str(s)
    str(s1)
    mybuilding=Building()
    mybuilding.load_from_file(s)
    call = Calls()
    test = call.load_from_file(s1)
    algo=MyElevAlgo(mybuilding)
    f = open("output.csv", "w")
    for i in range(len(test)):
       algo.allocateAnElevator(test[i])
       f.write(test[i].__str__())
       f.write("\n")
    f.close()

