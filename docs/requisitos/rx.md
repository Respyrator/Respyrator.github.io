# Enviar comandos

Para modificar parámetros del respirador, hay que enviar una trama con el siguiente formato:

| Campo | Dirección (byte) | Tamaño (bits) | Uso, Valores, Comentarios |
| :- | :-: | :-: | :- |
| Header | 0x00 | 8 | 0x55 |
| Protocol Version | 0x01 | 8 | 0x10: v1.0 |
| Frame Number | 0x02 | 8 | Incremental counter, to keep track of answers and ACK. |
| Command | 003 | 8 | 0x01: stRPM<br>0x02: setPeakPressure<br>003: setPeepPressure<br>0x04: setTriggerFlow<br>0x05: setRamp<br><br>0x11: setAlarmVolumeLowbr>0x12: setAlarmVolumeHigh<br>x13: setAlarmRPMLow<br>0x14: setAarmRPMHigh<br>0x15:setAlarmPeakPressureLowbr>0x16: setAlarmPeakPressueHigh<br>0x17: setAlarmPeepPressurLow<br>0x18: setAlarmPeepPressreHigh<br>0x19: setAlarBatteryLow<br><br>0x1: getAlarmVolumeLow<br>0x22: getAlarmVolumeHigh<br>x23: getAlarmRPMLow<br>0x24: getAarmRPMHigh<br>0x25:getAlarmPeakPressureLowbr>0x26: getAlarmPeakPressueHigh<br>0x27: getAlarmPeepPressureLow<br>0x28: getAlarmPeepPressureHigh<br>0x29: getAlarmBatteryLow<br><br>0x50: getFimwareVersion |
| Value (High Byte) | 0x04 | 8 | Value (High Byte) |
| Value (Low Byte) | 0x05 | 8 | Value (Low Byte) |
| CRC | 0x06<br>0x07 | 8 (high)<br>8 (low) | Frame CRC |
