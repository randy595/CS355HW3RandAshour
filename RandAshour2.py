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
    



