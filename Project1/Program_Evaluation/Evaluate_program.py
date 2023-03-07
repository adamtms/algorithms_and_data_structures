import time

def evaluate_program(function, input):
    start_time = time.time()
    function(input)
    program_time = (time.time() - start_time)
    return program_time