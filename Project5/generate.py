from random import randint

class Instance:
    def __init__(self, capacity, num_items, items) -> None:
        self.capacity: int = capacity
        self.num_items: int = num_items
        self.items: list[tuple[int: 2]] = items
        self.weights: list = [x[0] for x in items]
        self.values: list = [x[1] for x in items]

    def __repr__(self) -> str:
        return f"({self.capacity=}, {self.num_items=}, {self.items=})"

def get_instance(capacity: int = 20, num_items: int = 10, weight_range: tuple[int] = (1,10), 
                 value_range: tuple[int] = (1,5)) -> Instance:
    instance = Instance(capacity, num_items,
                [(randint(*weight_range), randint(*value_range)) for i in range(num_items)])
    return instance

if __name__ == "__main__":
    print(get_instance())