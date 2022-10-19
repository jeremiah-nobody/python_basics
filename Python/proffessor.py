import random

values = [1, 2, 3]




def main():
     check = 0
     score = 0
     level = get_level()
     
     for i in range(10):
          check = 0
          a = generate_integer(level)
          b = generate_integer(level)

          while True:

               try:
                    answer = int(input(f"{a} + {b} = "))
                    if answer == a + b:
                         pass
                    else:
                         check+=1
                         print("EEE")
                         continue
                         
                    break
               except:
                    check += 1
                    pass
          if check == 0:
               score+=1
          else:
               pass
     print(f"Score: {score}")



     generate_integer(level)


def get_level():
     while True:
          try:
               level = int(input("Level: "))
               if level not in values:
                    continue
               break
          except:
               pass
     return level


def generate_integer(level):
     if level == 1:
          num = random.randint(0, 9)
          return num
     elif level == 2:
          num = random.randint(0, 99)
          return num
     elif level == 3:
          num = random.randint(9, 999)
          return num
     else:
          return ValueError


if __name__ == "__main__":
    main()