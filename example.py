from main import WatchLaterList

wl = WatchLaterList()
wl.add("v1", "Python Tutorial")
wl.add("v2", "React Basics")
wl.add("v1", "Python Tutorial")  # Should move to top again
wl.add("v3", "Data Structures")
wl.print_list()

wl.remove_by_index(1)
wl.print_list()

"""
Output:

Watch Later List:
0: [v3] Data Structures
1: [v1] Python Tutorial
2: [v2] React Basics
------------------------------
Watch Later List:
0: [v3] Data Structures
1: [v2] React Basics
------------------------------
"""
