"""A recursive function that receives a list of numbers as input and returns a list of numbers as the original 
list is being cumulatively added."""


def csum(lst, sum_lst=[]):
    if len(lst) == 0:
        return sum_lst
    else:
        if len(sum_lst) == 0:
            sum_lst.append(lst[0])
        else:
            sum_lst.append(sum_lst[len(sum_lst)-1] + lst[0])
        del lst[0]
        return csum(lst, sum_lst)
    
    
numbers = [1, 2, 3, 4, 5, 6, 7]
print("List of numbers:")
print(numbers)
print("\nCumulative list:")
print(csum(numbers))
