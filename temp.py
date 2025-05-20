import random
random.seed(0)

def rollDie():
    return random.randint(1,6)

def runSim(goal, numTrials, txt):
    """Simulates rolling dice to estimate the probability of forming a specific string.
    
    This function runs multiple trials, each consisting of rolling a die several times to form a string, and estimates the probability of matching a target string.

    Args:
        goal (str): The target string to match, representing the desired sequence of die rolls.
        numTrials (int): The number of simulation trials to run.
        txt (str): A label for the target string, used in output messages.

    Returns:
        None: Prints the actual and estimated probabilities to the console.
    """
    totalNeededTrials = 0

    for _ in range(numTrials):
        # result = ''
        # for _ in range(len(goal)): # for every trial we roll the dice len(goal) number of times and check if the formed string is equal to our required string
        #     result += str(rollDie())
        result = ''.join(str(rollDie()) for _ in range(len(goal)))
        
        if result == goal: # if the formed string does match our required string we increment by 1 our needed trials as in how many times we got the required string in the given numTrials
            totalNeededTrials += 1 # this is used to get estimated probability

    print('Actual probability of', txt, '=', round(1/(6**len(goal)), 8))

    estProbability = round(totalNeededTrials/numTrials, 8)
    print('Estimated Probability of', txt, '=', round(estProbability, 8))

runSim('11111', 1000000, '11111') # if the event is rare you better run a lot of trials before you believe you estimated probability