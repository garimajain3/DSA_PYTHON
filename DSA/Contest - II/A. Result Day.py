n = int(input())
marks = list(map(int,input().split()))
pass_mark = int(input())


pass_student = 0
fail_student = 0

for i in range(len(marks)):
    if(marks[i]>=pass_mark):
        pass_student+=1
    else:
        fail_student+=1
print(f'Pass: {pass_student}')
print(f'Fail: {fail_student}')