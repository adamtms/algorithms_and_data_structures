from random import randint
from statistics import mean

class Instance():
    __slots__ = ("capacity", "num_items", "items", "weights", "values")

    def __init__(self, capacity, num_items, items) -> None:
        self.capacity: int = capacity
        self.num_items: int = num_items
        self.items: list[tuple[int: 2]] = items
        self.weights: list = [x[0] for x in items]
        self.values: list = [x[1] for x in items]

    def __repr__(self) -> str:
        return f"({self.capacity=}, {self.num_items=}, {self.items=})"
    
    def result_is_correct(self, choosen_elems):
        actual_capacity = 0
        for elem in choosen_elems:
            weight, _ = elem
            actual_capacity += weight
            if actual_capacity > self.capacity:
                return False
        return True

def get_instance(capacity: int = None, num_items: int = 10, weight_range: tuple[int] = (1,10), 
                 value_range: tuple[int] = (1,5)) -> Instance:
    if capacity == None:
        capacity = num_items * mean(weight_range)
    instance = Instance(capacity, num_items,
                [(randint(*weight_range), randint(*value_range)) for i in range(num_items)])
    return instance

if __name__ == "__main__":
    print(get_instance())