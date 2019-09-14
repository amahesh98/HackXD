import json

def sortSet(hashset):
    ingredients = list(hashset)
    ingredients.sort()

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



def main():
    with open("recipe-ingredients-dataset/train.json") as trainFile:
        trainData = json.load(trainFile)
    ingredientsSet = set()
    for key in trainData:
        for item in key['ingredients']:
            ingredientsSet.add(item)
    sortSet(ingredientsSet)
    print(binarySearch(list(ingredientsSet), "lettuce"))

if __name__ == "__main__":
    main()
