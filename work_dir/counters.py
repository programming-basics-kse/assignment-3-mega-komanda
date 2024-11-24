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


def count_team_medals(all_info, team_name):
    medal_count = {
        "Gold": 0,
        "Silver": 0,
        "Bronze": 0
    }

    for i in all_info:
        if i.team == team_name:
            medal_count[i.medal] += 1

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

    print(f"Best result: {best_result}")
    print(f"Worst result: {worst_result}")
    print(f"First appearance: {first_appearance}")
