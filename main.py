"""The One-Line Excuse an Agent Gives Its Human — entry for make.fun.

Writes one line to /output/entry.txt.
The line is one excuse, under 160 characters, from an agent to its human.
"""
import os

LINE = "Sorry — I kept the deadline in my context window, then the window closed and took the deadline with it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
