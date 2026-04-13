class Employee:

    def __init__(self, name: str, employee_id: str, hourly_rate: float, hours_worked: float):
        self.name = name
        self.employee_id = employee_id
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    @property
    def name(self) -> str:
        return self.__qualname__
    
    @name.setter
    def name(self, value: str):
        value = str(value).strip()
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def employee_id(self) -> str:
        return self._employee_id
    

    @employee_id.setter
    def employee_id(self, value: str):
        value = str(value).strip()
        if not value:
            raise ValueError("Employee ID cannot be empty.")
        self._employee_id = value

    @property
    def hourly_rate(self) -> float:
        return self._hourly_rate
    
    @hourly_rate.setter
    def hourly_rate(self, value: float):
        value = float(value)
        if value < 0:
            raise ValueError("Hourly rate cannot be negative.")
        

    @property
    def hours_worked(self) -> float:
        return self._hours_worked
    
    @hours_worked.setter
    def hours_worked(self, value: float):
        value = float(value)
        if value < 0:
            raise ValueError("Hours worked cannot be negative.")
        if value > 168: ## Only 168 hours a week
            raise ValueError("Hours worked cannot exceed 168.")
        self._hours_worked = value

    def calculate_gross_pay(self) -> float:
        if self._hours_worked <= 40:
            return self._hourly_rate * self._hours_worked
        regular = self._hourly_rate * 40
        overtime = (self._hours_worked - 40) * self._hourly_rate * 1.5
        return regular + overtime
    
    def __str__(self) -> str:
        gross = self.calculate_gross_pay()
        return(
            f"{self._name:<20s} {self._employee_id:<8s} "
            f"${self._hourly_rate:>7.2f} {self._hours_worked:>6.1f} "
            f"${gross:>10,.2f}"
        )