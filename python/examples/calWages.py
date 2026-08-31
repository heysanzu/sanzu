def get_float(prompt, min_value=None, default=None):
    while True:
        try:
            s = input(prompt).strip()
            if s == "" and default is not None:
                return float(default)
            value = float(s)
            if min_value is not None and value < min_value:
                print(f"Please enter a value >= {min_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def calculate_gross_pay(hours, rate, standard_hours=40, overtime_multiplier=1.5):
    if hours <= standard_hours:
        return hours * rate
    regular = standard_hours * rate
    overtime = (hours - standard_hours) * rate * overtime_multiplier
    return regular + overtime

def calculate_net_pay(gross, tax_rate_percent=20.0):
    tax_rate = tax_rate_percent / 100.0
    tax = gross * tax_rate
    net = gross - tax
    return net, tax

def format_currency(value):
    return f"₹{value:,.2f}"

def main():
    print("Wage Calculator")
    name = input("Employee name (optional): ").strip()
    hours = get_float("Hours worked: ", min_value=0)
    rate = get_float("Hourly rate: ", min_value=0)
    tax_rate = get_float("Tax rate (percent, default 20): ", min_value=0, default=20.0)
    overtime_multiplier = get_float("Overtime multiplier (default 1.5): ", min_value=1.0, default=1.5)
    standard_hours = get_float("Standard hours per week (default 40): ", min_value=0, default=40.0)

    gross = calculate_gross_pay(hours, rate, standard_hours=standard_hours, overtime_multiplier=overtime_multiplier)
    net, tax = calculate_net_pay(gross, tax_rate_percent=tax_rate)

    print("\n-- Pay Breakdown --")
    if name:
        print("Employee:", name)
    print("Hours worked:", hours)
    print("Hourly rate:", format_currency(rate))
    print("Gross pay:", format_currency(gross))
    print("Tax withheld:", format_currency(tax), f"({tax_rate:.2f}%)")
    print("Net pay:", format_currency(net))
    print("--------------------")
    print("Monthly pay:", format_currency(net * 30))

if __name__ == "__main__":
    main()