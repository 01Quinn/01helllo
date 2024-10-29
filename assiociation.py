# 1
class Elevator:

    def __init__(self, num_top, num_bottom):
        self.num_top = num_top
        self.num_bottom = num_bottom
        self.new_elevator = num_bottom

    def go_to_floor(self,floor):
        if floor < self.num_bottom or floor > self.num_top:
            print("Error!")
            return
        if floor > self.new_elevator:
            self.floor_up(floor)
        elif floor < self.new_elevator:
            self.floor_down(floor)
        else:
            print(f"The elevator is on {floor}")


    def floor_up(self, floor):
        while self.new_elevator < floor:
            self.new_elevator += 1
            print(f"The elevator is moving from {floor}to the floor{self.new_elevator}")


    def floor_down(self, floor):
        while self.new_elevator > floor:
            self.new_elevator -= 1
            print(f"The elevator is moving from {floor}to {self.new_elevator}")

# 2
class Elevator:

    def __init__(self, num_top, num_bottom):
        self.num_top = num_top
        self.num_bottom = num_bottom
        self.new_elevator = num_bottom

    def go_to_floor(self,floor):
        if floor < self.num_bottom or floor > self.num_top:
            print("Error!")
            return
        if floor > self.new_elevator:
            self.floor_up(floor)
        elif floor < self.new_elevator:
            self.floor_down(floor)
        else:
            print(f"The elevator is on the floor{floor}")


    def floor_up(self, floor):
        while self.new_elevator < floor:
            self.new_elevator += 1
            print(f"The elevator is on the floor{floor}")


    def floor_down(self, floor):
        while self.new_elevator > floor:
            self.new_elevator -= 1
            print(f"The elevator is on the floor{floor}")

class Building:
    def __init__(self, floor):
        self.floor = floor


    def run_elevator(self, number_of_elevators, destination_floor):

elevators = []
