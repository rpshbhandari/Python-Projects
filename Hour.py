class Hour:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    @classmethod
    def from_string(cls, time_string):
        """
        Create an Hour object from a string in the format of 'HH:MM'
        """
        hours, minutes = map(int, time_string.split(':'))
        return cls(hours, minutes)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

    def __repr__(self):
        return f"Hour(hours={self.hours}, minutes={self.minutes})"

    def __add__(self, other):
        total_minutes = self.hours * 60 + self.minutes + other.hours * 60 + other.minutes
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return Hour(hours, minutes)

    def __sub__(self, other):
        total_minutes = self.hours * 60 + self.minutes - (other.hours * 60 + other.minutes)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        return Hour(hours, minutes)
