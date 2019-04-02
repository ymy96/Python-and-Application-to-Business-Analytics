nodes = ('EUR','USD','CNY','JPY','GBP','CAD')
for a in (0.01,0.02,0.05):
    for b in (0.01,0.02,0.05):
        costs = {'EUR':{'USD':1.16*(1-b),'CNY':7.94,'JPY':131.19,'GBP':0.89,'CAD':1.48},
                 'USD':{'CNY':6.87/(1+a),
                        'JPY':113.57/(1+a),
                        'GBP':0.77/(1+a),
                        'CAD':1.28/(1+a)},
                 'CNY':{'EUR':0.13},
                 'JPY':{'EUR':0.0076},
                 'GBP':{'EUR':1.12},
                 'CAD':{'EUR':0.68}}
        unvisited_nodes = {node: None for node in nodes}
        start_node = 'EUR'
        visited_nodes = {}
        current_node = start_node
        current_cost = 1
        unvisited_nodes[current_node] = current_cost
        while True:
            for neighbor, cost in costs[current_node].items():
                if neighbor not in unvisited_nodes:
                    continue
                new_cost = current_cost * cost
                if unvisited_nodes[neighbor] is None or new_cost > unvisited_nodes[neighbor]:
                    unvisited_nodes[neighbor] = new_cost
            visited_nodes[current_node] = current_cost
            del unvisited_nodes[current_node]
            if not unvisited_nodes:
                break
            candidates = [node for node in unvisited_nodes.items()if node[1]]
            current_node, current_cost = sorted(candidates, key=lambda x:x[1])[0]
        del visited_nodes['USD']
        print("a = " + str(a) + ", " + "b = " + str(b))
        print(visited_nodes)
        for currency in ('CNY','JPY','GBP','CAD'):
            if costs['EUR'][currency] == visited_nodes[currency]:
                print("For " + str(currency) + ", we can get more money if we convert it directly.")
            else:
                print("For " + str(currency) + ", we can get more money if we convert it to USD first.")
        print("---------------------------------------------------------------------")
