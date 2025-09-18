from langchain.agents import AgentType, initialize_agent, Tool
from langchain_openai import OpenAI
from utils.config import OPENAI_API_KEY

# Import the functions from our agent files
from agents.demand_forecaster import forecast_product_demand
from agents.inventory_optimizer import optimize_inventory_reorder
from agents.logistics_planner import plan_shipping_route
from agents.crisis_agent import check_for_supply_chain_disruptions

def run_supply_chain_ai():
    """Initializes and runs the AI Supply Chain Manager."""

    if not OPENAI_API_KEY or OPENAI_API_KEY == "your_openai_api_key":
        print("FATAL: OpenAI API key not found. Please set it in your .env file.")
        return

    # Initialize the LLM
    llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

    # Define the suite of tools the agent can use
    tools = [
        Tool(
            name="Demand Forecaster",
            func=forecast_product_demand,
            description="Use this to forecast future sales demand for a specific product ID. Input should be a product ID and the number of days to forecast."
        ),
        Tool(
            name="Inventory Optimizer",
            func=optimize_inventory_reorder,
            description="Use this to calculate the optimal reorder quantity for inventory. It takes the output from the Demand Forecaster as input."
        ),
        Tool(
            name="Logistics Planner",
            func=plan_shipping_route,
            description="Use this to find the distance and travel time between two locations. Useful for planning shipping and delivery routes."
        ),
        Tool(
            name="Crisis Agent",
            func=check_for_supply_chain_disruptions,
            description="Use this to scan for breaking news about global supply chain disruptions. Input should be keywords like 'port congestion' or 'trade dispute'."
        )
    ]

    # Initialize the main agent (the orchestrator)
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True  # Set to True to see the agent's thought process
    )

    print("🤖 AI Supply Chain Manager is online. How can I help you?")

    # Main loop to interact with the agent
    while True:
        try:
            user_query = input("> ")
            if user_query.lower() in ["exit", "quit"]:
                print("Shutting down. Goodbye!")
                break
            
            response = agent.run(user_query)
            print(f"\n🤖: {response}\n")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_supply_chain_ai()