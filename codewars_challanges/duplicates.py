#Python program to remove consecutive strings.
 
# def remove_duplicates(sentence):
#     words = sentence.split(" ")
#     result = []
#     for word in words:
#         if word not in result:
#             result.append(word)
#     return " ".join(result)
 
# sentence = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
# print(remove_duplicates(sentence))

def remove_consecutive_duplicates(s):
    results =[]
    for word in s.split():
        if word not in results:
            results.append(word)
        elif results[-1] != word:
            results.append(word)
    return ' '.join(results)

s = 'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'
print(remove_consecutive_duplicates(s))