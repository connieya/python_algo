x ,y  = map(int, input().split())

days = [0 ,0,31,59,90, 120, 151 ,181,212,243,273,304,334,365 ]
weeks = ['SUN','MON','TUE','WED','THU','FRI','SAT']
print(weeks[(days[x]+y )% 7])