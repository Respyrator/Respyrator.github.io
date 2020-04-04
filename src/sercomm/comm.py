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
from dataclasses import dataclass
from typing import Optional
from abc import abstractmethod
# Installed -------------------------------------------------------------------
import serial
# Coded -----------------------------------------------------------------------
from src import logapp
from src.device import Device
# Program ---------------------------------------------------------------------

@dataclass
class CommConfig:
    """Configuration for a serial connection."""
    BAUDRATE:int
    BYTESIZE: int
    PARITY:int
    STOPBITS:float

class Comm(Device):

    def __init__(self, configuration: CommConfig):
        """Create a new class instance.
        
        :param config: Serial configuration.
        """
        super().__init__()
        self.log_prefix: str = "COMM:"
        self.read_timeout: float = 1.0
        self.write_timeout: float = 1.0
        self.__ser: Optional[serial.Serial] = None
        self.configuration = configuration

    @property
    def ser(self):
        """Connection to the serial port."""
        if self.__ser:
            return self.__ser
        self.__ser: serial.Serial = serial.Serial(
            baudrate=self.configuration.BAUDRATE,
            bytesize=self.configuration.BYTESIZE,
            parity=self.configuration.PARITY,
            stopbits=self.configuration.STOPBITS,
            timeout=self.read_timeout,
            write_timeout=self.write_timeout
        )
        return self.__ser

    def _reset_buffers(self) -> None:
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

    def _check_device(self, field, reference) -> bool:
        logapp.debug(f'{self.log_prefix} _check_device({field}, {reference})')
        return True if (field is not None) and (reference.find(field) > -1) \
            else False

    @abstractmethod
    def respirator_port(self):
        raise NotImplementedError("repirator_port method not implemented")

    def connect(self, rep=3) -> bool:
        logapp.debug(f'{self.log_prefix} connect({3})')
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
        logapp.debug(f'{self.log_prefix} read()')
        try:
            if self.ser.is_open or self.connect():
                t_start = time()
                elapsed = False
                while not self.ser.in_waiting and not elapsed:
                    if time() - t_start > READ_TIMEOUT:
                        elapsed = True
                if not elapsed:
                    msg = self.ser.readline()
                    logapp.debug(f'{self.log_prefix} received = {msg}')
                    return msg
            raise CommException('Respirator is not connected')
        except serial.SerialException as err:
            logapp.exception(f'{self.log_prefix} error = {err}')
            return b''

    def read_bytes(self) -> bytes:
        logapp.debug(f'{self.log_prefix} read_bytes()')
        return self._read()

    def read_string(self) -> str:
        logapp.debug(f'{self.log_prefix} read_string()')
        return self._read().decode('utf-8').strip('\r\n')

    def _send(self, data: bytes):
        logapp.debug(f'{self.log_prefix} _send({data})')
        try:
            if self.ser.is_open or self.connect():
                self.ser.write(data)
            else:
                raise CommException('Respirator is not connected')
        except (serial.SerialException, serial.SerialTimeoutException) as err:
            logapp.debug(f'{self.log_prefix} error = {err}')
            raise err

    def send_bytes(self, data: bytes):
        logapp.debug(f'{self.log_prefix} send_bytes({data})')
        self._send(data)

    def send_string(self, data: str):
        logapp.debug(f'{self.log_prefix} send_string({data})')
        self._send(data.encode())

    def close(self):
        logapp.debug(f'{self.log_prefix} close()')
        self.ser.close()


class CommException(Exception):
    pass
