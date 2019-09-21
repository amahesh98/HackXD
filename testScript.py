import json
import bayes


def buildFile():
    with open("train.json") as train:
        trainData = json.load(train)
    f = open("ingredientsList", "w")
    ingredientsSet = set()
    for item in trainData:
        ingredients = item["ingredients"]
        for ingredient in ingredients:
            ingredientsSet.add(ingredient)
    f.write("[")
    for ingredient in ingredientsSet:
        f.write("\"%s\"," % (ingredient))
    f.write("]")


def predict(model, testVector):
    predictions = model.predictOnSample(testVector)
    for item in predictions:
        print(item)


def main():
    # buildFile()
    trainFile = "validation_train.json"
    testFile = "validation_test.json"
    bayesianModel = bayes.NaiveBayesModel(trainFile, testFile)
    bayesianModel.trainModel()
    testVector = [
        "asian eggplants",
        "fresh ginger",
        "basil leaves",
        "garlic cloves",
        "fresh coriander",
        "roast",
        "sauce",
        "lime leaves",
        "chicken stock",
        "cherry tomatoes",
        "mint leaves",
        "green chilies",
        "fresh pineapple",
        "brown sugar",
        "cooking oil",
        "red curry paste",
        "coconut milk"
    ]
    predict(bayesianModel, testVector)


if __name__ == "__main__":
    main()
