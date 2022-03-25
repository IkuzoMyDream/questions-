subject_score = []
subject_output = ['THAI','MATH','ENGLISH','SCIENCE','SPORT']

for i in range(5):
    subject_input = float(input())
    subject_score.append(subject_input)
for j in range(5):
    print(subject_output[j] + ' ' + '=' + ' ' + str(subject_score[j]))

gpa = sum(subject_score) / 5
print('---')
print('GPA' + ' ' + '=' + ' ' + str(gpa))
