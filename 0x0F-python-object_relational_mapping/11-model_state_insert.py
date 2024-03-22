#!/usr/bin/python3

""" Script that adds State object to a database """

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    if len(sys.argv) < 4:
        exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)

    state_instance = session.query(State).filter_by(name='Louisiana').first()
    print(state_instance.id)

    session.commit()
