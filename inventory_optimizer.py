import pandas as pd
import pulp

def optimize_inventory_reorder(forecasted_demand_str: str) -> str:
    """
    Based on a demand forecast string (e.g., 'Total forecasted sales units: 5000'),
    this tool calculates the optimal reorder quantity for a product to meet demand
    while minimizing holding costs.
    """
    try:
        # A simple parser to extract the forecasted units
        demand = int(forecasted_demand_str.split("Total forecasted sales units: ")[1].split("\n")[0])

        # For this example, we use static data. In a real scenario, this would come from a database.
        current_stock = 800
        holding_cost_per_unit = 0.1  # cost per unit per period
        order_cost = 50  # fixed cost per order
        
        # Define the problem
        prob = pulp.LpProblem("Inventory_Optimization", pulp.LpMinimize)
        
        # Decision variable
        reorder_quantity = pulp.LpVariable("ReorderQuantity", lowBound=0, cat='Integer')
        
        # Objective function: Minimize (Holding Costs + Ordering Costs)
        # Simplified model: holding cost applies to average inventory after reorder
        prob += (holding_cost_per_unit * (current_stock + reorder_quantity - demand/2) + 
                 order_cost * (reorder_quantity > 0)), "TotalCost"
        
        # Constraint: Ensure stock can meet forecasted demand
        prob += current_stock + reorder_quantity >= demand, "Demand_Satisfaction"
        
        prob.solve(pulp.PULP_CBC_CMD(msg=False))
        
        optimal_quantity = int(reorder_quantity.varValue)

        return (f"Inventory Optimization Plan:\n"
                f"- Forecasted Demand: {demand} units.\n"
                f"- Current Stock: {current_stock} units.\n"
                f"- Recommended Reorder Quantity: {optimal_quantity} units.")
    except Exception as e:
        return f"An error occurred during inventory optimization: {e}"