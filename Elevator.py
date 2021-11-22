class Elevator:

    def __init__(self ,id=int ,MinFloor=int, MaxFloor=int,closetime=int,opentime=int,speed=int
                 ,starttime=int,stoptime=int,listofcalls=list):
        self.id=id;
        self.MinFloor=MinFloor;
        self.MaxFloor=MaxFloor;
        self.opentime=opentime;
        self.closetime=closetime;
        self.speed=speed;
        self.starttime=starttime;
        self.stoptime=stoptime;
        self.listofcalls=listofcalls;

    def calctime(self):
        time = 0

        if len(self.listofcalls) == 0:
            return time
        for i in range(len(self.listofcalls)):
            a=int(self.listofcalls[i].Src)
            b=int(self.listofcalls[i].Dest)
            time += 2*self.stoptime + 2*self.starttime + 2*self.closetime + 2*self.opentime + self.speed * (abs(a-b))
        return time
    def createlist (self):
        mylist = []
        self.listofcalls=mylist


