# COMP455: Extreme Computing - Real Estate Search Tool

This project is an **extreme computing application** that enables efficient searching and filtering of real estate properties across the United States. It leverages a **large dataset** containing detailed property information and provides an intuitive web-based interface for users to filter and sort properties based on various criteria.

The application demonstrates the use of:
- **Flask** for building the web application.
- **SQLite** for managing property data.
- **SQLAlchemy** for database operations.
- **JavaScript** for dynamic front-end functionality (autocomplete and filtering).
- **Pandas** for data preprocessing.

---

## Features

- **Large Dataset Handling**: Optimized search and filtering of over 500,000 real estate properties.
- **Autocomplete Functionality**: Dynamically suggests city names based on user input.
- **Advanced Search Filters**:
  - Price range
  - Number of bedrooms and bathrooms
  - House size (square feet)
  - State and city selection
- **Dynamic Results Page**:
  - Display of search results with sorting options.
  - Additional filtering directly on the results page.
- **Responsive Web Interface**: Built with modern design principles for a user-friendly experience.

---

## Prerequisites

1. **Python 3.x** installed.
2. All dependencies listed in `requirements.txt` (see installation steps below).
3. **USA Real Estate Dataset**: Download from [Kaggle](https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset).

---

## Getting Started

### Step 1: Download and Set Up the Dataset

- Download the dataset from [this Kaggle link](https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset).
- Save the `.csv` file in the root directory of your project folder.
  - Ensure the file is named **`realtor-data.zip.csv`** for compatibility with the program.

---

### Step 2: Install Dependencies

Install all required Python libraries using:
```bash
pip install -r requirements.txt
``` 
### Step 3: Generate Database
```bash
python generate_db.py
``` 
#### This step will:

- Filter the dataset for properties with a "for_sale" status.
- Clean and preprocess the data.
- Generate an SQLite database named real_estate_new.db.

### Step 4: Run the Application
```bash
python app.py
```
### Step 5: Use the Application
1. Open your browser and navigate to http://localhost:5000/.
2. Use the search form to input your criteria:
    - Select a state or city.
    - Set price, bedroom, bathroom, and house size filters (optional).
    - Sort results by price or house size.
3. Click Search to view the results.
4. Further refine your search on the results page using additional filters.

## Known Issues and Improvements
- The dataset is too large to be included in the repository. Ensure you download it from Kaggle.
- Additional features like property visualization (e.g., maps or images) can be added.

## License
This project is licensed under the MIT License. See LICENSE for details.
