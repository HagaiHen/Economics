
def median (list):
    return list[int(len(list)/2)]

def add2votes(c, t, n):
    ans = []
    for i in range(n-1):
        ans.append((i+1)*t*c) # Linear function
    return ans


def fun (list1, list2, list3, budget):
    iter = 0

    # Range of t
    left = 0
    right = 1

    t = (left+right)/2
    sumOfMedians = 0

    OriginalList1 = list(list1)
    OriginalList2 = list(list2)
    OriginalList3 = list(list3)

    ans = []

    while sumOfMedians != budget:

        print("\n ======================================= Iter # " + str(iter) +"\n")
        print("t = ", t)
        votes = add2votes(budget, t, 3)
        print("Added Votes ", votes)
        for i in range(2):
            list1.append(votes[i])
            list2.append(votes[i])
            list3.append(votes[i])

        list1.sort()
        list2.sort()
        list3.sort()

        print("List 1: " ,list1)
        print("List 2: ", list2)
        print("List 3: ", list3)

        sumOfMedians = median(list1) + median(list2) + median(list3)

        print("Sum of Medians: ", sumOfMedians)

        if sumOfMedians > budget: # we want to
            right = t
            t = (right + left)/2
        else:
            if sumOfMedians < budget:
                left = t
                t = (right + left) / 2
            else:
                ans.append(median(list1))
                ans.append(median(list2))
                ans.append(median(list3))

        list1 = list(OriginalList1)
        list2 = list(OriginalList2)
        list3 = list(OriginalList3)

        iter += 1


    print()
    return ans





if __name__ == '__main__':
    list1 = [30, 0, 0]
    list2 = [0, 15, 15]
    list3 = [0, 15, 15]
    print("The chosen Budget is:", fun(list1, list2, list3, 30))