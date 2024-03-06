if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    value=str(sum(student_marks[query_name])/3)
    print('{0:1.2f}'.format(float(value)))
    
# github:@coding-viper
