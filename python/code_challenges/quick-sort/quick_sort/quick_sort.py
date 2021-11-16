def quick_sort(li, left, right):
    """
    Sort an array of integers given the array, its leftmost index, and rightmost index.

    Args:
        li (list): a list of integers.
        left (int): the index of the leftmost element in the list.
        right (int): the index of the rightmost elment in the list.
    """
    if left < right :
        position = partition(li, left, right)
        quick_sort(li, left, position - 1)
        quick_sort(li, position + 1, right)

def partition(li, left, right):
    """
    Iterate over the given list comparing each number with the pivot and return the correct index for the pivot.

    Args:
        li (list): a list of integers.
        left (int): the index of the leftmost element in the list.
        right (int): the index of the rightmost elment in the list.

    Returns:
        int: the correct index of the pivot.
    """
    pivot = li[right]
    low = left - 1
    for i in range(left,right):
        if li[i] <= pivot:
            low += 1
            swap(li, i, low)
    swap(li, right, low + 1)
    return low +1

def swap(li, i, low):
    """
    Swap between two values in a list given thier indicies.

    Args:
        li (list): the list containing the two numbers
        i (the current index of the pivot): [description]
        low (int): the index of the smallest number after before the index of the pivot.
    """
    temp = li[i]
    li[i] = li[low]
    li[low] = temp

if __name__ == "__main__":
    li = [8,4,23,42,16,15]
    quick_sort(li, 0, len(li) - 1)
    print(li)