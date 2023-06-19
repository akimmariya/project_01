# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
#a=input('введи строку c восклиц знаками')
#def remove_exclamation_marks(a):
 #  b=a.replace('!','')
  # print (b)
#remove_exclamation_marks(a)



                             



# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"
d=input('введи строку c восклиц знаками')
def remove_last_em(d):
   if d[-1]=='!':
      c=d[:-1]
      print (c)
remove_last_em (d)
    



# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""Hi!
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

#a=input('введи строку c восклиц знаками')
#def remove_word_with_one_em(a):
 #  b=a.split(' ',2)
  # print (b)
  # for i in b:
  #    d=b[i].find(b[i],'!') 
  #    print (d)
#remove_word_with_one_em(a)