class TextWriter:
    def write(self):
        filename = input("Hallo! Wie soll die Textdatei heißen? ")
        count = int(input("Wie viele Zeilen willst du reinschreiben? "))
        with open(filename + ".txt", "w") as file:
            for i in range(0,count):
                line = input("Was soll in die " + str(i+1) + ". Zeile rein? ")
                file.write(line + "\n")
        print("Fertig!")

f = TextWriter()
f.write()
