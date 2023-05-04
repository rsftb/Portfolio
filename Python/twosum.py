"""
A function that solves the two-sum problem
What are all permutations of a given sequence of numbers that add up to the target number?
"""

numbers = [5, 7, 4, 1, 3, 8, 5, 2, 14, 1]

def twoSum(seq, target):
    permutations = []

    for static_num in range(0, len(seq)):
        for dynamic_num in range(0, len(seq)):

            if static_num == dynamic_num:
                continue   
            if seq[static_num] + seq[dynamic_num] == target: # or seq[static_num] - seq[dynamic_num] == target
                permutations.append((seq[static_num], seq[dynamic_num]))

    if not permutations:
        print("No combination of numbers hit the target")
        return None
    else:
        return permutations


print(twoSum(numbers, 10))
