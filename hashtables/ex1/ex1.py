class Weight:
    def __init__(self, weight, limit, index):
        self.match = abs(limit - weight)
        self.i = index
def get_indices_of_item_weights(weights, length, limit):
    index = {}
    for i, weight in enumerate(weights):
        if weight in index:
            index[weight].append(Weight(weight, limit, i))
        else:
            index[weight] = [Weight(weight, limit, i)]
    for weight in index:
        for c in index[weight]:
            if c.match in index:
                if len(index[c.match]) > 1:
                    return sorted([ index[c.match][1].i, c.i ], reverse=True)
                else:
                    return sorted([ index[c.match][0].i, c.i ], reverse=True)
    return None
