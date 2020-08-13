# Function caching
# store the value in cache by using these program run fast

import time
from functools import lru_cache

@lru_cache(maxsize=3)  # Decorator with how many value stored maxsize = n
def somework(n):
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running somework")
    somework(4)
    somework(2)
    somework(7)
    print('Done.... Calling again')
    somework(4) # Does not required to wait 4 sec again bcz these value are already present in cache
    print('Called again')
