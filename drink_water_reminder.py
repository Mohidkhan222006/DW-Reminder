from datetime import datetime
from plyer import notification
c=datetime.now()
current_time=c.strftime("%H:%M")
print(current_time)
set_hours=int(input("enter hours"))
set_min=int(input("enter min"))
settime=f"{set_hours:02d}:{set_min:02d}"
if current_time==settime:
    notification.notify(title="SUBJECT:WATER REMINDER",message="drink water!!!!",timeout=100)
else:
    print("stay hydrated")
