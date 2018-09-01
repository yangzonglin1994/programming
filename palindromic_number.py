"""
Find the closest palindrome number to a certain number.
Wrong solution. But don't want to delete it.
See solution 564 of `programming-java` project.
"""


def partition(n):
    n_str = str(n)
    if len(n_str) == 1:
        raise ValueError('len of n should be bigger than 1.')
    elif len(n_str) % 2 != 0:
        front = int(n_str[:len(n_str)//2+1])
    else:
        front = int(n_str[:len(n_str)//2])
    end = int(n_str[:(len(n_str)//2-1):-1])
    return front, end


def combine(front, is_len_even):
    front = str(front)
    end = front[::-1]
    if is_len_even:
        return front+end
    else:
        return front[:-1]+end


def bigger(n):
    if n < 0:
        n = 0
    n_str = str(n)
    if len(n_str) == 1:
        n += 1 if n != 9 else 2
        return n
    else:
        front, end = partition(n)
        if front <= end:
            front += 1
        is_len_even = True if len(n_str) % 2 == 0 else False
        return combine(front, is_len_even)


def smaller(n):
    if n < 0:
        n = 0
    n_str = str(n)
    if len(n_str) == 1:
        n -= 1 if n > 0 else 0
        return n
    else:
        front, end = partition(n)
        if front >= end:
            front -= 1
        is_len_even = True if len(n_str) % 2 == 0 else False
        return combine(front, is_len_even)

if __name__ == '__main__':
    n = 999
    n_bigger = int(bigger(n))
    n_smaller = int(smaller(n))
    n_closest = n_smaller if n-n_smaller < n_bigger-n else n_bigger
    print(n_closest)
