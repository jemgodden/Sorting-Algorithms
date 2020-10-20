import time


sortingAlgNames = ["Bubble Sort", "Comb Sort", "Insertion Sort", "Selection Sort", "Quick Sort", "Merge Sort",
                   "Shell Sort", "Heap Sort"]


def printList(valList):
    '''
    Prints all values in list in current order. Values are tab separated.
    :param valList: List of values.
    '''
    for value in valList:
        print(value, "\t", end='')
    print("\n")


def __checkList(sortedValList, valList):
    '''
    Checks that the list has been correctly sorted by the written function by comparing lengths and each element to the
    same list sorted by in-built Python sorting function. Raise an exception if this is the case.
    :param sortedValList: List sorted by written function.
    :param valList: Original form of list being sorted.
    '''
    sortedList = sorted(valList)

    if len(sortedList) != len(sortedValList):
        raise Exception("Error: The length of the list has been changed, indicating that values were removed.")

    for i in range(len(sortedValList)):
        if sortedList[i] != sortedValList[i]:
            raise Exception("Error: The list was incorrectly sorted. The correctly sorted list has {} at element {}, "
                            "whereas the list sorted by one of the written algorithms has {}.".format(sortedList[i], i,
                                                                                                      sortedValList[i]))


def findTimeTaken(func):
    '''
    Decorator to time how long a function (func()) takes to run.
    '''
    def __timeWrapper(valList):
        # Time how long the func() takes to run.
        startTime = time.time()
        sortedValList = func(valList)
        endTime = time.time()

        # Check that the list is correctly sorted.
        __checkList(sortedValList, valList)

        return endTime - startTime
    return __timeWrapper


def __swap(valList, i, j):
    '''
    Swaps the values of two variables.
    :param valList: List including elements to be swapped.
    :param i: Index of first element to be swapped.
    :param j: Index of second element to be swapped.
    '''
    valList[i], valList[j] = valList[j], valList[i]


def __bubblePass(valList):
    '''
    Conducts one pass of the Bubble sort algorithm on a list.
    :param valList: List of values in current state.
    :return done: Boolean to say if the list is in ascending order.
    '''
    # Boolean initially set to True and is proved otherwise.
    done = True

    for i in range(len(valList) - 1):
        if valList[i] > valList[i + 1]:
            # Sets done variable to False if any numbers have to be changed.
            done = False
            __swap(valList, i, i + 1)

    return done


@findTimeTaken
def bubbleSort(valList):
    '''
    Sorts the list using the Bubble Sort algorithm.
    :param valList: List of values to be sorted.
    :return timeTaken: The time taken for the list to be sorted.
    '''
    # Boolean to indicate when list is sorted.
    done = False

    while not done:
        done = __bubblePass(valList)

    return valList


def __combPass(valList, gap):
    '''
    Conducts a single pass of the Comb Sort algorithm on a list.
    :param valList: List of values in current state.
    :param gap: Distance between two elements who are compared and potentially swapped.
    '''
    # Boolean initially set to True and is proved otherwise.
    done = True

    for i in range(len(valList) - gap):
        if valList[i] > valList[i+gap]:
            __swap(valList, i, i + gap)
            done = False

    return done


@findTimeTaken
def combSort(valList):
    '''
    Sorts the list using the Comb Sort algorithm.
    :param valList: List of values to be sorted.
    :return timeTaken: The time taken for the list to be sorted.
    '''
    # Shrink factor is the value used to change gap between compared values.
    shrinkFactor = 1.23
    gap = int(len(valList) / shrinkFactor)

    # Boolean to indicate when list is sorted.
    done = False

    while not done:
        done = __combPass(valList, gap)

        if gap > 1:
            # Gap value cannot fall below 1.
            gap = int(gap / shrinkFactor)

    return valList


@findTimeTaken
def insertionSort(valList):
    '''
    Sorts the list using the Insertion Sort algorithm.
    :param valList: List of values to be sorted.
    :return timeTaken: The time taken for the list to be sorted.
    '''
    # Begins second value in the list, to compare to values previous to current.
    for i in range(1, len(valList)):
        # Use temp variable to store the position of current value being inspected.
        temp = i
        for j in range(i-1, -1, -1):
            if valList[temp] < valList[j]:
                __swap(valList, temp, j)
                temp -= 1
            else:
                # Stop loop once initial value has found correct place in list.
                break

    return valList


@findTimeTaken
def selectionSort(valList):
    '''
    Sorts the list using the Selection Sort algorithm.
    :param valList: List of values to be sorted.
    :return timeTaken: The time taken for the list to be sorted.
    '''
    # Iterate over all but last element, which will be in correct position by that point.
    for i in range(len(valList) - 1):
        # Initialising where the location of minimum value in list is.
        minLoc = i
        for j in range(i, len(valList)):
            if valList[j] < valList[minLoc]:
                # Update location of minimum value in list if smaller value found in unsorted part of list.
                minLoc = j
        # Puts smallest value of unsorted list in earliest position, sorting it.
        __swap(valList, i, minLoc)

    return valList


