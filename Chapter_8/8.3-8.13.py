import sys
def test(did_pass):
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
    
#7
def reverse(word):
    return(word[::-1])



#9
def remove_letter(letter,string):
    the_word_after=""
    for i in string:
        if i != letter:
            the_word_after += i
    return the_word_after

#10
def is_palindrome(word):
    if word == reverse(word):
        return True
    else:
        return False

#8
def mirror(string):
    final=string+reverse(string)
    return final


#11
def count(sub,string):
    count = 0
    if string.find(sub) >= 0:
        count += 1
    return count


def test_suite():
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)

test_suite()


print("i\ti*2\ti*3\ti*4\ti*5\ti*6\ti*7\ti*8\ti*9\ti*10\ti*11\ti*12")
for i in range(1, 13):
    print(i, "\t", i*2, "\t", i*3, "\t", i*4, "\t", i*5, "\t", i*6, "\t", i*7, "\t", i*8, "\t", i*9, "\t", i*10, "\t", i*11, "\t", i*12 )


