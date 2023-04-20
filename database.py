from sqlalchemy import create_engine
import os

URL_DB = os.getenv("URL_DB")

engine = create_engine(URL_DB)

depth_min = 2000
grad_min = 0.075

query = f"""
    SELECT latitude, longitude, depth, gradient
    FROM wells
    WHERE depth > {depth_min} AND gradient > {grad_min}
"""
conn = engine.connect()

results = conn.execute(query).fetchall()

conn.close()

print(results)