from typing import Any

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    try:
        args_sum = 0
        args_len = len(args)
        args_list = list(args)
        for num in args:
            args_sum += num
    except TypeError as e:
        print("ERROR: ", e)

    try:
        for key, value in kwargs.items():
            if value == "mean":
                 mean(args_sum, args_len)
            if value == "median":
                median(args_list)

    except:
        print("ERROR")


def mean(args_sum, args_len):
    try:
        mean = args_sum / args_len
        return print("mean :", mean)
    except:
        print("ERROR")

def median(args_list):
    try:
        args_list.sort()
        median = len(args_list) // 2
        return print("median: ", args_list[median])
    except :
        print("ERROR median")

