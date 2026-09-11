# Tugas Khusus ORCA

## Identitas
Firdaus Muhammad Faris - 26/581420/TK/66198

## Tugas 1 - Komponen ROV
Program buat nyatet data komponen robot:
* `KomponenROV` (class utama / parent)
* `Thruster` (child class, ada atribut power)
* `Sensor` (child class, ada atribut nilai)

## Tugas 2 - Mission Manager
Program buat nentuin status misi robot dari input penglihatan/kamera:
* `SEARCHING`: objek ga ketemu atau confidence < 0.70
* `DETECTED`: objek ketemu (confidence >= 0.70, jarak > 2m)
* `APPROACHING`: jarak ke objek <= 2 meter
* `MISSION_COMPLETE`: jarak ke objek <= 0.5 meter
