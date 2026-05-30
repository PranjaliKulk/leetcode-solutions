def timeReqToBuyTickets(ticktes, k):
    time = 0 #to count total seconds

    for i in range(len(ticktes)):
        if i <=k:
            time += min(ticktes[i], ticktes[k])
        else:
            time += min(ticktes[i], ticktes[k] - 1)
    return time