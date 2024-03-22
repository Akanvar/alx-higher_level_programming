#!/usr/bin/python3
""" script that lists all State objects """
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base

    if len(sys.argv) < 4:
        exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    state_list = session.query(State).order_by(State.id).all()

    for state in state_list:
        print(f"{state.id}: {state.name}")

    session.close()


