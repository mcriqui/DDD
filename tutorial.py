for x in range(1,23):
    print '=IMPORTHTML("http://en.wikipedia.org/wiki/List_of_Diners,_Drive-Ins,_and_Dives_episodes", "table", {0})'.format(x)