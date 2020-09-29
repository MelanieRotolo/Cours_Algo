def combi():
  a = 0
  b = 0
  c = 0
  while a<=b<=c:
    while a<=9:
      b=a+1
      while b<=9:
        c=b+1
        while c<=9:
          print (str(a)+str(b)+str(c))
          c=c+1
        b=b+1
      a=a+1
  
combi()