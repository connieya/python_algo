# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import Counter


def solution(S):
    # Implement your solution here
    size = len(S)
    counter = Counter(S)
    odd = 0
    even = 0
    if len(counter) == 1:
        for key in counter:
            if counter[key] % 2 == 1: return 1
            return 0

    for value in counter:
        if counter[value] % 2 == 1:
            odd += 1
        else:
            even += 1
    if size % 2 == 1:
        cnt = 0
        for key in counter:
            if counter[key] % 2 == 1:
                cnt += 1
        return cnt

    if odd == 0: return 0
    answer = 0
    for key in counter:
        if counter[key] % 2 == 1:
            answer += 1

    return answer
    pass


# S = "aaccd"
# S = "xxxaa"
# S ="ddssaa"
# S ="axaxcdx"
S ="aaaddxa"
print(solution(S))