class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        max_speed = max_speed.split("mph")
        self.max_speed = max_speed[0]
        self.miles = 0
    #this method displays the bike's price, maximum speed, and the total miles.
    def displayInfo(self):
        print "Bike Price: $" + str(self.price), "\nMaxixmum Speed:", self.max_speed, "\nTotal Miles:", self.miles
        return self
    # display "Riding" on the screen and increase the total miles ridden by 10
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    
    # display "Reversing" on the screen and decrease the total miles ridden by 5...
    def reverse(self):
        print "Reversing"
        if self.miles > 5:
            self.miles -= 5
        return self

print "\nTest"
test = bike(200,"25mph")
test.displayInfo()

# first instance ride three times, reverse once and have it displayInfo()
print "\nInstance One"
int_one = bike(200,"30mph").ride().ride().ride().reverse().displayInfo()

# second instance ride twice, reverse twice and have it displayInfo()
print "\nInstance Two"
int_two = bike(250,"30mph").ride().ride().reverse().reverse().displayInfo()

# third instance reverse three times and displayInfo()
print "\nInstance Three"
int_three = bike(300,"30mph").reverse().reverse().reverse().displayInfo()