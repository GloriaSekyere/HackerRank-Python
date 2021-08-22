if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    if n >= 2 and n <= 10:
        marks = student_marks[query_name]
        if len(marks) == 3:
            for index, value in enumerate(marks):
                if value >= 0 and value <= 100:
                    average = sum(marks)/len(marks)
                    average_float = f"{average:.2f}"
            print(average_float)
