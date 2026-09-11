class MissionManager:
    def __init__(self):
        self.state = "IDLE"
        self.action = "STANDBY"

    def update_kondisi(self, object_name, confidence, distance):
        if object_name == "" or object_name == "None" or confidence < 0.70:
            self.state = "SEARCHING"
            self.action = "SEARCH TARGET"
        elif distance <= 0.5:
            self.state = "MISSION_COMPLETE"
            self.action = "STOP"
        elif distance <= 2.0:
            self.state = "APPROACHING"
            self.action = "APPROACH TARGET"
        else:
            self.state = "DETECTED"
            self.action = "APPROACH TARGET"

baris1 = input()
baris2 = input()
baris3 = input()

pecah1 = baris1.split(":")
object_name = pecah1[1].strip()

pecah2 = baris2.split(":")
confidence = float(pecah2[1].strip())

pecah3 = baris3.split(":")
distance = float(pecah3[1].strip())

manager = MissionManager()
manager.update_kondisi(object_name, confidence, distance)

print("Object detected:", object_name)
print("Confidence:", "{:.2f}".format(confidence))
print("Distance:", "{:.2f}".format(distance), "m")
print()
print("Mission State:", manager.state)
print("Action:", manager.action)