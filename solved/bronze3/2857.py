import sys

answer = []
for i in range(1,6):
    sentence = sys.stdin.readline().rstrip()
    if "FBI" in sentence:
        answer.append(i)

if answer:
    print(*answer)
else:
    print("HE GOT AWAY!")