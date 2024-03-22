#!/usr/bin/python3

""" Script that prints all City objects from database """

if __name__ == '__main__':
    
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    import sys

    if len(sys.argv) < 4:
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()

    for instance in (session.query(State.name, City.id, City.name)
            .filter(State.id == City.state_id).order_by(City.id)):
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
