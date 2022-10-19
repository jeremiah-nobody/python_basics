def main():
     while True:
          fraction = input("Fraction: ")

          try:
               next = int(convert(fraction))
          except:
               continue
          
          final = gauge(next)

          print(final)
          break




def convert(fraction):
     try:
          a = int(fraction[0])
          b = int(fraction[2])

          if int(fraction[2]) == 0 or fraction[1] != "/":
               pass
          elif "." in fraction:
               pass
          elif fraction[0] > fraction[2]:
               pass
          else:
               c = (float(a) / float(b)) * 100
               return(round(c))

     except:
          return "error"


def gauge(percentage):
     if int(percentage) > 99:
          return 'F'
     elif int(percentage) <= 1:
          return 'E'
     else:
          return f"{percentage}%"

if __name__ == "__main__":
    main()