from info_class import Info
def open_file(args):
    all_info = []
    with open(args.filename, "r") as file:
        next(file)
        for line in file:
            s = line.split("\t")
            if args.total is None:
                team_search = " ".join(args.medals[:-1]).lower()
                year_search = args.medals[-1]
                if (team_search in s[6].lower() or team_search in s[7].lower()) and year_search == s[9] and s[14] != "NA\n":
                    all_info.append(Info(s[0], s[1], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14][:-1]))
            else:
                if args.total == s[9] and s[14] != "NA\n":
                    all_info.append(Info(s[0], s[1], s[6], s[7], s[8], s[9], s[10], s[11], s[12], s[13], s[14][:-1]))
        all_info.sort(key=lambda x: x.medal_to_num())
        return all_info

def count_total_medals(all_info):
    medal_count = {
        "Gold": 0,
        "Silver": 0,
        "Bronze": 0
    }
    for i in all_info:
        medal_count[i.medal14] += 1
    return f"\n Gold: {medal_count["Gold"]}\n Silver: {medal_count["Silver"]}\n Bronze: {medal_count["Bronze"]}"

def count_team_medals(all_info, team_name):
    medal_count = {
        "Gold": 0,
        "Silver": 0,
        "Bronze": 0
    }

    for i in all_info:
        if i.team6 == team_name:
            medal_count[i.medal14] += 1

    return f"{team_name}: Gold-{medal_count["Gold"]} Silver-{medal_count["Silver"]} Bronze-{medal_count["Bronze"]}"

def write_file(args, all_info, total_dict=None):
    with open(args.output, "w") as file:
        if total_dict:
            file.write(f"TOTAL {args.total}\n\n")
            for i in total_dict:
                file.write(total_dict[i]+"\n")
        else:
            file.write(f"{" ".join(args.medals[:-1]).upper()} {args.medals[-1]}\n\n")
            if len(all_info) < 10:
                for el in all_info:
                    file.write(el.return_stat() + "\n")
            else:
                for i in range(10):
                    file.write(all_info[i].return_stat() + "\n")
            file.write(count_total_medals(all_info))
