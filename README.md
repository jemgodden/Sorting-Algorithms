# Sorting-Algorithms

This program contains the implementation of 8 different sorting algorithms, these being: Bubble Sort, Comb Sort, Insertion Sort, Selection Sort, Quick Sort, Merge Sort, Shell Sort and Heap Sort.

The purpose of this project is to compare the efficiency of these algorithms when sorting a varity of different sized lists. This is done by returning the time taken to sort a given list by each algorithm implementation and plotting this information, for multiple different sized lists, on a log-scaled plot. This allows for visual comparisons to be made between each algorithm depending on their runtime. The average time taken to sort a single element is also printed. Both of these things are done in the file sortAlgComp.py.


The algorithms have the following computation complexity from their implementation:

Bubble Sort - Worst case: О(n^2). Best case: О(n).

Comb Sort - Worst case: О(n^2). Best case: О(nlog(n)).

Insertion Sort - Worst case: О(n^2). Best case: О(n).

Selection Sort - Worst case: О(n^2). Best case: О(n).

Quick Sort - Worst case: О(n2). Best case: О(nlog(n)).

Merge Sort - Worst case: О(nlog(n)). Best case: О(nlog(n)).

Shell Sort - Worst case: О(n^2). Best case: О(nlog(n)).

Heap Sort - Worst case: О(nlog(n)). Best case: О(nlog(n)).


The generated lists have elements with a value ranging from 0-100 and are created with the help of the random python library.

# Downloading

The easiest way to download the code is to press the download button on the home page of the GitHub repository.

# Requirements

To run the program a python compiler is required, along with the following libraries: time, random, matplotlib and argparse.

# Use

Currently, sortAlgComp.py is the only program that can be run by the user. 
It takes a single command line argument, called repeats, which allows the user to specify how many unique lists of length n should be generated and sorted by each algorithm in order to get a mean average run-time. This is available as the random lists generated can sometimes be less suited to certain algorithms.

A typical command line using this option would look like:

>>> python sortAlgComp.py -r 5
or 
>>> python sortAlgComp.py --repeats 5

This will do 5 unique n-sized lists to be sorted by each algorithm. The given value must be an integer. The default value is set to 1 if there is no specified value. 

# Log

Initial version uploaded to GitHub.

Updated comments on sortAlgs.py and sortAlgComp.py.