def __quickSortRecursive(valList):
    '''
    Recursive function used to sort a list during the Quick Sort algorithm. The pivot is set as the last element in
    each list passed into function. Should only be called by itself and quickSort().
    :param valList: List of values to be sorted.
    :return sortedList: list of values passed into function in ascending order.
    '''
    if len(valList) <= 1:
        return valList

    # Pivot is set at each call to last element.
    pivot = valList[-1]
    lowValList = []
    highValList = []

    for i in range(len(valList)-1):
        # Sorts list into two sub-lists of values smaller and bigger than the pivot value.
        if valList[i] <= pivot:
            lowValList.append(valList[i])
        elif valList[i] > pivot:
            highValList.append(valList[i])

    # Calls itself if both sub-lists are larger than one element, returning it's concatenated result.
    return __quickSortRecursive(lowValList) + [pivot] + __quickSortRecursive(highValList)


@findTimeTaken
def quickSort(valList):
    '''
    Sorts the list using the Quick Sort algorithm.
    :param valList: List of values to be sorted.
    :return timeTaken: The time taken for the list to be sorted.
    '''
    # Calls recursive function to sort list.
    return __quickSortRecursive(valList)


def __mergeSortRecursive(valList):
    '''
    Recursive function used to sort a list during the Merge Sort algorithm. The pivot is set as the last element in
    each list passed into function. Should only be called by itself and mergeSort().
    :param valList: List of values to be sorted.
    :return sortedList: list of values passed into function in ascending order.
    '''
    if len(valList) == 1:
        # Checks size of list and returns if it cannot be split anymore.
        return valList
    else:
        mid = len(valList) // 2
        # Recursive function called until each sub-list is one element long.
        leftValList = __mergeSortRecursive(valList[:mid])
        rightValList = __mergeSortRecursive(valList[mid:])

        newValList = []
        i = j = 0

        while i < len(leftValList) and j < len(rightValList):
            # Comparing first value from each list to see which should be put in new list first.
            if rightValList[j] <= leftValList[i]:
                newValList.append(rightValList[j])
                j += 1
            else:
                newValList.append(leftValList[i])
                i += 1

        # Puts in all remaining values from lists.
        while i < len(leftValList):
            newValList.append(leftValList[i])
            i += 1
        while j < len(rightValList):
            newValList.append(rightValList[j])
            j += 1

        return newValList


@findTimeTaken
def mergeSort(valList):
    '''
    Sorts the list using the Merge Sort algorithm.
    :param valList: List of values to be sorted.
    :return timeTaken: The time taken for the list to be sorted.
    '''
    # Calls recursive function to sort list.
    return __mergeSortRecursive(valList)


@findTimeTaken
def shellSort(valList):
    '''
    Sorts the list using the Shell Sort algorithm.
    :param valList: List of values to be sorted.
    :return timeTaken: The time taken for the list to be sorted.
    '''
    h = len(valList) // 2
    # Once a pass has been completed at h=1, the list will be sorted.
    while h > 0:
        for i in range(h, len(valList)):
            # Loop from the element h and compare to all elements before it.
            for j in range(i, h-1, -h):
                # If it swaps with the element h elements before it, then go back h elements again and compare.
                if valList[j] < valList[j-h]:
                    __swap(valList, j, j - h)
                else:
                    break
        # Change the value of h after each pass.
        h = h // 2

    return valList


def __heapify(valList, n, i):
    '''
    Recursive function to convert the list into a binary heap.
    :param valList: List of values to be sorted.
    :param n: Length of list.
    :param i: List element correlating to root node of binary heap.
    '''
    # Element location of left and right children of root/parent node.
    left = 2 * i
    right = (2 * i) + 1
    # Initialise the root node as being the element with the largest value.
    largest = i

    if left < n and valList[left] > valList[i]:
        # Check if left child node is present and set reassign list element with largest value if necessary.
        largest = left

    if right < n and valList[right] > valList[largest]:
        # Check if right child node is present and set reassign list element with largest value if necessary.
        largest = right

    if largest != i:
        # If the largest value is not the root node, swap the necessary values in the list.
        __swap(valList, i, largest)
        # Call itself to ensure that the heap has the largest values at the top.
        __heapify(valList, n, largest)


@findTimeTaken
def heapSort(valList):
    '''
    Sorts the list using the Heap Sort algorithm.
    :param valList: List of values to be sorted.
    :return timeTaken: The time taken for the list to be sorted.
    '''
    n = len(valList)
    for i in range((n // 2) - 1, -1, -1):
        # Convert list into a binary heap, with all the largest value at the top.
        __heapify(valList, n, i)

    for i in range(n - 1, 0, -1):
        # Move large values to the end of the list and re.
        __swap(valList, 0, i)
        __heapify(valList, i, 0)

    return valList
