{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "98929abc-2679-4f66-b4e7-5ee114a607da",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1\n",
    "def dna_count(dna):\n",
    "    dna = dna.upper()\n",
    "    count_A = dna.count('A')\n",
    "    count_C = dna.count('C')\n",
    "    count_G = dna.count('G')\n",
    "    count_T = dna.count('T')\n",
    "    dna_dict = {\n",
    "        \"A\" : count_A,\n",
    "        \"C\" : count_C,\n",
    "        \"G\" : count_G,\n",
    "        \"T\" : count_T\n",
    "    }\n",
    "    return dna_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "80b2b322-24c1-41cf-9ba1-280db08286a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2\n",
    "def dna2rna(dna):\n",
    "    rna = \"\"\n",
    "    for symbol in dna:\n",
    "        if symbol == \"A\":\n",
    "            rna = rna + \"A\"\n",
    "        elif symbol == \"T\":\n",
    "            rna = rna + \"U\"\n",
    "        elif symbol == \"G\":\n",
    "            rna = rna + \"G\"\n",
    "        elif symbol == \"C\":\n",
    "            rna = rna + \"C\"\n",
    "    return rna"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b20db15d-083a-45cb-bf06-cb27d434af51",
   "metadata": {},
   "outputs": [],
   "source": [
    "#3\n",
    "def reverse_complement(dna):\n",
    "    dna_list.reverse\n",
    "    dna_comp = \"\"\n",
    "    for letter in dna_list:\n",
    "        if letter == \"A\":\n",
    "            dna_comp += \"T\"\n",
    "        elif letter == \"T\":\n",
    "            dna_comp += \"A\"\n",
    "        elif letter == \"G\":\n",
    "            dna_comp += \"C\"\n",
    "        elif letter == \"C\":\n",
    "            dna_comp += \"G\"\n",
    "    return dna_comp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b77e687f-c433-4494-8331-b4ecc79cd5f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#4\n",
    "def mendels_law( hom, het, rec )\n",
    "    import math\n",
    "    def comb( n, k ):\n",
    "        return math.factorial( n ) / math.factorial( k ) / math.factorial( n - k )\n",
    "    total = hom + het + rec \n",
    "    space = comb( total, 2 )\n",
    "    p_of_alleles = {\n",
    "        \"hethet\" : 0,\n",
    "        \"hethom\" : 0,\n",
    "        \"hetrec\" : 0,\n",
    "        \"homhom\" : 0,\n",
    "        \"homrec\" : 0,\n",
    "        \"recrec\" : 0\n",
    "    }\n",
    "    p_of_comb = {\n",
    "        \"hethet\" : 3 / 4\n",
    "        \"hethom\" : 1\n",
    "        \"hetrec\" : 1 / 2\n",
    "        \"homhom\" : 1\n",
    "        \"homrec\" : 1\n",
    "        \"recrec\" : 0\n",
    "    }\n",
    "    if total < 2:\n",
    "        return \"Invalid\"\n",
    "    else:\n",
    "        if het >= 2:\n",
    "            p_of_alleles[ \"hethet\" ] = comb( het, 2 ) / space\n",
    "        if hom >= 2:\n",
    "            p_of_alleles[ \"homhom\" ] = comb( hom, 2 ) / space\n",
    "        if rec >= 2:\n",
    "            p_of_alleles[ \"recrec\" ] = comb( rec, 2 ) / space\n",
    "        p_of_alleles[ \"hethom\" ] = het * hom / space\n",
    "        p_of_alleles[ \"hetrec\" ] = het * rec / space\n",
    "        p_of_alleles[ \"homrec\" ] = hom * rec / space\n",
    "    total_prob = 0\n",
    "    for key in p_of_alleles:\n",
    "        total_prob += p_of_alleles[ key ] * p_of_comb[ key ]\n",
    "    return total_prob"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
