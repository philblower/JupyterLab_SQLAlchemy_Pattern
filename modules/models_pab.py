import db_config as db
from sqlalchemy import Column, Integer, Numeric, String, ForeignKey


class Owner(db.Base2):
    __tablename__ = 'owner'
    id = Column(Integer, primary_key=True)
    name = Column(
        String(255),
        nullable=False,
        # I don't use info, but left it here as an example
        info={"description":"Name", "label":"Name"}
    )
    email = Column(
        String(255),
        nullable=False
    )

    def __str__(self):
        return self.name


class Pet(db.Base2):
    __tablename__ = 'pet'
    id = Column(Integer, primary_key=True)
    name = Column(
        String(255),
        nullable=False
    )
    animal = Column(
        String(255),
        nullable=False
    )
    owner_id =  Column(Integer, ForeignKey("owner.id", ondelete="SET NULL", onupdate="CASCADE"))
    weight_lb = Column(
        Numeric(precision=5, asdecimal=False)
    )
    weight_kg = Column(
        Numeric(precision=5, asdecimal=False)
    )
    weight_st = Column(
        Numeric(precision=5, asdecimal=False)
    )

    def __str__(self):
        return self.name

    def set_computed_columns(self):
        self.compute_weight_kg()
        self.compute_weight_st()

    def compute_weight_kg(self):
        self.weight_kg = self.weight_lb / 2.205

    def compute_weight_st(self):
        self.weight_st = self.weight_lb / 14.0
