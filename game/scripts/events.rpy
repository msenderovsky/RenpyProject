init python:
    class Calendar(object):
        def __init__(self, hours, hour, days, day, months, month, weekDays, monthDays):
            self.hours = hours
            self.hour = hour
            self.days = days
            self.day = day
            self.months = months
            self.month = month
            self.weekDays = weekDays
            self.monthDays = monthDays

        @property
        def output(self):
            return self.weekDays[self.day] + " " + self.months[self.month] + " " + str(self.days+1) + " " + str(self.hours).zfill(2) + ":00"
        def addTime(self,hours):
            self.hours +=hours
            if self.hours > 23:
                self.hours -= 24
                self.day += 1
                self.days += 1
            if self.day > 6:
                self.day = 0
            if self.days > self.monthDays[self.month]:
                self.month += 1
                self.day = 0
            if self.month > 11:
                self.month = 0

    class Event(object):
        def __init__(self, hour, day, month, bock, isActive):
            self.hour=hour
            self.day=day
            self.month=month
            self.bock=bock
            self.isActive=isActive

        def DateCheck(self,c):
            if self.day == c.day and self.hour == c.hour and self.month == c.month and self.isActive:
                return True
            else:
                return False
        
        def setInactive(self):
            self.isActive = False

    class Item(object):
        def __init__(self, name, value, weight, noOwned, id):
            self.name = name
            self.value = value
            self.weight = weight
            self.noOwned = noOwned
            self.id=id

        def addItem(self):
            maxWeight = 50
            if (self.currentWeight + self.weight) > maxWeight:
                return
            else:
                self.noOwned += 1
        @property
        def currentWeight(self):
            currentW = 0
            for q in inventory:
                currentW += (q.weight * q.noOwned)
            return currentW

    class Place(object):
        def __init__(self, ID, x, y, name, isActive):
            self.ID = ID
            self.x = x
            self.y = y
            self.name = name
            self.isActive = isActive

        @property
        def rooms(self):
            outList = []
            for q in subLocations:
                if q.parent == self.ID:
                    outList.append(q.ID)
            return outList
        
    class SubPlace(object):
        def __init__(self, ID, parent, name, isActive):
            self.ID = ID
            self.parent = parent
            self.name = name
            self.isActive = isActive

    places = []
    subLocations = []
    events = []
    inventory = []
    t = 0

    while t < 50:
        events.append(Event(0, 0, 0, "", False))
        inventory.append(Item("none", 0, 0, 0, t))
        places.append(Place(t, 0, 0, "", False))
        subLocations.append(SubPlace(t, -1, "", False))
        t += 1

    places[0]= Place(0, 1000, 600, "School", True)
    places[1]= Place(1, 1000, 800, "Shop", True)
    places[2]= Place(2, 1000, 1000, "Home", True)

    subLocations[0] = SubPlace(0, 2, "Bathroom", True)
    subLocations[1] = SubPlace(1, 2, "Bedroom", True)
    subLocations[2] = SubPlace(2, 2, "Kitchen", True)
    subLocations[3] = SubPlace(3, 2, "Living Room", True)