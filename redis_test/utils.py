from .db import get_db_connection
import json


def get_deportes():
    return [ 
        {
            'Post_id': '635216',
            'Insert_at': '2022-09-09' 
        },
        {
            'Post_id': '435216',
            'Insert_at': '2022-09-08' 
        }
    ]

def get_bailes():
    return [ 
        {
            'Post_id': '735216',
            'Insert_at': '2022-09-09' 
        },
        {
            'Post_id': '535216',
            'Insert_at': '2022-09-07'
        }
    ]

def adding_data_to_db():
    db = get_db_connection()
    deportes_list = get_deportes()
    bailes_list = get_bailes()
    print("DEPORTES:")
    for x in deportes_list:
        print(x)
    print("BAILES:")
    for x in bailes_list:
        print(x)
    db.sadd("Deporte", json.dumps(deportes_list[0]), json.dumps(deportes_list[1]))
    db.sadd("Baile", json.dumps(bailes_list[0]), json.dumps(bailes_list[1]))

def flush_db():
    db = get_db_connection()
    db.flushall()