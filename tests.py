import sys
import os
import json
import hashlib
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'odgovori.json'))
assert os.path.exists(file_path), "Manjka datoteka odgovori.json"

def hash_answer(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

from code import square, is_even

# testiranje funkcij
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-1) == 1

def test_is_even():
    assert is_even(0) is True
    assert is_even(3) is False
    assert is_even(4) is True

# testi teorija
# Correct hashed answers
q1_hash = "7c24674b754ce14cc94b6034c41b13278a344c9c5c4e194625a6dc711a66c26d"
q2_hash = "0a0261cd58c6f631f39441598f69f0506e56e8442cd89f453d5e68c1d6dbe193"
def test_q1():
    with open("odgovori.json", encoding="utf-8") as f:
        data = json.load(f)
    assert hash_answer(data["q1"]) == q1_hash

def test_q2():
    with open("odgovori.json", encoding="utf-8") as f:
        data = json.load(f)
    assert hash_answer(data["q2"]) == q2_hash