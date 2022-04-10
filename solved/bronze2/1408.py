import sys

sys.stdin = open('input.txt')
h1, m1, s1 = map(int, sys.stdin.readline().split(":"))
h2, m2, s2 = map(int, sys.stdin.readline().split(":"))

s2 -= s1
if s2 < 0:
    s2 += 60
    m2 -= 1

m2 -= m1
if m2 < 0:
    m2 += 60
    h2 -= 1

h2 -= h1
if h2 <0:
    h2 +=24


print("%02d:%02d:%02d"%(h2,m2,s2))