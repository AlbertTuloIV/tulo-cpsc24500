from payroll_processor import PayrollProcessor

class PayrollReport:

    def __init__(self, processor: PayrollProcessor):
        self._processor = processor

    def display_all_employees(self) -> None:
        print("=" * 65)
        print(f"{'Name':<20s} {'ID':<8s} {'Rate':>8s} {'Hours':>6s} {'Gross Pay':>10s}")
        print("=" * 65)
        for emp in self._processor.employees:
            print(emp)
        print("=" * 65)

    def display_payroll_summary(self) -> None:
        print("--- Payroll Summary ---")
        print(f"Total employees: {self._processor.get_employee_count()}")
        print(f"Total payroll:    ${self._processor.calculate_total_payroll():,.2f}")
        print(f"Average pay:      ${self._processor.calculate_average_pay():,.2f}")

        highest = self._processor.find_highest_paid()
        lowest = self._processor.find_lowest_paid()

        if highest:
            print(f"Highest paid:     {highest.name} (${highest.calculate_gross_pay():,.2f})")
        if lowest:
            print(f"Lowest paid:      {lowest.name} (${lowest.calculate_gross_pay():,.2f})")

    def generate_report_file(self, filename: str) -> None:
        lines: list[str] = []
        sep = "=" * 65

        lines.append(sep)
        lines.append(f"{'Name':<20s} {'ID':<8s} {'Rate':>8s} {'Hours':>6s} {'Gross Pay':>10s}")
        lines.append(sep)

        for emp in self._processor.employees:
            lines.append(str(emp))

        lines.append(sep)
        lines.append("")
        lines.append("--- Payroll Summary ---")
        lines.append(f"Total employees {self._processor.get_employee_count()}")
        lines.append(f"Total payroll:   ${self._processor.calculate_total_payroll():,.2f}")
        lines.append(f"Average pay:     ${self._processor.calculate_average_pay():,.2f}")

        highest = self._processor.find_highest_paid()
        lowest = self._processor.find_lowest_paid()
        if highest:
            lines.append(f"Highest paid:      {highest.name} (${highest.calculate_gross_pay():,.2f})")
        if lowest:
            lines.append(f"Lowest paid:       {lowest.name} (${lowest.calculate_gross_pay():,.2f})")

        with open(filename, "w") as f:
            f.write("\n".join(lines) + "\n")
        
        print(f"Report written to {filename}")