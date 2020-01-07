class Human:
    def __init__(self):
        self.name="nagababu"
        self.head=self.Head()
        self.brain=self.Brain()
    def display(self):
        print("Hello ...",self.name)
    class Head:
        def talk(self):
            print("Talking...")

    class Brain:
        def think(self):
            print("thinking.....")
h=Human()
h.display()
h.head.talk()
h.brain.think()