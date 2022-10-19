def main():
     courses = int(input("How many courses: "))
     scores = get_score(courses)
     cgp_a = cgpa(scores)
     print(cgp_a)

def get_score(courses):
     scores = {}
     for i in range(courses):
          unit = int(input("unit: "))
          score = int(input("score: "))
          if score >= 70:
               grade = 5
          elif score >= 60 and score <= 69:
               grade = 4
          elif score >= 50 and score <= 59:
               grade = 3
          elif score >= 45 and score <= 49:
               grade = 2
          elif score >= 40 and score <= 44:
               grade = 1
          else:
               grade = 0
          scores[f"{unit}"] = grade
     return scores


def cgpa(scores):
     x = 0
     tu = 0
     for unit, score in scores.items():
          x += int(unit) * int(score)
          tu += int(unit)
     cgpa = round(x / tu)
     return cgpa

main()