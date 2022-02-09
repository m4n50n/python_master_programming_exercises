def apple_sharing(nperson, napples):
  one = int(napples / nperson)
  two = napples - (one * nperson)

  return one, two
    
print(apple_sharing(6,50))
