import json
import math
import sys

def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def simulate(filename):
    with open(filename, "r") as f:
        data = json.load(f)

    warehouses = data["warehouses"]
    agents = data["agents"]
    packages = data["packages"]

    report = {a: {"packages_delivered": 0, "total_distance": 0.0}
              for a in agents}

    for pkg in packages:
        wh_loc = warehouses[pkg["warehouse"]]

        nearest_agent = None
        min_dist = float("inf")

        for agent, a_loc in agents.items():
            d = euclidean(a_loc, wh_loc)
            if d < min_dist:
                min_dist = d
                nearest_agent = agent

        d1 = euclidean(agents[nearest_agent], wh_loc)
        d2 = euclidean(wh_loc, pkg["destination"])

        report[nearest_agent]["packages_delivered"] += 1
        report[nearest_agent]["total_distance"] += (d1 + d2)

    best_agent = None
    best_eff = float("inf")

    for agent, stats in report.items():
        if stats["packages_delivered"] > 0:
            eff = stats["total_distance"] / stats["packages_delivered"]
        else:
            eff = 0

        stats["total_distance"] = round(stats["total_distance"], 2)
        stats["efficiency"] = round(eff, 2)

        if eff > 0 and eff < best_eff:
            best_eff = eff
            best_agent = agent

    report["best_agent"] = best_agent
    return report

if __name__ == "__main__":
    input_file = sys.argv[1]
    output = simulate(input_file)

    out_file = input_file.replace(".json", "_report.json")
    with open(out_file, "w") as f:
        json.dump(output, f, indent=4)

    print(f"{input_file} processed → {out_file}")
