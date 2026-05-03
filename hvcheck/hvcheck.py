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


def hvsrcheck(data):

    results = {}

    # -------------------------
    # RELIABLE CRITERIA
    # -------------------------

    r1 = data["F0"] > (10 / data["winlength"])

    nc = (
        data["winlength"]
        * data["window"]
        * data["F0"]
    )

    r2 = nc > 200

    idfr1 = np.where(
        data["frhv"] > 0.5 * data["F0"]
    )[0]

    idfr2 = np.where(
        data["frhv"] < 0.5 * data["F0"]
    )[0]

    r31 = (
        np.all(data["stdhv"][idfr1] < 2)
        if len(idfr1) > 0 else False
    )

    r32 = (
        np.all(data["stdhv"][idfr2] < 3)
        if len(idfr2) > 0 else False
    )

    r3 = r31 and r32

    results["reliable_1"] = r1
    results["reliable_2"] = r2
    results["reliable_3"] = r3
    results["nc"] = nc

    # -------------------------
    # CLEAR PEAK
    # -------------------------

    clear = []

    idfr1 = np.where(
        (data["frhv"] >= data["F0"] / 4)
        & (data["frhv"] <= data["F0"])
    )[0]

    cp1 = (
        len(idfr1) > 0
        and np.any(
            data["hvsr"][idfr1]
            < data["A0"] / 2
        )
    )

    clear.append(cp1)

    idfr2 = np.where(
        (data["frhv"] >= data["F0"])
        & (data["frhv"] <= 4 * data["F0"])
    )[0]

    cp2 = (
        len(idfr2) > 0
        and np.any(
            data["hvsr"][idfr2]
            < data["A0"] / 2
        )
    )

    clear.append(cp2)

    cp3 = data["A0"] > 2

    clear.append(cp3)

    F0min = data["F0"] * 0.95
    F0max = data["F0"] * 1.05

    idmin = np.argmax(data["minstdhv"])
    idmax = np.argmax(data["maxstdhv"])

    cp4 = (
        F0min <= data["frhv"][idmin] <= F0max
        and
        F0min <= data["frhv"][idmax] <= F0max
    )

    clear.append(cp4)

    eps = epsilon_f0(data["F0"])

    cp5 = data["stdf0"] < eps

    clear.append(cp5)

    theta = theta_f0(data["F0"])

    cp6 = data["stdA"] < theta

    clear.append(cp6)

    results["clear_count"] = int(sum(clear))
    results["is_clear_peak"] = int(sum(clear)) >= 5
    results["clear_vector"] = clear

    return results