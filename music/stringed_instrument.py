from instrument import Instrument

class StringedInstrument(Instrument):
    def __init__(self, name, number_of_strings):
        super().__init__(name)
        self.number_of_strings = number_of_strings
        
    def sound(self):
        pass
    
    def play(self):
        return self.sound()
