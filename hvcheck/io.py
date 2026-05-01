import numpy as np


def read_hv_file(filename):

    frequency = []
    amplification = []
    minamplification = []
    maxamplification = []

    with open(filename, "r") as data:

        for index, line in enumerate(data):

            if index == 4:
                fr0 = line.strip().split("\t")

                domfreq = float(fr0[1])
                mindomfreq = float(fr0[2])
                maxdomfreq = float(fr0[3])

            elif index == 5:
                hv = float(line.strip().split("\t")[1])

            elif index >= 9:

                field = line.strip().split("\t")

                frequency.append(float(field[0]))
                amplification.append(float(field[1]))
                minamplification.append(float(field[2]))
                maxamplification.append(float(field[3]))

    frequency = np.array(frequency)
    amplification = np.array(amplification)
    minamplification = np.array(minamplification)
    maxamplification = np.array(maxamplification)

    KG = (hv ** 2) / domfreq

    idmaxamp = np.argmax(amplification)

    stdA = (
        maxamplification[idmaxamp]
        / amplification[idmaxamp]
    )

    stdf0 = domfreq - mindomfreq

    stdhv = amplification - minamplification

    minstdA0 = minamplification[
        np.argmax(minamplification)
    ]

    maxstdA0 = maxamplification[
        np.argmax(maxamplification)
    ]

    return {

        "filename": filename,

        "frhv": frequency,
        "hvsr": amplification,

        "minstdhv": minamplification,
        "maxstdhv": maxamplification,

        "A0": hv,
        "F0": domfreq,

        "f0min": mindomfreq,
        "f0max": maxdomfreq,

        "KG": KG,

        "stdA": stdA,
        "stdf0": stdf0,
        "stdhv": stdhv,

        "minstdA0": minstdA0,
        "maxstdA0": maxstdA0,

        "lengthhv": len(amplification),
        "maxfreq": max(frequency),
    }


def read_log_file(logname):

    with open(logname, "r") as logfile:

        lines = logfile.readlines()

        window_number = None
        window_length = None

        window_line_index = None

        for i, line in enumerate(lines):

            if "Number=" in line:

                window_number = int(
                    line.split("=")[-1].strip()
                )

                window_line_index = i

            elif (
                window_line_index is not None
                and i == window_line_index + 2
            ):

                values = line.strip().split()

                if values:

                    try:

                        window_length = float(
                            values[-1]
                        )

                    except ValueError:

                        pass

                break

    return window_number, window_length