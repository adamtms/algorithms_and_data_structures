import time

def evaluate_program(function, input):
    start_time = time.time()
    function(input)
    print("--- %s seconds ---" % (time.time() - start_time))