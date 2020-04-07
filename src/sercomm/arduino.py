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
"""Arduino connection implementation."""
import serial
from serial.tools.list_ports import comports

from src.sercomm.comm import CommConfig, Comm, logapp

class Arduino(Comm):

    def __init__(self, configuration, identifier):
        super().__init__(configuration)
        self.identifier = identifier


    def respirator_port(self) -> str:
        logapp.debug(f'{self.log_prefix} respirator_port()')
        for i in comports():
            logapp.debug(f'{self.log_prefix} Serial devices at {i.device}')
            if self._check_device(i.manufacturer, self.identifier):
                logapp.debug(f'{self.log_prefix} respirator at {i.device}')
                return i.device
        logapp.debug(f'{self.log_prefix} respirator not finded')
        return ''


__configuration = CommConfig(
    BAUDRATE = 115200,
    BYTESIZE = serial.EIGHTBITS,
    PARITY = serial.PARITY_NONE,
    STOPBITS = serial.STOPBITS_ONE
)

# List of Arduinos ready to be used
ARDUINO_MEGA = Arduino(__configuration, "Arduino (www.arduino.cc)")
UNNOFICIAL_ARDUINO_MEGA = Arduino(__configuration, "USB2.0-Serial")
