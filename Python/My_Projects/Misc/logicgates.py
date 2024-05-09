class gate:
    name = ""
    gateinput = gateoutput = []
    def __init__(self, name, inputsize=1, outputsize=1) -> None:
        self.name = name
        for i in range(inputsize):
            self.gateinput[i] = False
        for i in range(outputsize):
            self.gateoutput=[i] = False