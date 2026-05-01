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

    print("-----------------------------------------------------------------------")
    print(f"File Name\t\t: {data['filename']}")
    print("-----------------------------------------------------------------------")

    print("CRITERIA FOR A RELIABLE H/V CURVE")

    print(
        "RELIABLE 1:",
        "OK" if results["reliable_1"] else "NO"
    )

    print(
        "RELIABLE 2:",
        "OK" if results["reliable_2"] else "NO"
    )

    print(
        "RELIABLE 3:",
        "OK" if results["reliable_3"] else "NO"
    )

    print("\nCLEAR PEAK SUMMARY:",
          results["clear_count"],
          "out of 6")

    if results["is_clear_peak"]:
        print("H/V IS CLEAR PEAK")
    else:
        print("H/V IS NOT CLEAR PEAK")