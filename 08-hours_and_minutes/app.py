def hours_minutes(secs):
  minutes = int(secs / 60)
  hour = int((secs / 60) / 60)
  
  return hour, minutes

print(hours_minutes(3900))
