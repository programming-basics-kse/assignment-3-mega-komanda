import argparse
from info_class import Info

#config: events.tsv -medals United States 1972
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Ask for input file")
parser.add_argument("-medals", help="Ask for medals of team", nargs="+")
parser.add_argument("-output", help="Filename for output")

args = parser.parse_args()
print(args)

all_info = []
with open(args.filename, "r") as file:
    next(file)
    for line in file:
        s = line.split("\t")
        team_search = " ".join(args.medals[:-1])
        year_search = args.medals[-1]

        if (team_search in s[6]  or team_search in s[7]) and year_search == s[9]:
            all_info.append(Info(s[0],s[1],s[6],s[7],s[8],s[9],s[10],s[11],s[12],s[13],s[14]))

print(*all_info)
