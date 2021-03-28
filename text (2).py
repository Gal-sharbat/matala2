
def revword(word:str) -> str:
    answer=word[::-1]
    return(answer.lower())
    
def countword()->int:
    matala=open('text.txt')
    word=matala.readline()
    word=word.rstrip()
    word=word.lower()
    cunter=1
    for l in matala:
        line=l.split()
        for w in line:
            if revword(w)==word:
                cunter+= 1
    return(cunter)           
                
            
        
    
