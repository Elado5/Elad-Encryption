import string

asc = list(string.ascii_letters) + list(string.digits)
print(len(asc))

"""Encryption function - takes a text (string) and a key, turns the text in a list, creates a new list and an int
 counter, loops for each letter in the string (turned list), raise the counter by 1 and add that letter to the new list,
 with the addition of the key multiplied by the counter+key if the modulo of the key by the current counter returns 0.
 Then we turn return the new list after we turn it into a string and reverse it to make it more ambiguous."""


def enc(text, key):
    e = list(text)
    lst = []
    counter = 0
    for x in e:
        counter += 1
        lst += x
        if key % counter == 0:
            lst += str(key * (counter + key))
    res = ''.join(lst)[::-1]
    res = res.replace("\n", "r6r5r6r5###2345)(05gd%^&bM-=4")
    return res


"""Reverses the encryption process"""


def dec(text, key):
    el = str(text).replace("r6r5r6r5###2345)(05gd%^&bM-=4", "\n")
    el = el[::-1]
    e = list(el)
    counter = 0

    for x in e:
        counter += 1
        if key % counter == 0:
            cipher_addition = str(key * (counter + key))
            el = el.replace(cipher_addition, "", 1)
    return el


"""forced decryption - takes a text hint (so it knows what to look for in general) and then a key search range.
   A 'for' loop starts and runs the decryption algorithm for *search range* times, if a result that contains the hint
   text exists - it returns the result and the key that worked and then the loop ends.
   New lines will be replaced with a long random text (very close to 0 that this exact text will exist in a text file
   the user wants to decrypt so there shouldn't be a problem with that.
   If it doesn't find a string that contains the hint text, it returns 'no plausible result found'"""


def force_dec(text, hint, search_range):
    for num in range(search_range):
        el = str(text).replace("r6r5r6r5###2345)(05gd%^&bM-=4", "\n")
        el = el[::-1]
        e = list(el)

        counter = 0
        for x in e:
            counter += 1
            if num % counter == 0:
                cipher_addition = str(num * (counter + num))
                el = el.replace(cipher_addition, "", 1)
        if hint in el:
            return "Decrypted text: " + el + "\nkey: " + str(num)

    return "No plausible result found"


txt = "elado123@gmail.com\n555\nroberto"
# print(txt)

output = enc(txt, 51030)
print(output)

output2 = dec(output, 51030)
print(output2)

output3 = force_dec(output, "gmail.com", 55001)
print(output3)
