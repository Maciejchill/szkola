a = float(input())
b = float(input())
c = float(input())
#  if a + b > c:
#      if c + b > a:
#          if a + c > b:
#              print("to jest tr")
#          else:
#              print("To nie jest tr")
#      else:
#          print ("To nie jest tr")
#  else:
#      print("To nie jest tr")

#  if a + b > c and c + b > a and a + c >b:
#      print("To jest tr")
#  else:
#      print("to nie jest tr")



if a + b > c and c + b > a and a + c >b:
    print("To jest tr")
    if a == b == c:
        print("to jest tr rownoboczny")
    elif a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or b**2 + c**2 == a**2:
        print("to jest tr prostokaktny")
    else:
        print("to jes tr")
else:
    print("to nie jest tr")
if a==b or b==c or a==c:
    print("to nie jest tr rown")
