from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def htmlWebpage():
	return render_template('Playground_Level1.html')

"""@app.route('/play/<colorInput>')
def colorWebpage(colorInput=None):
    return render_template('Playground.html', setColor="green", colorInput=colorInput)"""

@app.route('/play/<numberString>')
def numberWebpage(numberString=None):
	numberInput = int(numberString)
	return render_template('Playground_Level2.html', setColor="green", numberInput=numberInput)

@app.route('/play/<numberString>/<colorInput>')
def colorNumberWebpage(numberString=None,colorInput=None):
	numberInteger = int(numberString)
	#numberInput = numberInteger + 1
	numberInput = numberInteger
	return render_template('Playground_Level3.html', setColor="green", numberInput=numberInput, colorInput=colorInput)

if __name__=="__main__":
    app.run(debug=True)