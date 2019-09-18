import json

def uniqueCuisines(data):
    cuisines = []
    for entry in data:
        if entry['cuisine'] not in cuisines:
            cuisines.append(entry['cuisine'])
    return cuisines

def findCounts(data, cuisines):
    cuisineDict = {}
    for cuisine in cuisines:
        cuisineDict[cuisine] = {}
    for entry in data:
        thisCuisine = entry['cuisine']
        for item in entry['ingredients']:
            if item not in cuisineDict[thisCuisine]:
                cuisineDict[thisCuisine][item]=1
            else:
                cuisineDict[thisCuisine][item]+=1
    return cuisineDict

def findSimilarities(dictionary, c1, c2):
    dict1 = dictionary[c1]
    dict2 = dictionary[c2]

    sharedItems = []
    for key1 in dict1:
        for key2 in dict2:
            if(key1 == key2 and key2 not in sharedItems):
                sharedItems.append(key2)
    return sharedItems

def cleanData(data):
    newData=[]
    for entry in data:
        if(len(entry['ingredients']) > 5):
            newData.append(entry)
    return newData

if __name__ == '__main__':
    with open("train.json", "r") as data_file:
        raw_data = json.load(data_file)
        data = cleanData(raw_data)
        print(type(data))
        print(len(data))
        cuisines = uniqueCuisines(data)
        print(cuisines)
        cuisineDict = findCounts(data, cuisines)
        findSimilarities(cuisineDict, 'thai', 'irish')
        