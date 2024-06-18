def show_menu():
    """Displays the conversion options menu."""
    print("Measurement Converter Menu:")
    print("1. Millimeters to Centimeters")
    print("2. Centimeters to Meters")
    print("3. Meters to Kilometers")
    print("4. Feet to Meters")
    print("5. Miles to Kilometers")

def mm_to_cm(mm):
    """Converts millimeters to centimeters."""
    return mm / 10.0

def cm_to_m(cm):
    """Converts centimeters to meters."""
    return cm / 100.0

def m_to_km(m):
    """Converts meters to kilometers."""
    return m / 1000.0

def ft_to_m(ft):
    """Converts feet to meters."""
    return ft / 3.28084

def miles_to_km(miles):
    """Converts miles to kilometers."""
    return miles * 1.60934

def main():
    show_menu()
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        mm = float(input("Enter length in millimeters: "))
        result = mm_to_cm(mm)
        print(f"{mm} millimeters is equal to {result} centimeters")
    elif choice == '2':
        cm = float(input("Enter length in centimeters: "))
        result = cm_to_m(cm)
        print(f"{cm} centimeters is equal to {result} meters")
    elif choice == '3':
        m = float(input("Enter length in meters: "))
        result = m_to_km(m)
        print(f"{m} meters is equal to {result} kilometers")
    elif choice == '4':
        ft = float(input("Enter length in feet: "))
        result = ft_to_m(ft)
        print(f"{ft} feet is equal to {result} meters")
    elif choice == '5':
        miles = float(input("Enter length in miles: "))
        result = miles_to_km(miles)
        print(f"{miles} miles is equal to {result} kilometers")
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
