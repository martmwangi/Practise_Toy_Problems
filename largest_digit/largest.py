def largest(num):
    a = list(str(num))
    b = sorted(a, reverse = True)
    return ''.join(b)
print (largest(234))
