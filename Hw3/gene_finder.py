# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Yun-Hsin Cynthia Chen
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle 


def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output




def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    # taking a DNA sequence (splitting it into groups of three) and looks for corresponding amino acids
    # list of all of the dna is listed under dnasequence    
    dnasequence = list(dna) 
    # next we also need to set all of the amino acids into a string
    aminoacids_sequence = []

    # next we need to split the list of dnasequence into groups of three
    for a in range(len(dnasequence)):
        start = 3*a #to start at 0 when a is 0, 3 when a is 1,...
        stop = 3*a + 3 #to stop at 3 when a is 0, 6 when a is 2...
        dnagroup = dna[start:stop] #the codon sequence we want to pass in the for loop each time
        for b in range(0, len(aa)): #the range in which the codons can be found in the amino_acids script
            if dnagroup in codons[b]: #searches for the place where the codons are 
                aminoacids_sequence.append(aa[b]) #returns the corresponding amino acids back to back
    
    # next we need to return the actual amino acid in a string form
    return ''.join(aminoacids_sequence)
    
if __name__=='__main__':
    print coding_strand_to_AA()



def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
        
    # This function should call your coding_strand_to_AA function with various inputs
    dna = str(raw_input('What is your value for dna?\n'))
    # next we want the program to generate a line stating the output
    print 'input:' + dna + ', output:' + coding_strand_to_AA(dna)

if __name__=='__main__':
    print coding_strand_to_AA_unit_tests()
    
    

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    # We are going to create a list for reverse_complement and then join them into a string
    reverse_complement = []
    
    for letter in dna: # takes each letter of the dna sequence and assigns the complement base, and then adds it to the previous one
        if letter == 'A':
            reverse_complement.append('T')
        elif letter == 'T': 
            reverse_complement.append('A')
        elif letter == 'G':
            reverse_complement.append('C')
        elif letter == 'C':
            reverse_complement.append('G')
            
        # Without the reverse_complement.append part under if and elif statements, I only got one of the complementary
        # bases. So I got help with that part, and found out I need to append all of them 
    return ''.join(reverse_complement)[::-1] # joins all of the complements into a string and then reverses the sequence

if __name__=='__main__':
    print get_reverse_complement()
    
    
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    # asks for any dna sequence    
    dna = str(raw_input('What is the value for DNA?\n'))
    # print out the dna sequence and the reverse complement of the dna sequence
    print 'Input: ' + dna + ', Output:' + get_reverse_complement(dna)
    
