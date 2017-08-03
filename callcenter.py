class call(object):
    def __init__(self, uid, name, number, time, reason):
        self.uid = uid
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    
    def display(self):
        print "Unique ID:", self.uid
        print "Name:", self.name
        print "Phone Number:", self.number
        print "Time:", self.time
        print "Reason:", self.reason
        return self

class callcenter(call):
    def __init__(self):
        self.calls = []
        self.queue = 0

    def add(self, call):
        self.calls.append(call)
        self.queue += 1
        return self

    def remove(self):
        newlist = []
        for i in range(1,len(self.calls)):
            newlist.append(self.calls[i])
        self.calls = newlist
        self.queue -= 1
        return self

    def removecall(self, number):
        for i in range(0, len(self.calls)):
            if self.calls[i].number == number:
                self.calls.remove(self.calls[i])
                self.queue -= 1
                break
        return self

    def info(self):
        for i in range(0,len(self.calls)):
            print self.calls[i].name + " - " + self.calls[i].number
        print "Calls in queue:", self.queue
        return self

    def sort_time(self):
        self.calls = sorted(self.calls, key=lambda calls: calls.time)
        return self

call1 = call(1, "Ben", "123-1234", 5, "chat")
call2 = call(2, "Jen", "321-1234", 6, "chat")
call3 = call(3, "Ken", "123-4321", 1, "chat")

callcenter = callcenter().add(call1).add(call2).add(call3).info()
# callcenter.removecall("321-1234").info()
callcenter.sort_time().info()