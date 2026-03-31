class FlipFlopBell:
    def __init__(self):
        self._flip = True

    def ring(self):
        if self._flip:
            print("flip")
        else:
            print("flop")
        self._flip = not self._flip


bell = FlipFlopBell()
bell.ring()
bell.ring()
bell.ring()
