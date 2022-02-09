def digital_clock(integer):
  hour = int(integer / 60)
  return hour, integer - (hour * 60)  

print(digital_clock(150))
