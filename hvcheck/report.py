import numpy as np
import pandas as pd
import os

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

    print("CRITERIA FOR A RELIABLE H/V CURVE")

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
    print("\n-----------------------------------------------------------------------")
    print("RELIABILITY OUTPUT")

    print(
        "RELIABLE 1:",
        f"{'CRITERIA FULFILLED' if results["reliable_1"] else 'CRITERIA NOT FULFILLED'} \t\t\t ",
        f"{data["F0"]:.2f} {'>' if results["reliable_1"] else '<'} {10/data["winlength"]}"
    )
    
    print(
        "RELIABLE 2:",
        f"{'CRITERIA FULFILLED' if results["reliable_2"] else 'CRITERIA NOT FULFILLED'} \t\t\t ",
        f"{data["winlength"]*data["window"]*data["F0"]:.2f} {'>' if results["nc"] else '<'} 200"
    )

    print(
        "RELIABLE 3:",
        f"{'CRITERIA FULFILLED' if results["reliable_3"] else 'CRITERIA NOT FULFILLED'} \t\t\t ",
        f"{data["stdhv"][0]:.2f} {'<' if results["reliable_3"] else '>'} 2"
    )
    
    print("\nCLEAR PEAK OUTPUT")
    
    idfr1 = np.where(
        (data["frhv"] >= data["F0"] / 4)
        & (data["frhv"] <= data["F0"])
    )[0]

    idfr2 = np.where(
        (data["frhv"] >= data["F0"])
        & (data["frhv"] <= 4 * data["F0"])
    )[0]
    
    print(
        "CLEAR PEAK 1:", 
        f"{'CRITERIA FULFILLED' if np.any(data["hvsr"][idfr1] < data["A0"]/2) else 'CRITERIA NOT FULFILLED'} \t\t ",
        f"A_H/V(f\u207b) {'<' if data["A0"]/2 else '>'} {(data["A0"]/2):.2f}"
    )

    print(
        "CLEAR PEAK 2:",
        f"{'CRITERIA FULFILLED' if np.any(data["hvsr"][idfr2] < data["A0"]/2) else 'CRITERIA NOT FULFILLED'} \t\t ",
        f"A_H/V(f\u207a) {'<' if data["A0"]/2 else '>'} {(data["A0"]/2):.2f}"
    )

    print(
        "CLEAR PEAK 3:",
        f"{'CRITERIA FULFILLED' if data["A0"] > 2 else  "CRITERIA NOT FULFILLED"} \t\t ",
        f"{data["A0"]:.2f} {'>' if data["A0"] > 2 else '<'} 2"
    )

    print(
        "CLEAR PEAK 4:",
        f"{'CRITERIA FULFILLED' if results["clear_4"] else 'CRITERIA NOT FULFILLED'} \t\t ",
        f"f_0 {'±' if results["clear_4"] else 'GREATER THAN'} 5%"
    )

    print(
        "CLEAR PEAK 5:",
        f"{'CRITERIA FULFILLED' if results["clear_5"] else 'CRITERIA NOT FULFILLED'} \t\t ",
        f"{data['stdf0']:.2f} {'<' if data["stdf0"] < epsilon_f0(data["F0"]) else '>'} {epsilon_f0(data["F0"]):.2f}"
    )

    print(
        "CLEAR PEAK 6:",
        f"{'CRITERIA FULFILLED' if results["clear_6"] else 'CRITERIA NOT FULFILLED'} \t\t ",
        f"{data["stdA"]:.2f} {'<' if data["stdA"] < theta_f0(data["F0"]) else '>'} {theta_f0(data["F0"]):.2f}"
    )

    print("-----------------------------------------------------------------------")

def save_csv(data, results):
    names = data["filename"]
    reliable = results["reliable_1"], results["reliable_2"], results["reliable_3"]
    clear = results["clear_1"], results["clear_2"], results["clear_3"], results["clear_4"], results["clear_5"], results["clear_6"]

    row = {
        "FILENAME": names,
        "RELIABLE 1": reliable[0],
        "RELIABLE 2": reliable[1],
        "RELIABLE 3": reliable[2],
        "CLEAR PEAK 1": clear[0],
        "CLEAR PEAK 2": clear[1],
        "CLEAR PEAK 3": clear[2],
        "CLEAR PEAK 4": clear[3],
        "CLEAR PEAK 5": clear[4],
        "CLEAR PEAK 6": clear[5]
    }

    df = pd.DataFrame([row])

    df.to_csv("sesame_criteria.csv", mode="a", index=False, header=not os.path.exists("sesame_criteria.csv"))

    # output = [names] + list(reliable) + list(clear)
