from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATA_FILE = "courses.json"


class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str


def load_courses():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_courses(courses):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)


@app.get("/")
def root():
    return {"message": "FastAPI Course Records API"}


@app.get("/courses")
def get_courses():
    courses = load_courses()
    return courses


@app.post("/courses")
def add_course(course: Course):
    courses = load_courses()

    new_course = course.model_dump()
    courses.append(new_course)

    save_courses(courses)

    return {
        "message": "Course added successfully",
        "course": new_course,
        "total_count": len(courses)
    }