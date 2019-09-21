from flask import Flask, session, jsonify, render_template, redirect, request
app=Flask(__name__)
app.secret_key='ChefMate!!'
import bayes

Bayes_Model = bayes.NaiveBayesModel('train.json', 'test.json')
Bayes_Model.trainModel()

@app.route('/')
def renderIndex():
    session['items']=[]
    return render_template("index.html")

@app.route('/addItem/<item>')
def addItem(item):
    items = session['items']
    items.append(item)
    session['items']=items
    return jsonify({'addedItem': item, 'items':items})

@app.route('/processSearch')
def processSearch():
    print("Searching")
    items=session['items']
    prediction = Bayes_Model.predictOnSample(items)
    print("Prediction:", prediction)
    return jsonify({'prediction':prediction[0]})


if __name__ == '__main__':
    app.run(debug=True)