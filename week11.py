class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def adder(self):
        print("Addition:",self.a+self.b)
    def subtractor(self):
        print("Subtraction:", self.a-self.b)
    def multiplier(self):
        print("Multiplication:",self.a*self.b)
    def divider(self):
        print("Division:",self.a/self.b)
    def clear(self):
        self.a=0
        self.b=0
        print("Cleared!")

print("Enter 2 numerical inputs: ")
inputs=input().split(",")
inputs[0]=float(inputs[0])
inputs[1]=float(inputs[1])
x=Calculator(inputs[0],inputs[1])
x.adder()
x.subtractor()
x.multiplier()
x.divider()
x.clear()
class clockTime:
    def __init__(self):
        self.hours=0
        self.minutes=0
        self.seconds=0
    def setHours(self,hours):
        while hours>24 or hours <0:
            print("Invalid Hours, Re-enter!")
            hours = int(input())

        else:
            self.hours=hours
    def setMinutes(self,minutes):
        while minutes>59 or minutes<0:
            print("Invalid Minutes, Re-enter!")
            minutes = int(input())
        else:
            self.minutes=minutes

    def setSeconds(self,seconds):
        while seconds>59 or seconds<0:
            print("Invalid Seconds, Re-enter!")
            seconds = int(input())

        else:
            self.seconds=seconds
        
    def setTime(self,hours,minutes,seconds): 
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)
    def showTime(self):
        print("Setted time:",self.hours,":",self.minutes,":",self.seconds)
clock=clockTime()
print("Enter hours’ value,minutes’ value, and seconds’ value: ")
inputs=input().split(",")
clock.setTime(int(inputs[0]),int(inputs[1]),int(inputs[2]))
clock.showTime()
        