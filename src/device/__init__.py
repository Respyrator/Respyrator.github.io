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
"""Generic device for interacting with a Medical Respirator."""

from abc import ABC, abstractmethod
from inspect import stack
from contextlib import contextmanager

class DeviceError(Exception):
    """Errors raised due to errors related to the Device."""

class DeviceConnectionError(Exception):
    """Errors related to Device connections."""

class DeviceReadError(Exception):
    """Read errors from the Device."""

class DeviceWriteError(Exception):
    """Write errors from the Device."""

class Device(ABC):
    """Generic device.
    
    This is the interface to interact with a Medical Respirator.
    """

    def __init__(self):
        """Create a new class instance."""
        self.log_prefix: str = "DEVICE"
        self.read_timeout: float = 1.0
        self.write_timeout: float = 1.0

    @abstractmethod
    def connect(self, retries: int = 0) -> None:
        """Connect to the device.
        
        :param retries: number of retries for the connection.
        :returns: `True` if the connection was successful.
        """
        raise NotImplementedError(
            f"Method {inspect.stack()[0][3]} not implemented"
        )

    @abstractmethod
    def read_bytes(self) -> bytes:
        """Read bytes from the device.

        :returns: avilable bytes in the device buffer.
        """
        raise NotImplementedError(
            f"Method {inspect.stack()[0][3]} not implemented"
        )

    @abstractmethod
    def read_string(self) -> bytes:
        """Read a string from the device.

        :returns: avilable string in the device buffer.
        """
        raise NotImplementedError(
            f"Method {inspect.stack()[0][3]} not implemented"
        )

    @abstractmethod
    def send_bytes(self, data: bytes) -> None:
        """Send bytes to the device.

        :param data: data to send to the device.
        """
        raise NotImplementedError(
            f"Method {inspect.stack()[0][3]} not implemented"
        )

    @abstractmethod
    def send_string(self, data: str) -> bytes:
        """Send a string to the device.

        :param data: data to send to the device.
        """
        raise NotImplementedError(
            f"Method {inspect.stack()[0][3]} not implemented"
        )

    @abstractmethod
    def close(successful) -> None:
        """Send a string to the device.

        :param data: data to send to the device.
        """
        raise NotImplementedError(
            f"Method {inspect.stack()[0][3]} not implemented"
        )

    def __enter__(self) -> "Device":
        """Context manager init."""
        self.connect()
        return self

    def __exit__(self, *args) -> None:
        """Context manager exit."""
        self.close()
