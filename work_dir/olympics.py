import argparse
from info_class import Info
from secondary_funcs import open_file, count_total_medals, write_file, count_team_medals

# test configs:
#     events.tsv -medals United States 1972
#     events.tsv -medals United States 1972 -output file.txt
#     events.tsv -total 1972 -output file.txt
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Ask for input file")
parser.add_argument("-medals", help="Ask for medals of team", nargs="+")
parser.add_argument("-output", help="Filename for output")
parser.add_argument("-total", help="Total stats for chosen year")

args = parser.parse_args()

all_info = open_file(args)

def output():
    team_dict = None
    if args.total is not None:
        team_dict = {}
        for info in all_info:
            team_dict[info.team6] = count_team_medals(all_info,info.team6)
        for i in team_dict:
            print(team_dict[i])

    else:
        if len(all_info) == 0:
            print(f"There is no information about {" ".join(args.medals[:-1])} in {args.medals[-1]}")
            return
        elif len(all_info) < 10:
            for el in all_info:
                print(el.return_stat())
        else:
            for i in range(10):
                print(all_info[i].return_stat())
        print(count_total_medals(all_info))

    if args.output is not None:
        write_file(args, all_info, team_dict)


output()
# print(*all_info)
