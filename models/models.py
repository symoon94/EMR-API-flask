from sqlalchemy import Column, String, Integer, BigInteger, ForeignKey
from . import Base


class Person(Base):
    __tablename__ = 'person'

    person_id = Column(BigInteger(), primary_key=True)
    gender_concept_id = Column(Integer())
    race_concept_id = Column(Integer())
    ethnicity_concept_id = Column(Integer())
    year_of_birth = Column(Integer())

class Death(Base):
    __tablename__ = 'death'

    person_id = Column(BigInteger(), ForeignKey(
        "person.person_id"), primary_key=True)


class Visit(Base):
    __tablename__ = 'visit_occurrence'

    visit_occurrence_id = Column(BigInteger(), primary_key=True)
    person_id = Column(BigInteger(), ForeignKey(
        "person.person_id"))
    visit_concept_id = Column(Integer())
