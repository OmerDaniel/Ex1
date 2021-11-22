import json
from Elevator import Elevator


class Building:

    def __init__(self, MinFloor = int, MaxFloor =int, Elevators = list, **kwargs):
        self.MaxFloor = MaxFloor;
        self.MinFloor = MinFloor;
        self.Elevators =Elevators;

    def load_from_file(self, file_name):
            try:
                with open(file_name, "r") as f:
                    dict_building = json.load(f)
                    values =dict_building.values()
                    values_list=list(values)
                    self.MinFloor = values_list[0]
                    self.MaxFloor = values_list[1]
                    self.Elevators = values_list[2]
                    MyEle=[]
                for i in range(len(self.Elevators)):
                    values = self.Elevators[i].values()
                    values_list = list(values)
                    elev = Elevator()
                    elev.id=values_list[0]
                    elev.speed = values_list[1]
                    elev.MinFloor=values_list[2]
                    elev.MaxFloor=values_list[3]
                    elev.closetime=values_list[4]
                    elev.opentime=values_list[5]
                    elev.starttime=values_list[6]
                    elev.stoptime=values_list[7]
                    MyEle.append(elev)
                self.Elevators=MyEle

            except FileExistsError as e:
                print(e)
"""
if __name__ == '__main__':
    Building=Building()
    Building.load_from_file("C:/Users/omer/PycharmProjects/Ex1/data/Ex1_input/Ex1_Buildings/B3.json")
    print(Building.Elevators)
    elev=Building.Elevators[0].MaxFloor
    print(elev)
    print(Building.Elevators[1].starttime)
"""
