import random

class patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed = None;

    def info(self):
        print "Patient ID:", self.id
        print "Patient name:", self.name
        print "Patient allergies:", self.allergies
        print "Patient bed:", self.bed
        return self

class hospital(patient):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity

    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Hospital is full."
        else:
            self.patients.append(patient)
            patient.bed = random.randrange(1,100,1)
        return self

    def discharge(self, id):
        for i in range(0, len(self.patients)):
            if self.patients[i].id == id:
                self.patients.remove(self.patients[i])
                self.patients[i].bed = None;
                break
        return self

    def info(self):
        print "Hospital Name:", self.name
        print "Capacity:", self.capacity
        for i in range(0,len(self.patients)):
            print self.patients[i].name
        return self


patient1 = patient(1, "Ben", None)
patient2 = patient(2, "Ken", "Pollen")
patient3 = patient(3, "Jen", "Pollen")
patient4 = patient(4, "Len", "Pollen")

hospital1 = hospital("UW Medicine", 3).admit(patient1).admit(patient2).admit(patient3).admit(patient4)
hospital1.discharge(1).info()