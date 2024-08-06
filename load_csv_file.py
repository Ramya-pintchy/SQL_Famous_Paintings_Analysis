#Python Script to connect PostgreSQL and python to load .csv files into the Database[PostgreSQL]

import pandas as pd
from sqlalchemy import create_engine

conn_string = 'postgresql://Username:user_password@host_name/Famous_paintings'
db = create_engine(conn_string)
conn = db.connect()

fi = ['Artist', 'canvas_size', 'image_link', 'museum', 'museum_hours', 'product_size', 'subject', 'work']
for file in fi:
 df = pd.read_csv(f'your_file_path/{file}.csv')
 df.to_sql(file, con=conn, if_exists='replace', index=False)
