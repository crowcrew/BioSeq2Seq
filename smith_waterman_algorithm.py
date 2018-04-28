import sys

class smith_waterman(object):

	def __init__(self):
		self.database_sequence = []
		self.substitution_symbols = [] # from substitution_matrix.txt
		self.substitution_values = [] # from substitution_matrix.txt
		self.user_input = []
		self.scoring_matrix = []
		self.gap_value = -2
		self.finalresults = []
		self.read_from_files()
		self.get_user_input()
		self.get_substitution_value
		self.smith_waterman()

	def read_from_files(self):
		# database sequence disk read
		openfile =  open('database_sequence_example_smith_waterman.fa', 'r')
		readfile = openfile.read().split('\n')
		self.database_sequence = [letter for letters in [line for line in readfile[1:] if len(line)>0] for letter in letters]
		openfile.close()
	
		# substitution matrix disk read
		openfile = open('substitution_matrix_example_smith_waterman.txt','r')
		readfile = openfile.read().split('\n')
		# reading the substitution matrix symbols
		self.substitution_symbols = [symbol for symbol in readfile[0] if symbol!=' ']
		# reading the substitution matrix values
		self.substitution_values = [map(int,number) for number in [line.split(' ') for line in readfile[1:] if len(line)>0]]
		openfile.close()
		print "database sequence:\n", self.database_sequence
		print "substitution symbols:\n", self.substitution_symbols
		print "substitution values:\n", self.substitution_values

	def maxtuple(self,*args):
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

	def get_user_input(self):
		self.user_input = [letter for letters in raw_input("please input your dna sequence\n") for letter in letters]
		print "user input:\n", self.user_input
	def get_substitution_value(self,a, b):
		a_index = self.substitution_symbols.index(a)
		b_index = self.substitution_symbols.index(b)
		return self.substitution_values[a_index][b_index]


	def backtracking(self,max_score, result=[]):
		while max_score[0] > 0 :
			substitution_value = self.get_substitution_value(self.database_sequence[max_score[1]-1], self.user_input[max_score[2]-1])
			max_score_temp = self.maxtuple (\
					[self.scoring_matrix[max_score[1]-1][max_score[2]-1]+substitution_value , max_score[1]-1 , max_score[2]-1],\
	 				[self.scoring_matrix[max_score[1]][max_score[2]-1]+gap_value,max_score[1],max_score[2]-1],\
	 				[self.scoring_matrix[max_score[1]-1][max_score[2]]+gap_value,max_score[1]-1,max_score[2]])
			if type(max(max_score_temp))==list:
				for tuple_index in range(len(max_score_temp)):
					if max_score[2] != max_score_temp[tuple_index][2] and max_score[1] != max_score_temp[tuple_index][1] :
						tempresult = [(self.database_sequence[max_score[1]-1],self.user_input[max_score[2]-1])] + result
					elif max_score[2] != max_score_temp[tuple_index][2] and max_score[1] == max_score_temp[tuple_index][1] :
						tempresult = [('-',self.user_input[max_score[2]-1])] + result
					elif max_score[2] == max_score_temp[tuple_index][2] and max_score[1] != max_score_temp[tuple_index][1] :
						tempresult = [(self.database_sequence[max_score[1]-1],'-')] + result
					self.backtracking([self.scoring_matrix[max_score_temp[tuple_index][1]][max_score_temp[tuple_index][2]],max_score_temp[tuple_index][1],max_score_temp[tuple_index][2]], result=tempresult)
				return
			else:
				if max_score[2] != max_score_temp[2] and max_score[1] != max_score_temp[1] :
					result = [(self.database_sequence[max_score[1]-1],self.user_input[max_score[2]-1])] + result
				elif max_score[2] != max_score_temp[2] and max_score[1] == max_score_temp[1] :
					result = [('-',self.user_input[max_score[2]-1])] + result
				elif max_score[2] == max_score_temp[2] and max_score[1] != max_score_temp[1] :
					result = [(self.database_sequence[max_score[1]-1],'-')] + result
				max_score = [self.scoring_matrix[max_score_temp[1]][max_score_temp[2]],max_score_temp[1],max_score_temp[2]]
		self.finalresults.append(result)

	def smith_waterman(self):
		max_score = [-1000,-1,-1]
		self.scoring_matrix = [[0 for x in range(len(self.user_input)+1)] for y in range(len(self.database_sequence)+1)]
		for index_i, element_i in enumerate(self.database_sequence):
			for index_j, element_j in enumerate(self.user_input):
				substitution_value = self.get_substitution_value(element_i, element_j)
				self.scoring_matrix[index_i+1][index_j+1] = max(self.scoring_matrix[index_i][index_j]+substitution_value, self.scoring_matrix[index_i][index_j+1]+gap_value, self.scoring_matrix[index_i+1][index_j]+gap_value, self.scoring_matrix[index_i+1][index_j+1])
				max_score = self.maxtuple(max_score, [self.scoring_matrix[index_i+1][index_j+1],index_i+1,index_j+1])
				if type(max(max_score))==list:
					max_score = max_score[0]
		print "scoring matrix:\n", self.scoring_matrix
		print "max score:\n", max_score
		self.backtracking(max_score)
		print self.finalresults


if __name__ == '__main__' :
	sw == smithwaterman()






















