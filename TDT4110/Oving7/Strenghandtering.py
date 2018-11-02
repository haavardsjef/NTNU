# Strenghåndtering, Oving 7 ITGK
# Håvard Hjelmeseth


# definer funksjoner
def check_equal(str1, str2):
    return str1 == str2


def reversed_word(str):
    reversed = []
    for i in range(-1, -1 - len(str), -1):
        reversed.append(str[i])
    return "".join(reversed)


def check_palindrome(str):
    return str == reversed_word(str)


def contains_string(str1, str2):
    return str1.find(str2)


# Test av kode 1
print("Test av kode 1")
str1 = 'hei'
str2 = 'hello'
str3 = 'hello'
print(check_equal(str1, str2))
print(check_equal(str3, str2))
print()


# Test av kode 2
print("Test av kode 2")
str = 'Morna Jens'
print(reversed_word(str))
print()

# Test av kode 3
print("Test av kode 3")
str1 = 'agnes i senga'
str2 = 'hello'
print(check_palindrome(str1))
print(check_palindrome(str2))
print()

# Test av kode 4
print("Test av kode 4")
str1 = 'pepperkake'
str2 = 'per'
str3 = 'ola'
print(contains_string(str1, str2))
print(contains_string(str1, str3))
print()
