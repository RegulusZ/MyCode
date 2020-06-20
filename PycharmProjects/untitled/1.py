def isPalindrome(x):
    if x < 0:
        return False
    a = []
    while x > 0:
        a.append(x % 10)
        x = x//10
    b = list(reversed(a))
    if a == b:
        return True

print(isPalindrome(121))