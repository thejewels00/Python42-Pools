
from datetime import datetime

now = datetime.now()
epoch_time = now.timestamp()
print("Seconds since January 1, 1970:", epoch_time,"or" ,"{:.2e}".format(epoch_time), "in scientific notation")

print(now.strftime("%b %d %Y"))
