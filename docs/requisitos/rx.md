# Enviar comandos

| Campo  | Dirección (byte) | Tamaño (bits) |  Uso, Valores, Comentarios |  
| -----  | ---------------- | ------------- | -------------------------- |
| Header | 0x00 | 8 | 0x55 |


Protocol Version
0x01
8
0x10: v1.0

Frame Number
0x02
8
Incremental counter, to keep track of answers and ACK. 

Command
0x03
8
0x01: setRPM
0x02: setPeakPressure
0x03: setPeepPressure
0x04: setTriggerFlow
0x05: setRamp

0x11: setAlarmVolumeLow
0x12: setAlarmVolumeHigh
0x13: setAlarmRPMLow
0x14: setAlarmRPMHigh
0x15: setAlarmPeakPressureLow
0x16: setAlarmPeakPressureHigh
0x17: setAlarmPeepPressureLow
0x18: setAlarmPeepPressureHigh
0x19: setAlarmBatteryLow

0x21: getAlarmVolumeLow
0x22: getAlarmVolumeHigh
0x23: getAlarmRPMLow
0x24: getAlarmRPMHigh
0x25: getAlarmPeakPressureLow
0x26: getAlarmPeakPressureHigh
0x27: getAlarmPeepPressureLow
0x28: getAlarmPeepPressureHigh
0x29: getAlarmBatteryLow

0x50: getFimwareVersion

Value (High Byte)
0x04
8
Value (High Byte)

Value (Low Byte)
0x05
8
Value (Low Byte)

CRC
0x06
0x07
8 (high)
8 (low)
Frame CRC
