from collections import defaultdict


def airportConnections(airports, routes, startingAirport):
    # Write your code here.
    airport_num = len(airports)
    edges = defaultdict(list)
    group = defaultdict(lambda: None)
    for start, goal in routes:
        edges[start].append(goal)

    requird_route_count = 0

    for airport in airports:
        if group[airport] is not None:
            continue

        group[airport] = requird_route_count
        stack = [airport]
        visited = set()
        while stack:
            ap = stack.pop()
            visited.add(ap)
            for next_ap in edges[ap]:
                if next_ap not in visited:
                    group[next_ap] = requird_route_count
                    stack.append(next_ap)

        requird_route_count += 1

    return requird_route_count

airports = [
  "BGI",
  "CDG",
  "DEL",
  "DOH",
  "DSM",
  "EWR",
  "EYW",
  "HND",
  "ICN",
  "JFK",
  "LGA",
  "LHR",
  "ORD",
  "SAN",
  "SFO",
  "SIN",
  "TLV",
  "BUD",
]
routes = [
  ["DSM", "ORD"],
  ["ORD", "BGI"],
  ["BGI", "LGA"],
  ["SIN", "CDG"],
  ["CDG", "SIN"],
  ["CDG", "BUD"],
  ["DEL", "DOH"],
  ["DEL", "CDG"],
  ["TLV", "DEL"],
  ["EWR", "HND"],
  ["HND", "ICN"],
  ["HND", "JFK"],
  ["ICN", "JFK"],
  ["JFK", "LGA"],
  ["EYW", "LHR"],
  ["LHR", "SFO"],
  ["SFO", "SAN"],
  ["SFO", "DSM"],
  ["SAN", "EYW"],
],
start = "LGA"

print(airportConnections(airports, routes, start))
