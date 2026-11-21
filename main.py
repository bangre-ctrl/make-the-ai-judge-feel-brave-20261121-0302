"""Write one original short relaxing text to /output/entry.txt.
Deterministic: the same text on every run."""
import os

TEXT = (
    "You read one page, then another.\n"
    "The lamp does not hurry.\n"
    "Outside, the street grows quiet, one footstep at a time.\n"
    "There is nothing to chase.\n"
    "Only the next line, waiting where you left it, warm as a held cup.\n"
)

out_dir = "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
