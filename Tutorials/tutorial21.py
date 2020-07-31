# time module
import time

# Calculate while loop execution time Vs for loop execution time
initial = time.time()
print(initial)
for i in range(45):
    print(f'{i}', end=' ')

print('\nFor loop time in ', time.time() - initial, 'second')
initial2 = time.time()
i = 0
while i < 45:
    print(i, end=' ')
    i += 1
print('\nwhile loop time in ', time.time() - initial2, 'second')

# Local time
locatime = time.asctime(time.localtime(time.time()))
print(locatime)  # Output -> Tue Jul 21 14:11:55 2020

time.sleep(2)  # after 2second next code execute
print('Sleep function')