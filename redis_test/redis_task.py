import json
from datetime import datetime
from .db import get_db_connection
from .utils import flush_db, adding_data_to_db

def run_redis_task():
    # Getting DB Connection
    db = get_db_connection()
    # Deleting Database data
    flush_db()
    # Adding Dummy Data
    adding_data_to_db()

    # Making union and storing into new Key
    db.sunionstore("Merge", ["Deporte", "Baile"])
    # Getting results
    result = db.smembers("Merge")
    data = [json.loads(r.decode("ascii")) for r in result]

    # Sorting by date
    date_format = "%Y-%m-%d"
    output_data = sorted(data, key=lambda x: datetime.strptime(x['Insert_at'], date_format), reverse=True)

    # Printing output to console
    print("\nMERGE:")
    for x in output_data:
        print(x)
    