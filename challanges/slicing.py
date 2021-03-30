challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def flatten(l):
    res = []
    for i in l:
        if isinstance(i, list): res.extend(flatten(i))
        else: res.append(i)
    return res

fChallenge = flatten(challenge)

sqa = fChallenge[2:5]
print(f"My {sqa[1]}! The {sqa[0]} do {sqa[2]}!")

def flattenDict(lD):
    res = []
    for ele in trial:
        if isinstance(ele, dict): res.extend(ele)
        else: res.append(ele)
    return res
challange = fChallenge
trial = flattenDict(trial)
nightmare = flattenDict(nightmare)

def printMessage(one, two, three):
    print(f"My {one}! The {two} do {three}!")

printMessage(challange[3], challange[2], challange[4])
printMessage(trial[2], trial[3], trial[4])
printMessage(nightmare[2],nightmare[3],nightmare[4] )
