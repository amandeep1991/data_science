def zipped_tuples(input_iterable_tuple):
    min_length = min([ len(t_ele) for t_ele in input_iterable_tuple])
    wrong_iterables = list(filter(lambda x: len(x)>min_length, input_iterable_tuple))
    if len(wrong_iterables) == 0:
        return zip(*input_iterable_tuple)
    else:
        raise ValueError('all elements in the parameter "input_iterable_tuple" must be of same length')

print(list(zipped_tuples(("abc","abc","abc"))))
print(list(zipped_tuples(([1,2,3,4],['a','b','c','d'],[1.0,2.0,3.0,4.0],"abcd"))))