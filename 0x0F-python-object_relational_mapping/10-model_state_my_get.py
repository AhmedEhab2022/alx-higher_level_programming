#!/usr/bin/python3
"""a script that lists all State objects from the database
hbtn_0e_6_usa with MySQLAlchemy"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_id = session.query(State.id).filter_by(name=sys.argv[4]).scalar()
    if state_id:
        print(state_id)
    else:
        print("Not found")
