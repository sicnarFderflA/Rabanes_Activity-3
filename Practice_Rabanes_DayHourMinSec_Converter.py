print("Behold The Seconds Calculator!!!")
print("I can convert seconds to Days/Hours/Minutes/Seconds.")
secs = int(input("Enter Seconds to Convert: "))

# I used formula because im lazy to compute the seconds in days and in hours ^_^ .
day = secs // ((60 * 60) * 24)
rday = secs % ((60 * 60) * 24)
# ((60 * 60) * 24) is the number of seconds each day.

hour = rday // (60 * 60)
rhour = rday % (60 * 60)
# (60 * 60) is the number of seconds per hour.

min = rhour // 60
rsecs = rhour % 60

#ordered it to the highest conversion which is day/s to no conversion needed which is seconds.
print(secs, "Seconds is", day, "Day/s and", hour, "Hour/s and", min ,"Minute/s and", rsecs, "Second/s")