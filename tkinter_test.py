# -------------------------------------------------
import json
from difflib import get_close_matches
import tkinter as tk
import tkinter.messagebox


file_path = './data/data1.json'
data = [json.loads(line) for line in open(file_path, 'r')]
word_dict = data[0]
word_list = list(word_dict.keys())


def show_text(word):
    # Show the fixed 'result':
    lbl_fixed_result['text'] = "Result:"
    #
    meaning = '\n'.join(['- ' + word for word in word_dict[word]])
    txt_result.delete(1.0, tk.END)
    txt_result.insert(tk.END, f'{meaning}')


def translate():
    # lower() helps return meaning for both "Hello" and "hello" case
    w = ent_enter.get().lower()
    if w in word_list:
        show_text(w)
    elif w.capitalize() in word_list:
        show_text(w.capitalize())
    # Misspelling handling
    else:
        similar_words = get_close_matches(w, word_list, 3, 0.6)
        if len(similar_words) == 0:
            txt_result['text'] = 'Khong tim thay tu vung!!!'
        else:
            # SHOW QUESTION BOX
            suggest_list = ', '.join(['"'+word+'"' for word in similar_words])
            answer = tkinter.messagebox.askquestion(title='No word found',
                                                    message=f'Did you mean "{similar_words[0]}"?\
                                                            nSome of the suggestion are {suggest_list}')
            # hàm này sẽ trả về giá trị boolean
            if answer == 'yes':
                w = similar_words[0]
                show_text(w)
                ent_enter.delete(0, tk.END)
                ent_enter.insert(0, f'{w}')
            else:
                ent_enter.delete(0, tk.END)


# Creating GUI
window = tk.Tk()
window.title("Simple dictionary")
window.rowconfigure([0, 1, 2], minsize=40, weight=1)
window.columnconfigure([0, 1, 2], minsize=40, weight=1)

frm_title = tk.Frame(master=window)
lbl_title = tk.Label(master=frm_title, text="Simple English Dictionary")
lbl_title.pack()

frm_window = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
lbl_enter = tk.Label(master=frm_window, text="Enter: ")
ent_enter = tk.Entry(master=frm_window)
btn_translate = tk.Button(master=frm_window, text='Translate', command=translate, bg='pink')
lbl_enter.grid(row=1, column=0, padx=5, pady=5, sticky='news')
ent_enter.grid(row=1, column=1, padx=5, pady=5, sticky='news')
btn_translate.grid(row=1, column=2, padx=5, pady=5)

lbl_fixed_result = tk.Label(master=window)
txt_result = tk.Text(master=window)

frm_title.grid(row=0, column=1)
frm_window.grid(row=1, column=1, sticky='news', padx=5)
lbl_fixed_result.grid(row=2, column=0, sticky='ne', padx=5, pady=18)
txt_result.grid(row=2, column=1, sticky='nw', padx=5, pady=20)

window.mainloop()

