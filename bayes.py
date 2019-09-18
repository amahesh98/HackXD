from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
import numpy as np
import json

class NaiveBayesModel():

    #Constructor
    def __init__(self, trainFilePath, testFilePath):
        #Initialize model variables
        with open(trainFilePath) as train:
            self.trainData = json.load(train)
        with open(testFilePath) as test:
            self.testData = json.load(test)
        self.uniqueIngredients, self.numUnique = self.getUniqueIngredients(self.trainData)
        self.trainVectors, self.trainLabels = self.getTrainVectors(self.trainData)
        self.testVectors = self.getTestVectors(self.testData)
        self.model = GaussianNB()

    #Get number of unique ingredients
    def getUniqueIngredients(self,trainData):
        ingredientsDictionary = {}
        uniqueIndentifier = 1
        for item in self.trainData:
            for ingredient in item["ingredients"]:
                if ingredient not in ingredientsDictionary:
                    ingredientsDictionary[ingredient] = uniqueIndentifier
                    uniqueIndentifier += 1
        return ingredientsDictionary, uniqueIndentifier - 1

    #Get train vectors
    def getTrainVectors(self,trainData):
        #Create trainVectors list and labels list
        # trainVectors = np.asarray([np.asarray(vector["ingredients"]) for vector in self.trainData])
        trainLabels = [np.asarray(vector["cuisine"]) for vector in self.trainData]
        trainVectors = []
        for item in trainData:
            featureVector = [0.0] * 65 #max length of an ingredient vector in trainData
            currentCount = 0
            for ingredient in item["ingredients"]:
                featureVector[currentCount] = self.uniqueIngredients[ingredient]
                currentCount += 1
            while currentCount < 65:
                featureVector[currentCount] = 0
                currentCount += 1
            trainVectors.append(featureVector)
        return trainVectors,trainLabels

    #Get test vectors
    def getTestVectors(self, testData):
        testVectors = []
        for item in testData:
            featureVector = [0.0] * 65 #max length of an ingredient vector in testData
            currentCount = 0
            for ingredient in item["ingredients"]:
                if ingredient in self.uniqueIngredients:
                    featureVector[currentCount] = self.uniqueIngredients[ingredient]
                else:
                    featureVector[currentCount] = 0
                currentCount += 1
            while currentCount < 65:
                featureVector[currentCount] = 0
                currentCount += 1
            testVectors.append(featureVector)
        return testVectors

     #Train model on trainData
    def trainModel(self):
        self.model.fit(self.trainVectors, self.trainLabels)

    #Make predictions on testData
    def predict(self):
        predictions = self.model.predict(self.testVectors)
        for item in predictions:
            print(item)



    
def main():
    # iris = datasets.load_iris()
    # print(iris.data.shape)
    trainFile = "train.json"
    testFile = "test.json"
    bayesianModel = NaiveBayesModel(trainFile, testFile)
    bayesianModel.trainModel()
    bayesianModel.predict()
    
    

if __name__ == '__main__':
    main()
