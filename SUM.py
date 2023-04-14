#create a function that takes a list of numbers as input and returns
#the sum of those numbers
#write a fuction that takes a string as input and returns a
#number of vowels in the string

def sum_numbers(numbers):
    total=0
    for numbers in numbers:
        total+=numbers
    return total
numbers_list=[1,2,3,4,5,6]
print(sum_numbers(numbers_list))

def count_vowels(mystring):
    vowel="aeiou"
    count=0
    for letters in mystring:
        if letters.lower() in vowel:
            count+=1
    return count
word="underneath"
print(count_vowels(word))