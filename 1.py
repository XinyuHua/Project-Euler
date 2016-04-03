threshold_3 = 1000 / 3 + 1 
threshold_5 = 1000 / 5 + 1
summation = 0
for k in range(threshold_3):
    cur = 3 * k
    if cur % 5 != 0 and cur < 1000:
        summation += cur
for k in range(threshold_5):
    cur = 5 * k
    if cur < 1000:
        summation += cur
print summation


