def students_credits(*args):
    diyans_dict = {}
    courses_tracker = []
    MIN_CREDITS_FOR_DIPLOMA = 240
    for i in range(len(args)):
        string_ = args[i].split("-")
        course_name, credits_, max_test_points, points_of_diyan = string_
        if course_name not in diyans_dict.keys():
            diyans_dict[course_name] = 0
        diyans_dict[course_name] = (int(points_of_diyan) / int(max_test_points)) * int(credits_)
        courses_tracker.append(string_)
        # print(string_)
        # print(diyans_dict)

    total_credits = sum([n for n in diyans_dict.values()])
    have_enough_credits = total_credits >= MIN_CREDITS_FOR_DIPLOMA
    sorted_dict = list(sorted(diyans_dict.items(), key=lambda x: x[1]))

    # print(sorted_dict)

    if have_enough_credits:
        sorted_dict.append(f'Diyan gets a diploma with {total_credits:.1f} credits.')

    else:
        sorted_dict.append(f"Diyan needs {MIN_CREDITS_FOR_DIPLOMA - total_credits:.1f} credits more for a diploma.")
    print(sorted_dict)
    result = []
    for x in sorted_dict:
        if len(x) > 2:
            result.append(x)
        else:
            string_to_append = f"{x[0]} - {x[1]:.1f}"
            result.append(string_to_append)

    return "\n".join(result[::-1])


# print(total_credits)
# print(MIN_CREDITS_FOR_DIPLOMA - total_credits)


#
# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
