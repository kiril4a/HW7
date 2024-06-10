from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, desc
from models import Student, Grade, Subject, Teacher, Group, engine

Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    return session.query(
        Student.fullname, 
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_id):
    return session.query(
        Student.fullname, 
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).filter(Grade.subject_id == subject_id).group_by(Student.id).order_by(desc('avg_grade')).first()
from sqlalchemy import join
def select_3(subject_id):
    return session.query(
        Group.name,
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).select_from(
        join(Group, Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
    ).filter(
        Grade.subject_id == subject_id
    ).group_by(
        Group.id
    ).all()

def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).all()

def select_5(teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

def select_6(group_id):
    return session.query(Student.fullname).filter(Student.group_id == group_id).all()

def select_7(group_id, subject_id):
    return session.query(
        Student.fullname, 
        Grade.grade
    ).join(Grade).filter(Student.group_id == group_id, Grade.subject_id == subject_id).all()

def select_8(teacher_id):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).join(Subject).filter(Subject.teacher_id == teacher_id).all()

def select_9(student_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id).all()

def select_10(student_id, teacher_id):
    return session.query(Subject.name).join(Grade).filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id).all()
