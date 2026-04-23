from payroll_processor import PayrollProcessor
from payroll_report import PayrollReport

def main():
    processor = PayrollProcessor()
    processor.load_from_file("employees.txt")

    report = PayrollReport(processor)

    print("=" * 40)
    print("    Payroll Management System")
    print("=" * 40)

    while True:
        print()
        print("(1) View All Employees")
        print("(2) View Payroll Summary")
        print("(3) Generate report file")
        print("(4) Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            report.display_all_employees()
        elif choice == "2":
            report.display_payroll_summary()
        elif choice == "3":
            filename = input ("Enter output filename: ").strip()
            if filename:
                report.generate_report_file(filename)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()