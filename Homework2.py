#Homework 2

DNA=ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT


#Count the number of G's
DNA_count_g = dna.count("G")
#Count the number of C's
DNA_count_c = dna.count("C")
#Determine the length of the sequence
DNA_len = float(len(DNA))
#Divide the total number of G's and C's vs the length of the sequence
DNA_GC_percent = ((DNA_count_g + DNA_count_c) / DNA_len) * 100
#Report the percentage of the GC content
Print(DNA_GC_percent)