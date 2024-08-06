# SQL_Famous_Paintings_Analysis

## Introduction
   This project involves analyzing data on famous paintings. The analysis is performed using PostgreSQL connected to Python with pandas for data manipulation and SQL scripts for querying the database.

#### Refer the schema_diagram for referenece:
![SQL_Famous_Paintings_Analysis](Famous_Paintings.png)

**LEVEL**- Intermmediate

## Skills you'll acquire
   - Able to connect csv files to python to load the files in PostgreSQL.
   - Analysis of artists and their work
   - Insights into museum collection and their details
   - Exploration of painting subjects and sizes
            
## Tools Used - 
   - **PostgreSQL:** Database management system
   - **Excel/.csv:** Format used for storing raw data.
   - **Python Scripts:** Used for data manipulation and connection to the database with pandas.
   - **pandas:** Python library for data manipulation and analysis.

## Usage

### Prerequisites
- Ensure PostgreSQL is installed on your machine. You can download it from [here](https://www.postgresql.org/download/).
- Ensure Python is installed on your machine. You can download it from [here](https://www.python.org/downloads/).
- Install the necessary Python packages using pip:
  ```sh
  pip install pandas psycopg2
  pip install sqlalchemy

#### Import Data:
1. Clone the repository"
   ```sh
   git clone https://github.com/Ramya-pintchy/SQL_Famous_Paintings_Analysis.git
   cd SQL_Famous_Paintings_Analysis
   
2. Open PostgreSQL and create a new database:
   ```sql
   CREATE DATABASE Famous_Paintings;

3. Open your choice Python editor: [I've used VScode]
   ```sh
   import pandas as pd
   from sqlalchemy import create_engine

   conn_string = 'postgresql://Username:user_password@host_name/Famous_paintings'
   db = create_engine(conn_string)
   conn = db.connect()

   fi = ['Artist', 'canvas_size', 'image_link', 'museum', 'museum_hours', 'product_size', 'subject', 'work']
   for file in fi:
    df = pd.read_csv(f'your_file_path/{file}.csv')
    df.to_sql(file, con=conn, if_exists='replace', index=False)

4. Run the SQL queries in the Query window.

## Getting Started
1. Clone the repository:
   ```sh
   git clone https://github.com/Ramya-pintchy/SQL_Famous_Paintings_Analysis.git
   cd SQL_Famous_Paintings_Analysis
2. Set up your PostgreSQL database and import the data using the provided Python script.
3. Run the SQL scripts to start analyzing the paintings data.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Special thanks to all resources and tutorials that helped in the creation of this project.

### Explanation:
```markdown
- **Project Structure:** Lists the main components of your project.
- **Features:** Describes what the project does.
- **Tools and Technologies:** Lists the main tools and technologies used in the project.
- **Usage:** Provides step-by-step instructions for setting up and running the project, including prerequisites, data import, and running SQL scripts.
- **Getting Started:** A quick start guide to clone the repository and set up the project.
- **Example Queries:** Instructions for running example queries.
- **License and Acknowledgments:** Standard sections for open-source projects.
