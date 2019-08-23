import markovify

with open("nicemessages.txt") as messages:
    text = messages.read()

sentence = markovify.NewlineText(text, state_size=1)

for i in range(1):
    print (sentence.make_short_sentence(280))

