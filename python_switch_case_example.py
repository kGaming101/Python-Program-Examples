a = input("Pick a movie number : ")

if a.isdigit() :
  a = int(a)
  if a>0 and a<5:
    match a:
      case 1:
        print("You picked Lion King")
      case 2:
          print("You picked The Little Mermaid")
      case 3:
          print("You picked Frozen")
      case 4:
          print("You picked Beauty and the Beast")
  else:
    print("You picked an invalid number")
else:
  print("That wasn't an integer")