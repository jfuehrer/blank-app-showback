# intital show back model

import pandas as pd
import numpy as np
#import ace_tools as tools

# Define cost parameters
cost_factors = {
    "Compute (CPU/GPU)": {"rate_per_hour": 0.12, "usage_hours": [500, 700, 1200]},  # $ per hour
    "Storage (TB)": {"rate_per_tb": 20, "usage_tb": [10, 15, 25]},  # $ per TB
    "Networking (Data Transfer in TB)": {"rate_per_tb": 5, "usage_tb": [2, 3, 5]},  # $ per TB
    "Software Licenses": {"rate_per_license": 500, "licenses": [5, 7, 10]},  # $ per license
    "Support Fees": {"rate_per_team": 1000, "teams": [1, 1, 1]},  # $ per team
}

# Teams
teams = ["AI Research", "Simulations", "Software Dev"]

# Calculate costs
cost_data = []
for i, team in enumerate(teams):
    compute_cost = cost_factors["Compute (CPU/GPU)"]["rate_per_hour"] * cost_factors["Compute (CPU/GPU)"]["usage_hours"][i]
    storage_cost = cost_factors["Storage (TB)"]["rate_per_tb"] * cost_factors["Storage (TB)"]["usage_tb"][i]
    network_cost = cost_factors["Networking (Data Transfer in TB)"]["rate_per_tb"] * cost_factors["Networking (Data Transfer in TB)"]["usage_tb"][i]
    software_cost = cost_factors["Software Licenses"]["rate_per_license"] * cost_factors["Software Licenses"]["licenses"][i]
    support_cost = cost_factors["Support Fees"]["rate_per_team"] * cost_factors["Support Fees"]["teams"][i]
    
    total_cost = compute_cost + storage_cost + network_cost + software_cost + support_cost

    cost_data.append([team, compute_cost, storage_cost, network_cost, software_cost, support_cost, total_cost])

# Create DataFrame
columns = ["Team", "Compute Cost ($)", "Storage Cost ($)", "Network Cost ($)", "Software Cost ($)", "Support Cost ($)", "Total Cost ($)"]
cost_df = pd.DataFrame(cost_data, columns=columns)

# Display cost model
tools.display_dataframe_to_user(name="Cost Model for Multi-Cloud Environment", dataframe=cost_df)
