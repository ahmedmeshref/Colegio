from enum import unique
import os 
from sqlalchemy import Column, String, Integer, Date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# setup db for the flask app instance
def setup_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()


student_courses = db.Table('student_courses',
    db.Column('course_id', db.Integer, db.ForeignKey('course.id')),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'))
)


class Student(db.Model):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    registration_date = Column(Date, nullable=False)
    name = Column(String(20), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    # we hash the user password to a 60 string long
    password = Column(db.String(60), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Course(db.Model):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    facilitator_id = Column(Integer, db.ForeignKey('facilitator.id'), unique=True, nullable=False)
    students = db.relationship("Student", secondary=student_courses)


class Facilitator(db.Model):
    __tablename__ = 'facilitator'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    facilitator_id = Column(Integer, unique=True, nullable=False)
    phone_number = Column(String(20), unique=True)
    courses = db.relationship('Course', backref='teach', lazy=True)
