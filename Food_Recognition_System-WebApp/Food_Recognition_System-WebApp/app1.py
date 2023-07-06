from flask import *
import os
from werkzeug.utils import secure_filename
import label_image
import PreProcessing

def load_image(image):
    text = label_image.main(image)
    return text

app = Flask(__name__)

pp = PreProcessing
@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')

 
  
    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/index1')
def index1():
    #return "Index Page"
    return render_template('index1.html')

@app.route('/',methods = ['POST'])
def result():
    grains = request.form['grains']
    vegetables = request.form['vegetables']
    fruits = request.form['fruits']
    protein = request.form['protein']
    grains = float(grains)
    vegetables = float(vegetables)
    fruits = float(fruits)
    protein = float(protein)
    predictedResult = pp.healthy_diet(grains,vegetables,fruits,protein)
    print('Experience is ',predictedResult)
    predictedResult1 = pp.protein_diet(grains,vegetables,fruits,protein)
    print('Experience is ',predictedResult1)
    predictedResult2 = pp.grains_diet(grains,vegetables,fruits,protein)
    print('Experience is ',predictedResult2)    
    predictedResult3 = pp.vegetables_diet(grains,vegetables,fruits,protein)
    print('Experience is ',predictedResult3)    
    return render_template('result.html', PredictedResult = predictedResult,PredictedResult1 = predictedResult1,PredictedResult2 = predictedResult2,PredictedResult3 = predictedResult3,)

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)
        # Make prediction
        result = load_image(file_path)
        result = result.title()
        d = {"Chicken Curry":" → Nutrition Data- Protein 27.63g, Carbs 5.09g, Fat 11.97g, Fiber 1.1g Calories 243cal",
	'Fried Rice':" → Nutrition Data- Protein 9.39g, Carbs 31.38g, Fat 9.28g, Fiber 0.8g Calories 250cal",
        "Dosai":" → Nutrition Data- Protein 2.51g, Carbs 21.24g, Fat 1.04g, Fiber 0.8g Calories 106cal",
        "Chicken Briyani":" → Nutrition Data- Protein 15.9g, Carbs 48.07g, Fat 9.82g, Fiber 0.8g Calories 348cal",
        "Rice":" → Nutrition Data- Protein 4.2g, Carbs 44.08g, Fat 0.44g, Fiber 0.8g Calories 204cal",
        "Vada":" → Nutrition Data- Protein 10.59g, Carbs 40.97g, Fat 8.64g, Fiber 0.8g Calories 282cal",
        "Poori":" → Nutrition Data- Protein 7.54g, Carbs 46.73g, Fat 9.43g, Fiber 0.8g Calories 296cal",
        "Idly":" → Nutrition Data- Protein 5.72g, Carbs 23.68g, Fat 0.56g, Fiber 7.8g Calories 121cal"}
        result = result+d[result]
        #result2 = result+d[result]
        #result = [result]
        #result3 = d[result]        
        print(result)
        #print(result3)
        os.remove(file_path)
        return result
        #return result3
    return None

if __name__ == '__main__':
    app.run()