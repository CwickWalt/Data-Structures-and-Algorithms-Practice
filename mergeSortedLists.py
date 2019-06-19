def mergeSortedLists(list1, list2, mergedList):
    list1Item = list1[0]
    list2Item = list2[0]
    # if EITHER list1 OR list2 are NOT empty, continue.
    if len(list1) > 0 or len(list2) > 0:
        # if list1 is empty, add list2 onto mergedList and return mergedList.
        if len(list1) == 0:
            mergedList.extend(list2)
            return mergedList
        # if list2 is empty, add list1 onto mergedList and return mergedList.
        elif len(list2) == 0:
            mergedList.extend(list1)
            print(mergedList)
        # if both lists are NOT empty, find the smallest number of each list 
        # at index 0, pop it, then append to mergedList
        else:
            # if list1 contains the smaller number at index 0, pop it from the 
            # list, then append it to mergedList
            if list1Item <= list2Item:
                list1Item = list1.pop(0)
                mergedList.append(list1Item)
                # if the previous operation leaves list1 empty, add list2 to 
                # mergedList and print mergedList
                if len(list1) == 0:
                    mergedList.extend(list2)
                    print(mergedList)
                else:
                    # if list1 is NOT empty, call the function again
                    mergeSortedLists(list1, list2, mergedList)
            # same as above if statement, but repeated for list2
            elif list1Item >= list2Item:
                list2Item = list2.pop(0)
                mergedList.append(list2Item)
                if len(list2) == 0:
                    mergedList.extend(list1)
                    print(mergedList)
                else:
                    mergeSortedLists(list1, list2, mergedList)
    # if line 5 of the function is false, print mergedList
    else:
        print(mergedList)


l1 = [1, 4, 6, 8, 9, 20, 53, 67]
l2 = [2, 3, 5, 7, 11, 19, 77, 88, 91]
l3 = []

mergeSortedLists(l1, l2, l3)
