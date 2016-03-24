import unittest

try:
    from app.person.tests import *
except ImportError:
    print("Please do \"export PYTHONPATH='.'\" and re-run.")
    exit(0)

if __name__ == '__main__':
    unittest.main()
