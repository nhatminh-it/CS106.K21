#Chọn người cho công việc
def chose_people(a, time, id):
    min_time = a[0]
    vt = 0
    for i in range(len(a)):
        if a[i]<min_time :
            min_time = a[i]
            vt = i
    if len(id)>1:
#sắp xếp tăng dần thời gian làm việc của người được chọn và sắp xếp thời gian làm việc của những công việc khác theo mảng này.
        for i in range(len(time[vt])):
            for j in range(i + 1, len(time[vt])):
                if time[vt][i] > time[vt][j]:
                    time[vt][i], time[vt][j] = time[vt][j], time[vt][i]
                    id[i], id[j] = id[j], id[i]
                    for k in range(m):
                        if k!=vt:
                            time[k][i], time[k][j] = time[k][j], time[k][i]
#thêm việc đã chọn vô mảng
    a[vt] = a[vt] + time[vt][0]
    return vt
n, m = map(int,input().split())
people = []  # các người thực hiện công việc
id = [] # tên công việc
time = [] # thời gian thực hiện công việc
result = [] # kết quả sắp xếp công việc
for i in range(m):
    time.append([])
# Nhập công việc
for i in range(n):
    work_id, *work_time = input().split()
    id.append(work_id)
    for j in range(m):
        time[j].append(int(work_time[j]))
# Khởi tạo người làm và kết quả
for i in range(m):
    people.append(0)
    result.append([])
    temp = str(i+1)
    result[i].append("Người thứ "+temp+":")
# Chọn máy
while len(id)!=0:
    vt = chose_people(people,time, id)
    time[vt].pop(0)
    result[vt].append(id[0])
    id.pop(0)
    for i in range(m):
        if i!=vt:
            time[i].pop(0)
print("Thời gian tối thiểu để thực hiện các công việc là:",max(people))
print("Công việc được sắp xếp như sau: ")
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=" ")
    print()
