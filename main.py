# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from operator import add

def partFind(pc, points, ev, init):
    if not init:
        newPC = pc[-1]
        points[newPC] = 1
        for r in range(1, 4):
            sphereGen3(r, newPC, points, ev)
    else:
        for core in pc:
            points[core] = 1
            for r in range(1, 4):
                sphereGen3(r, core, points, ev)

    minval, foundPC, hold = minfind(points,ev)
    TfoundPC = list(foundPC)
    if minval != 0:
        print(minval, foundPC, pc, 'c')

        for p in hold:
            pc.append(p)
            newpcList = pc.copy()
            print(minval, foundPC, newpcList, 'c')
            pc.pop(-1)
            partFind(newpcList, points, ev, False)



        # for i in range(len(foundPC)):
        #     TfoundPC[i] += 1
        #     if points[tuple(TfoundPC)] == 3:
        #         pc.append(tuple(TfoundPC))
        #         partFind(pc, points, ev, False)
        #         del pc[-1]
        #     TfoundPC[i] -= 2
        #     if points[tuple(TfoundPC)] == 3:
        #         pc.append(tuple(TfoundPC))
        #         partFind(pc, points, ev, False)
        #         del pc[-1]

    else:
        pc.append(foundPC)
        print(minval, foundPC, pc, 'x')



def minfind(points, ev):
    minP = (100,100,100)
    min = 20
    holdmin = []
    for epoint in ev:

        temp = 0
        hold = []
        Tepoint = list(epoint)
        for i in range(len(epoint)):
            Tepoint[i] += 1
            if tuple(Tepoint) in points:
                #print(points[tuple(Tepoint)])
                if points[tuple(Tepoint)] == 3:
                    temp += 1
                    hold.append(tuple(Tepoint))
            Tepoint[i] -= 2
            if tuple(Tepoint) in points:
                # print(points[tuple(Tepoint)])
                if points[tuple(Tepoint)] == 3:
                    temp += 1
                    hold.append(tuple(Tepoint))
            Tepoint[i] += 1

        if temp < min:
            min = temp
            minP = tuple(Tepoint)
            holdmin = hold
    return min, minP, holdmin

def sphereGen3(r, pc, points, ev):
    for x in range(-1*r, r + 1):
        if abs(x) == r:
            place(pc, r, (x,0,0), points, ev)
        else:
            for y in range(abs(x)-r, r-abs(x) + 1):
                z = r - abs(x) - abs(y)
                place(pc, r, (x,y,z), points, ev)
                if abs(y) != (r - abs(x)):
                    place(pc, r, (x, y, -1*z), points, ev)


def place(pc, r, offset, points, ev):
    temp = tuple(map(add, list(pc), list(offset)))
    if temp in points:
        val = points[temp]
        if val > r:
            points[temp] = r
            if (val == 2) != (r == 2):
                if val == 2:
                    ev.remove(temp)
                else:
                    ev.append(temp)
    else:
        if r == 2:
            ev.append(temp)
        points[temp] = r




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("hi")
    partFind([(0, 0, 0), (-3, 0, 0)], {}, [], True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
