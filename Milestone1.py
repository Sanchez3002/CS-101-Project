#1
def s(dna):
    dna = dna.upper()
    count_A = dna.count('A')
    count_C = dna.count('C')
    count_G = dna.count('G')
    count_T = dna.count('T')
    dna_dict = {
        "A" : count_A,
        "C" : count_C,
        "G" : count_G,
        "T" : count_T
    }
    return dna_dict
    
#2
def dna2rna(dna):
    rna = ""
    for symbol in dna:
        if symbol == "A":
            rna = rna + "A"
        elif symbol == "T":
            rna = rna + "U"
        elif symbol == "G":
            rna = rna + "G"
        elif symbol == "C":
            rna = rna + "C"
    return rna
   
#3
def reverse_complement(dna):
    dna_list = list( dna.upper() )
    dna_list.reverse()
    dna_comp = ""
    for letter in dna_list:
        if letter == "A":
            dna_comp += "T"
        elif letter == "T":
            dna_comp += "A"
        elif letter == "G":
            dna_comp += "C"
        elif letter == "C":
            dna_comp += "G"
    return dna_comp
   
#4
def mendels_law( hom, het, rec ):
    import math
    def comb( n, k ):
        return math.factorial( n ) / math.factorial( k ) / math.factorial( n - k )
    total = hom + het + rec 
    space = comb( total, 2 )
    p_of_alleles = {
        "hethet" : 0,
        "hethom" : 0,
        "hetrec" : 0,
        "homhom" : 0,
        "homrec" : 0,
        "recrec" : 0
    }
    p_of_comb = {
        "hethet" : 3 / 4,
        "hethom" : 1,
        "hetrec" : 1 / 2,
        "homhom" : 1,
        "homrec" : 1,
        "recrec" : 0
    }
    if total < 2:
        return "Invalid"
    else:
        if het >= 2:
            p_of_alleles[ "hethet" ] = comb( het, 2 ) / space
        if hom >= 2:
            p_of_alleles[ "homhom" ] = comb( hom, 2 ) / space
        if rec >= 2:
            p_of_alleles[ "recrec" ] = comb( rec, 2 ) / space
        p_of_alleles[ "hethom" ] = het * hom / space
        p_of_alleles[ "hetrec" ] = het * rec / space
        p_of_alleles[ "homrec" ] = hom * rec / space
    total_prob = 0
    for key in p_of_alleles:
        total_prob += p_of_alleles[ key ] * p_of_comb[ key ]
    return total_prob
#5
def fibonacci_rabbits(n, k): 
    if n < 2:
        return 1
    return k*fibonacci_rabbits(n-2, k) + fibonacci_rabbits(n-1, k)

#6
def GC_content(dna_list):
    content_list = []
    for dna_string in dna_list:
        count_AT = 0 
        count_GC = 0
        dna_string = dna_string.upper()
        for letter in dna_string:
            if letter == "G" or letter == "C":
                count_GC += 1 
            elif letter == "A" or letter == "T":
                count_AT += 1 
        content_list.append(count_GC / (count_AT + count_GC) * 100)
    highest = content_list[0] #find string with highest gc_content
    for content in content_list:
        if content > highest:
            highest = content 
    return (content_list.index(highest), highest)

#9
def hamming_dist(dna1,dna2):
    i=0
    count = 0
    for i in range(0,len(dna1)):
        if dna1[i] != dna2[i]:
            count+=1
        else:
            i+=1
    return count
