# app.py
from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, text


# initialize the flask app
app = Flask(__name__)
# create a db engine to connect to the SQLite db
engine = create_engine("sqlite:///real_estate_new.db")  # Updated database name

# route to accomplish autocomplete suggestions based on user input
@app.route('/autocomplete/cities', methods=['GET'])
def autocomplete_cities():
    query = request.args.get("q", "")
    state = request.args.get("state", "")

    with engine.connect() as conn:
        if state:
            result = conn.execute(
                text("SELECT DISTINCT city FROM properties WHERE city LIKE :query AND state = :state ORDER BY city"),
                {"query": f"{query}%", "state": state}
            )
        else:
            result = conn.execute(
                text("SELECT DISTINCT city FROM properties WHERE city LIKE :query ORDER BY city"),
                {"query": f"{query}%"}
            )
        cities = [row["city"] for row in result]
    return jsonify(cities)

# define a custom template filter to format numbers with commas 
@app.template_filter("intcomma")
def intcomma(value):
    if value is None:
        return "N/A"
    return f"{value:,.2f}"

# Home route with search form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
# Retrieve the form inputs and store them in variables
def search():
    city = request.form.get("city")
    state = request.form.get("state")
    status = request.form.get("status")
    min_price = request.form.get("min_price")
    max_price = request.form.get("max_price")
    min_bed = request.form.get("min_bed")
    max_bed = request.form.get("max_bed")
    min_bath = request.form.get("min_bath")
    max_bath = request.form.get("max_bath")
    min_house_size = request.form.get("min_house_size")
    max_house_size = request.form.get("max_house_size")
    sort_by = request.form.get("sort_by")

    # build SQL query dynamically based on filters in UI

    # a base query to select all entries give that 1 = 1 is true (which is it always is) used as a placeholder
    query = "SELECT * FROM properties WHERE 1=1"
    # dictionary to store query parameters
    params = {}

    # Add filters to the query if the user has input a value for each field
    if city:
        query += " AND city = :city"
        params["city"] = city
    if state:
        query += " AND state = :state"
        params["state"] = state
    if status:
        query += " AND status = :status"
        params["status"] = status
    if min_price:
        query += " AND price >= :min_price"
        params["min_price"] = min_price
    if max_price:
        query += " AND price <= :max_price"
        params["max_price"] = max_price
    if min_bed:
        query += " AND bed >= :min_bed"
        params["min_bed"] = min_bed
    if max_bed:
        query += " AND bed <= :max_bed"
        params["max_bed"] = max_bed
    if min_bath:
        query += " AND bath >= :min_bath"
        params["min_bath"] = min_bath
    if max_bath:
        query += " AND bath <= :max_bath"
        params["max_bath"] = max_bath
    if min_house_size:
        query += " AND house_size >= :min_house_size"
        params["min_house_size"] = min_house_size
    if max_house_size:
        query += " AND house_size <= :max_house_size"
        params["max_house_size"] = max_house_size

    # Sorting logic based on user selection
    if sort_by == "price":
        query += " ORDER BY price"
    elif sort_by == "bed":
        query += " ORDER BY bed"
    elif sort_by == "bath":
        query += " ORDER BY bath"

    # execute the SQL query with the params provided
    with engine.connect() as conn:
        results = conn.execute(text(query), params).mappings().all()

    # Render the results page with the list of properties that match the search criteria
    return render_template('results.html', properties=results)

if __name__ == "__main__":
    app.run(debug=True)
