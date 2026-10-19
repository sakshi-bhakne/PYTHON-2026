#Ques 1 : Given an array of integers, return the element that appears the most times.If multiple elements share the highest 
# frequency, return the smallest element among them.

def highest_occurring_element(nums):
    max_freq = 0
    ans = float('inf')

    for num in nums:
        count = 0

        for other in nums:
            if other == num:
                count += 1

        if count > max_freq:
            max_freq = count
            ans = num
        elif count == max_freq and num < ans:
            ans = num

    return ans


nums = [2, 4, 3, 2, 5, 4]
print(highest_occurring_element(nums))  