if __name__ == '__main__':
    # for graph, check out ../Self Covering (Greedy).png
    states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az', 'az'}

    stations = {}
    stations['kone'] = {'id', 'nv', 'ut'}
    stations['ktwo'] = {'wa', 'id', 'mt'}
    stations['kthree'] = {'or', 'nv', 'ca'}
    stations['kfour'] = {'nv', 'ut'}
    stations['kfive'] = {'ca', 'az'}

    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        final_stations.add(best_station)

    print(final_stations)
    print(states_needed)
    print(stations)
    # kfour is not in the final_stations set ebecause it is not covered by any of the final_stations
    print(final_stations == {'kone', 'ktwo', 'kthree', 'kfive'}) # True
