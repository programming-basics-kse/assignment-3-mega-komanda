from info_class import Info


def count_total_medals(all_info):
    medal_count = {
        "Gold": 0,
        "Silver": 0,
        "Bronze": 0
    }
    for i in all_info:
        medal_count[i.medal] += 1
    return f"\n Gold: {medal_count["Gold"]}\n Silver: {medal_count["Silver"]}\n Bronze: {medal_count["Bronze"]}"


def count_team_medals(all_info, team_name, return_dict=False):
    medal_count = {
        "Gold": 0,
        "Silver": 0,
        "Bronze": 0,
        "NA": 0
    }

    for i in all_info:
        if i.team.lower() == team_name.lower() or i.NOC.lower() == team_name.lower():
            medal_count[i.medal] += 1
    if return_dict:
        return medal_count
    else:
        return f"{team_name}: Gold-{medal_count["Gold"]} Silver-{medal_count["Silver"]} Bronze-{medal_count["Bronze"]}"


def get_overall(all_info, team_name, best_result=True):
    year_dict = dict()
    for i in all_info:
        if i.team.lower() == team_name.lower() or i.NOC.lower() == team_name.lower():
            year_dict[i.year] = 1 if not year_dict.get(i.year) else year_dict.get(i.year) + 1
    if best_result:
        max_medals = [0, 0]
        for year in year_dict:
            if year_dict[year] > max_medals[1]:
                max_medals[0] = year
                max_medals[1] = year_dict[year]
        return f"{team_name}: {max_medals[1]} medals in {max_medals[0]}"
    else:
        min_medals = [None, None]
        for year in year_dict:
            if not min_medals[0] or year_dict[year] < min_medals[1]:
                min_medals[0] = year
                min_medals[1] = year_dict[year]
        return f"{team_name}: {min_medals[1]} medals in {min_medals[0]}"


def interactive_statistics(args, all_info, country):
    worst_result = get_overall(all_info, country, False)
    best_result = get_overall(all_info, country)
    first_appearance = None
    for i in all_info:
        if not first_appearance:
            first_appearance = i.year
        else:
            if i.year < first_appearance:
                first_appearance = i.year
    all_participation = set()
    for i in all_info:
        all_participation.add(i.year)
    all_participation = len(all_participation)
    if all_participation > 0:
        all_medals = count_team_medals(all_info, country, True)
        for medal in all_medals:
            all_medals[medal] //= all_participation

        print(f"Best result:{best_result.split(":")[1]}")
        print(f"Worst result:{worst_result.split(":")[1]}")
        print(f"First appearance: {first_appearance}")
        print(
            f"Average amount of medals: Gold-{all_medals["Gold"]} Silver-{all_medals["Silver"]} Bronze-{all_medals["Bronze"]}")
        res_dict = {
            "Team": country,
            "Best": best_result.split(":")[1],
            "Worst": worst_result.split(":")[1],
            "First": first_appearance,
            "Average": [all_medals["Gold"], all_medals["Silver"], all_medals["Bronze"]]
        }
        return res_dict
    else:
        print("There is no information about this team")
