#1
def s(dna):
    dna = dna.upper()
    count_A = dna.count('A')
    count_T = dna.count('T')
    count_G = dna.count('G')
    count_C = dna.count('C')
    dna_dict = {
        "A" : count_A,
        "T" : count_T,
        "G" : count_G,
        "C" : count_C
    }
    return dna_dict
    
#2
def dna2rna(dna):
    rna = ""
    for i in dna:
        if i == "A":
            rna = rna + "A"
        elif i == "T":
            rna = rna + "U"
        elif i == "G":
            rna = rna + "G"
        elif i == "C":
            rna = rna + "C"
    return rna
   
#3
def reverse_complement(dna):
    dna_list = list( dna.upper() )
    dna_list.reverse()
    dna_comp = ""
    for i in dna_list:
        if i == "A":
            dna_comp += "T"
        elif i == "T":
            dna_comp += "A"
        elif i == "G":
            dna_comp += "C"
        elif i == "C":
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
def fibonacci_rabbits( n, k ): 
    if n <= 2:
        return 1
    return k * fibonacci_rabbits( n - 2, k ) + fibonacci_rabbits( n - 1, k )

#6
def GC_content( dna_list ):
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
        content_list.append( count_GC / ( count_AT + count_GC ) * 100 )
    highest = content_list[0] #find string with highest gc_content
    for content in content_list:
        if content > highest:
            highest = content 
    return (content_list.index(highest), highest)

#7
def rna2codon(rna):
    if rna == "":
        return ""
        
    genetic_codon = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',

        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',

        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',

        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }
   
    output = ""
    stop = False
    i=0
    while not stop:
        codon_string = rna[i: i + 3]
        if genetic_codon[codon_string] == '*':
            stop = True
            continue
        output += genetic_codon[codon_string]
        i+=3
    return output

#8
def locate_substring( dna_snippet, dna ):
    dnaC = dna.upper()
    position = []
    for i in range( len ( dna ) ):
        if dnaC[ i : i + len( dna_snippet ) ] == dna_snippet.upper():
            position.append( i )
    return position

#9
def hamming_dist(dna1,dna2):
    i = 0
    count = 0
    for i in range( 0, len ( dna1 ) ):
        if dna1[ i ] != dna2[ i ]:
            count += 1
        else:
            i += 1
    return count

#10
def count_dom_phenotype(genotypes):
    return (2 * genotypes[0]) + (2 * genotypes[1]) + (2 * genotypes[2]) + ((3/2) * genotypes[3]) + (genotypes[4])

#11
def source_rna(protein):
    to_return = 3   # =3 since stop = 3
    reference_dict = {
        'F': 2, 'L': 6, 'I': 3, 
        'M': 1, 'S': 6, 'T': 4, 
        'Y': 2, 'N': 2, 'K': 2, 
        'C': 2, 'W': 1, 'R': 6,
        'A': 4, 'P': 4, 'H': 2,
        'Q': 2, 'V': 4, 'G': 4,
        'E': 2, 'D': 2
    }
    for c in protein:
        to_return = to_return * reference_dict[c]
    return to_return

#12
def splice_rna( dna, intron_list ):
    for i in intron_list:
        dna = dna.replace( i, '' )
    rna = dna2rna( dna )
    pro = rna2codon( rna )
    return pro
