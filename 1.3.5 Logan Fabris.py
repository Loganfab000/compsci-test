paragraph = 'There, is that 3 points?'
// It's not three points, it's only 2
def how_eligible(paragraph):
    total = 0
    if '?' in paragraph:
            total += 1
    if '!' in paragraph:
            total += 1
    if '"' in paragraph:
            total += 1 
    if ',' in paragraph:
            total += 1     
    print (total)   
            
    
    
    
    

