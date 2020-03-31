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
