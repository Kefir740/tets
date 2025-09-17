from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String


sqlite_database = "sqlite:///maps.db"
engine = create_engine(sqlite_database, echo=True)


class Base(DeclarativeBase):
    pass


class Maps(Base):
    __tablename__ = "maps"

    id = Column(Integer, primary_key=True, index=True)
    mapname = Column(String, unique=True)
    mapstyle = Column(String)
    gjson = Column(String)


Base.metadata.create_all(bind=engine)


def add_record(mapname, mapstyle, gjson):
    with Session(autoflush=False, bind=engine) as db:
        new_map = Maps(mapname=mapname,
                       mapstyle=mapstyle,
                       gjson=gjson)
        db.add(new_map)
        db.commit()


def delete_record(mapname):
    with Session(autoflush=False, bind=engine) as db:
        del_map = db.query(Maps).filter(Maps.mapname==mapname).first()
        db.delete(del_map)
        db.commit()


def get_mapstyle(mapname):
    with Session(autoflush=False, bind=engine) as db:
        mapstyle = db.query(Maps).filter(Maps.mapname==mapname).first()
        return mapstyle.mapstyle


def get_maps_list():
    with Session(autoflush=False, bind=engine) as db:
        maps_list = list(db.query(Maps.mapname).order_by(Maps.id))
        # print(maps_list)
        return maps_list


if __name__ == '__main__':
    print(get_maps_list())
    # for i in range(1, 50):
    #     add_record(mapname=f'test_name{i}',
    #                mapstyle='test_style',
    #                gjson='test_json')

    # print('MAPSTYLE: ', get_mapstyle(mapname='test_name'))
    #
    # delete_record(mapname='test_name')
