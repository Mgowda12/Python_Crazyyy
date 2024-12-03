# This message sender will send messages to your friend continuosly to annoy ur friend in whats app
# run this code and put the cursor in the chat window of your friend in whats app and press enter to send message

import pyautogui as pg
import time
import random


animals=['Dog','cat','donkey']
time.sleep(8)

for i in range(20):
  a=random.choice(animals)
  pg.write(f"You are a {a}")
  pg.press('enter')

