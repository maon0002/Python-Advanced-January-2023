def add_songs(*args):
    titles = set(f"- {x[0]}" for x in args)
    # print(songs_dict)
    songs_dict = dict()
    for item in args:
        title = f"- {args[0]}"
        lyr = f"{args[1]}"
        if title not in songs_dict.keys():
            songs_dict[title] = ""
        songs_dict[title] += lyr

    print(songs_dict)



    # return "\n".join(final_list)


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



#
# def add_songs(*args):
#     titles_tuple = list(x[0] for x in args)
#     print(titles_tuple)
#     final_list = []
#     titles = []
#
#     for i in range(len(args)):
#         title = args[i][0]
#         lyrics = args[i][1]
#         title_to_append = f"- {title}"
#
#         if title_to_append not in titles:
#             final_list.append(title_to_append)
#             titles.append(title_to_append)
#         else:
#             for line in lyrics:
#                 line_to_append = f"{line}"
#                 final_list.append(line_to_append)
#
#
#
#     return "\n".join(final_list)