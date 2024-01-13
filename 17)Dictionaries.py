# dectionary is contains keys & values

MonthConversions={
    "jan":"January",
    "feb":"February",
    "mar":"March",
    "apr":"April",
    "may":"May",
    "jun":"June",
    "jul":"July",
    "aug":"August",
    "sep":"September",
    "oct":"October",
    "nov":"November",
    "dec":"December"
}

# How to access these dictionories
print(MonthConversions["nov"])
print(MonthConversions["may"])
print(MonthConversions.get("dec"))
print(MonthConversions.get("luv"))
print(MonthConversions.get("luv","Not a valid key"))

#You can also use numbers as key in dictionory
'''
MonthConversions={
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}
'''