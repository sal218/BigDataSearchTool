# app.py
from flask import Flask, render_template, request
from sqlalchemy import create_engine, text

app = Flask(__name__)
engine = create_engine("sqlite:///real_estate.db")

# Home route with search form
@app.route('/')
def index():
    return render_template('index.html')

# Route for search results
@app.route('/search', methods=['GET', 'POST'])
def search():
    city = request.form.get("city")
    neighborhood = request.form.get("neighborhood")
    property_type = request.form.get("property_type")
    min_price = request.form.get("min_price")
    max_price = request.form.get("max_price")
    min_bedrooms = request.form.get("min_bedrooms")
    max_bedrooms = request.form.get("max_bedrooms")
    sort_by = request.form.get("sort_by")

    # Build SQL query dynamically based on filters
    query = "SELECT * FROM properties WHERE 1=1"
    params = {}

    if city:
        query += " AND city = :city"
        params["city"] = city
    if neighborhood:
        query += " AND neighborhood = :neighborhood"
        params["neighborhood"] = neighborhood
    if property_type:
        query += " AND property_type = :property_type"
        params["property_type"] = property_type
    if min_price:
        query += " AND price >= :min_price"
        params["min_price"] = min_price
    if max_price:
        query += " AND price <= :max_price"
        params["max_price"] = max_price
    if min_bedrooms:
        query += " AND bedrooms >= :min_bedrooms"
        params["min_bedrooms"] = min_bedrooms
    if max_bedrooms:
        query += " AND bedrooms <= :max_bedrooms"
        params["max_bedrooms"] = max_bedrooms

    # Sorting
    if sort_by == "price":
        query += " ORDER BY price"
    elif sort_by == "size":
        query += " ORDER BY size"
    elif sort_by == "recent":
        query += " ORDER BY date_listed DESC"

    with engine.connect() as conn:
        results = conn.execute(text(query), params).fetchall()

    return render_template('results.html', properties=results)

if __name__ == "__main__":
    app.run(debug=True)
