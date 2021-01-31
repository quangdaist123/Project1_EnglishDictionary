import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

word = "rain"
cursor = con.cursor()
query = cursor.execute(f"SELECT Definition FROM Dictionary where Expression = '{word}'")
result = cursor.fetchall()
print(result)

#
#
# def translate(w):
#     similar_words = get_close_matches(w, word_list, 3, 0.8)
#     if w in word_list:
#         print(*word_dict[w], sep='\n')
#     elif w.capitalize() in word_list:
#         print(*word_dict[w.capitalize()], sep='\n')
#     else:
#         if len(similar_words) == 0:
#             print('Khong tim thay tu vung')
#         else:
#             print(f'Did you mean: {similar_words}?')
#             choice = int(input(f'Enter position of the word, from 1 to {len(similar_words)}: '))
#             translate(similar_words[choice-1])
#
#
# # Get the input from the user
# while True:
#     word = str(input('Nhap tu can tra: ')).lower()
#     translate(word)
#     if word == "exit":
#         break
#
