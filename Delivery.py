# Import required modules
import json          # To read and write JSON files
import math          # To calculate square root for distance
import sys           # To read command line arguments
import os            # To check if file exists


# Function to calculate distance between two points
def distance(point1, point2):
    # Extract x and y coordinates
    x1, y1 = point1
    x2, y2 = point2

    # Euclidean distance formula
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Main function that performs delivery simulation
def simulate(filename):

    # Check whether input file exists or not
    if not os.path.exists(filename):
        print("Input file not found:", filename)
        return

    # Open and load JSON input file
    with open(filename, "r") as file:
        data = json.load(file)

    # Extract data from JSON
    warehouses = data["warehouses"]
    agents = data["agents"]
    packages = data["packages"]

    # Initialize report dictionary for agents
    report = {}

    for agent in agents:
        report[agent] = {
            "packages_delivered": 0,   # Number of packages delivered
            "total_distance": 0        # Total distance travelled
        }

    # Process each package one by one
    for package in packages:

        # Get warehouse location for the package
        warehouse_id = package["warehouse"]
        warehouse_location = warehouses[warehouse_id]

        # Find the nearest agent to the warehouse
        nearest_agent = None
        shortest_distance = None

        for agent_id in agents:
            agent_location = agents[agent_id]
            d = distance(agent_location, warehouse_location)

            # Select agent with minimum distance
            if shortest_distance is None or d < shortest_distance:
                shortest_distance = d
                nearest_agent = agent_id

        # Calculate distance from agent to warehouse
        agent_to_warehouse = distance(
            agents[nearest_agent], warehouse_location
        )

        # Calculate distance from warehouse to destination
        warehouse_to_destination = distance(
            warehouse_location, package["destination"]
        )

        # Total distance travelled for this package
        total = agent_to_warehouse + warehouse_to_destination

        # Update agent delivery details
        report[nearest_agent]["packages_delivered"] += 1
        report[nearest_agent]["total_distance"] += total

    # Find the best agent based on efficiency
    best_agent = None
    best_efficiency = None

    for agent in report:
        count = report[agent]["packages_delivered"]

        # Calculate efficiency
        if count > 0:
            efficiency = report[agent]["total_distance"] / count
        else:
            efficiency = 0

        # Round values for readability
        report[agent]["total_distance"] = round(
            report[agent]["total_distance"], 2
        )
        report[agent]["efficiency"] = round(efficiency, 2)

        # Select agent with minimum efficiency
        if efficiency > 0:
            if best_efficiency is None or efficiency < best_efficiency:
                best_efficiency = efficiency
                best_agent = agent

    # Add best agent to final report
    report["best_agent"] = best_agent
    return report


# Program execution starts here
if __name__ == "__main__":

    # Check whether input file is passed from command line
    if len(sys.argv) < 2:
        print("Usage: python Delivery.py <input_file>")
        sys.exit(1)

    # Read input file name
    input_file = sys.argv[1]

    # Run simulation
    output = simulate(input_file)

    # Write output report to JSON file
    if output:
        output_file = input_file.replace(".json", "_report.json")

        with open(output_file, "w") as file:
            json.dump(output, file, indent=4)

        print(input_file, "processed ->", output_file)

