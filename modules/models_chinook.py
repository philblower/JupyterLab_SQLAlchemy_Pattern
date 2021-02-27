import db_config as db
from sqlalchemy import Column, Integer, String, ForeignKey


class Album(db.Base1):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    title = Column(
        String(160),
        nullable=False
    )

    artistid =  Column(Integer, ForeignKey("artist.id", ondelete="SET NULL", onupdate="SET NULL"))


class Artist(db.Base1):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(
        String(120),
        nullable=True
    )

    def __str__(self):
        return self.name
