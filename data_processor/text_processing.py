

class TextProcessing:
    def __init__(self, stt, hostile_list, less_hostile_list):
        self.stt = stt.split()
        self.hostile_list = hostile_list
        self.less_hostile_list = less_hostile_list

    def text_classification(self):
        x = 0
        for  word in self.stt:
            if word in self.hostile_list:
                x += 2
            if word in self.less_hostile_list:
                x += 1
        return x

    def bds_percent(self):
        stt_len = len(self.stt)

        return round((self.text_classification() * 100) / stt_len) * 10

    def get_bds_threat_level(self):
        bds_threat_level = "none"
        if self.bds_percent() > 49:
            bds_threat_level = "high"
        elif (self.bds_percent() < 49) and (self.bds_percent() > 0):
            bds_threat_level = "medium"

        return bds_threat_level

