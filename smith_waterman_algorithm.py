import sys

class smith_waterman(object):

	def __init__(self):
		self.database_sequence = []
		substitution_symbols = [] # from substitution_matrix.txt
		substitution_values = [] # from substitution_matrix.txt
		user_input = []
		scoring_matrix = []
		gap_value = -2
		finalresults = []

	def read_from_files():
		# database sequence disk read
		global self.database_sequence
		openfile =  open('database_sequence_example_smith_waterman.fa', 'r')
		readfile = openfile.read().split('\n')
		self.database_sequence = [letter for letters in [line for line in readfile[1:] if len(line)>0] for letter in letters]
		openfile.close()
	
		# substitution matrix disk read
		openfile = open('substitution_matrix_example_smith_waterman.txt','r')
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
		while max_score[0] > 0 :
			substitution_value = get_substitution_value(self.database_sequence[max_score[1]-1], user_input[max_score[2]-1])
			max_score_temp = maxtuple (\
					[scoring_matrix[max_score[1]-1][max_score[2]-1]+substitution_value , max_score[1]-1 , max_score[2]-1],\
	 				[scoring_matrix[max_score[1]][max_score[2]-1]+gap_value,max_score[1],max_score[2]-1],\
	 				[scoring_matrix[max_score[1]-1][max_score[2]]+gap_value,max_score[1]-1,max_score[2]])
			if type(max(max_score_temp))==list:
				for tuple_index in range(len(max_score_temp)):
					if max_score[2] != max_score_temp[tuple_index][2] and max_score[1] != max_score_temp[tuple_index][1] :
						tempresult = [(self.database_sequence[max_score[1]-1],user_input[max_score[2]-1])] + result
					elif max_score[2] != max_score_temp[tuple_index][2] and max_score[1] == max_score_temp[tuple_index][1] :
						tempresult = [('-',user_input[max_score[2]-1])] + result
					elif max_score[2] == max_score_temp[tuple_index][2] and max_score[1] != max_score_temp[tuple_index][1] :
						tempresult = [(self.database_sequence[max_score[1]-1],'-')] + result
					backtracking([scoring_matrix[max_score_temp[tuple_index][1]][max_score_temp[tuple_index][2]],max_score_temp[tuple_index][1],max_score_temp[tuple_index][2]], result=tempresult)
				return
			else:
				if max_score[2] != max_score_temp[2] and max_score[1] != max_score_temp[1] :
					result = [(self.database_sequence[max_score[1]-1],user_input[max_score[2]-1])] + result
				elif max_score[2] != max_score_temp[2] and max_score[1] == max_score_temp[1] :
					result = [('-',user_input[max_score[2]-1])] + result
				elif max_score[2] == max_score_temp[2] and max_score[1] != max_score_temp[1] :
					result = [(self.database_sequence[max_score[1]-1],'-')] + result
				max_score = [scoring_matrix[max_score_temp[1]][max_score_temp[2]],max_score_temp[1],max_score_temp[2]]
		finalresults.append(result)

	def smith_waterman():
		global scoring_matrix
		global gap_value
		max_score = [-1000,-1,-1]
		scoring_matrix = [[0 for x in range(len(user_input)+1)] for y in range(len(self.database_sequence)+1)]
		for index_i, element_i in enumerate(self.database_sequence):
			for index_j, element_j in enumerate(user_input):
				substitution_value = get_substitution_value(element_i, element_j)
				scoring_matrix[index_i+1][index_j+1] = max(scoring_matrix[index_i][index_j]+substitution_value, scoring_matrix[index_i][index_j+1]+gap_value, scoring_matrix[index_i+1][index_j]+gap_value, scoring_matrix[index_i+1][index_j+1])
				max_score = maxtuple(max_score, [scoring_matrix[index_i+1][index_j+1],index_i+1,index_j+1])
				if type(max(max_score))==list:
					max_score = max_score[0]
		print "scoring matrix:\n", scoring_matrix
		print "max score:\n", max_score
		backtracking(max_score)
		print finalresults

				
			
	

if __name__ == '__main__':
	read_from_files()
	print "database sequence:\n", self.database_sequence
	print "substitution symbols:\n", substitution_symbols
	print "substitution values:\n", substitution_values
	get_user_input()
	get_substitution_value
	print "user input:\n", user_input
	smith_waterman()
