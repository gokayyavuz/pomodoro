import time
import datetime
import streamlit as st

# print(time.localtime())

x = 10

# Timer
for i in range(x):
    secondi = x - i - 1
    print(secondi)
    print(datetime.timedelta(seconds=secondi))
    time.sleep(1)

# Auswahlmöglichkeit wie die Zyklen aussehen
