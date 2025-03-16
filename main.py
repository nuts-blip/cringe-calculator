import random
import string
import math
inp = input("On?")
Used = 0
while string.capitalize(inp) != "On":
  inp = input("On?")
if string.capitalize(inp) == "On":
  while inp != "off":
    inpu = input("Equation")
    if Used == 3:
      print("You okay bro?!")
    if Used == 5:
      print("Why you using the calculator??? You too stupid?")
    if Used == 7:
      print("WHY YOU USING ME??? YOU ARE SO BAD AT MATH YO GONNA FAIL YO MATH TEST! I quit...GET HELP FROM YO FATHER WHO GONNA GIVE YO A BEATING")
      break
    Used += 1
    
    if "+" in inpu:
      Ans = int(inpu.split("+")[0])+int(inpu.split("+")[1])
      if Ans > 9:
        l = list(str(Ans))
        random.shuffle(l)
        print(''.join(l))
      else:
        b = bin(Ans)
        print(b)
    elif "-" in inpu:
      Ans = int(inpu.split("-")[0])-int(inpu.split("-")[1])
      if Ans > 9:
        l = list(str(Ans))
        random.shuffle(l)
        print(''.join(l))
      else:
        b = bin(Ans)
        print(b)
    elif "x" in inpu:
      Ans = int(inpu.split("x")[0])*int(inpu.split("x")[1])
      if Ans > 9:
        l = list(str(Ans))
        random.shuffle(l)
        print(''.join(l))
      else:
        b = bin(Ans)
        print(b)
    elif "*" in inpu:
      Ans = int(inpu.split("*")[0])*int(inpu.split("*")[1])
      if Ans > 9:
        l = list(str(Ans))
        random.shuffle(l)
        print(''.join(l))
      else:
        b = bin(Ans)
        print(b)
    elif "**" in inpu:
      Ans = int(inpu.split("+")[0])**int(inpu.split("*")[1])
      if Ans > 9:
        l = list(str(Ans))
        random.shuffle(l)
        print(''.join(l))
      else:
        b = bin(Ans)
        print(b)
    elif "^" in inpu:
      first, last = inpu.split("^")
      Ans = int(first)**int(last)
      if Ans > 9:
        l = list(str(Ans))
        random.shuffle(l)
        print(''.join(l))
      else:
        b = bin(Ans)
        print(b)
    elif "/" in inpu:
      secret_to_zero = True
      if int(inpu.split("/")[1]) == 0:
        print("Hey! Are you stupid, you can't divide by zero!")
        Ans = 0
      else:
        Ans = float(int(inpu.split("/")[0])/int(inpu.split("/")[1]))
      if Ans > 9 and secret_to_zero:
        l = list(str(Ans))
        random.shuffle(l)
        print(''.join(l))
      else:
        b = float(int(inpu.split("/")[0])*int(inpu.split("/")[1]))
        print(b)