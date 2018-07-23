import sys

from algorithm_needleman_wunsch import *
from algorithm_smith_waterman import *


def findalignments(user_file, sellected_database_files, selected_algorithms):
    dic = {}
    for algorithm in selected_algorithms:
        if algorithm == 'needleman_wunsch':
            nw = needleman_wunsch(user_file, sellected_database_files)
            dic['needleman_wunsch'] = nw.return_overall_results()
        if algorithm == 'smith_waterman':
            sw = smith_waterman(user_file, sellected_database_files)
            dic['smith_waterman'] = sw.return_overall_results()
    return dic


if __name__ == '__main__':
    user_file = 'TGTTACGG'
    sellected_database_files = [
        'database/database_sequence_example_smith_waterman.fa',
        'database/database_sequence_example_needleman_wunsch.fa'
    ]
    selected_algorithms = ['needleman_wunsch', 'smith_waterman']
    print(findalignments(user_file, sellected_database_files,
                         selected_algorithms))
