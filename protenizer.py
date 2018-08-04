# Credits: https://gist.github.com/Vini2/96ed2becdd6de1fcf4ff99be2af5caf0#file-translating_dna_into_protein-py

import sys, os

class protenizer(object):

    def __init__(self, user_input):
        self.amino_acids = {"TTT" : "F", "CTT" : "L", "ATT" : "I", "GTT" : "V",
                   "TTC" : "F", "CTC" : "L", "ATC" : "I", "GTC" : "V",
                   "TTA" : "L", "CTA" : "L", "ATA" : "I", "GTA" : "V",
                   "TTG" : "L", "CTG" : "L", "ATG" : "M", "GTG" : "V",
                   "TCT" : "S", "CCT" : "P", "ACT" : "T", "GCT" : "A",
                   "TCC" : "S", "CCC" : "P", "ACC" : "T", "GCC" : "A",
                   "TCA" : "S", "CCA" : "P", "ACA" : "T", "GCA" : "A",
                   "TCG" : "S", "CCG" : "P", "ACG" : "T", "GCG" : "A",
                   "TAT" : "Y", "CAT" : "H", "AAT" : "N", "GAT" : "D",
                   "TAC" : "Y", "CAC" : "H", "AAC" : "N", "GAC" : "D",
                   "TAA" : "STOP", "CAA" : "Q", "AAA" : "K", "GAA" : "E",
                   "TAG" : "STOP", "CAG" : "Q", "AAG" : "K", "GAG" : "E",
                   "TGT" : "C", "CGT" : "R", "AGT" : "S", "GGT" : "G",
                   "TGC" : "C", "CGC" : "R", "AGC" : "S", "GGC" : "G",
                   "TGA" : "STOP", "CGA" : "R", "AGA" : "R", "GGA" : "G",
                   "TGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"
                   }
        self.protein_sequence = ""
        self.dna_sequence = [
            letter
            for letters in [line for line in user_input[user_input.find("\n")+1:] if len(line) > 0]
            for letter in letters if letter != '\n'
        ]
        self.dna_sequence = ''.join(self.dna_sequence)

    def protenize(self):
        for i in range(0, len(self.dna_sequence)-(3+len(self.dna_sequence)%3), 3):
            if self.amino_acids[self.dna_sequence[i:i+3]] == "STOP" :
                break
            self.protein_sequence += self.amino_acids[self.dna_sequence[i:i+3]]
        return self.protein_sequence

if __name__ == '__main__':
    sample_dna_sequence = 'ATGGAAGTATTTAAAGCGCCACCTATTGGGATATAAG'
    protein = protenizer(sample_dna_sequence)
    print(protein.protenize())
