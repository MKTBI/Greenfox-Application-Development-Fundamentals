from stringed_instrument import StringedInstrument

class ElectricGuitar(StringedInstrument):
    def __init__(self):
        super().__init__("Electric Guitar",6)
        
    def sound(self):
        return "Twang"