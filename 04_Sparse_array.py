def matchingStrings(strings, queries):
    # Write your code here
    counts = []
    for query in queries:
        if query in strings:
            counts.append(strings.count(query))
        else:
            counts.append(0)    
    return counts   


print(matchingStrings(['ab','ab','abc'],['ab','abc','bc']))   