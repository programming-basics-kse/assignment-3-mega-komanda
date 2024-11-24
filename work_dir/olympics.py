import argparse
from info_class import Info

# test configs:
#     events.tsv -medals United States 1972
#     events.tsv -medals United States 1972 -output file.txt
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Ask for input file")
parser.add_argument("-medals", help="Ask for medals of team", nargs="+")
parser.add_argument("-output", help="Filename for output")

args = parser.parse_args()


all_info = []
with open(args.filename, "r") as file:
    next(file)
    for line in file:
        s = line.split("\t")
        team_search = " ".join(args.medals[:-1])
        year_search = args.medals[-1]

        if (team_search in s[6] or team_search in s[7]) and year_search == s[9] and s[14] != "NA\n":
            all_info.append(Info(s[0], s[1], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14][:-1]))

    all_info.sort(key=lambda x: x.medal_to_num())

def count_total_medals():
    medal_count = {
        "Gold": 0,
        "Silver": 0,
        "Bronze": 0
    }
    for i in all_info:
        medal_count[i.medal14] += 1
    return f"\n Gold: {medal_count["Gold"]}\n Silver: {medal_count["Silver"]}\n Bronze: {medal_count["Bronze"]}"

def output(to_file=False):
    if len(all_info) == 0:
        print(f"There is no information about {" ".join(args.medals[:-1])} in {args.medals[-1]}")
        return
    elif len(all_info) < 10:
        for el in all_info:
            print(el.return_stat())
    else:
        for i in range(10):
            print(all_info[i].return_stat())
    print(count_total_medals())

    if to_file:
        with open(args.output, "w") as file:
            file.write(f"{" ".join(args.medals[:-1])} {args.medals[-1]}\n\n")
            if len(all_info) < 10:
                for el in all_info:
                    file.write(el.return_stat() + "\n")
            else:
                for i in range(10):
                    file.write(all_info[i].return_stat() + "\n")
            file.write(count_total_medals())


output(args.output is not None)
# print(*all_info)
