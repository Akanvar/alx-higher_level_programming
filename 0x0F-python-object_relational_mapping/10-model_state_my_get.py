#!/usr/bin/python3

""" Script that prints State object with name passed as argument """

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    if len(sys.argv) < 5:
        exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    my_query = session.query(State).filter(State.name == sys.argv[4]).all()
    if len(my_query) == 0:
        print("Not Found")
    else:
        print(my_query[0].id)

    session.close()
