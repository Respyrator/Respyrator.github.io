# Copyright (C) 2020 Respyrador
# This file is part of Respyrador <https://respyrator.github.io/respirador/>.
#
# Respyrador is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Respyrador is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Respyrador.  If not, see <http://www.gnu.org/licenses/>.

# Built-in --------------------------------------------------------------------
from time import sleep, time
# Installed -------------------------------------------------------------------
import serial
from serial.tools.list_ports import comports
# Coded -----------------------------------------------------------------------
from src import logapp
# Program ---------------------------------------------------------------------
LOG = 'COMM:'

BAUDRATE = 115200
BYTESIZE = serial.EIGHTBITS
PARITY = serial.PARITY_NONE
STOPBITS = serial.STOPBITS_ONE
READ_TIMEOUT = 1.0
WRITE_TIMEOUT = 1.0

# Official Arduino Mega Board identifier
ARDUINO_MANUFACTURER = 'Arduino (www.arduino.cc)'
# Unofficial Arduino Mega Board identifier
OEM_PRODUCT = 'USB2.0-Serial'


class Comm:
    def __init__(self):
        logapp.debug(f'{LOG} __init__()')
        self.ser: serial.Serial = serial.Serial(
            baudrate=BAUDRATE,
            bytesize=BYTESIZE, parity=PARITY, stopbits=STOPBITS,
            timeout=READ_TIMEOUT, write_timeout=WRITE_TIMEOUT
        )

    def _reset_buffers(self):
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def _check_device(self, field, reference) -> bool:
        logapp.debug(f'{LOG} _check_device({field}, {reference})')
        return True if (field is not None) and (reference.find(field) > -1) \
            else False

    def respirator_port(self) -> str:
        logapp.debug(f'{LOG} respirator_port()')
        for i in comports():
            logapp.debug(f'{LOG} Serial devices at {i.device}')
            if self._check_device(i.manufacturer, ARDUINO_MANUFACTURER) or \
               self._check_device(i.product, OEM_PRODUCT):
                logapp.debug(f'{LOG} respirator at {i.device}')
                return i.device
        logapp.debug(f'{LOG} respirator not finded')
        return ''

    def connect(self, rep=3) -> bool:
        logapp.debug(f'{LOG} connect({3})')
        if rep:
            if not self.ser.is_open:
                port = self.respirator_port()
                if port != '':
                    self.ser.port = port
                    self.ser.open()
                    sleep(1.0)
                return self.connect(rep-1)
            self._reset_buffers()
            return True
        return False

    def _read(self, rep=3) -> bytes:
        logapp.debug(f'{LOG} read()')
        try:
            if self.ser.is_open or self.connect():
                t_start = time()
                elapsed = False
                while not self.ser.in_waiting and not elapsed:
                    if time() - t_start > READ_TIMEOUT:
                        elapsed = True
                if not elapsed:
                    msg = self.ser.readline()
                    logapp.debug(f'{LOG} received = {msg}')
                    return msg
            raise CommException('Respirator is not connected')
        except serial.SerialException as err:
            logapp.exception(f'{LOG} error = {err}')
            return b''

    def read_bytes(self) -> bytes:
        logapp.debug(f'{LOG} read_bytes()')
        return self._read()

    def read_string(self) -> str:
        logapp.debug(f'{LOG} read_string()')
        return self._read().decode('utf-8').strip('\r\n')

    def _send(self, data: bytes):
        logapp.debug(f'{LOG} _send({data})')
        try:
            if self.ser.is_open or self.connect():
                self.ser.write(data)
            else:
                raise CommException('Respirator is not connected')
        except (serial.SerialException, serial.SerialTimeoutException) as err:
            logapp.debug(f'{LOG} error = {err}')
            raise err

    def send_bytes(self, data: bytes):
        logapp.debug(f'{LOG} send_bytes({data})')
        self._send(data)

    def send_string(self, data: str):
        logapp.debug(f'{LOG} send_string({data})')
        self._send(data.encode())

    def close(self):
        logapp.debug(f'{LOG} close()')
        self.ser.close()


class CommException(Exception):
    pass
