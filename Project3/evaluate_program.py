import time
from statistics import mean

def measureTime(function, functionInput: list):
    start_time = time.time()
    function(*functionInput)
    program_time = (time.time() - start_time)
    return program_time