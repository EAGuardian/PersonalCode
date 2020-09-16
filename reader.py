import csv

def ReaderTips():
    print('''
            for records:
            [0] time, [1] Source, [2] Sport, [3] Destination, 
            [4]dport, [5] protocol, [6] length.\n
            Loader(fileName,T list) loads data from file with name of \'file_name\'
            into list and return the number of records.\n
            ShowAll(list) print everything in list.\n
            GetByTime(start, end, oriList, newList) load data betweent start-end from
            ori_list to new_list and return the number of records loaded.\n
            merge_length(list) merges data with the same [1] Source, [2] Sport, [3] Destination, 
            [4]dport by length addition.
        ''')

def Loader(fileName, list):
    with open(fileName, 'r') as f:
        reader = csv.reader(f)
        print("Successfully opened the file:", fileName)
        print(type(reader))
        i = 0

        print("Started reading...")
        for row in reader:
            list.append(row)
            print(list[i])
            i+=1
        del list[0]
        i-=1
        print("Successfully loaded the file with", i, end='')
        print("records")
        return i

def ShowAll(list):
    for row in list:
        print(row)

def GetByTime(start, end, oriList, newList):
    i = 0
    for row in oriList:
        if float(row[0]) >= start and float(row[0]) <= end:
            newList.append(row)
            i+=1
    print("Successfully loaded by time")
    return i

def MergeLength_1(list, list1):
    print("Start merging...")
    i = 0
    tag = []
    tag.append(list[0][1])
    tag.append(list[0][2])
    tag.append(list[0][3])
    tag.append(list[0][4])
    sum = 0
    n = 0
    while i < len(list):
        if list[i][1] == tag[0] and list[i][2] == tag[1] and list[i][3] == tag[2] and list[i][4] == tag[3]:
            sum += int(list[i][6])
        else:
            tag[0] = list[i][1]
            tag[1] = list[i][2]
            tag[2] = list[i][3]
            tag[3] = list[i][4]
            if (sum>=120):
                list1.append(sum)
                n+=1
            sum = 0
        i+=1
        print(i)
    print("merge done")
    return n

def merge_length_2(list, list1):
    print("Start merging...")
    i = 0
    j = 0
    leng = len(list)
    tag = []
    tag.append(list[0][1])
    tag.append(list[0][2])
    tag.append(list[0][3])
    tag.append(list[0][4])
    sum = 0
    n = 0
    while i < len(list):
        if list[i][1] == tag[0] and list[i][2] == tag[1] and list[i][3] == tag[2] and list[i][4] == tag[3]:
            sum += int(list[i][6])
        else:
            j = i+1
            if (j==leng):
                break
            while (float(list[j][0]) < float(list[i][0])+0.0002):
                if list[i][1] == list[j][1] and list[i][2] == list[j][2] and list[i][3] == list[j][3] and list[i][4] == list[j][4]:
                    i=j
                    break
                if (j+1 < leng):
                    j+=1
            if (i!=j):
                tag[0] = list[i][1]
                tag[1] = list[i][2]
                tag[2] = list[i][3]
                tag[3] = list[i][4]
                if (sum > 0):
                    list1.append(sum)
                    n+=1
                    sum = 0
        i+=1
        print(i)
    print("merge done")
    return n



def GetAverage(list):
    sum = 0
    i = 0
    n = len(list)
    while i < n:
        sum+=int(list[i])
        i+=1
    return sum/n

def GetAverage_1(list):
    sum = 0
    i = 0
    n = len(list)
    while i < n:
        sum+=int(list[i][6])
        i+=1
    return sum/n

def JudegeAttack(list, list1):
    print("Start judging...")
    i = 0
    j = 0
    leng = len(list)
    tag = []
    tag.append(list[0][1])
    tag.append(list[0][2])
    tag.append(list[0][3])
    tag.append(list[0][4])
    sum = 0
    temp = 0
    n = 0
    start = 0
    while i < len(list):
        if list[i][1] == tag[0] and list[i][2] == tag[1] and list[i][3] == tag[2] and list[i][4] == tag[3]:
            sum += int(list[i][6])
            temp+=1
            i+=1
        else:
            i-=1
            j = i + 1
            if (j == leng):
                break
            while (float(list[j][0]) < float(list[i][0]) + 0.0002):
                if list[i][1] == list[j][1] and list[i][2] == list[j][2] and list[i][3] == list[j][3] and list[i][4] == \
                        list[j][4]:
                    i = j
                    break
                if (j + 1 < leng):
                    j += 1
                else:
                    break

            if (i != j):
                if (sum >= temp*5880 and temp>0):
                    list[start][6] = str(sum)
                    print(sum, end='-')
                    print(temp, end='-')
                    print(list[start][0])
                    temp = 0
                    sum = 0
                    list1.append(list[start])
                    n += 1
                    i += 1
                    tag[0] = list[i][1]
                    tag[1] = list[i][2]
                    tag[2] = list[i][3]
                    tag[3] = list[i][4]
                else:
                    temp = 0
                    sum = 0
                    i += 1
                    tag[0] = list[i][1]
                    tag[1] = list[i][2]
                    tag[2] = list[i][3]
                    tag[3] = list[i][4]
                start = i
    print("judege done")
    return n
