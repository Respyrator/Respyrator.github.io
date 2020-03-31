# Built-in --------------------------------------------------------------------
from datetime import datetime
from pathlib import Path
import configparser
import logging
# Installed -------------------------------------------------------------------
# Coded -----------------------------------------------------------------------
# Program ---------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
print(f'BASE_DIR = {BASE_DIR}')
SRC_DIR = BASE_DIR / 'src'
# PARSE CONFIGURATION ---------------------------------------------------------
CONF_FILE = SRC_DIR / 'configuration.ini'
cfg = configparser.ConfigParser()
cfg.read(str(CONF_FILE))
# LOG -------------------------------------------------------------------------
LOG_DIR = BASE_DIR / 'log'
LOG_DIR.mkdir(parents=True, exist_ok=True)
# Loggers
logapp = logging.getLogger('app')
logapp.setLevel(logging.DEBUG)
logser = logging.getLogger('serial')
logser.setLevel(logging.DEBUG)
# Handlers
timestamp = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
LOG_APP_FILE = LOG_DIR / f'app_{timestamp}.log'
LOG_SER_FILE = LOG_DIR / f'serial_{timestamp}.log'
app_filehandler = logging.FileHandler(filename=str(LOG_APP_FILE))
app_filehandler.setLevel(logging.DEBUG)
serial_filehandler = logging.FileHandler(filename=str(LOG_SER_FILE))
serial_filehandler.setLevel(logging.DEBUG)
console_streamhandler = logging.StreamHandler()
console_streamhandler.setLevel(logging.DEBUG)
# Formatter
fmt = '%(asctime)s | %(levelname)s | %(module)s | %(funcName)s ' \
    '| %(message)s'
formatter = logging.Formatter(fmt)
app_filehandler.setFormatter(formatter)
serial_filehandler.setFormatter(formatter)
console_streamhandler.setFormatter(formatter)
# Add handlers to loggers
logapp.addHandler(app_filehandler)
logapp.addHandler(console_streamhandler)
logser.addHandler(serial_filehandler)
# First message
LOG = 'SETTINGS:'
logapp.debug(f'{LOG} Log settings completed ---------------------------------')
logser.debug(f'{LOG} Log settings completed ---------------------------------')
# SERIAL ----------------------------------------------------------------------
cfg_ser = {
    'baud': cfg.getint('SERIAL', 'baudrate'),
    'bytesize': cfg.getint('SERIAL', 'bytesize'),
    'parity': cfg.get('SERIAL', 'bytesize'),
    'stopbits': cfg.getint('SERIAL', 'bytesize'),
    'read_timeout': cfg.getfloat('SERIAL', 'read_timeout'),
    'write_timeout': cfg.getfloat('SERIAL', 'write_timeout')
}
