from student_manager import StudentManager

def test_add_student():
    sm = StudentManager()
    assert sm.add_student("Alice", "1RV23IS001") == True
    assert len(sm.students) == 1

def test_add_student_invalid():
    sm = StudentManager()
    assert sm.add_student("", "") == False

def test_search_student():
    sm = StudentManager()
    sm.add_student("Bob", "1RV23IS002")
    result = sm.search_student("1RV23IS002")
    assert result is not None
    assert result["name"] == "Bob"