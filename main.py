import os  # to get file name on in save dialog function
import pyperclip  # to copy output text to clipboard
from tkinter import *
from tkinter import filedialog

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


"""function to show the result of the encryption in the output label.
it checks if a valid input exists in the "shift" field and outputs the result or an error message."""


def encrypt():
    # print(str(shift.get("1.0", "end")))
    try:
        int(key.get("1.0", "end"))
        is_dig = True
    except:
        is_dig = False

    if is_dig:
        output.config(
            text=(enc(textbox.get("1.0", "end"), int(key.get("1.0", "end"))
                      ).rstrip("\n")))

        return
    else:
        output.config(
            text="error - wrong key input")
        print(str(key.get("1.0", "end")))


"""function to show the result of the decryption in the output label.
it checks if a valid input exists in the "shift" field and outputs the result or an error message."""


def decrypt():
    # print(str(shift.get("1.0", "end")))
    try:
        int(key.get("1.0", "end"))
        is_dig = True
    except:
        is_dig = False

    if is_dig:
        output.config(
            text=(dec(textbox.get("1.0", "end"), int(key.get("1.0", "end"))
                      )))
        return
    else:
        output.config(
            text="error - wrong shift input")
        print(str(key.get("1.0", "end")).rstrip("\n"))


def force_decrypt():
    try:
        int(search_range.get("1.0", "end"))
        is_dig = True
    except:
        is_dig = False

    if is_dig:

        if int(search_range.get("1.0", "end")) > 1500000:
            output.config(
                text="That search range could be harmful to your PC, try below 1500000")
            return

        output.config(
            text=(force_dec(textbox.get("1.0", "end"), str(hint.get("1.0", "end")).rstrip("\n"), int(search_range.get
                                                                                                     ("1.0", "end")))))
        # print(str(hint.get("1.0", "end")))
        return
    else:
        output.config(
            text="error - wrong search range input")


"""Import file dialog function"""


def import_dialog():
    file1 = filedialog.askopenfilename()

    # if you click 'cancel' in the dialog 'file1' is simply an empty string.
    if file1 == "":
        textbox.delete('1.0', END)
        output.config(text="")
        return

    # if it isn't a text file
    elif not file1.endswith('.txt'):
        textbox.delete('1.0', END)
        textbox.insert("1.0", "Wrong file type, please use text files.")

    else:
        file2 = open(file1, "r")
        if file2.readable():
            textbox.delete('1.0', END)
            textbox.insert("1.0", file2.read())
            file2.close()


"""Save output from 'output' box to file - dialog function"""


def save_dialog():
    # if there's an error text in output label or if it's empty - give error
    if "error" in str(output.cget("text")) or len(str(output.cget("text"))) == 0:
        output.config(
            text="error - no encryption/decryption result to save")
        return

    s_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if s_file is None:
        return
    file_text = str(output.cget("text"))
    s_file.write(file_text)


"""Output encrypted result to file - dialog function"""


def save_dialog_en():
    if len(textbox.get("1.0", "end-1c")) == 0:
        output.config(
            text="error - no text was given")
        return

    try:
        int(key.get("1.0", "end"))
        is_dig = True
    except:
        is_dig = False

    if is_dig:
        text_var = (enc(textbox.get("1.0", "end"), int(key.get("1.0", "end")),
                        ))

        s_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if s_file is None:
            return
        s_file.write(text_var)

        only_file_name = os.path.basename(s_file.name)

        output.config(
            text=("File saved successfully - file name: " + only_file_name))

    else:
        output.config(
            text="error - wrong shift input")


"""Output decrypted result to file - dialog function"""


def save_dialog_force_de():
    if len(textbox.get("1.0", "end-1c")) == 0:
        output.config(
            text="error - no text was given")
        return

    if len(str(hint.get("1.0", "end")).replace("\n", "", 1)) == 0:
        output.config(
            text="error - no hint was given")
        return

    try:
        int(search_range.get("1.0", "end").replace("\n", "", 1))
        is_dig = True
    except:
        is_dig = False

    if is_dig:

        if int(search_range.get("1.0", "end")) > 1500000:
            output.config(
                text="That search range could be harmful to your PC, try below 1500000")
            return

        text_var = (force_dec(textbox.get("1.0", "end"), str(hint.get("1.0", "end")).rstrip("\n"), int(search_range.get
                                                                                                       ("1.0", "end"))))

        if text_var == "No plausible result found":
            output.config(
                text=text_var)
            return

        s_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if s_file is None:
            return
        s_file.write(text_var)

        # filtering the file name from file path
        only_file_name = os.path.basename(s_file.name)

        output.config(
            text=("File saved successfully - file name: " + only_file_name))

    else:
        output.config(
            text="error - wrong search range input")


def save_dialog_de():
    if len(textbox.get("1.0", "end-1c")) == 0:
        output.config(
            text="error - no text was given")
        return

    try:
        int(key.get("1.0", "end"))
        is_dig = True
    except:
        is_dig = False

    if is_dig:
        text_var = (dec(textbox.get("1.0", "end"), int(key.get("1.0", "end"))
                        )).replace("\n", "", 1)

        s_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if s_file is None:
            return
        s_file.write(text_var)

        # filtering the file name from file path
        only_file_name = os.path.basename(s_file.name)

        output.config(
            text=("File saved successfully - file name: " + only_file_name))

    else:
        output.config(
            text="error - wrong shift input")


