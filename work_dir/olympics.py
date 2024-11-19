import argparse
from info_class import Info

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Ask for input file")
parser.add_argument("-medals", help="Ask for medals of team")

args = parser.parse_args()

all_info = []
with open(args.filename, "r") as file:
    next(file)
    for line in file:
        s = line.split("\t")
        check1 = f"{s[6]} {s[9]}"
        check2 = f"{s[7]} {s[9]}"
        if args.medals == check1  or args.medals == check2:
            all_info.append(Info(s[0],s[1],s[6],s[7],s[8],s[9],s[10],s[11],s[12],s[13],s[14]))

print(*all_info)
