import numpy as np
import pandas as pd
import time


def printList(arr):
    for i in arr:
        print(i)


def matrix():
    # Timer to keep track of total time program is running is started
    start_time = time.time()

    # Reads in data from file and stores data in input matrix
    input_matrix = pd.read_csv('../data/G - V.csv', sep=',', header=0)

    # Empty list for weighted
    weighted_sums = []

    # Matrix for storing output is initialized
    output_matrix = []
    for i in range(29):
        new = []
        for j in range(29):
            new.append(0)
        output_matrix.append(new)

    # Matrix for storing final numbers used in Table 4 is initialized
    final_results = []
    for i in range(29):
        new = []
        for j in range(5):
            new.append(0)
        final_results.append(new)

    # Nested For loops are used to make every possible combination
    # 0 - 4  = [0, 0, 0, 0, 0, 0, 0, 0] ~ [4, 4, 4, 4, 4, 4, 4, 4]
    for i1 in range(5):
        for i2 in range(5):
            for i3 in range(5):
                for i4 in range(5):
                    for i5 in range(5):
                        for i6 in range(5):
                            for i7 in range(5):
                                for i8 in range(5):

                                    # Each alternative is selected from the original value input matrix
                                    for alternative in input_matrix.iterrows():
                                        # The weighted sum is calculated for each alternative
                                        weighted_sums.append(alternative[1][0] * i1 + alternative[1][1] * i2 +
                                                             alternative[1][2] * i3 + alternative[1][3] * i4 +
                                                             alternative[1][4] * i5 + alternative[1][5] * i6 +
                                                             alternative[1][6] * i7 + alternative[1][7] * i8)
                                    # For every place winner
                                    for i in range(29):

                                        # Weighted average is checked to make sure it's not zero
                                        if np.max(weighted_sums) != 0:
                                            # The highest winner is selected and the winner of that alternative
                                            # is increased by 1
                                            output_matrix[i][np.argmax(weighted_sums)] += 1

                                            # That exact position on the weighted_sums list is replaced with a zero
                                            # to make sure that alternative is not selected again
                                            weighted_sums[np.argmax(weighted_sums)] = 0

                                    # The weight_sums list is cleared
                                    weighted_sums.clear()

    # The entire output matrix is printed
    print("-------------- Entire Matrix ---------------")
    print("--------------------------------------------")
    printList(output_matrix)
    print("--------------------------------------------")
    print("--------------------------------------------")
    print()
    print()

    print("-------------- First 5 Places --------------")
    print("--------------------------------------------")
    for i in range(5):
        index = 0
        for place in output_matrix[i]:
            final_results[index][i] = (round((place / 390624) * 100, 1))
            index += 1
    printList(final_results)
    print("--------------------------------------------")
    print("--------------------------------------------")

    # The total time elapsed is calculated and printed out
    print("My program took " + str(time.time() - start_time) + " to run")


if __name__ == '__main__':
    matrix()
