#Sắp xếp lại công việc theo thời gian giảm dần
def sort_works(a = [],b = []):
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]<a[j]:
                a[i],a[j] = a[j],a[i]
                b[i],b[j] = b[j], b[i]
#Chọn máy cho công việc
def chose_machine(work, a = []):
    min_time = a[0]
    vt = 0
    for i in range(len(a)):
        if a[i]<min_time :
            min_time = a[i]
            vt = i
    a[vt] = a[vt]+work
    return vt

n, m = map(int,input().split())
machines = []  # các máy
id = [] # tên công việc
time = [] # thời gian thực hiện công việc
result = [] # kết quả sắp xếp công việc
# Nhập công việc
for i in range(n):
    work_id, work_time = input().split()
    id.append(work_id)
    time.append(int(work_time))
if n < m:
    print("Thời gian tối thiểu để thực hiện các công việc là:",max(time))
else:
    # Khởi tạo máy và kết quả
    for i in range(m):
        machines.append(0)
        result.append([])
        temp = str(i+1)
        result[i].append("Máy "+temp+":")
    #sắp xếp thời gian giảm dần công việc
    sort_works(time,id)
    # Chọn máy
    while len(time)!=0:
        vt = chose_machine(time[0],machines)
        time.pop(0)
        result[vt].append(id[0])
        id.pop(0)
    print("Thời gian tối thiểu để thực hiện các công việc là:",max(machines))
    print("Công việc được sắp xếp như sau: ")
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end=" ")
        print()

