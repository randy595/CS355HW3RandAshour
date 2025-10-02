#I/We _____Rand Ashour__________ declare that I/We have completed this computer code in accordance with the UAB Academic Integrity Code and the UAB CS Honor Code.  I/We have read the UAB Academic Integrity Code and understand that any breach of the Code may result in severe penalties.	
#Student signature(s)/initials: _____R.A_______	
#Date: ______10/1/2025______

import random

def seating(trials=50000):
    friends=["Alice", "Bob", "F3", "F4", "F5", "F6", "F7", "F8"]
    count=0
    for _ in range (trials):
        random.shuffle(friends)
        for i in range(len(friends) - 1):
            if (friends[i] == "Alice" and friends[i + 1] == "Bob") or \
               (friends[i] == "Bob" and friends[i + 1] == "Alice"):
                count += 1
                break 
    simulatedprob = count / trials
    return simulatedprob
if __name__ == "__main__":
    trials = 50000
    simulated= seating(trials)
    exact=.25
    diff= abs(simulated-exact)
    print("Simulated:", simulated)
    print("Exact: ", exact)
    print("Difference: ", diff)
    



