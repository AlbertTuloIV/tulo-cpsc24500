from employee import Employee

class PayrollProcessor:

    def __init__(self):
        self._employees: list[Employee] = []

    @property
    def employees(self) -> list[Employee]:
        return list(self._employees)
    
    def load_from_file(self, filename: str) -> None:
        try:
            with open(filename, "r") as f:
                for line_num, line in enumerate(f, start=1):
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split("\t")
                    if len(parts) != 4:
                        print(f"Warning: line {line_num} skipped (expected 4 fields, got {len(parts)})")
                        continue
                    try:
                        name, emp_id, rate, hours = parts
                        emp = Employee(name, emp_id, float(rate), float(hours))
                        self._employees.append(emp)
                    except ValueError as e:
                        print(f"Warning: line {line_num} skipped ({e})")
        
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        
    def calculate_total_payroll(self) -> float:
        return sum(e.calculate_gross_pay() for e in self._employees)
    
    def find_highest_paid(self) -> Employee | None:
        if not self._employees:
            return None
        return max(self._employees, key=lambda e: e.calcualte_gross_pay())
    
    def get_employee_count(self) -> int:
        return len(self._employees)
    
    def calculate_average_pay(self) -> float:
        if not self._employees:
            return 0.0
        return self.calculate_total_payroll() / len(self._employees)