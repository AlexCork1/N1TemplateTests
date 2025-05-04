import sys
import os
import json
import hashlib
import atexit

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'odgovori.json'))

def hash_answer(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

from student_code import square, is_even

# Prepare grading dictionary
results = {
    "square": False,
    "is_even": False,
    "q1": False,
    "q2": False
}

# Test and record outcomes manually
def test_square():
    try:
        assert square(2) == 4
        assert square(3) == 9
        assert square(-1) == 1
        results["square"] = True
    except:
        results["square"] = False
        raise

def test_is_even():
    try:
        assert is_even(0) is True
        assert is_even(3) is False
        assert is_even(4) is True
        results["is_even"] = True
    except:
        results["is_even"] = False
        raise

q1_hash = "7c24674b754ce14cc94b6034c41b13278a344c9c5c4e194625a6dc711a66c26d"
def test_q1():
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        assert hash_answer(data["q1"]) == q1_hash
        results["q1"] = True
    except:
        results["q1"] = False
        raise

q2_hash = "0a0261cd58c6f631f39441598f69f0506e56e8442cd89f453d5e68c1d6dbe193"
def test_q2():
    try:
        assert os.path.exists(file_path), "Manjka datoteka odgovori.json"
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
        assert hash_answer(data["q2"]) == q2_hash
        results["q2"] = True
    except:
        results["q2"] = False
        raise

def write_grade_summary():
    # Calculate scores and write the grade summary
    results["total_score"] = sum(results.values())
    results["max_score"] = len([k for k in results if isinstance(results[k], bool)])
    try:
        with open("grade_summary.json", "w") as f:
            json.dump(results, f, indent=2, sort_keys=True)
    except Exception as e:
        print(f"⚠️ Failed to write grade summary: {e}")

@atexit.register
def write_fallback_summary():
    write_grade_summary()

def pytest_sessionfinish(session, exitstatus):
    write_grade_summary()


if __name__ == "__main__":
    print("Run with pytest, not directly.")
