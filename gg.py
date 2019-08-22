import markovify

with open("nicemessages.txt", encoding="utf-8") as messages:
    text = messages.read()

text_model = markovify.NewlineText(text)

for i in range(1):
    print (text_model.make_sentence(tries=50))