"""creating the tkinter window"""
window = Tk()
window.title("Elad - Encryption Project")
window.wm_geometry("900x700")  # app size
window.resizable(0, 0)

photo = PhotoImage(file="BGTK.png")
background_label = Label(window, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Label(window, text="Enter the text you want to encrypt/decrypt:", bg="LightSteelBlue4", fg="white",
      font="none 12 bold").grid(
    row=1, column=0, sticky=W)

"""creating a text widget for the input text"""
textbox = Text(window, width=40, height=3, bg="LightSteelBlue1")
textbox.grid(row=2, column=0, sticky=W)

"""import file button"""
f_btn = Button(window, width=11, height=2, bg="turquoise2", command=import_dialog, text="Import file")
f_btn.grid(row=2, column=1, sticky=W)

"""encrypt to file button"""
en_btn = Button(window, width=20, height=2, bg="DeepSkyBlue2", command=save_dialog_en, text="Encrypt To File")
en_btn.grid(row=3, column=1, sticky=W)

"""decrypt to file button"""
de_btn = Button(window, width=20, height=2, bg="DeepSkyBlue3", command=save_dialog_de, text="Decrypt To File")
de_btn.grid(row=4, column=1, sticky=W)

"""force decrypt to file button"""
de_btn = Button(window, width=20, height=2, bg="SteelBlue3", command=save_dialog_force_de, text="Force Decrypt To File")
de_btn.grid(row=5, column=1, sticky=W)

Label(window, text="Enter encryption/decryption key:", bg="LightSteelBlue4",
      fg="white",
      font="none 12 bold").grid(row=3, column=0, sticky=W)

"""text widget for key input"""
key = Text(window, width=40, height=1, bg="LightSkyBlue1", font="none 11")
key.grid(row=4, column=0, sticky=W)

"""copy key to clipboard button"""
copy_btn = Button(window, width=21, height=2, bg="SteelBlue1",
                  command=lambda: pyperclip.copy(key.get("1.0", "end").replace("\n", "", 1)),
                  text="Copy "
                       "Key "
                       "To"
                       " Cli"
                       "pbo"
                       "ard")
copy_btn.grid(row=6, column=1, sticky=W)

"""encryption button"""
btn = Button(window, width=11, height=2, bg="SteelBlue1", command=encrypt, text="Encrypt")
btn.grid(row=5, column=0, sticky=W)

"""decryption button"""
btn2 = Button(window, width=11, height=2, bg="SteelBlue2", command=decrypt, text="Decrypt")
btn2.grid(row=6, column=0, sticky=W)

"""hint explanation"""
Label(window, text="Enter a text hint for the forced decryption to look for (i.e. '@gmail.com')", bg="LightSteelBlue4",
      fg="white",
      font="none 10 bold").grid(
    row=7, column=0, sticky=W)

"""text widget for text hint input"""
hint = Text(window, width=30, height=1, bg="LightSkyBlue1", font="none 11")
hint.grid(row=8, column=0, sticky=W)

"""search range explanation"""
Label(window, text="Enter a the range of keys you want the forced decryption to look for (for example: 5000 is "
                   "0-4999)\n"
                   "If the key result is 0 it means it was semi-decrypted.\n"
                   "Keep in mind a key too high (i.e. 200000+) could affect your pc, max key is 1500000:", bg="LightSteelBlue4", fg="white",
      font="none 9 bold").grid(
    row=9, column=0, sticky=W)

"""text widget for text search range input"""

search_range = Text(window, width=30, height=1, bg="LightSkyBlue1", font="none 11")
search_range.grid(row=10, column=0, sticky=W)

"""forced decryption button"""
force_btn = Button(window, width=11, height=2, bg="SteelBlue3", command=force_decrypt, text="Try Force")
force_btn.grid(row=11, column=0, sticky=W)

"""the result label"""
output = Label(window, text="", width=100, height=8, bg="azure2")
output.grid(row=12, column=0, sticky=W)

"""search range explanation"""
Label(window, text="If the output is very long it could go off-screen, you can copy/save it to view the whole text."
      , bg="LightSteelBlue4", fg="white",
      font="none 8").grid(
    row=13, column=0, sticky=W)

"""copy output to clipboard button"""
copy_btn = Button(window, width=11, height=2, bg="deep sky blue", command=lambda: pyperclip.copy(output.cget('text')
                                                                                                 .replace("\n", "", 1)),
                  text="Copy Output")
copy_btn.grid(row=14, column=0, sticky=W)

"""save output to file button"""
s_btn = Button(window, width=11, height=2, bg="DeepSkyBlue2", command=save_dialog, text="Save To File")
s_btn.grid(row=15, column=0, sticky=W)

"""exit button"""
btn = Button(window, width=11, height=2, bg="dark orange", command=window.destroy, text="Exit")
btn.grid(row=16, column=0, sticky=W)

window.mainloop()
