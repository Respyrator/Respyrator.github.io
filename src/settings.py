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
from datetime import datetime
from pathlib import Path
import configparser
import logging
# Installed -------------------------------------------------------------------
# Coded -----------------------------------------------------------------------
# Program ---------------------------------------------------------------------
PROJECT_DIR = Path(__file__).resolve().parents[1]
BASE_DIR = Path(__file__).resolve().parents[0]
# PARSE CONFIGURATION ---------------------------------------------------------
CONF_FILE = BASE_DIR / 'configuration.ini'
cfg = configparser.ConfigParser()
cfg.read(str(CONF_FILE))
# LOG -------------------------------------------------------------------------
LOG_DIR = PROJECT_DIR / 'log'
LOG_DIR.mkdir(parents=True, exist_ok=True)
# Loggers
logapp = logging.getLogger('app')
logapp.setLevel(logging.DEBUG)
logmcu = logging.getLogger('mcu')
logmcu.setLevel(logging.DEBUG)
# Handlers
timestamp = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
LOG_APP_FILE = LOG_DIR / f'app_{timestamp}.log'
app_filehandler = logging.FileHandler(filename=str(LOG_APP_FILE))
app_filehandler.setLevel(logging.DEBUG)
LOG_MCU_FILE = LOG_DIR / f'mcu_{timestamp}.log'
mcu_filehandler = logging.FileHandler(filename=str(LOG_MCU_FILE))
mcu_filehandler.setLevel(logging.DEBUG)
console_streamhandler = logging.StreamHandler()
console_streamhandler.setLevel(logging.DEBUG)
# Formatter
fmt = '%(asctime)s | %(levelname)s | %(module)s | %(funcName)s ' \
    '| %(message)s'
formatter = logging.Formatter(fmt)
app_filehandler.setFormatter(formatter)
mcu_filehandler.setFormatter(formatter)
console_streamhandler.setFormatter(formatter)
# Add handlers to loggers
logapp.addHandler(app_filehandler)
logapp.addHandler(console_streamhandler)
logmcu.addHandler(mcu_filehandler)
# First message
LOG = 'SETTINGS:'
logapp.debug(f'{LOG} Log settings completed ')
# logmcu.debug(f'{LOG} Log settings completed ')
# SERIAL ----------------------------------------------------------------------
cfg_ser = {
    'baud': cfg.getint('SERIAL', 'baudrate'),
    'bytesize': cfg.getint('SERIAL', 'bytesize'),
    'parity': cfg.get('SERIAL', 'bytesize'),
    'stopbits': cfg.getint('SERIAL', 'bytesize'),
    'read_timeout': cfg.getfloat('SERIAL', 'read_timeout'),
    'write_timeout': cfg.getfloat('SERIAL', 'write_timeout')
}
