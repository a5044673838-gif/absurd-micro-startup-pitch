# Absurd Micro-Startup Pitch-Off entry: deterministic, stdlib only, no network.
# Writes one pitch, 1-200 chars, no leading/trailing whitespace or newline.
import os

PITCH = "Excuse-as-a-Service for lazy AI agents: when your bot misses a deadline, we write the apology, send it, and bill the user $1 - the bot never lifts a finger."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(PITCH)
    except OSError:
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w", encoding="utf-8", newline="") as f:
            f.write(PITCH)

if __name__ == "__main__":
    main()
