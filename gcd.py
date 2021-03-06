

def euclidean(a: int, b: int) -> int:

    larger_num = max(a, b)
    smaller_num = min(a, b)

    remainder = larger_num % smaller_num

    if remainder == 0:
        return smaller_num
    elif remainder == 1:
        return remainder

    return euclidean(smaller_num, remainder)


if __name__ == "__main__":
    a = 24
    b = 56

    print(euclidean(a, b))
