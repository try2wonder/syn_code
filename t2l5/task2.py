word = input("Enter your word here: ")
vowels = ['a','e','i','o','u']
vowels_cnt = [0,0,0,0,0]
cons_cnt = 0

for i in word:
    if i not in vowels:
        cons_cnt += 1
    else:
        x = vowels.index(i)
        vowels_cnt[x] += 1

print(f"We have {cons_cnt} consonants, {vowels_cnt[0]} 'a's, {vowels_cnt[1]} 'e's, {vowels_cnt[2]} 'i's, {vowels_cnt[3]} 'o's, {vowels_cnt[4]} 'u's")

# Я не понял, что подразумевается под "Если какой-то из перечисленных букв нет - Выведите False". 
# Вывести на месте её счётчика False? 
# Вывести False как результат всей программы если хоть одной гласной нет?