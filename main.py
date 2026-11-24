"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather for the invented city of Dribbleford to
/output/entry.txt: light rain, then sunshine, and a bus that is late
anyway. Standard library only, no network, deterministic output.
"""

from pathlib import Path

FORECAST = (
    "In Dribbleford, light rain until nine, then sunshine \u2014 "
    "the 8:15 is late again, but at least the weather turned up on time."
)

MAX_CHARS = 140

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if len(FORECAST) > MAX_CHARS:
        raise ValueError(
            f"forecast is {len(FORECAST)} characters, over the {MAX_CHARS} limit"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(FORECAST, encoding="utf-8")


if __name__ == "__main__":
    main()
