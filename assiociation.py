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
            print(f"The elevator is on the floor{floor}")


    def floor_up(self, floor):



    def floor_down(self, floor):
