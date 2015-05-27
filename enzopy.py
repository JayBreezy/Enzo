
with open('testSeq.txt', 'r') as textfile: #open DNA seq as continuous string
    DNAseq = textfile.read().replace('\n','') #rid of line breaks or spaces

print 'Imported sequence:'
print DNAseq #check

RNAseq = '' #empty string for RNAsequence

def transcription(DNAstr): #transcribes DNA seq to mRNA seq
    '''Input continuous string of DNA seq. Output string of RNA seq.'''
    RNAstr = '' 
    for char in DNAstr:
        if char == 'A':
            RNAstr += 'U'
        elif char == 'T':
            RNAstr += 'A'
        elif char == 'C':
            RNAstr += 'G'
        elif char == 'G':
            RNAstr += 'C'
    return RNAstr

def findStart(DNAstr): #finds start of coding DNA, cuts down seq
    '''Input continuous string of DNA seq. Output cut DNA sequence'''
    tempSeq = '' #empty string for temporary storing up to 5 bases seq
    count = 0 #keeps count of sequence location
    for char in DNAstr:
        tempSeq += str(char) #holds current seq of bases
        if tempSeq == 'AAAAA': #if start codon is found
            cutDNAstr = str(DNAstr[count+1:]) #cut all beginning code including start
            return cutDNAstr
        elif len(tempSeq) >= 5: #limits to 5 base pairs at a time
            tempSeq = str(tempSeq[1:])
        else:
            count += 1
    print 'No start codon'
            
def findStop(codonLst): #locates stop codon, truncates end of sequence
    '''Input list of 3 char codon strings. Output truncated list after stop codon'''
    stopCodons = ['UAA', 'UAG', 'UGA']
    count = 0 #keeps location of sequence through loop
    for codon in codonLst: 
        if codon in stopCodons:
            codonLst = codonLst[:count]
            return codonLst
        else:
            count += 1
            
            
def codonChop1(RNAstr):#1 of 2 ways to segment into codons
    '''Input string of RNA seq. Output list of codons.'''
    count = 0
    codonLst = []
    while count < len(RNAstr):
        tempSeq = '' #temp sequence of codons
        for i in range(3): #for each of 3 letters
            tempSeq += RNAstr[count] #add to temp sequence
            count +=1
        codonLst.append(tempSeq) #append to growing list of codons
    return codonLst

def codonChop2(RNAstr): #2 of 2 ways to segment into codons
    '''Input string of RNA seq. Output list of segments codons.'''
    count = 0
    codonLst = []
    while count < len(RNAstr): 
        codonLst.append(RNAstr[count:count+3]) #add strings of 3's
        count += 3 #move through sequence by 3's
    return codonLst

def translate(codonLst): #translates from codons to amino acids
    '''Input list of codons. Output list of amino acids.'''
    for codon in codonLst:
        aaLst.append(aaDic[codon]) #append dictonary value by codon index
    return aaLst

DNAseq = findStart(DNAseq)

print 'DNAseq:'
print DNAseq

RNAseq = transcription(DNAseq)

print 'RNAseq:'
print RNAseq

#codonList = codonChop1(RNAseq) 

codonList = codonChop2(RNAseq) #less complicated of the 2 functions

print 'codon list:'
print codonList

codonList = findStop(codonList)

print 'codon list truncated:'
print codonList

aaList = translate(codonList)

print 'aa list:'
print aaList

    
        
