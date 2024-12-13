from sqlalchemy.orm import Session
from models import Student
from schemas import StudentCreate, StudentUpdate

def create_student(db: Session, student: StudentCreate):
    db_student = Student(name=student.name, age=student.age, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def update_student(db: Session, student_id: int, student: StudentUpdate):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        if student.name:
            db_student.name = student.name
        if student.age:
            db_student.age = student.age
        if student.email:
            db_student.email = student.email
        db.commit()
        db.refresh(db_student)
        return db_student
    return None

def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return db_student
    return None