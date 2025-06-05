from statistics import mode

def calculate_mean(data):
    mean = sum(data) / len(data)
    return mean

def calculate_median(data):
    data.sort()
    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        median = (data[mid - 1] + data[mid]) / 2
    else:
        median = data[mid]
    return median

mean