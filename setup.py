import argparse, subprocess
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument('year')
parser.add_argument('day')

args = parser.parse_args()

year = str(args.year)

if int(args.day) < 10:
    day = "0" + args.day
else:
    day = args.day

if not Path(f"./{year}").is_dir():
    subprocess.run(["mkdir", f"{year}"])

subprocess.run(["touch", f"./{year}/day{day}.py"])

if not Path(f"./{year}/data").is_dir():
    subprocess.run(["mkdir", f"./{year}/data"])

subprocess.run(["touch", f"./{year}/data/day{day}-a.txt"])
subprocess.run(["touch", f"./{year}/data/day{day}-b.txt"])
subprocess.run(["touch", f"./{year}/data/day{day}-c.txt"])
