def main():
    print(ft_filter.__doc__)

    '''Test filtering even numbers'''
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\nnumbers = ", numbers)

    print("\nFilter even numbers:")
    even_numbers = ft_filter(lambda x: x % 2 == 0, numbers)
    print(list(even_numbers))

    '''Test filtering odd numbers'''
    print("\nFilter odd numbers:")
    odd_numbers = ft_filter(lambda x: x % 2 != 0, numbers)
    print(list(odd_numbers))

    print("\nFilter true values from [0, 1, '', 'hello', False, True]")
    '''Test filtering true values'''
    true_values = ft_filter(None, [0, 1, '', 'hello', False, True])
    print(list(true_values))

    words = ['apple', 'banana', 'grape', 'kiwi', 'oranges']
    print("\nwords: ", words)
    print("Filter words longer than 5 letters")
    long_words = ft_filter(lambda x: len(x) > 5, words)
    print(list(long_words))


def ft_filter(func, iterable):
    '''Return an iterator yielding those items of iterable for which function
(item) is true. If function is None, return the items that are true.'''
    if func is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if func(item)]


if __name__ == "__main__":
    main()
