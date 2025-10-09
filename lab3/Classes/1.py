class Upstring:
    def __init__(self,string: str):
        self.string = string
    
    def getString(self):
        return self.string
    
    def printString(self):
        print(self.string.upper())

        
def main():
    string =  Upstring(string = input())
    string.printString()

if __name__ == "__main__":
    main()