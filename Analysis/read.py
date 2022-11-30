# For reading txt files

# # UCS Solution Path Length
# with open('ucs_merged.txt', "r") as myfile:
#     for myline in myfile:
#         if "Solution Path Length: " in myline:
#             print(myline.rstrip("\n"))

# # UCS Search Path Length
# with open('ucs_merged.txt', "r") as myfile:
#     for myline in myfile:
#         if "Search Path Length: " in myline:
#             print(myline.rstrip("\n"))

# # UCS Runtime
# with open('ucs_merged.txt', "r") as myfile:
#     for myline in myfile:
#         if "Runtime: " in myline:
#             print(myline.rstrip("\n"))

# # GBFS Solution Path Length
# with open('gbfs_merged.txt', "r") as myfile:
#     for myline in myfile:
#         if "Solution Path Length: " in myline:
#             print(myline.rstrip("\n"))
#
# # GBFS Search Path Length
# with open('gbfs_merged.txt', "r") as myfile:
#     for myline in myfile:
#         if "Search Path Length: " in myline:
#             print(myline.rstrip("\n"))
#
# # GBFS Runtime
# with open('gbfs_merged.txt', "r") as myfile:
#     for myline in myfile:
#         if "Runtime: " in myline:
#             print(myline.rstrip("\n"))

# A/A* Solution Path Length
with open('astar_merged.txt', "r") as myfile:
    for myline in myfile:
        if "Solution Path Length: " in myline:
            print(myline.rstrip("\n"))

# A/A* Search Path Length
with open('astar_merged.txt', "r") as myfile:
    for myline in myfile:
        if "Search Path Length: " in myline:
            print(myline.rstrip("\n"))

# A/A* Runtime
with open('astar_merged.txt', "r") as myfile:
    for myline in myfile:
        if "Runtime: " in myline:
            print(myline.rstrip("\n"))