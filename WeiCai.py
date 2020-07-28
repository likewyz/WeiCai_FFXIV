#coding: utf-8

lineName = ['横1','横2','横3', '竖1','竖2','竖3', '㇏', '丿']
reward = [10000, 36, 720, 360, 80, 252, 108, 72, 54, 180, 72, 180, 119,36,306,1080,144,1800,3600]

def fun(t,subl):
    result = []
    for l in t:
        for i in range(0, len(t[0]) + 1):
            result.append(l[0:i] + subl + l[i:len(t)])
    return result

def createSequence(inl):
    l = []
    l.append(inl[0:1])
    for i in range(1,len(inl)):
        l = fun(l,inl[i:i+1])
    return l


def rewardOf(sum):
    return reward[sum - 6]

def change(pos, num):
    cai[pos] = num
    posUnknown.pop(posUnknown.index(pos))
    numbersLeft.pop(numbersLeft.index(num))

def h1(l):
    return rewardOf(l[0] + l[1] + l[2])

def h2(l):
    return rewardOf(l[3] + l[4] + l[5])

def h3(l):
    return rewardOf(l[6] + l[7] + l[8])

def v1(l):
    return rewardOf(l[0] + l[3] + l[6])

def v2(l):
    return rewardOf(l[1] + l[4] + l[7])

def v3(l):
    return rewardOf(l[2] + l[5] + l[8])

def dr(l):
    return rewardOf(l[0] + l[4] + l[8])

def dl(l):
    return rewardOf(l[2] + l[4] + l[6])


while(1):

    numbersLeft = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    posUnknown = list(range(0, 9))
    cai = [0] * 9
    Exception = [0] * 8

    for i in range(0, 4):
        pos = int(input("input position >>")) - 1
        num = int(input("the number is >>"))
        change(pos, num)

    table = createSequence(numbersLeft)
    kinds = 120.0
    for sublist in table:
        for i in posUnknown:
            cai[i] = sublist.pop(0)

        Exception[0] += h1(cai) / kinds
        Exception[1] += h2(cai) / kinds
        Exception[2] += h3(cai) / kinds
        Exception[3] += v1(cai) / kinds
        Exception[4] += v2(cai) / kinds
        Exception[5] += v3(cai) / kinds
        Exception[6] += dr(cai) / kinds
        Exception[7] += dl(cai) / kinds
    maxE = max(Exception)
    print(lineName[Exception.index(maxE)] + ' :' + str(int(maxE)))