from flask import Flask, render_template, request
import google.generativeai as genai  # Assuming correct import path
import markdown

app = Flask(__name__)

# Load your Google API key from a secure environment variable
GOOGLE_API_KEY = "AIzaSyDzkoyl8p3hDfsV1CzWyCyNGj4_cvNTo-k"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_itinerary', methods=['POST'])
def generate_itinerary():
    location = request.form['location']
    soil = request.form['soil']

    # Generate content using the model
    response = model.generate_content(f"Give 5 suitable and 3 unsuitable crops for '{location} for type of soil {soil}'")

    # Convert Markdown to HTML
    markdown_text = response.text
    html_content = markdown.markdown(markdown_text)

    # Pass the HTML content to the template
    return render_template('result.html', itinerary_html=html_content)

if __name__ == '__main__':
    app.run(debug=True)
