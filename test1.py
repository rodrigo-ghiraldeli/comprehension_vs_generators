import time

def list_comprehension():
    squares = [x ** 2 for x in range(10_000_000)]
    for square in squares:
        if square > 1000:
            return square

def generator_expression():
    squares = (x ** 2 for x in range(10_000_000))
    for square in squares:
        if square > 1000:
            return square

for function in list_comprehension, generator_expression:
    start_time = time.time()
    function()
    duration = time.time() - start_time
    print(f"{function.__name__} took {duration:0.5f} seconds")
