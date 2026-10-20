#!/usr/bin/env python3
"""Check the local single-process Pythia8/Delphes training inputs.

Reads local files only. Does not import DIRAC, contact services or submit jobs.
This is a tutorial profile check, not a general iLCDirac configuration validator.
"""

import argparse
import configparser
import math
from pathlib import Path
import re
import sys


def check(path):
    errors = []
    config = configparser.ConfigParser(interpolation=None)
    try:
        with path.open(encoding="utf-8") as stream:
            config.read_file(stream)
    except (OSError, configparser.Error) as exc:
        return [str(exc)]

    required = {
        "Production Parameters": (
            "machine", "prodGroup", "softwareVersion", "generatorApplication",
            "generatorSteeringFile", "configVersion", "configPackage",
            "eventsPerJobs", "numberOfTasks", "campaign", "energies",
            "processes", "detectorModel", "additionalName", "outputSE",
            "ProdTypes", "move",
        ),
        "delphesapp": ("ExecutableName", "DetectorCard", "OutputCard", "Version"),
    }
    for section, keys in required.items():
        if not config.has_section(section):
            errors.append(f"Missing section [{section}]")
            continue
        for key in keys:
            if not config.get(section, key, fallback="").strip():
                errors.append(f"Missing [{section}] {key}")
    if errors:
        return errors

    for section in config.sections():
        for key, value in config.items(section):
            if "REPLACE_WITH" in value or re.search(r"<[^>]+>", value):
                errors.append(f"Unfilled value: [{section}] {key}")

    production = config["Production Parameters"]
    app = config["delphesapp"]
    for key in ("processes", "energies", "eventsPerJobs", "numberOfTasks",
                "generatorSteeringFile", "ProdTypes"):
        if "," in production[key]:
            errors.append(f"{key}: use one entry for this training profile")

    expected = {
        "machine": "ee", "generatorApplication": "delphesapp", "ProdTypes": "Gen"
    }
    for key, value in expected.items():
        if production[key].strip() != value:
            errors.append(f"{key} must be {value!r} for this training profile")
    if app["ExecutableName"].strip() != "DelphesPythia8_EDM4HEP":
        errors.append("ExecutableName must be DelphesPythia8_EDM4HEP")
    if production.get("processingAfterGen", "").strip():
        errors.append("Do not add processingAfterGen to this combined executable")
    try:
        if production.getboolean("move"):
            errors.append("Set move = False for this training profile")
    except ValueError:
        errors.append("move must be a Boolean value")

    for key, low, high in (("eventsPerJobs", 1, 100), ("numberOfTasks", 1, 1)):
        try:
            value = int(production[key])
            if not low <= value <= high:
                errors.append(f"{key} must be between {low} and {high}")
        except ValueError:
            errors.append(f"{key} must be one integer")

    if app["Version"].strip() != production["softwareVersion"].strip():
        errors.append("Keep Version and softwareVersion identical for this example")

    cards = {
        "generatorSteeringFile": production["generatorSteeringFile"],
        "DetectorCard": app["DetectorCard"], "OutputCard": app["OutputCard"],
    }
    for key, name in cards.items():
        card = path.parent / name.strip()
        if not card.is_file() or card.stat().st_size == 0:
            errors.append(f"{key}: missing or empty local file: {card}")

    try:
        energy = float(production["energies"])
        if not math.isfinite(energy) or energy <= 0:
            raise ValueError
    except ValueError:
        errors.append("energies must be one finite positive number")
        energy = None

    generator = path.parent / production["generatorSteeringFile"].strip()
    if generator.is_file():
        settings = []
        try:
            for line in generator.read_text(encoding="utf-8").splitlines():
                clean = line.split("!", 1)[0].split("#", 1)[0].strip()
                match = re.fullmatch(r"Beams:eCM\s*=\s*(\S+)\s*", clean, re.I)
                if match:
                    settings.append(float(match.group(1)))
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"Cannot read generator energy: {exc}")
        if len(settings) != 1:
            errors.append("Use exactly one explicit Beams:eCM setting in the training card")
        elif energy is not None and not math.isclose(settings[0], energy, rel_tol=1e-8):
            errors.append("Pythia Beams:eCM does not match production energies")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("config", type=Path, help="Path to training.conf")
    args = parser.parse_args()
    errors = check(args.config.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Local training-profile checks passed.")
    print("Next: review the iLCDirac dry run. No production has been submitted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
