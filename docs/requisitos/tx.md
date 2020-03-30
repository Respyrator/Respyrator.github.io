# Leer datos del respirador

El respirador manda una trama estructurada de la siguiente manera:

| Campo | Dirección (byte) | Tamaño (bits) | Uso, Valores, Comentarios |
| :- | :-: | :-: | :-  |
| Header | 0x00 | 8 | 0x44 |
| Protocol Version | 0x01 | 8 | 0x10: v1.0 |
| UUID | 0x02 | 8 (high)<br>8 (low) |  |
| Tag/Free use SN | 0x06 | 8 (high)<br>8 (low) |  |
| RPM Setting | 0x0A<br>0x0B| 8 (high)<br>8 (low) |  |
| RPM Measure | 0x0C<br>0x0D | 8 (high)<br>8 (low) |  |
| PeakPresure setting | 0x0E<br>0x0F | 8 (high)<br>8 (low) |  |
| PeakPreasure measure | 0x10<br>0x11 | 8 (high)<br>8 (low) |  |
| PeepPresure setting | 0x12<br>0x12 | 8 (high)<br>8 (low) |  |
| PeepPreasure measure | 0x14<br>0x15 | 8 (high)<br>8 (low) |  |
| TriggerFlow setting | 0x16<br>0x17 | 8 (high)<br>8 (low) |  |
| Flow measure | 0x18<br>0x19 | 8 (high)<br>8 (low) |  |
| Ramp setting | 0x1A<br>0x1B | 8 (high)<br>8 (low) |  |
| ActiveAlarmCode | 0x1C | 8 | 0x00: noAlarmActive<br>0x01: alarmVolumeLow<br>0x02: alarmVolumeHigh<br>0x03: alarmRPMLow<br>0x04: alarmRPMHigh<br>0x05: alarmPeakPressureLow<br>0x06: alarmPeakPressureHigh<br>0x07: alarmPeepPressureLow<br>0x08: alarmPeepPressureHigh<br>0x09: alarmBatteryLow<br>If more than one alarm present, they alternate with 1 sec. cycle |
| Status Bit Field | 0x1D | 8 | b0: currCycleWasTriggered<br>b1: lastCycleWasTriggered<br>b2: edditingEnc1 (show tempValueEnc1)<br>b3: edditingEnc2 (show tempValueEnc2)<br>b4: edditingEnc3 (show tempValueEnc3)<br>b5: edditingEnc4 (show tempValueEnc4)<br>b6: ACK<br>b7: NACK<br>If this frames contains no answer, b6 and b7 are 0. |
| tempValueEnc1 | 0x1E<br>0x1F | 8 (high)<br>8 (low) | Value to be shown during edition |
| tempValueEnc2 | 0x20<br>0x21 | 8 (high)<br>8 (low) | Value to be shown during edition |
| tempValueEnc3 | 0x22<br>0x23 | 8 (high)<br>8 (low) | Value to be shown during edition |
| tempValueEnc4 | 0x24<br>0x25 | 8 (high)<br>8 (low) | Value to be shown during edition
| Answer | 0x26<br>0x27 | 8 (high)<br>8 (low) | Requested Value |
| Answer to Frame Number | 0x28 | 8 | Incremental counter, to keep track of answers and ACK. |
| CRC16 | 0x29 | 8 (high)<br>8 (low) | Frame CRC16
