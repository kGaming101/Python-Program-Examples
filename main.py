a = input("""
What python file do you want to run?
------------------------------------
              Options
------------------------------------
1 - Python Switch Case Example
2 - Random Number Guessing Game
3 - Random Python Quiz
4 - Automatic Rock Paper Scissors
------------------------------------
       Enter Number (1-4)
------------------------------------
""")

print("------------------------------------")
if a.isdigit():
  a = int(a)
  if a == 1:
    import python_switch_case_example
    print("------------------------------------")
  elif a == 2:
    import random_number_guessing_game
    print("------------------------------------")
  elif a == 3:
    import Random_Python_Quiz.random_python_quiz
    print("------------------------------------")
  elif a == 4:
    import automatic_rock_paper_scissor
    print("------------------------------------")
  else:
    print("That wasn't an option")
    print("------------------------------------")
else:
  print("That wasn't an integer")
  print("------------------------------------")
print("Program Closing")