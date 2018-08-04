import sys

from algorithm_needleman_wunsch import *
from algorithm_smith_waterman import *
from protenizer import *


def findalignments(user_file, sellected_database_files, selected_algorithm):
    result = []
    if selected_algorithm == 'needleman_wunsch':
        nw = needleman_wunsch(user_file, sellected_database_files)
        result = nw.return_overall_results()
    if selected_algorithm == 'smith_waterman':
        sw = smith_waterman(user_file, sellected_database_files)
        result = sw.return_overall_results()
    return result

def findprotein(user_file):
    proteinEngine = protenizer(user_file)
    return proteinEngine.protenize()

if __name__ == '__main__':
    user_file = 'TGTTACGG'
    sellected_database_files = [
        'database/database_sequence_example_smith_waterman.fa',
        'database/database_sequence_example_needleman_wunsch.fa'
    ]
    selected_algorithms = ['needleman_wunsch']
    print(findalignments(user_file, sellected_database_files,
                         selected_algorithms))
