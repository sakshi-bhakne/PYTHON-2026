#Ques : Given an array, find the sum of:
#The highest frequency of any element.
#The lowest frequency of any element.
#We add frequency values, not the elements themselves.

def sum_highest_lowest_frequency(arr):
    max_freq = 0
    min_freq = float('inf')

    for num in arr:
        count = 0

        for other in arr:
            if other == num:
                count += 1

        max_freq = max(max_freq, count)
        min_freq = min(min_freq, count)

    return max_freq + min_freq


print(sum_highest_lowest_frequency([10, 9, 7, 7, 8, 8, 8]))  