#I/We _____Rand Ashour__________ declare that I/We have completed this computer code in accordance with the UAB Academic Integrity Code and the UAB CS Honor Code.  I/We have read the UAB Academic Integrity Code and understand that any breach of the Code may result in severe penalties.	
#Student signature(s)/initials: _____R.A_______	
#Date: ______10/1/2025______

from itertools import combinations
import numpy as np
n=100000
faces = np.arange(1, 14).tolist()
suits = ['spades', 'diamonds', 'hearts', 'clubs']

cards = []
for face in faces:
    for suit in suits:
        cards.append([face, suit])

cards
[[1, 'spades'],
[1, 'diamonds'],
[1, 'hearts'],
[1, 'clubs'],
[2, 'spades'],
[2, 'diamonds'],
[2, 'hearts'],
[2, 'clubs'],
[3, 'spades'],
[3, 'diamonds'],
[3, 'hearts'],
[3, 'clubs'],
[4, 'spades'], 
[4, 'diamonds'],
[4, 'hearts'],
[4, 'clubs'],
[5, 'spades'],
[5, 'diamonds'],
[5, 'hearts'],
[5, 'clubs'],
[6, 'spades'],
[6, 'diamonds'],
[6, 'hearts'],
[6, 'clubs'],
[7, 'spades'],
[7, 'diamonds'],
[7,'hearts'],
[7,'clubs'],
[8, 'spades'],
[8, 'diamonds'],
[8,'hearts'],
[8,'clubs'],
[9, 'spades'],
[9, 'diamonds'],
[9,'hearts'],
[9,'clubs'],
[10, 'spades'],
[10, 'diamonds'],
[10,'hearts'],
[10,'clubs'],
[11, 'spades'],
[11, 'diamonds'],
[11,'hearts'],
[11,'clubs'],
[12, 'spades'],
[12, 'diamonds'],
[12,'hearts'],
[12,'clubs'],
[13, 'spades'],
[13, 'diamonds'],
[13, 'hearts'],
[13, 'clubs']]
all_hands = list(combinations(cards, 5))
counter = 0
for hand in all_hands:
    hand_faces = [card[0] for card in hand] # Get the face of each card
    unique_faces = set(hand_faces)
    if len(unique_faces) == 2 and (hand_faces.count(list(unique_faces)[0]) in [2,3]):
        counter += 1
counter

total_hands = len(all_hands)
simprobability = counter / total_hands
print("Simulated:", simprobability)
exact=.00144
print("exact: ", exact)
diff=simprobability-exact
print("Difference: " ,diff)


