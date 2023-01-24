from stringed_instrument import StringedInstrument

class BassGuitar(StringedInstrument):
    def __init__(self):
        super().__init__("Bass Guitar",4)
        
    def sound(self):
        return "Duum-duum-duum"
