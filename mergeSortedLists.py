def mergeSortedLists(list1, list2, mergedList):
    list1Item = list1[0]
    list2Item = list2[0]

    if len(list1) > 0 or len(list2) > 0:
        if len(list1) == 0:
            mergedList.extend(list2)
            return mergedList
        elif len(list2) == 0:
            mergedList.extend(list1)
            print(mergedList)
        else:
            if list1Item <= list2Item:
                list1Item = list1.pop(0)
                mergedList.append(list1Item)
                if len(list1) == 0:
                    mergedList.extend(list2)
                    print(mergedList)
                else:
                    mergeSortedLists(list1, list2, mergedList)
            elif list1Item >= list2Item:
                list2Item = list2.pop(0)
                mergedList.append(list2Item)
                if len(list2) == 0:
                    mergedList.extend(list1)
                    print(mergedList)
                else:
                    mergeSortedLists(list1, list2, mergedList)
    else:
        print(mergedList)


l1 = [1, 4, 6, 8, 9, 20, 53, 67]
l2 = [2, 3, 5, 7, 11, 19, 77, 88, 91]
l3 = []

mergeSortedLists(l1, l2, l3)
