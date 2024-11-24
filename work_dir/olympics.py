import argparse
from info_class import Info
from counters import count_total_medals, count_team_medals, get_overall, interactive_statistics
from file_worker import open_file, write_file

# test configs:
#     events.tsv -medals United States 1972
#     events.tsv -medals United States 1972 -output file.txt
#     events.tsv -total 1972 -output file.txt
#     events.tsv -overall Ukraine Ireland Canada
#     events.tsv -overall Ukraine Ireland Canada -output file.txt
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Ask for input file")
parser.add_argument("-medals", help="Ask for medals of team", nargs="+")
parser.add_argument("-output", help="Filename for output")
parser.add_argument("-total", help="Total stats for chosen year")
parser.add_argument("-overall", help="List countries to get information", nargs="+")
parser.add_argument("-interactive", help="Enter interactive mode", action="store_true")

args = parser.parse_args()

if not args.interactive:
    all_info = open_file(args)


def output():
    team_dict = None
    if args.total is not None:
        team_dict = {}
        for info in all_info:
            team_dict[info.team] = count_team_medals(all_info, info.team)
        for i in team_dict:
            print(team_dict[i])
    elif args.overall is not None:
        team_dict = {}
        for team in args.overall:
            team_dict[team] = get_overall(all_info, team)
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


if args.interactive:
    country = input("Enter team name or code: ")
    args.overall = country
    all_info = open_file(args)
    interactive_statistics(args, all_info, country)
else:
    output()
