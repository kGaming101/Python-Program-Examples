def QA(Q):
  print("How many questions do you want (max:",Q,")")

  GTG = input()

  if GTG.isdigit():
    GTG = int(GTG)
    if len(QnAs) < GTG:
      GTG = len(QnAs)
    elif GTG < 1:
      GTG = 1

  print()
  print("You will be asked",GTG,"questions")

  Temp = input("Is this correct (y/n) : ")

  return Temp, GTG

# How to add your own question
"""
(add comma at the end of the previous bracket pair)
(
  "Question here",
  (
    "A", #Choise 1
    "B", # Choise 2
    "C", # Choise 3
    "D # Choise 4
  ),
  0) # The position of the right answer
"""
QnAs = (
  (
    "Who is the creator of python ?",
    (
      "Bill Gates",
      "Guido van Rossum",
      "James Gosling",
      "Mark Zuckerberg"
   ),
    1),
  (
    "What type of programming language is python ?",
    (
      "Object Oriented Programming Language",
      "Procedural Programming Language",
      "Functional Programming Language",
      "All Of The Available Options"
    ),
    3),
  (
    "How do you make a comment in python ?",
    (
      "// and /*",
      "# and =begin , =end",
      "- - and {- , -}",
      "# and \"\"\"   \"\"\" or \'\'\'   \'\'\'"
    ),
    3),
  (
    "What is a variable ?",
    (
      "A container for storing data values",
      "A container for storing numbers",
      "None of them",
      "I don't know"
    ),
    0),
  (
    "What is 20.0 ?",
    (
      "Integer",
      "String",
      "Float",
      "Boolean"
    ),
    2),
  (
    "Which command prints a random integer ?",
    (
      "print(random())",
      "print(randomNumber())",
      "print(random.randint())",
      "random().print()"
    ),
    2)
)