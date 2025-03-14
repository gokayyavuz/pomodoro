import time
import datetime

# print(time.localtime())

x = 10

for i in range(x):
    secondi = x - i - 1
    print(secondi)
    print(datetime.timedelta(seconds=secondi))
    time.sleep(1)
