import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:Vfrcbv0405@localhost:5432/northwind")

connection = engine.connect()

result = connection.execute("SELECT * FROM region")

for r in result:
    print(r)

result.close()

# trans = connection.begin()
# try:
#     connection.execute("INSERT INTO superheroes(hero_name, strength) VALUES ('Iron man', 58)")
#     trans.commit()
# except:
#     trans.rollback()
#     raise
# with connection.begin() as trans:
#     connection.execute("INSERT INTO superheroes(hero_name, strength) VALUES ('Hulk', 105)")
#
# result = connection.execute("SELECT * FROM superheroes")
#
# for r in result:
#     print(r)
#
# result.close()

base = declarative_base()


class Heroes(base):
    __tablename__ = 'heroes'

    heroes_id = Column(Integer, primary_key=True)
    full_name = Column(String)
    rating = Column(Float)


base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

heroes = Heroes(heroes_id=3, full_name='Black Widow', rating = 4.5)
session.add(heroes)
heroes = Heroes(heroes_id=2, full_name='Capitan America', rating = 4.0)
session.add(heroes)

session.flush() #передает данные в бд. Но это не commit
session.commit()

for item in session.query(Heroes).order_by(Heroes.rating):
    print(item.full_name,' ', item.rating)