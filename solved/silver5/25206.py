grade = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,

}

a = 0
b = 0

for _ in range(20):
    name, score, rate = input().split()
    if rate == "P": continue
    a += grade[rate] * float(score)
    b += float(score)

print(round(a / b, 5))
