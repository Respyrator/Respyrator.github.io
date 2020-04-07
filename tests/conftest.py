# Built-in --------------------------------------------------------------------
# Installed -------------------------------------------------------------------
from pytest import fixture
# Coded -----------------------------------------------------------------------
from src.sercomm.arduino import ARDUINO_MEGA
# Program ---------------------------------------------------------------------


@fixture(scope='class')
def get_comm():
    ser = ARDUINO_MEGA
    yield ser
    ser.close()
