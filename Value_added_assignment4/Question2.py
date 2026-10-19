#Ques 2: Given an array, return the element with the second-highest distinct frequency.If multiple elements have that 
# frequency, choose the smallest element. If no second distinct frequency exists, return -1.

def second_highest_occurring_element(arr):
    elements = []
    frequencies = []

    for num in arr:
        if num not in elements:
            count = 0

            for other in arr:
                if other == num:
                    count += 1

            elements.append(num)
            frequencies.append(count)

    max_freq = max(frequencies)
    second_freq = 0

    for count in frequencies:
        if count < max_freq and count > second_freq:
            second_freq = count

    if second_freq == 0:
        return -1

    answer = float('inf')

    for i in range(len(elements)):
        if frequencies[i] == second_freq:
            answer = min(answer, elements[i])

    return answer


print(second_highest_occurring_element([10, 9, 7, 7]))  # 9