if __name__=='__main__':
    print get_reverse_complement_unit_tests()
    
    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """

    dnaseq = list(dna)
    dnalist = []# we want a list that reenters the ORFs
    #start_codon = ['ATG']
    stop_codon = ['TAG','TAA','TGA'] #we want it to search within the stop_codons to locate if each group of three is start or stop
    stop2 = -1 # accounts for the fact that we want only the start codon if there is no stop codon at all

    for a in range(len(dnaseq)/3):# indicates the step size as each group of three
        start = 3*a # starting location
        stop = 3*a + 3 #stopping location
        dnathree = dna[start:stop] # entire start to stop
        dnalist.append(dnathree) # adds the next group of three into a list of all groups of three
        for b in range(len(stop_codon)): # b in range of how many stop_codons is 1 (only one object)
            if dnalist[a] in stop_codon[b]: # if any of the groups of three matches a stop codon, it will look for where
                stop2 = dnalist.index(stop_codon[b]) 
                ORF_rest = dnalist[:stop2] # it will create a list of the start to stop codons
                break
        if stop2 == -1: # in case that there is no stop, the function will just output all the codons
            ORF_rest = dnalist[:]

    return ''.join(ORF_rest) # joins all the codons into one ORF
    
if __name__=='__main__':
    print rest_of_ORF()
                       
    
    
    
def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
        
    dna = str(raw_input('What is the value for DNA?\n'))
    # print out the dna sequence and the ORF of the dna sequence
    print 'Input: ' + dna + ', Output:' + rest_of_ORF(dna)
    
if __name__=='__main__':
    print rest_of_ORF_unit_tests()
        
        
        
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    dnalists = [] # where the groups of three codons will be put
    i = 0 # while loop starting position
    
    while i<(len(dna)/3): # states that while the new i each turn is less than
        start = 3*i # start at 0 when i is 0, start at 3 when i is 1
        stop = 3*i + 3 # stop at 3 when i is 0, stop at 6 when i is 1 
        dnagroups = dna[start:stop] # creates each of the groups of three into one
        if dnagroups == 'ATG': # sees if it is a start codon
            dnalists.append(rest_of_ORF(dna[start:])) # if it is, it will add on the dnagroup into the list
            i = i + len(dnalists[len(dnalists)-1])/3 # finds where to look next: where the start codon was found minus one location of where that previous ATG was found, divided by groups of three to find the codon number
        i += 1        # next iteration of a starts
    return dnalists
        
if __name__=='__main__':
    print find_all_ORFs_oneframe()
    
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

            
    dna = str(raw_input('What is the value for DNA?\n'))
    # print out the dna sequence and all of the ORFs of the dna sequence
    print 'Input: ' + dna + ', Output:' + ','.join(find_all_ORFs_oneframe(dna))
    
if __name__=='__main__':
    print find_all_ORFs_oneframe_unit_tests()

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    all_ORFs = []
    
    for i in range (3): # will change the i value of each step
        strand = dna[i:] # indicate the new dna strand will start at the index of dna that corresponds to the number
        if not find_all_ORFs_oneframe(strand) == []: # finds if there are ORFs in the strand to continue adding it as a string into the list
            all_ORFs.extend(find_all_ORFs_oneframe(strand))
        
    
    return all_ORFs

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
        
    dna = str(raw_input('What is the value for DNA?\n'))
    # print out the dna sequence and all of the ORFs of the dna sequence
    string_find_all_ORFs = ','.join(find_all_ORFs(dna))
    print 'Input: ' + dna + ', Output:' + string_find_all_ORFs
    
if __name__=='__main__':
    print find_all_ORFs_unit_tests()



def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    # will take into the reverse complement of the dna strand
    both_strands = [] # list in which all of the ORFs will go into as strings
    both_strands.extend(find_all_ORFs(dna)) # looks for the ORFs of the dna
    both_strands.extend(find_all_ORFs(get_reverse_complement(dna))) # looks for the reverse complements of the dna
        
    return both_strands
        
        

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    dna = str(raw_input('What is the value for DNA?\n'))
    # print out the dna sequence and all of the ORFs of both strands of the dna sequence
    print 'Input: ' + dna + ', Output:' + ','.join(find_all_ORFs_both_strands(dna))
    
if __name__=='__main__':
    print find_all_ORFs_both_strands_unit_tests()
    
    

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    mylist = find_all_ORFs_both_strands(dna) # creates a list of all of the ORFs
    if len(mylist) == 0: # sees if the ORFs are length of 0, if so returns nothing
        return ''
    else: # searches for the maximum ORF of the list depending on the lengths of each ORF
        return max(mylist, key =len)

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    dna = str(raw_input('What is the value for DNA?\n'))
    # print out the dna sequence and the longest ORF of the dna sequence
    print 'Input: ' + dna + ', Output:' + longest_ORF(dna)
    
if __name__=='__main__':
    print longest_ORF_unit_tests()

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    
    dnaseq = list(dna) #makes all of the dna into a list of letters
    ORF_Long = ''
    ORF_Longest_Len = 0;
    
    for i in range (num_trials):# it will cycle through the for loop depending on the num_trials
        shuffle(dnaseq) # shuffle all of the letters of the sequence
        collapse(dnaseq) 
        orf = longest_ORF(''.join(dnaseq)) # find the longest ORF possible for when the letters are combined into a new sequence
        if len(orf)>ORF_Longest_Len: # will see if the length of the longest ORF is greater than 0 in the first cycle, greater than what was the longest ORF in the previous cycle
            ORF_Longest_Len = len(orf) # replaces the longest ORF len variable with the new length
            ORF_Long = orf # gives the sequence of the longer orf
    
    return len(ORF_Long)/3 # returns the location of the newest longer orf


def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # the conservative threshold for distinguishing between genes 
    # and non-genes is 769
    a = find_all_ORFs_both_strands(dna) # a is a list of all of the ORFs
    for i in range(len(a)): # for all of the ORFs in the list
        if len(a[i]) > threshold: # it will search for the length of each ORF, and see if it is greater than threshold size
            return coding_strand_to_AA(a[i]) # if so, it will find the amino acid sequence that matches the ORF
    
    # the uncovered amino acid through BLAST that fits the build turned out to be 'MGDVSAVSSSGNILLPQQDEVGGLSEALKKA
    #VEKHKTEYSGDKKDRDYGDAFVMHKETALPLLLAAWRHGAPAKSEHHNGNVSGLHHNGKSELRIAEKLLKVTAEKSVGLISAEAKVDKSAALLSSK
    #NRPLESVSGKKLSADLKAVESVSEVTDNATGISDDNIKALPGDNKAIAGEGVRKEGAPLARDVAPARMAAANTGKPEDKDHKKVKDVSQLPLQPTT
    #IADLSQLTGGDEKMPLAAQSKPMMTIFPTADGVKGEDSSLTYRFQRWGNDYSVNIQARQAGEFSLIPSNTQVEHRLHDQWQNGNPQRWHLTRDDQQNPQQQQHRQQSGEEDDA'
    
    # the corresponding information about the amino acid is in salmonella.txt
        