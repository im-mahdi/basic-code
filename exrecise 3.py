def calculate_student_gpa(grades):
    avg=sum(grades)/len(grades)
    return avg


student_lists=[
    {
        "studen_id":1,
        "name":"Ali",
        "grades":[18,19,19.5]
    },
        {
        "studen_id":2,
        "name":"zahra",
        "grades":[18.5,17,20]
    },
        {
        "studen_id":3,
        "name":"mahdi",
        "grades":[20,19,19.5]
    }

]
for student in student_lists:
    gpa=calculate_student_gpa(student["grades"])
    print(f"GPA {student['name']}: {gpa:.2f}")#.2f یعنی تا دو رقم اعشار دیگه بقیش نمایش داده نمیشه چون بعضیا زیاده اعشارش