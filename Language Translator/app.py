
import numpy as np
from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow import keras
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import custom_object_scope
# from Language_Translator.positional_embedding import PositionalEmbedding


app=Flask(__name__)

# # Get the absolute path to the model file
# model_path = os.path.join(os.path.Language Translator(__file__), "model.h5")

# # Load the model
# model = load_model(model_path)


# path='F:/Projects1/Language Translator/'
# with custom_object_scope({"PositionalEmbedding": PositionalEmbedding}):
model = tf.keras.models.load_model('F:/Projects/Projects1/Language Translator/model.h5')


@app.route('/')

def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/translatehere')
def translatehere():
    return render_template('translatehere.html')

@app.route('/predict',methods=['POST'])
def predict():
  int_features= [float(x) for x in request.form.values()]
  features=[np.array(int_features)]
  prediction=model.predict(features)

  output = prediction[0]
  return render_template('translatehere.html',prediction_text='Your tranlated Spanish text is {}'.format(output))

if __name__=="__main__":
  app.run(debug=True)

