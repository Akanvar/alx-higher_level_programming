#!/usr/bin/python3

""" Script that prints the first State object from database """

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

    for instance in session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=': ')
