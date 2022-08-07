from flask import Flask, render_template, request

app = Flask(__name__)

@app.get('/')
def form():
  return render_template('form.html')

COST = {
  'paradosiaki': 0.50,
  'araviki':1.20,
  'pork_gyro':1.70,
  'chicken_gyro':1.70,
  'pork':1.90,
  'chicken':1.90,
  'veggie':1.20,
  'fries':0.30,
  'bacon':0.50
}

@app.post('/calculate')
def calculate():
  # Read form variables
  name = request.form.get('name')
  quantity = request.form.get('quantity', type=int, default=1)
  pita = request.form.get('pita')
  meat = request.form.get('meat')
  extras = request.form.getlist('extras')
  
  # Calculate Cost
  cost = sum([COST[material] for material in (pita, meat, *extras)])
  
  # Render a dynamic page
  return str(cost)

app.run(host='0.0.0.0', port=81)