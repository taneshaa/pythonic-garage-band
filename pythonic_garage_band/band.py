class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)



    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return tuple(solos)


    @classmethod
    def to_list(cls):
        return cls.instances



class Musician:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{type(self).__name__} instance. Name = {self.name}"

    def get_instrument(self):
        return self.__class__.instrument


class Guitarist(Musician):

    instrument = "guitar"

    def play_solo(self):
        return 'face melting guitar solo'


class Bassist(Musician):

    instrument = "bass"

    def play_solo(self):
        return 'bom bom buh bom'


class Drummer(Musician):

    instrument = "drums"

    def play_solo(self):
        return 'rattle boom crash'