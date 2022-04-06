import sys
avg = 0
for i in range(5):
    score = int(sys.stdin.readline())
    if score < 40:
        score = 40
    avg += score

print(avg // 5)
