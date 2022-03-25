data = []
output = ['--- Customer Detail ---','Name : ','Address : ','Gender : ','Tel : ']

for i in range(5):
    infor_ = input()
    data.append(infor_)
for j in range(5):
    if j == 0:
        print(output[0])
    elif j == 1:
        print(output[1] + data[0] + ' ' + data[1])
    else:
        print(output[j] + data[j] )
