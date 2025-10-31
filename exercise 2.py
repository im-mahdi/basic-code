def min_core(scores):
    avg = sum(scores) / len(scores)

    if avg >= 17:
        print("That's great :)")
    elif 12 < avg < 17:
        print("Good :)")
    else:
        print("False :(")

n = int(input("Enter the number of courses: "))

scores = []
for i in range(n):
    s = float(input(f"Please enter score for course {i+1}: "))
    scores.append(s)

min_core(scores)