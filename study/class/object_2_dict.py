def create_student(name , korean, math ,english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

students = [
    create_student("윤인성",87,98,88,95),
    create_student("연하진",98,98,96,98),
    create_student("구지연",76,96,94,90),
    create_student("나선주",98,92,96,92),
    create_student("윤아린",95,98,98,98),
    create_student("윤명월",64,88,92,92),
]

print(students[0])
print(students[2])

print(students[1]["math"])