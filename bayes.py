from sklearn.naive_bayes import BernoulliNB
from sklearn import datasets
import numpy as np
import json
import pickle

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
        # self.testVectors, self.testLabels = self.getTestVectors(self.testData)
        self.model = BernoulliNB()

    #Get Model Hyperparameters
    def getInfo(self):
        print(self.model.get_params())

    #Remove all samples with less than 5 ingredients
    def cleanData(self, data):
        newData = []
        for entry in data:
            if(len(entry['ingredients']) > 5):
                newData.append(entry)
        return newData

    #Get number of unique ingredients
    def getUniqueIngredients(self, trainData):
        ingredientsDictionary = {}
        uniqueIndentifier = 1
        for item in self.trainData:
            for ingredient in item["ingredients"]:
                if ingredient not in ingredientsDictionary:
                    ingredientsDictionary[ingredient] = uniqueIndentifier
                    uniqueIndentifier += 1
        return ingredientsDictionary, uniqueIndentifier

    #Get train vectors
    def getTrainVectors(self, trainData):
        #Create trainVectors list and labels list
        trainLabels = [vector["cuisine"] for vector in self.trainData]
        trainVectors = []
        for item in trainData:
            featureVector = [0.0] * self.numUnique
            for ingredient in item["ingredients"]:
                uniqueId = self.uniqueIngredients[ingredient]
                featureVector[uniqueId] = 1
            trainVectors.append(featureVector)
        return trainVectors, trainLabels

    #Get test vectors
    def getTestVectors(self, testData):
        testVectors = []
        testLabels = [vector["cuisine"] for vector in testData]
        for item in testData:
            featureVector = [0.0] * self.numUnique
            for ingredient in item["ingredients"]:
                if ingredient in self.uniqueIngredients:
                    uniqueId = self.uniqueIngredients[ingredient]
                    featureVector[uniqueId] = 1
            testVectors.append(featureVector)
        return testVectors, testLabels

    #Train model on trainData
    def trainModel(self):
        self.model.fit(self.trainVectors, self.trainLabels)

    #Make predictions on testData
    def predict(self):
        predictions = self.model.predict(self.testVectors)
        numCorrect = 0
        totalSamples = len(self.testLabels)
        for prediction, trueLabel in zip(predictions, self.testLabels):
            if(prediction == trueLabel):
                numCorrect += 1
        print("Accuracy on validation set: %.2f%%" % (100 * (numCorrect / totalSamples)))

    #Predict given one single vector
    def predictOnSample(self, testVector):
        totalTests = []
        featureVector = [0.0] * self.numUnique
        featureCount = 0
        for ingredient in testVector:
            if ingredient in self.uniqueIngredients:
                uniqueId = self.uniqueIngredients[ingredient]
                featureVector[uniqueId] = 1
        totalTests.append(featureVector)
        return self.model.predict(totalTests)

def main():
    trainFile = "validation_train.json"
    testFile = "validation_test.json"
    bayesianModel = NaiveBayesModel(trainFile, testFile)
    bayesianModel.trainModel()
    bayesianModel.predict()

if __name__ == '__main__':
    main()
