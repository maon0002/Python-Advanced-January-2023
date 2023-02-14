def add_songs(*args):
    # print(args)
    songs_dict = {}
    for i in range(len(args)):
        pair = args[i]
        title = pair[0]
        lyr = pair[1]
        if title not in songs_dict.keys():
            songs_dict[title] = []
        songs_dict[title].append(lyr)
    # print(songs_dict)
    final_list = []
    for x, y in songs_dict.items():
        title_to_append = f"- {x}"
        final_list.append(title_to_append)
        for line in y:
            if line:
                for l in line:
                    line_to_append = f"{l}"
                    final_list.append(line_to_append)

    return "\n".join(final_list)


#
# print(add_songs(
#     ("Bohemian Rhapsody", []),
#     ("Just in Time",
#      ["Just in time, I found you just in time",
#       "Before you came, my time was running low",
#       "I was lost, the losing dice were tossed",
#       "My bridges all were crossed, nowhere to go"])
# ))


# print(add_songs(
#     ("Beat It", []),
#     ("Beat It",
#      ["Just beat it (beat it), beat it (beat it)",
#       "No one wants to be defeated"]),
#     ("Beat It", []),
#     ("Beat It",
#      ["Showin' how funky and strong is your fight",
#       "It doesn't matter who's wrong or right"]),
# ))


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
