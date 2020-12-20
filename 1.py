Picture = [
   [0,0,0,1,0,0,0],
   [0,0,1,1,1,0,0],
   [0,1,1,1,1,1,0],
   [1,1,1,1,1,1,1],
   [0,0,0,1,0,0,0],
   [0,0,0,1,0,0,0]
]

for image in Picture:
  for pixel in image:
    if (pixel):
      print('*',end ="")
    else:
      print(' ', end ="")
    print('')
