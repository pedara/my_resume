from flask_script import Manager
from resume import app, db, Professor, Course

manager = Manager(app)

@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    sivaraman = Professor(name='Anuradha Sivaraman', department='Business and Economics')
    sharma = Professor(name='Pratyush Nidhi Sharma', department='Accounting & MIS')
    detwiler = Professor(name='Timothy Detwiler', department='Business and Economics')
    wang = Professor(name='Jiannan Wang', department='Accounting & MIS')
    course1 = Course(course_number= 'BUAD 301', title='Introduction to Marketing', description='Examines individual, group, and organizational determinants of work behavior in organizations.')
    course2 = Course(course_number='MISY 330', title='Database Design & Implementation', description='Learning data mining alogorithms and the SQL language.')
    course3 = Course(course_number='FINC 312', title='Intermediate Financial Management', description='Focuses on the role of the corporate financial manager in shareholder wealth maximization.')
    course4 = Course(course_number='MISY 350', title='Web Application Development', description='Fundamentals of web development, including Python and Flask.')
    db.session.add(sivaraman)
    db.session.add(sharma)
    db.session.add(detwiler)
    db.session.add(wang)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
