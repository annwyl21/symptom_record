from application import app

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

if __name__ == "__main__":
    app.run(debug=True)

# Future Development Plans
# 1. Add a database to store the symptoms and the date they were recorded
# 2. Add a scattergraph to show the symptoms over time
# 3. Add a feature to allow the user to record symptoms for multiple patients, eg. family members & pets
