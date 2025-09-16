from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String

# строка подключения
sqlite_database = "sqlite:///maps.db"
# создаем движок SqlAlchemy
engine = create_engine(sqlite_database, echo=True)


# создаем модель, объекты которой будут храниться в бд
class Base(DeclarativeBase):
    pass


class Maps(Base):
    __tablename__ = "maps"

    id = Column(Integer, primary_key=True, index=True)
    mapname = Column(String, unique=True)
    mapstyle = Column(String)
    gjson = Column(String)


# создаем таблицы
Base.metadata.create_all(bind=engine)


def add_record(mapname='test_name', mapstyle='test_style', gjson='test_json'):
    with Session(autoflush=False, bind=engine) as db:
        new_map = Maps(mapname=mapname,
                       mapstyle=mapstyle,
                       gjson=gjson)
        db.add(new_map)  # добавляем в бд
        db.commit()  # сохраняем изменения


def delete_record(mapname):
    with Session(autoflush=False, bind=engine) as db:
        pass


def get_mapstyle(mapname):
    with Session(autoflush=False, bind=engine) as db:
        pass

#
# # создаем сессию подключения к бд
# with Session(autoflush=False, bind=engine) as db:
#     pass
    # создаем объект Person для добавления в бд
    # tom = Maps()
    # db.add(tom)  # добавляем в бд
    # db.commit()  # сохраняем изменения
    # print(tom.id)  # можно получить установленный id