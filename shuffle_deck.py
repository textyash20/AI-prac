import random
cardfaces=[]
suits=['Hearts','Diamond','Clubes','Spades']
royals=[ " ] "," Q "," K "," A "]
deck=[]
for i in range(2,11):
    cardfaces.append(str(i))
for j in range(4):
    cardfaces.append(royals[j])
for k in range(4):
    for l in range(13):
        card=(cardfaces[l]+" of "+suits[k])
        deck.append(card)
random.shuffle(deck)
for m in range(52):
    print(deck[m])
