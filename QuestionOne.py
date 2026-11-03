
import time
from random import choice


Day = time.strftime("%A")
Month = time.strftime("%B")

Numbers = list(range(50, 81))

# Picking 6 random Numbers
lucky_number = []
for i in range(6):
    lucky_number.append(str(choice(Numbers)))

# Output
print("The Lucky Numbers for", Day + ",", Month, "are --->", " ".join(lucky_number))
