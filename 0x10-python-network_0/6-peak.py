def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    
    # get the length of the list
    n = len(list_of_integers)
    
    # if the list is empty, return None
    if n == 0:
        return None
    
    # if the list has only one element, return it
    if n == 1:
        return list_of_integers[0]
    
    # initialize variables for the start and end of the list
    start = 0
    end = n - 1
    
    # loop until start and end meet
    while start < end:
        
        # calculate the midpoint of the list
        mid = (start + end) // 2
        
        # if the midpoint is a peak, return it
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        
        # otherwise, move towards the higher side of the list
        else:
            start = mid + 1
    
    # return the peak value
    return list_of_integers[start]

