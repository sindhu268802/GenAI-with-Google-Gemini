# Nutritionist Generative AI Doctor using Google Gemini

This is a Streamlit web application that uses Google Gemini model `gemini-2.5-flash` to analyze the images of food and provide a detailed calories of the food items in the plate and suggests healthy balanced meal plate.
## 🚀 Features
- Upload a meal image (JPG, PNG. JPEG)
- Detects food items in the picture
- Estimates calories per item & total calories
- Provides a nutrition tip (balanced, high carb, oily, etc.)
- Suggests a healthier alternative diet
- Simple Streamlit UI
## ⚙️ Installation & Setup
#### 1. Clone the Repository  
```
git clone https://github.com/your-username/nutritionist-coacher.git
cd nutritionist-coacher
```
#### 2. Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```
#### 3. Install Dependencies
```
pip install -r requirements.txt
```
#### 4. Set Up Google Gemini API
Create a `.env` file in the project root and add:
```
GEMINI_API_KEY=your_api_key_here
```
#### 5. Run the APP
```
streamlit run app.py
```
## 🎯 Usage
1. Upload an image of your meal.
2. Click Tell me about my meal
3. Get a detailed calories of all food items and suggestions on helathy balanced diet.
  
