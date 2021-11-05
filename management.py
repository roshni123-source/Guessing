# student information system
system=int(input('welcome to student database press 1 for enter your name, press 2 for id number, press 3 for total marks'))
while True:
    if (system == 1):
        student = (input('enter your name'))
        print('your name is:', student)
        break
    elif (system == 2):
        id = int(input('enter your id'))
        print('your id is:', id)
        break
    elif (system == 3):
        score = int(input('enter your score'))
        print('your score is:', score)
        break
    else:
        print('wrong information')


