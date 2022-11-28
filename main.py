eps = 0.1
def equalList (list1, list2):
    # check if equal
    i = 0
    for d in list1:
        if d != list2[i]:
            return False
        i += 1
    return True

def findMin(list):
    min = float('inf')
    index = 0
    i = 0
    for v in list:
        if v < min and v != -1:
            min = v
            index = i
        i += 1
    list[index] = -1
    return index, min

def checkTotalValue(player1val, player1Div):
    currTotalValue = 0
    for i in range(len(player1Div)):
        currTotalValue = currTotalValue + (player1Div[i] * player1val[i])
    return currTotalValue

def paretoImprove(player1val, player2val, player1Div, player2Div):
    divList1 = player1Div.copy()
    divList2 = player2Div.copy()

    lastTotal1 = checkTotalValue(player1val, player1Div)
    lastTotal2 = checkTotalValue(player2val, player2Div)

    for i in range(len(player1Div)): #add to player1 and sub to player2
        if (player1Div[i] != 0 and player1Div[i] != 1):
            while divList1[i] > 0 and divList2[i] > 0:
                divList1[i] = divList1[i] + eps
                divList2[i] = divList2[i] - eps
                j = i + 1
                last_j_val1 = divList1[j]
                last_j_val2 = divList2[j]
                while divList1[j] > 0 and divList2[j] > 0 and j < len(player1Div):
                    divList1[j] = divList1[j] - eps
                    divList2[j] = divList2[j] + eps
                    total1 = checkTotalValue(player1val, divList1)
                    total2 = checkTotalValue(player2val, divList2)
                    if total1 >= lastTotal1 and total2 >= lastTotal2:
                        return divList1, divList2
                divList1[j] = last_j_val1
                divList2[j] = last_j_val2
    divList1 = player1Div.copy()
    divList2 = player2Div.copy()

    for i in range(len(player1Div)):   #add to player2 and sub to player1
        if (player1Div[i] != 0 and player1Div[i] != 1):
            while divList1[i] > 0 and divList2[i] > 0:
                divList1[i] = divList1[i] - eps
                divList2[i] = divList2[i] + eps
                j = i + 1
                last_j_val1 = divList1[j]
                last_j_val2 = divList2[j]
                while divList1[j] > 0 and divList2[j] > 0 and j < len(player1Div):
                    divList1[j] = divList1[j] + eps
                    divList2[j] = divList2[j] - eps
                    total1 = checkTotalValue(player1val, divList1)
                    total2 = checkTotalValue(player2val, divList2)
                    if total1 >= lastTotal1 and total2 >= lastTotal2:
                        return divList1, divList2
                divList1[j] = last_j_val1
                divList2[j] = last_j_val2
    return "There is no Pareto Improve"



def orderDivide (player1val, player1Div, player2val, player2Div):
    global last_index
    ratio = []
    for i in range(len(player1val)):
        ratio.append(player1val[i]/player2val[i])
    print(ratio)
    bool = True
    init1 = [100]
    init2 = [0]
    res1 = []
    res2 = []

    for i in range(len(player1val)):
        res1.append(1)
        res2.append(0)
    i = 0
    while (bool):
        index, min = findMin(ratio)
        print (index, min)
        if min != -1:
            init1.append(init1[i] - player1val[index])
            init2.append(init2[i] + player2val[index])
            if init1[i] > init2[i]:
                res1[index] = 0
                res2[index] = 1
        if min == -1 or init1[i] == init2[i]:
            bool = False
        if init1[i] < init2[i]:
            x = (init1[i] - init2[i - 1] + player1val[last_index]) / (player1val[last_index] + player2val[last_index])
            print(x)
            res1[i-1] = 1-x
            res2[i-1] = x
            break
        i += 1
        last_index = index
        last_min = min

    print(init1)
    print(init2)
    print(res1)
    print(res2)

    if equalList(res1, player1Div):
        return "Yes"
    else:
        s = paretoImprove(player1val, player2val, player1Div, player2Div)
        return s


if __name__ == '__main__':
    p1v = [15, 15, 40, 30]
    p2v = [40, 25, 30, 5]
    p1d = [0, 0, 0.8, 1]
    p2d = [1, 1, 0.2, 0]
    print(orderDivide(p1v, p1d, p2v, p2d)) # There is no Pareto Improve
    print("\n")

    p1v = [15, 15, 40, 30]
    p2v = [40, 25, 30, 5]
    p1d = [0, 0, 0.9285714285714286, 1]
    p2d = [1, 1, 0.07142857142857142, 0]
    print(orderDivide(p1v, p1d, p2v, p2d)) # Yes
    print("\n")

    p1v = [40, 30, 20, 10]
    p2v = [10, 20, 30, 40]
    p1d = [1, 1, 0, 0]
    p2d = [0, 0, 1, 1]
    print(orderDivide(p1v, p1d, p2v, p2d)) # Yes
    print("\n")

    p1v = [40, 30, 20, 10]
    p2v = [10, 20, 30, 40]
    p1d = [0.7, 0.4, 0, 1]
    p2d = [0.3, 0.6, 1, 0]
    print(orderDivide(p1v, p1d, p2v, p2d)) # find Pareto Improve


