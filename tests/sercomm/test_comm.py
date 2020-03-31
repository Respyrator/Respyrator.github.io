# Built-in --------------------------------------------------------------------
# Installed -------------------------------------------------------------------
# Coded -----------------------------------------------------------------------
# Program ---------------------------------------------------------------------


class TestComm:
    def test_read_bytes(self, get_comm):
        MSG_BYTES = b'Hello World\r\n'
        assert MSG_BYTES == get_comm.read_bytes()

    def test_read_string(self, get_comm):
        MSG_STR = 'Hello World'
        assert MSG_STR == get_comm.read_string()

    def test_send_bytes(self, get_comm):
        MSG_BYTES = b'World Hello\r\n'
        get_comm.send_bytes(MSG_BYTES)
        assert MSG_BYTES == get_comm.read_bytes()

    def test_send_string(self, get_comm):
        MSG_STR = 'World Hello'
        get_comm.send_string(MSG_STR)
        get_comm.read_string()
        assert MSG_STR == get_comm.read_string()
