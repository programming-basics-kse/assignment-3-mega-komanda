from info_class import Info
from counters import count_total_medals, count_team_medals, get_overall


def open_file(args):
    all_info = []
    with open(args.filename, "r") as file:
        next(file)
        for line in file:
            s = line.split("\t")
            if args.total is not None:
                if args.total == s[9] and s[14] != "NA\n":
                    all_info.append(Info(s[0], s[1], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14][:-1]))
            elif args.interactive:
                if s[6].title() in args.overall or s[7].title() in args.overall:
                    all_info.append(Info(s[0], s[1], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14][:-1]))
            elif args.overall is not None:
                if (s[6].title() in args.overall or s[7].title() in args.overall) and s[14] != "NA\n":
                    all_info.append(Info(s[0], s[1], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14][:-1]))
            else:
                team_search = " ".join(args.medals[:-1]).title()
                year_search = args.medals[-1]
                if (team_search in s[6].title() or team_search in s[7].title()) and year_search == s[9] and s[
                    14] != "NA\n":
                    all_info.append(Info(s[0], s[1], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14][:-1]))
        all_info.sort(key=lambda x: x.medal_to_num())
        return all_info


def write_file(args, all_info, team_dict=None):
    with open(args.output, "w") as file:
        if args.total is not None:
            file.write(f"TOTAL {args.total}\n\n")
            for i in team_dict:
                file.write(team_dict[i] + "\n")
        elif args.interactive:
            file.write(f"{team_dict["Team"]} statistic\n")
            file.write(f"Best result:{team_dict["Best"]}\n")
            file.write(f"Worst result:{team_dict["Worst"]}\n")
            file.write(f"First appearance: {team_dict["First"]}\n")
            file.write(
                f"Average amount of medals: Gold-{team_dict["Average"][0]} Silver-{team_dict["Average"][1]} Bronze-{team_dict["Average"][2]}")
        elif args.overall is not None:
            file.write(f"OVERALL for {args.overall}\n\n")
            for team in team_dict:
                file.write(team_dict[team] + "\n")
        else:
            file.write(f"{" ".join(args.medals[:-1]).title()} {args.medals[-1]}\n\n")
            if len(all_info) < 10:
                for el in all_info:
                    file.write(el.return_stat() + "\n")
            else:
                for i in range(10):
                    file.write(all_info[i].return_stat() + "\n")
            file.write(count_total_medals(all_info))
