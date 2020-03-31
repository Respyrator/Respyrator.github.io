# Built-in --------------------------------------------------------------------
# Installed -------------------------------------------------------------------
from pytest import fixture
# Coded -----------------------------------------------------------------------
from src.sercomm.comm import Comm
# Program ---------------------------------------------------------------------


@fixture(scope='class')
def get_comm():
    ser = Comm()
    yield ser
    ser.close()
