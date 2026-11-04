class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, usn):
        if not name or not usn:
            return False
        self.students.append({"name": name, "usn": usn})
        return True

    def search_student(self, usn):
        for student in self.students:
            if student["usn"] == usn:
                return student
        return None