if __name__ == '__main__':
    
    N = int(input())
    if N >= 2 and N <= 5:
        all_students = []
        scores = []
        
        # Read input and generate list of records
        for _ in range(N):
            name = input()
            score = float(input())
            scores.append(score)
            all_students.append([name, score])
        
        # Find second lowest score
        scores.sort()
        lowest = min(scores)
        for i in range(len(scores)-1, -1, -1):
            if scores[i] != lowest:
                second_lowest = scores[i]
    
        # Print students with the second lowest score
        second_lowest_students = []
        for student in all_students:
            if student[1] == second_lowest:
                second_lowest_students.append(student[0])
        second_lowest_students.sort()
        for student in second_lowest_students:
            print(student)
        
