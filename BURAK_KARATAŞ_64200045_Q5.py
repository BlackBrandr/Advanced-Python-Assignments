import random
import time

array = [] # CREATE ARRAY
for ZAMAN in range(0,25,1):
    array.append(random.randint(0,100))

def DECORATER_TIME_FUNCTION(function):
    def TWO(MY_LIST):
        t = time.time() # START TIME
        start = time.time() # STARTS TIMER
        function(MY_LIST)  # EXECUTE TIMER
        finish = time.time()  # ENDS TIMER
        print((finish - start))
        return finish - start
    return TWO

@DECORATER_TIME_FUNCTION
def SORTBUBLE(array):  # BUBBLE SORT ALGORITHM
    ARRAY_SIZE = len(array)
    for ELEMENT in range(ARRAY_SIZE):
        for ELEMENT2 in range(0, ARRAY_SIZE - ELEMENT - 1):
            if array[ELEMENT2] > array[ELEMENT2 + 1]:
                array[ELEMENT2], array[ELEMENT2 + 1] = array[ELEMENT2 + 1], array[ELEMENT2]


print('BEFORE_BUBBLE_SORT ',array)  # NOT SORTED ARRAY
print("EXECUTION_TIME")
SORTBUBLE(array)
print('AFTER_BUBBLE_SORT ', array)  # SORTED ARRAY

