def palindrome(str):
    for i in range(len(str) // 2):
        if str[i] != str[-(i+1)]:
            return False

    return True

palindrome('anna')



print(palindrome('banana'))