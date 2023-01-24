from electric_guitar import ElectricGuitar
from bass_guitar import BassGuitar
from violin import Violin


class AppMusic:
    def main(self):
        print("Test 1, create Electric Guitar, Bass Guitar and Violin with default strings.")
        guitar = ElectricGuitar()
        bass_guitar = BassGuitar()
        violin = Violin()

        print("Test 1 Play")
        guitar.play()
        bass_guitar.play()
        violin.play()

        print("Test 2, create Electric Guitar, Bass Guitar with 7 and 5 strings .");
        guitar2 = ElectricGuitar(7)
        bass_guitar2 = BassGuitar(5)

        print("Test 2 Play")
        guitar2.play()
        bass_guitar2.play()


music = AppMusic()
music.main()