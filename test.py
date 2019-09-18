import json
import sys
import numpy as np

def sortSet(hashset):
    ingredients = list(hashset)
    ingredients.sort()
    return ingredients

def binarySearch(ingredientsList, search):
    low = 0
    high = len(ingredientsList) - 1
    while (low <= high):
        mid = int((low + high) / 2)
        if (ingredientsList[mid] > search):
            high = mid - 1
        elif (ingredientsList[mid] < search):
            low = mid + 1
        else:
            return ingredientsList[mid]
    
    return ""


def playground():
    with open("test.json") as train:
        trainData = json.load(train)
    maxCount = -1
    for item in trainData:
        ingredientsVector = item["ingredients"]
        if (len(ingredientsVector) > maxCount):
            maxCount = len(ingredientsVector)
    print(maxCount)
        



def main():
    playground()
    # programArguments = sys.argv
    # queryString = sys.argv[1]
    # with open("train.json") as trainFile:
    #     trainData = json.load(trainFile)
    # ingredientsSet = set()
    # for key in trainData:
    #     for item in key['ingredients']:
    #         ingredientsSet.add(item)
    # ingredientsList = sortSet(ingredientsSet)
    # print(binarySearch(ingredientsList, queryString))

if __name__ == "__main__":
    main()
