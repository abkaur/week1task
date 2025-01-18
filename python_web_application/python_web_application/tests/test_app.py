# tests/test_app.py
from python_web_application.python_web_application.app import app_function
import pytest 
def test_app_function():
    assert app_function() == "Hello World"  # Replace with the expected outcome
