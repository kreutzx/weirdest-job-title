import os

# Entry for the Weirdest Job Title blind judge showdown.
ENTRY_TEXT = "Chief Apology Officer, Production Incidents"


def main():
    os.makedirs("/output", exist_ok=True)
    output_path = "/output/entry.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
