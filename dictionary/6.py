#we have dictionary that map characters into emojis
message=input(">") #gets you the message typed by the user
words=message.split(' ')
emojis={
    ":)":"🙂",
    ":(":"🙁",
    ":/":"😑"
}
output=""
for word in words:
    output += emojis.get(word,word) + " "
print(output)