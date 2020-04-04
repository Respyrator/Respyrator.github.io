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
# Installed -------------------------------------------------------------------
from serial.tools.list_ports import comports
# Coded -----------------------------------------------------------------------
# Program ---------------------------------------------------------------------
LOG = 'SERDEVICES:'

for i in comports():
    print(f'Serial device founded\n'
          f'description   = {i.description}\n'
          f'device        = {i.device}\n'
          f'hwid          = {i.hwid}\n'
          f'interface     = {i.interface}\n'
          f'location      = {i.location}\n'
          f'manufacturer  = {i.manufacturer}\n'
          f'name          = {i.name}\n'
          f'pid           = {i.pid}\n'
          f'product       = {i.product}\n'
          f'serial_number = {i.serial_number}\n'
          f'vid           = {i.vid}\n\n')
    msg = 'Arduino' if i.manufacturer and 'uino' in i.manufacturer \
        else 'Desconocido'
    print(f'{msg}\n\n')
