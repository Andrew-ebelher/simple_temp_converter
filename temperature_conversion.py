print("\nThis is a program to convert between °C, °F and °K!")
temperature = float(input("\nEnter a temperature (int or float): "))
original_unit = str(input("\nEnter the unit of the entered temperature (C for °C, F for °F or K for °K): "))
converted_unit = str(input("\nEnter the unit you would like to convert to  (C for °C, F for °F or K for °K): "))

def c_to_f(temperature: float) -> float:
    """
    Convert the temperature input from °C to °F
    """
    return (temperature * (9/5)) + 32

def c_to_k(temperature: float) -> float:
    """
    Convert the temperature input from °C to °K
    """
    return temperature + 273.15

def k_to_c(temperature: float) -> float:
    """
    Convert the temperature input from °K to °C
    """
    return temperature - 273.15

def f_to_c(temperature: float) -> float:
    """
    Convert the temperature input from °F to °C
    """
    return (temperature - 32) * (5/9)

def f_to_k(temperature: float) -> float:
    """
    Convert the temperature input from °F to °K
    """
    return (temperature - 32) * (5/9) + 273.15

def k_to_f(temperature: float) -> float:
    """
    Convert the temperature input from °K to °F
    """
    return (temperature - 273.15) * (9/5) + 32

def main() -> None:
    #C to F
    if original_unit.upper() == "C" and converted_unit.upper() == "F":
        print(f"\n{temperature}°{original_unit} converted to °{converted_unit.upper()} = {c_to_f(temperature):.2f}°{converted_unit.upper()}")
    #C to K
    elif original_unit.upper() == "C" and converted_unit.upper() == "K":
        print(f"\n{temperature}°{original_unit} converted to °{converted_unit.upper()} = {c_to_k(temperature):.2f}°{converted_unit.upper()}")
    #K to C
    elif original_unit.upper() == "K" and converted_unit.upper() == "C":
        print(f"\n{temperature}°{original_unit} converted to °{converted_unit.upper()} = {k_to_c(temperature):.2f}°{converted_unit.upper()}")
    #F to C
    elif original_unit.upper() == "F" and converted_unit.upper() == "C":
        print(f"\n{temperature}°{original_unit} converted to °{converted_unit.upper()} = {f_to_c(temperature):.2f}°{converted_unit.upper()}")
    #F to K
    elif original_unit.upper() == "F" and converted_unit.upper() == "K":
        print(f"\n{temperature}°{original_unit} converted to °{converted_unit.upper()} = {f_to_k(temperature):.2f}°{converted_unit.upper()}")
    #K to F
    elif original_unit.upper() == "K" and converted_unit.upper() == "F":
        print(f"\n{temperature}°{original_unit} converted to °{converted_unit.upper()} = {k_to_f(temperature):.2f}°{converted_unit.upper()}")
    else:
        print("\n\033[1mERROR:\033[0m INVALID INPUT: Please enter: C for °C or F for °F")

main()