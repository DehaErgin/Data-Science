# #Question1
number = float(input("Enter any number: "))
if (number == 0):
    print("number = 0")
else:
    if (number > 0):
        sign = "number positive"
    else:
        sign = "number negative"

    if (number % 2 == 0):
        oddOrEven = "even"

    else:
        oddOrEven = "odd"
    print(f"{sign} {oddOrEven}")


# #Question2
word = input("Enter any word: ")
frequency = {}

for char in word:
    if(char) in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)


#Question3
password = input("Enter your password: ")
if len(password) < 8:
    print("Password should be at least 8 character")
else:
    hasUpper = False
    for char in password:
        if char.isupper():
            hasUpper = True
            break
    if not hasUpper:
        print("The password should contain at least 1 uppercase character")
    else:
        hasDigit = False
        for char in password:
            if char.isdigit():
                hasDigit = True
                break

        if not hasDigit:
            print("The password should contain at least 1 number")
        else:
            print("password is valid")


#Question4
numbers = [12, 4, 9, 25, 30, 7, 18]
average = sum(numbers) / len(numbers)
newList = [num for num in numbers if num > average]
print(f"list average: {average}\nNumbers greater than average: {newList}")


#Question5
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()

#Question6
total = 0
count = 0
while True:
    number = float(input("Enter any number: "))
    if (number == 0):
        break
    total += number
    count += 1
    average = total / count
print(f"Sum of numbers: {total}")
print(f"Average of numbers: {average}")

#Question7
word = input("Enter a words: ")
word_lower = word.lower()
reversed_word = word_lower[::-1]

if word_lower == reversed_word:
    print(f"'{word}' is palindrom")
else:
    print(f"'{word}' is not palindrom")

#Question8
#method 1
_list = []
for i in range(1,100):
    if (i % 3 == 0 and i % 5 == 0):
        _list.append(i**2)
print(_list)

# #list comprehension
# #method2
numbers = [i**2 for i in range(1, 100) if i % 3 == 0 and i % 5 == 0]
print(numbers)


#Question9
sentence = input("Enter a sentence: ")
words = sentence.split()
capitalizedWords = [word.capitalize() for word in words]
newSentence = " ".join(capitalizedWords)
print(newSentence)


#Mini Project
movieComments = []
commentNumbers = 0
goodCommentNumbers = 0
lengthOfComments = []

print("Write 'quit' to quit")

while True:
    comment = input(f"{commentNumbers + 1}. comment: ")
    if comment.lower() == "quit":
        break

    movieComments.append(comment)
    commentNumbers += 1

if not commentNumbers:
    print("no comments")
else:
    for comment in movieComments:
        lengthOfComments.append(len(comment))
        if "good" in comment.lower():
            goodCommentNumbers += 1
    
    longestComment = max(movieComments, key=len)
    shortestComment = min(movieComments, key=len)
    averageLenght = sum(lengthOfComments) / len(lengthOfComments)

    print(f"Total comment numbers: {commentNumbers}")
    print(f"Number of comments containing the word 'good': {goodCommentNumbers}")
    print(f"Longest comment: {longestComment}")
    print(f"Shortest comment: {shortestComment}")
    print(f"Average length of comments: {averageLenght}")
