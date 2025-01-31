# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='test_module', exit=False)


import numpy as np

def calculate(list):

    if(len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    ls = np.array(list)
    print(ls)

    mean_rows = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
    mean_columns = [ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()]

    var_rows = [ls[[0,1,2]].var(), ls[[3,4,5]].var(), ls[[6,7,8]].var()]
    var_columns = [ls[[0,3,6]].var(), ls[[1,4,7]].var(), ls[[2,5,8]].var()]

    std_rows = [ls[[0,1,2]].std(), ls[[3,4,5]].std(), ls[[6,7,8]].std()]
    std_columns = [ls[[0,3,6]].std(), ls[[1,4,7]].std(), ls[[2,5,8]].std()]

    max_rows = [ls[[0,1,2]].max(), ls[[3,4,5]].max(), ls[[6,7,8]].max()]
    max_columns = [ls[[0,3,6]].max(), ls[[1,4,7]].max(), ls[[2,5,8]].max()]

    min_rows = [ls[[0,1,2]].min(), ls[[3,4,5]].min(), ls[[6,7,8]].min()]
    min_columns = [ls[[0,3,6]].min(), ls[[1,4,7]].min(), ls[[2,5,8]].min()]

    sum_rows = [ls[[0,1,2]].sum(), ls[[3,4,5]].sum(), ls[[6,7,8]].sum()]
    sum_columns = [ls[[0,3,6]].sum(), ls[[1,4,7]].sum(), ls[[2,5,8]].sum()]


    return {
        'mean': [mean_columns, mean_rows, ls.mean()],
        'variance': [var_columns, var_rows, ls.var()],
        'standard deviation': [std_columns, std_rows, ls.std()],
        'max': [max_columns, max_rows, ls.max()],
        'min': [min_columns, min_rows, ls.min()],
        'sum': [sum_columns, sum_rows, ls.sum()]
    }


#Out put

[0 1 2 3 4 5 6 7 8]
{'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611], 'max': [[6, 7, 8], [2, 5, 8], 8], 'min': [[0, 1, 2], [0, 3, 6], 0], 'sum': [[9, 12, 15], [3, 12, 21], 36]}
[2 6 2 8 4 0 1 5 7]
.[9 1 5 3 3 3 2 9 0]
..
