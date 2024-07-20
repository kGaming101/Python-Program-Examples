import random
import Random_Python_Quiz.additionals as additionals

Temp = "n"
cache = []
cache_2 = []
QnAs = additionals.QnAs
Q = len(QnAs)
QD = 0
GTG = 0
correct = 0
ans = 0
given_2 = []
correct_2 = []
options = ["A","B","C","D"]

print("WELCOME TO THE PYTHON QUIZ")

while Temp.lower() != "y":
  Temp, GTG = additionals.QA(Q)

while QD < GTG:
  QTA = random.randint(0,Q-1)
  if QTA not in cache:
    cache.append(QTA)

    print()
    print("Q.",QD+1,"/",GTG)
    print(QnAs[QTA][0])
    print()

    for i in range(0,4):
      r = random.randint(0,3)
      while r in cache_2:
        r = random.randint(0,3)
      print(options[i],":" , QnAs[QTA][1][r])
      cache_2.append(r)

    pos = cache_2.index(QnAs[QTA][2])
    ans = options[pos]

    print()
    given = input("Enter the letter for the right answer : ")
    print()
    print("=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=")

    if given.upper() == ans:
      correct += 1

    given_2.append(given.upper())
    correct_2.append(ans)

    QD += 1
  cache_2 = []

print("The correct answers were",correct_2)
print("Your answers were",given_2)
print("Final Score:",int(correct/GTG*100),"%")