import sys

database_sequence = []
substitution_symbols = [] # from substitution_matrix.txt
substitution_values = [] # from substitution_matrix.txt
user_input = []
scoring_matrix = []
gap_value = -2

def read_from_files():
	# database sequence disk read
	global database_sequence
	openfile =  open('AB000263.fa', 'r')
	readfile = openfile.read().split('\n')
	database_sequence = [letter for letters in [line for line in readfile[1:] if len(line)>0] for letter in letters]
	openfile.close()
	
	# substitution matrix disk read
	openfile = open('substitution_matrix.txt','r')
	readfile = openfile.read().split('\n')
	# reading the substitution matrix symbols
	global substitution_symbols
	substitution_symbols = [symbol for symbol in readfile[0] if symbol!=' ']
	# reading the substitution matrix values
	global substitution_values
	substitution_values = [map(int,number) for number in [line.split(' ') for line in readfile[1:] if len(line)>0]]
	openfile.close()

def get_user_input():
	global user_input
	user_input = [letter for letters in raw_input("please input your dna sequence\n") for letter in letters]

def get_substitution_value(a, b):
	return 1

def smith_waterman():
	for index_i, element_i in enumerate(database_sequence):
		for index_j, element_j in enumerate(user_input):
			#print element_j, index_j
			adjacency_value = get_substitution_value(element_i, element_j)
			
				
	

if __name__ == '__main__':
	read_from_files()
	print database_sequence
	print substitution_symbols
	print substitution_values
	get_user_input()
	print user_input
	smith_waterman()
