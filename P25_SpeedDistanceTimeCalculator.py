def convert_to_hours(time, unit):
    unit = unit.lower()
    if unit == "seconds":
        return time / 3600
    elif unit == "minutes":
        return time / 60
    elif unit == "hours":
        return time
    else:
        raise ValueError("Invalid time unit.")

def convert_to_km(distance, unit):
    unit = unit.lower()
    if unit == "meters":
        return distance / 1000
    elif unit == "kilometers":
        return distance
    elif unit == "miles":
        return distance * 1.60934
    else:
        raise ValueError("Invalid distance unit.")

def convert_from_km(km, unit):
    unit = unit.lower()
    if unit == "meters":
        return km * 1000
    elif unit == "kilometers":
        return km
    elif unit == "miles":
        return km / 1.60934
    else:
        raise ValueError("Invalid distance unit.")

def convert_speed_kmph_to_unit(speed_kmph, unit):
    unit = unit.lower()
    if unit == "kmph":
        return speed_kmph
    elif unit == "mps":
        return speed_kmph * 1000 / 3600
    elif unit == "mph":
        return speed_kmph / 1.60934
    else:
        raise ValueError("Invalid speed unit.")

def convert_speed_to_kmph(speed, unit):
    unit = unit.lower()
    if unit == "kmph":
        return speed
    elif unit == "mps":
        return speed * 3600 / 1000
    elif unit == "mph":
        return speed * 1.60934
    else:
        raise ValueError("Invalid speed unit.")

def convert_time_from_hours(hours, unit):
    unit = unit.lower()
    if unit == "seconds":
        return hours * 3600
    elif unit == "minutes":
        return hours * 60
    elif unit == "hours":
        return hours
    else:
        raise ValueError("Invalid time unit.")

def calculate_speed():
    distance = float(input("Enter distance: "))
    d_unit = input("Enter distance unit (meters/kilometers/miles): ")
    time = float(input("Enter time: "))
    t_unit = input("Enter time unit (seconds/minutes/hours): ")
    speed_unit = input("Enter desired speed unit (kmph/mps/mph): ")

    distance_km = convert_to_km(distance, d_unit)
    time_hr = convert_to_hours(time, t_unit)
    speed_kmph = distance_km / time_hr
    result = convert_speed_kmph_to_unit(speed_kmph, speed_unit)

    print(f"\nSpeed = {result:.2f} {speed_unit}\n")

def calculate_time():
    distance = float(input("Enter distance: "))
    d_unit = input("Enter distance unit (meters/kilometers/miles): ")
    speed = float(input("Enter speed: "))
    s_unit = input("Enter speed unit (kmph/mps/mph): ")
    time_unit = input("Enter desired time unit (seconds/minutes/hours): ")

    distance_km = convert_to_km(distance, d_unit)
    speed_kmph = convert_speed_to_kmph(speed, s_unit)
    time_hr = distance_km / speed_kmph
    result = convert_time_from_hours(time_hr, time_unit)

    print(f"\nTime = {result:.2f} {time_unit}\n")

def calculate_distance():
    speed = float(input("Enter speed: "))
    s_unit = input("Enter speed unit (kmph/mps/mph): ")
    time = float(input("Enter time: "))
    t_unit = input("Enter time unit (seconds/minutes/hours): ")
    d_unit = input("Enter desired distance unit (meters/kilometers/miles): ")

    speed_kmph = convert_speed_to_kmph(speed, s_unit)
    time_hr = convert_to_hours(time, t_unit)
    distance_km = speed_kmph * time_hr
    result = convert_from_km(distance_km, d_unit)

    print(f"\nDistance = {result:.2f} {d_unit}\n")

def main():
    print("🚗 Welcome to the Time-Distance-Speed Converter!\n")

    while True:
        print("What do you want to calculate?")
        print("1. Speed")
        print("2. Time")
        print("3. Distance")
        choice = input("Enter 1, 2, or 3: ").strip()

        try:
            if choice == "1":
                calculate_speed()
            elif choice == "2":
                calculate_time()
            elif choice == "3":
                calculate_distance()
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.\n")
                continue
        except Exception as e:
            print(f"⚠️ Error: {e}\n")
            continue

        again = input("Do you want to convert more? (yes/no): ").strip().lower()
        if again != "yes":
            print("\n✅ Thanks for using the converter! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
