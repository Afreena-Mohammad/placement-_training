def separate_even_odd(lst):
    evens = [num for num in lst if num % 2 == 0]
    odds = [num for num in lst if num % 2 != 0]
    return evens, odds

def combine_recursively(evens, odds, evens_idx=0, odds_idx=0, results=None):
    if results is None:
        results = []

    if evens_idx >= len(evens):
        return results
    if odds_idx >= len(odds):
        return combine_recursively(evens, odds, evens_idx + 1, 0, results)
    
    results.append(evens[evens_idx] + odds[odds_idx])
    return combine_recursively(evens, odds, evens_idx, odds_idx + 1, results)

list1 = [6, 3, 2, 9, 4, 7]
list2 = [8, 7, 5, 3, 6, 9]

evens_list1, _ = separate_even_odd(list1)
_, odds_list2 = separate_even_odd(list2)

result = combine_recursively(evens_list1, odds_list2)
print(result)
