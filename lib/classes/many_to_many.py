class NationalPark:

    def __init__(self, name):
        self.name = name
        self._visitors = []
        self._trips = []


        #national park property name
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise Exception("Cannot change the name of the national park")
        elif isinstance(name, str) and len(name)>=3:
            self._name 
        else:
            raise Exception("The namemust be a string of 3 characters")
        
    #national park trips
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    #national park visitors
    def visitors(self):
        v_visited = []
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor not in v_visited:
                    v_visited.append(trip.visitor)
        return v_visited
    #national park total visits
    def total_visits(self):
        total_visit = 0
        for trip in Trip.all :
            if self not in total_visit:
                total_visit[self] += 1
        return total_visit(self)

    
    def best_visitor(self):
        pass


class Trip:

    all = [] #class level list to store all trip instances
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        #store all trips
        Trip.all.append(self)

        #establish a r/ship (bidirectional)
        self.national_park._visitors.append(self.visitor)
        self.national_park._trips.append(self)

        self.visitor._national_parks.append(self.national_park)
        self.visitor._trips.append(self)

    #Trip property start date
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date)

    #tripe property end date 
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >=7:
            self._end_date
        
        #tripe property visitor
        @property
        def visitor(self):
            return self._visitor

        @visitor.setter
        def visitor(self, visitor):
            if isinstance(visitor, Visitor):
                self._visitor = visitor
            else:
                raise Exception("Trip visitor must be a visitor object")


class Visitor:
    #visitor initialised
    def __init__(self, name):
        self.name = name
        self.national_parks = []
        self.trips = []

    #visitor property name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <len(name)< 15:
            self._name = name
        else:
            raise Exception("Visitor is initialized with a string")


        #visitor trips
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self ]
    
    def national_parks(self):
        p_visited = []
        for trip in Trip.all:
            if trip.visitor == self:
                if trip.national_park not in p_visited:
                    p_visited.append(trip.national_park)
        return p_visited
    
    def total_visits_at_park(self, park):
        visit_count = 0
        for trip in Trip.all:
            if trip.visitor == self and trip.national_park == park:
                visit_count[self] =+ 1
            return visit_count


    def __repr__(self):
        return f"{self.name}"