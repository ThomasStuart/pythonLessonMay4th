def checkPalindrome(inputString):
    start_index  = 0
    end_index    = len(inputString)
    head_counter = 0
    tail_counter = end_index - 1

    for index in range(start_index, int(end_index/2) ):
        #print( "head is", inputString[index] ," and ", end='')
        #print( "tail is ", inputString[tail_counter], end = ' || ')
        #print( "  Does", inputString[head_counter],"==", inputString[tail_counter], "??", end ="    ->")
        
        if inputString[head_counter] != inputString[tail_counter]:
            return False  # <- return value 
           
        head_counter = head_counter + 1
        tail_counter = tail_counter - 1

    return True  # <- return value 
