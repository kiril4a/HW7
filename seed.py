import random
from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Group, Teacher, Subject, Grade, engine
from datetime import datetime

fake = Faker()

Session = sessionmaker(bind=engine)
session = Session()

groups = [Group(name=f'Group {i}') for i in range(1, 4)]
session.add_all(groups)
session.commit()

teachers = [Teacher(fullname=fake.name()) for _ in range(3)]
session.add_all(teachers)
session.commit()

subjects = [Subject(name=f'Subject {i}', teacher=random.choice(teachers)) for i in range(1, 9)]
session.add_all(subjects)
session.commit()

students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(30)]
session.add_all(students)
session.commit()

for student in students:
    for subject in subjects:
        for _ in range(random.randint(1, 5)):
            grade = Grade(
                student=student,
                subject=subject,
                grade=random.uniform(60, 100),
                date_received=fake.date_time_this_year()
            )
            session.add(grade)
session.commit()
