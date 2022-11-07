person = input()
doctor = input()

person_cnt = 0
doctor_cnt = 0
for i in person:
    if i == 'a':
        person_cnt += 1

for j in doctor:
    if j == 'a':
        doctor_cnt += 1

if person_cnt >= doctor_cnt:
    print('go')
else:
    print('no')