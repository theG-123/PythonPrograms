#Updated in real time progress program

import time

for i in range(1, 101):
    print(f"Progress: {i}%", end='\r')
    time.sleep(0.2)

print("\nDone!")