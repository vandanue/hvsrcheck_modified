import numpy as np

def epsilon_f0(F0):

    if F0 < 0.2:
        return 0.25 * F0
    elif F0 < 0.5:
        return 0.2 * F0
    elif F0 < 1.0:
        return 0.15 * F0
    elif F0 < 2.0:
        return 0.10 * F0
    else:
        return 0.05 * F0


def theta_f0(F0):

    if F0 < 0.2:
        return 0.3
    elif F0 < 0.5:
        return 2.5
    elif F0 < 1.0:
        return 2.0
    elif F0 < 2.0:
        return 1.78
    else:
        return 1.58


def print_report(data, results):

    print("\n\n\n-----------------------------------------------------------------------")
    print(f"File Name\t\t: {data['filename']}")
    print("-----------------------------------------------------------------------")

    print("\nCRITERIA FOR A RELIABLE H/V CURVE")

    print(
        "RELIABLE 1:",
        "OK" if results["reliable_1"] else f"NO, f_0 < 10/l_w ({data["F0"]} < 10/{data["winlength"]})"
    )

    print(
        "RELIABLE 2:",
        "OK" if results["reliable_2"] else f"NO, n_c(f_0) < 200 ({data["winlength"]*data["window"]*data["F0"]} < 200)"
    )

    print(
        "RELIABLE 3:",
        "OK" if results["reliable_3"] else "NO, \u03C3 H/V(f) > 2"
    )

    print("\nCLEAR PEAK SUMMARY:",
          results["clear_count"],
          "out of 6")

    if results["is_clear_peak"]:
        print("H/V IS CLEAR PEAK")
    else:
        print("H/V IS NOT CLEAR PEAK")


def all_output(data, results):
    print("\n\n-----------------------------------------------------------------------")

    print(f"{data['filename']} OUTPUT")

    print(
        "RELIABLE 1:",
        f"{data["F0"]} {'>' if results["reliable_1"] else '<'} 10/l_w"
    )
    
    print(
        "RELIABLE 2:",
        f"{data["winlength"]*data["window"]*data["F0"]} {'>' if results["nc"] else '<'} 200"
    )

    print(
        "RELIABLE 3:",
        # f"{'\u03C3 H/V(f) > 2' if data["frhv"] > 0.5 * data["F0"] else }"
        f"\u03C3 H/V(f) {'<' if results["reliable_3"] else '>'} 2"
    )

    # Add all the clear peak output later