from flask import Flask, render_template, redirect, request
app=Flask(__name__)
app.secret_key='ChefMate!!'

@app.route('/')
def renderIndex():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)