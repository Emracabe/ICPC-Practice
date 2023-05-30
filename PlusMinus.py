n = int(input())
numbers = list(map(int, input().split()))

def get_percentage(b, total):
    return b / total

def plusMinus(arr):
    positive_values = len(list(filter(lambda number: number > 0, arr)))
    negative_values = len(list(filter(lambda number: number < 0, arr)))
    zeros = len(list(filter(lambda number: number == 0, arr)))

    positive_result = get_percentage(positive_values, len(arr))
    negative_result = get_percentage(negative_values, len(arr))
    zero_result = get_percentage(zeros, len(arr))

    print("{:.6f}".format(positive_result))
    print("{:.6f}".format(negative_result))
    print("{:.6f}".format(zero_result))

plusMinus(numbers)