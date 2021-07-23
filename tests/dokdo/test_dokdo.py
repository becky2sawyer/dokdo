import sys
import dokdo


def test_ping():
    sys.argv = ['foo', '10']
    dokdo.ping()

