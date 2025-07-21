


from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

#  Configure your Gemini API Key securely
API_KEY = ""
genai.configure(api_key=API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel(model_name="gemini-2.5-flash")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    ingredients = data['ingredients']
    preference = data['preference']
    cuisine = data['cuisine']
    
    

    prompt = f"""
    You are a helpful cooking assistant.
    Suggest a recipe using the following ingredients: {ingredients}.
    The user prefers {preference} dishes.
    Preferred cuisine: {cuisine}.
    Give the name of the dish, ingredients needed, and step-by-step cooking instructions.
    Keep it short and simple.
    """

    try:
        response = model.generate_content(prompt)
        recipe = response.text.strip()
        return jsonify({"recipe": recipe})
    except Exception as e:
        print("Gemini API Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
