if __name__ == '__main__':
    #            GRAPH                  | From  | To  |Cost|
    #                                   |-------|-----|----|
    #           -----                   |       |  A  | 6  |
    #     -->  |  A  | -----            | start |  B  | 2  |
    #    | 6    -----      | 1*         |       |     |    |
    #    |        ^        v            |   A   | FIN | 1  |
    #  -----      |      ------         |       |     |    |
    # |Start|  3* |     |Finish|        |   B   |  A  | 3  |
    #  -----      |      ------         |       | FIN | 5  |
    #    |        |        ^            |       |     |    |
    #    | 2*   -----      | 5          |  FIN  |  -  | -  |
    #     -->  |  B  | -----            |       |  -  | -  |
    #           -----                   |       |     |    |

    # below code is for the above graph
    graph = {}
    graph['start'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2

    graph['a'] = {}
    graph['a']['fin'] = 1

    graph['b'] = {}
    graph['b']['a'] = 3
    graph['b']['fin'] = 5
    graph['fin'] = {}  # finish line doesn't have any edges

    # prepare for the algorithm
    infinity = float('inf')  # use infinity to represent the cost we don't know yet ex. finish to finish

    #  | Node  | Cost  |
    #  |-------|-------|
    #  |  A    |  6    |
    #  |  B    |  2    |
    costs = {}
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = infinity

    #  | Node  | Parent  |
    #  |-------|---------|
    #  |  A    |  Start  |
    #  |  B    |  Start  |
    #  |  FIN  |   None  |
    parents = {}
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None
    processed = []  # list of nodes that have been processed


    def find_lowest_cost_node(costs):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:  # go through each node
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost # if it's the lowest cost so far, set it as the new lowest cost node
                lowest_cost_node = node
        return lowest_cost_node


    node = find_lowest_cost_node(costs)  # find the node with the lowest cost that has not been processed
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        # print('node: ', node, 'cost: ', cost)
        for n in neighbors.keys():  # Go through all the neighbors of the node
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:  # if it's cheaper to get to this node by going through this node
                costs[n] = new_cost  # then, update the cost for this node
                parents[n] = node  # This node is the new parent of the neighbor
        processed.append(node)  # Mark the node as processed
        node = find_lowest_cost_node(costs)  # find the next node with the lowest cost which not been processed and loop

    # print('Costs: ', costs)
    # print('Parents: ', parents)
    # print('Processed: ', processed)
    # print('Shortest path : ', costs['fin'])
    # print('Shortest path: ', parents['fin'])
