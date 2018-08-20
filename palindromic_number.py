"""
Find the closest palindrome number to a certain number.
"""


def get_front_end(n):
    n_str = str(n)
    if len(n_str) == 1:
        raise ValueError('len of n should be bigger than 1.')
    elif len(n_str) % 2 != 0:
        front = int(n_str[:len(n_str)//2+1])
        end = int(n_str[:(len(n_str)//2-1):-1])
        return front, end
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
    n_str = str(n)
    if len(n_str) == 1:
        n += 1 if n != 9 else 2
        return n
    elif len(n_str) % 2 != 0:
        front, end = get_front_end(n)
        if front <= end:
            front += 1
            return combine(front, False)
        else:
            return combine(front, False)
    else:
        front, end = get_front_end(n)
        if front <= end:
            front += 1
            return combine(front, True)
        else:
            return combine(front, True)


def smaller(n):
    n_str = str(n)
    if len(n_str) == 1:
        n -= 1 if n != 0 else 0
        return n
    elif len(n_str) % 2 != 0:
        front, end = get_front_end(n)
        if front >= end:
            front -= 1
            return combine(front, False)
        else:
            return combine(front, False)
    else:
        front, end = get_front_end(n)
        if front >= end:
            front -= 1
            return combine(front, True)
        else:
            return combine(front, True)

if __name__ == '__main__':
    n = 99998899999
    n_bigger = int(bigger(n))
    n_smaller = int(smaller(n))
    n_closest = n_bigger if n_bigger-n < n-n_smaller else n_smaller
    print(n_closest)
