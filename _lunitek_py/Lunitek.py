## -*- coding: utf-8 -*-
"""
Class for reading and writing Acoustic Emission .evt files from Lunitek.

Created on Sun Dec 28 02:48:00 2025

@author: pmmontanari (pmmontanari@proton.me)
"""

## --- User packages ---
import pandas as pd
from pathlib import Path
from datetime import datetime as dt
import json
import h5py

from dataclasses import dataclass, fields
from typing import Self

@dataclass
class Lunitek:
    """Class for reading and writing Acoustic Emission .evt files from Lunitek"""

    FILE: str = None
    TIMESTAMP_OF_FIRST_SIGNAL: str = None
    DATA: pd.DataFrame = None

    def read_evt(self, FILE) -> Self:
        """_summary_

        Args:
            FILE (_type_): _description_

        Returns:
            Self: _description_
        """
        ## Read lines and drop comments
        with open(Path(FILE).resolve(), "r") as input_file:
            lines = [
                line.rstrip().replace("CH", "").split(" ")
                for line in input_file.readlines()
                if not (line.startswith("#"))
            ]
        FILE = Path(FILE).name

        ## Put data into a DataFrame
        NAMES = [
            "channel",
            "tin_s_unix",
            "tout_s_unix",
            "amplitude_mV",
            "noscillations",
            "energy_au",
        ]  # au = arbitrary units
        DATA = pd.DataFrame(lines, columns=NAMES)

        ## Specify data formats
        DATA["channel"] = DATA["channel"].astype("uint8")
        DATA["tin_s_unix"] = DATA["tin_s_unix"].astype("float64")
        DATA["tout_s_unix"] = DATA["tout_s_unix"].astype("float64")
        DATA["amplitude_mV"] = DATA["amplitude_mV"].astype("float64")
        DATA["noscillations"] = DATA["noscillations"].astype("uint8")
        DATA["energy_au"] = DATA["energy_au"].astype("float64")

        ## Calculate signal duration and frequency
        DATA["duration_s"] = DATA["tout_s_unix"] - DATA["tin_s_unix"]
        DATA["frequency_kHz"] = (DATA["noscillations"] / DATA["duration_s"]) / 1000

        ## Drop unneeded columns and reorder columns
        DATA = DATA.drop(["tout_s_unix"], axis=1)

        DATA = DATA[
            [
                "channel",
                "tin_s_unix",
                "duration_s",
                "amplitude_mV",
                "frequency_kHz",
                "noscillations",
                "energy_au",
            ]
        ]

        ## Get file date and timestamp of first AE signal
        FIRST_TIMESTAMP = dt.fromtimestamp(DATA["tin_s_unix"].iloc[0])

        ## Note: Windows has a different behavior of strftime compared to
        # unix. The same string could be formatted using
        # '%Y-%m-%d %H:%M:%S.%6N %Z' on unix systems, however
        # "%N" is not valid on Windows. We are thus hardcoding this
        # format to prevent issues.
        microsecond = str(FIRST_TIMESTAMP.microsecond)
        FIRST_TIMESTAMP = FIRST_TIMESTAMP.strftime("%Y-%m-%d %H:%M:%S")
        FIRST_TIMESTAMP = FIRST_TIMESTAMP + "." + microsecond + " UTC"

        self.FILE = FILE
        self.TIMESTAMP_OF_FIRST_SIGNAL = FIRST_TIMESTAMP
        self.DATA = DATA
        return self

    def save_to_json(self, filename) -> None:
        """_summary_

        Args:
            filename (_type_): _description_. Defaults to None.
        """
        with open(filename, "w") as f:
            DATA = self.DATA.to_json(orient="columns")
            to_dump = {field.name: getattr(self, field.name) for field in fields(self)}
            to_dump["DATA"] = DATA
            json.dump(to_dump, f)
        return

    def save_to_h5(self, filename=None) -> None:
        """_summary_

        Args:
            filename (_type_, optional): _description_. Defaults to None.
        """
        if filename is None:
            filename = Path(self.FILE).stem + ".h5"

        with h5py.File(filename, "w") as f:
            f.create_dataset("channel", data=self.DATA["channel"])
            f.create_dataset("tin_s_unix", data=self.DATA["tin_s_unix"])
            f.create_dataset("duration_s", data=self.DATA["duration_s"])
            f.create_dataset("frequency_kHz", data=self.DATA["frequency_kHz"])
            f.create_dataset("n_oscillations", data=self.DATA["noscillations"])
            f.create_dataset("energy_au", data=self.DATA["energy_au"])
            f.attrs["FILE"] = self.FILE
            f.attrs["FIRST_TIMESTAMP"] = self.TIMESTAMP_OF_FIRST_SIGNAL
        return


def main() -> None:
    return


if __name__ == "__main__":
    main()
