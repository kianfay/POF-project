
""""""""""""
"""
Tallies votes in a list against a dictionary of candidates, and 
returns a winner and tally results

Parameters:
    - votes         - a list of votes
    - candidates    - dictionary of candidates with length <= 16
"""
""""""""""""
def tallyVotes(votes, candidates):
    numCandidates = len(candidates)

    candidateDictionary = {}
    voteTally = {c : 0 for c in candidates}

    candidateCodes = ['00', 'ff', '22', '33', '44', '55', '66', '77',
        '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', '11']
    for i in range(len(candidates)):
        candidateDictionary[candidateCodes[i]] = candidates[i]
    print('Translation mapping: ', candidateDictionary)
    
    translatedVotes = list(map(lambda x: candidateDictionary[x], votes))
    for vote in translatedVotes:
        voteTally[vote] = voteTally[vote] + 1

    return(voteTally)
