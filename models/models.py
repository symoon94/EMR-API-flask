from sqlalchemy import Column, String, Integer, BigInteger
from . import Base


class Person(Base):
    __tablename__ = 'person'

    person_id = Column(BigInteger(), primary_key=True)
    gender_concept_id = Column(Integer())
    race_concept_id = Column(Integer())
    ethnicity_concept_id = Column(Integer())


class Death(Base):
    __tablename__ = 'death'

    person_id = Column(BigInteger(), primary_key=True)
