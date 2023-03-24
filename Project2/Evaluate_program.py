import time
from statistics import mean

def measureTime(function, functionInput):
    start_time = time.time()
    function(*functionInput)
    program_time = (time.time() - start_time)
    return program_time

# def evaluate_program(sort, input_generator, input_size=5_000):
#     times = []
#     for _ in range(10):
#         sample_input = input_generator(input_size)
#         time = measure_time(sort, sample_input)
#         times.append(time)
#     return mean(times)