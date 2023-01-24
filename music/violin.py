from stringed_instrument import StringedInstrument

class Violin(StringedInstrument):
    def __init__(self):
        super().__init__("Violin",4)
        
    def sound(self):
        return "Screech"
