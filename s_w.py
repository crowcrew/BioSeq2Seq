import sys

input_file = ""
subt = []
symbols = []
user_input = ""
scoring_matrix = []
gap_value = -2

def read_from_files():
	global input_file
	f =  open('AB000263.fa', 'r')
	s = f.read().split('\n')
	for line in s[1:]:
		line = line.strip()
		if len(line) > 0:
			input_file += line
	f.close()
	
	ff = open('SubtMat','r')
	ss = ff.read().split('\n')
	# reading the dna symbols
	global symbols
	symbols = [symbol for symbol in ss[0] if symbol!=' ']

	global subt
	subt = [map(int,number) for number in [line.split(' ') for line in ss[1:] if len(line)>0]]

def get_user_input():
	global user_input
	user_input = raw_input("please input your dna sequence")

def get_substitution_value(a, b):
	return 1

def SmithWaterman():
	for index_i, element_i in enumerate(input_file):
		for index_j, element_j in enumerate(user_input):
			print element_j, index_j
			#adjacency_value = get_substitution_value(element_i, element_j)
			
				
	

if __name__ == '__main__':
	read_from_files()
	print input_file
	print symbols
	print subt
	get_user_input()
	SmithWaterman()
