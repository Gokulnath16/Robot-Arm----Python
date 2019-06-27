import json

with open("test.json") as json_file:
        json_data = json.load(json_file)
        print(json_data)
        list_robot=[]
        list_you = []
        list_1 = []
        for i in range(0, len(json_data)):
            list_robo = json_data[i]['robot']
            list_yo = json_data[i]['you']
            list_robot.append(list_robo)
            list_you.append(list_yo)
        print("List Robot", list_robot)
        print("List You",list_you)
        y = list_you[-1]
        z = list_robot[-3:]
        z.append(y)
        z.reverse()
        list_1.append(''.join(str(i) for i in z))
        a, b, c = -2, -4, -1
        for i in range(0,len(list_you)-3):
            y=list_you[a]
            z=list_robot[b:c]
            z.append(y)
            z.reverse()
            list_1.append(''.join(str(i) for i in z))
            a-=1
            b-=1
            c-=1
        print("List_1",list_1)
        count = 0
        for i in range(0,len(list_1)-1):
            if list_1[i] == list_1[i+1]:
                count+=1
        count = count%3
        if count == 0:
            print("0")
        elif count == 1:
            print("1")
        else:
            print("2")
