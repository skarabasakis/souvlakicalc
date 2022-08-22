from flask import Flask, render_template, request
from decimal import Decimal

app = Flask(__name__)

@app.get('/')
def form():
  return render_template('form.html')

COST = {
  'paradosiaki': Decimal('0.50'),
  'araviki': Decimal('1.20'),
  'pork_gyro': Decimal('1.70'),
  'chicken_gyro': Decimal('1.70'),
  'pork': Decimal('1.90'),
  'chicken': Decimal('1.90'),
  'veggie': Decimal('1.20'),
  'fries': Decimal('0.30'),
  'bacon': Decimal('0.10')
}

LABELS = {
  'paradosiaki': 'Παραδοσιακή πίτα',
  'araviki': 'Αραβική πίτα',
  'pork_gyro': 'Γύρο χοιρινό',
  'chicken_gyro': 'Γύρο κοτόπουλο',
  'pork': 'Καλαμάκι Χοιρινό',
  'chicken': 'Καλαμάκι κοτόπουλο',
  'veggie': 'Οικολογική',
  'fries': 'Πατάτες τηγανιτές',
  'bacon': 'Μπέικον'
}

@app.post('/calculate')
def calculate():
  # Read form variables
  name = request.form.get('name')
  quantity = request.form.get('quantity', type=int, default=1)
  pita = request.form.get('pita', default='')
  meat = request.form.get('meat')
  extras = request.form.getlist('extras')

  # Validate form variables
  # str.strip() removes whitespace from the beginning and the end of the string
  errors = validate(name, quantity, pita)
  if errors:
    return render_template('form.html', **locals())
  
  # Calculate Cost
  materials = (pita, meat, *extras)
  material_labels = [LABELS[m] for m in materials]
  cost = sum([COST[m] for m in materials]) * quantity
  
  # Render a dynamic page
  # locals() is a built-in python function that returns a dictionary of
  # all variables in the local scope
  return render_template('calculate.html', **locals())

def validate(name, quantity, pita):
  errors = []

  if len(name.strip()) == 0:
    errors.append('Μη έγκυρο όνομα')

  if quantity < 1:
    errors.append('Μη έγκυρη ποσότητα')

  if pita == '':
    errors.append('Πρέπει να επιλέξεις πίτα')

  return errors

app.run(host='0.0.0.0', port=81)