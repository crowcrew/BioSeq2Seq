import sys
import numpy as np

database_sequence = []
substitution_symbols = [] # from substitution_matrix.txt
substitution_values = [] # from substitution_matrix.txt
user_input = []
scoring_matrix = []
gap_value = -1
finalresults = []

def read_from_files():
	# database sequence disk read
	global database_sequence
	openfile =  open('database_sequence_needleman_wunsch.fa', 'r')
	readfile = openfile.read().split('\n')
	database_sequence = [letter for letters in [line for line in readfile[1:] if len(line)>0] for letter in letters]
	openfile.close()
	
	# substitution matrix disk read
	openfile = open('substitution_matrix_example_needleman_wunsch.txt','r')
	readfile = openfile.read().split('\n')
	# reading the substitution matrix symbols
	global substitution_symbols
	substitution_symbols = [symbol for symbol in readfile[0] if symbol!=' ']
	# reading the substitution matrix values
	global substitution_values
	substitution_values = [map(int,number) for number in [line.split(' ') for line in readfile[1:] if len(line)>0]]
	openfile.close()

def maxtuple(*args):
	maxval = [-1000,-1,-1]
	for arg_index in range(len(args)):
		maxval = (args[arg_index], maxval)[args[arg_index][0]<maxval[0]]
	maxvaltuple = [maxval]
	for arg_index in range(len(args)):
		if args[arg_index][0] == maxval[0] and (args[arg_index][1] != maxval[1] or args[arg_index][2] != maxval[2]):
			maxvaltuple.append(args[arg_index])
	if len(maxvaltuple) > 1:
		return maxvaltuple
	else:
		return maxval

def get_user_input():
	global user_input
	user_input = [letter for letters in raw_input("please input your dna sequence\n") for letter in letters]

def get_substitution_value(a, b):
	a_index = substitution_symbols.index(a)
	b_index = substitution_symbols.index(b)
	return substitution_values[a_index][b_index]


def backtracking(max_score, result=[]):
	global scoring_matrix
	global gap_value
	while max_score[1] >= 0 and max_score[2] >= 0 :
		substitution_value = get_substitution_value(database_sequence[max_score[1]-1], user_input[max_score[2]-1])
		max_score_temp = maxtuple (\
				[scoring_matrix[max_score[1]-1][max_score[2]-1]+substitution_value , max_score[1]-1 , max_score[2]-1],\
 				[scoring_matrix[max_score[1]][max_score[2]-1]+gap_value,max_score[1],max_score[2]-1],\
 				[scoring_matrix[max_score[1]-1][max_score[2]]+gap_value,max_score[1]-1,max_score[2]])
		if type(max(max_score_temp))==list:
			for tuple_index in range(len(max_score_temp)):
				backtracking([scoring_matrix[max_score_temp[tuple_index][1]][max_score_temp[tuple_index][2]],max_score_temp[tuple_index][1],max_score_temp[tuple_index][2]], result=result)
			return
		else:
			if max_score[2] != max_score_temp[2] and max_score[1] != max_score_temp[1] :
				result = [(database_sequence[max_score[1]-1],user_input[max_score[2]-1])] + result
			elif max_score[2] != max_score_temp[2] and max_score[1] == max_score_temp[1] :
				result = [('-',user_input[max_score[2]-1])] + result
			elif max_score[2] == max_score_temp[2] and max_score[1] != max_score_temp[1] :
				result = [(database_sequence[max_score[1]-1],'-')] + result
			max_score = [scoring_matrix[max_score_temp[1]][max_score_temp[2]],max_score_temp[1],max_score_temp[2]]
	finalresults.append(result)

def needleman_wunsch():
	global scoring_matrix
	global gap_value
	
	scoring_matrix = np.array([[-1*x+(-1*y) for x in range(len(user_input)+1)] for y in range(len(database_sequence)+1)])
	for index_i, element_i in enumerate(database_sequence):
		for index_j, element_j in enumerate(user_input):
			substitution_value = get_substitution_value(element_i, element_j)
			scoring_matrix[index_i+1][index_j+1] = max(scoring_matrix[index_i][index_j]+substitution_value, scoring_matrix[index_i][index_j+1]+gap_value, scoring_matrix[index_i+1][index_j]+gap_value)
			
			
	print "scoring matrix:\n", scoring_matrix
	last_score = [scoring_matrix[len(database_sequence)][len(user_input)],len(database_sequence),len(user_input)]
	
	backtracking(last_score)
	print finalresults

				
			
	

if __name__ == '__main__':
	read_from_files()
	print "database sequence:\n", database_sequence
	print "substitution symbols:\n", substitution_symbols
	print "substitution values:\n", substitution_values
	get_user_input()
	get_substitution_value
	print "user input:\n", user_input
	needleman_wunsch()
