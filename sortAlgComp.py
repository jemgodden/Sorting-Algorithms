from sortAlgs import *
import random
import matplotlib.pyplot as plt
import argparse

'''
This program compares the run-time for the implemented sorting algorithms in sortAlgs.py.

It generates numerous sized lists, containing values between 0-100, and takes the time taken for each algorithm to sort 
them, eventually plotting a log-log graph of the results, as well as the average time taken to sort a single element. 

Due to the random nature of of the generated lists, some sorting algorithms will have particular trouble with certain 
lists, that others may not have. In order to combat this, the user can specify a command line argument for how many 
lists of each sized should be generated and timed in order to get a mean average time taken to sort a list of size n.

A typical command line using this option would look like:

>>> python sortAlgComp.py -r 5
or 
>>> python sortAlgComp.py --repeats 5

This will do 5 unique n-sized lists to be sorted by each algorithm.
'''


def generateVals(n):
    '''
    Generate n-length list of ints with random values between 1-100.
    :param n: Desired size of list.
    :return valTuple: Tuple containing all values in list.
    '''
    return tuple(random.randrange(0, 100) for _ in range(n))


def plotData(nVals, sortTimes):
    '''
    Plots the timings of each sorting function against the size of the list being sorted. Allows for comparisons to be
    made. Uses the library matplotlib.
    :param nVals: List of list sizes being sorted.
    :param sortTimes: A list of lists, with each sublist containing information on how long each sorting algorithm took
                      to run for each size list.
    '''
    # Initialising look of the plot.
    fig, ax = plt.subplots()
    ax.set_xlabel("Number of Elements in List, $n$", fontsize=28, weight='bold')
    ax.set_ylabel("Time Taken to Sort $(seconds)$", fontsize=28, weight='bold')
    # Set the axis to scale logarithmically for a linear view of relationship.
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.tick_params(length=5, width=3, labelsize=24)

    # Plotting the actual data all with different colours and labels.
    ax.plot(nVals, sortTimes[0], 'b', linewidth=5, label='Bubble Sort')
    ax.plot(nVals, sortTimes[1], 'g', linewidth=5, label='Comb Sort')
    ax.plot(nVals, sortTimes[2], 'r', linewidth=5, label='Selection Sort')
    ax.plot(nVals, sortTimes[3], 'c', linewidth=5, label='Insertion Sort')
    ax.plot(nVals, sortTimes[4], 'm', linewidth=5, label='Shell Sort')
    ax.plot(nVals, sortTimes[5], 'y', linewidth=5, label='Quick Sort')
    ax.plot(nVals, sortTimes[6], 'k', linewidth=5, label='Merge Sort')
    ax.plot(nVals, sortTimes[7], 'saddlebrown', linewidth=5, label='Heap Sort')

    # Show legend on plot for clarity.
    ax.legend(loc='upper left', fontsize=22)
    plt.show()


def printTimePerElement(nVals, sortTimes):
    '''
    Prints the average time taken for each sorting algorithm to sort a single element.
    :param nVals: List of list sizes being sorted.
    :param sortTimes: A list of lists, with each sublist containing information on how long each sorting algorithm took
                      to run for each size list.
    '''
    for i in range(len(sortingAlgNames)):
        avgTimePerElement = 0

        for j in range(len(nVals)):
            # Summing the average time taken to sort each length list.
            avgTimePerElement += sortTimes[i][j] / nVals[j]

        # Print the sum of average time taken, divided by number of discrete length lists.
        print("\nThe {} algorithm took an average of {:.2g} seconds to sort a single element."
              .format(sortingAlgNames[i], (avgTimePerElement / len(nVals))))


def main():
    parser = argparse.ArgumentParser()
    # Read in a single command line argument to determine how many lists of length n should be sorted and timed, in
    # order to find an average sorting time.
    parser.add_argument('-r', '--repeats', type=int, nargs='?', default=3,
                        help='Specify number of repeats to conduct')
    args = parser.parse_args()
    noRepeats = args.repeats

    # Discrete sizes of lists to be sorted.
    nVals = [25, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800]
    sortTimes = [[] for _ in range(len(sortingAlgNames))]

    for n in nVals:
        avgTimes = [0 for _ in range(len(sortingAlgNames))]

        # Loop for number of strings of n length to be sorted, specified by command line argument.
        for _ in range(noRepeats):
            valTuple = generateVals(n)

            avgTimes[0] += bubbleSort(list(valTuple))
            avgTimes[1] += combSort(list(valTuple))
            avgTimes[2] += selectionSort(list(valTuple))
            avgTimes[3] += insertionSort(list(valTuple))
            avgTimes[4] += shellSort(list(valTuple))
            avgTimes[5] += quickSort(list(valTuple))
            avgTimes[6] += mergeSort(list(valTuple))
            avgTimes[7] += heapSort(list(valTuple))

        # Append data to lists of times correlating to n in nVals.
        sortTimes[0].append(avgTimes[0] / noRepeats)
        sortTimes[1].append(avgTimes[1] / noRepeats)
        sortTimes[2].append(avgTimes[2] / noRepeats)
        sortTimes[3].append(avgTimes[3] / noRepeats)
        sortTimes[4].append(avgTimes[4] / noRepeats)
        sortTimes[5].append(avgTimes[5] / noRepeats)
        sortTimes[6].append(avgTimes[6] / noRepeats)
        sortTimes[7].append(avgTimes[7] / noRepeats)

    plotData(nVals, sortTimes)
    printTimePerElement(nVals, sortTimes)


if __name__ == '__main__':
    main()
