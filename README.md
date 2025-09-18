# Intelligent-Supply-Chain-Management-Agent

**Intelligent Supply Chain Management** is a powerful, conversational AI agent designed to act as an automated manager for complex supply chain operations. Built on the **LangChain** framework and powered by **OpenAI**, this command-line application integrates multiple specialized tools to handle tasks ranging from demand forecasting and inventory optimization to logistics planning and crisis monitoring.

The system uses a central orchestrator agent that intelligently selects the right tool to respond to user queries, effectively simulating a multi-agent workflow.

---

## 🌟 Key Features

-   **Multi-Tool AI Agent**: A central agent orchestrates a suite of specialized tools, each designed for a specific supply chain function.
-   **Predictive Demand Forecasting**: Utilizes the **Prophet** library to analyze historical data and accurately forecast future product demand, complete with data visualizations.
-   **Algorithmic Inventory Optimization**: Employs the **PuLP** optimization library to calculate the optimal reorder quantity, minimizing holding costs while ensuring demand is met.
-   **Real-Time Logistics Planning**: Integrates with the **Google Maps API** to calculate optimal shipping routes, providing accurate distance and estimated travel time for logistics planning.
-   **Proactive Crisis Monitoring**: Scans global news headlines via the **NewsAPI** for keywords related to supply chain disruptions (e.g., port strikes, tariffs), providing early warnings.
-   **Interactive Command-Line Interface**: Allows users to interact with the AI manager in a conversational manner to perform complex, multi-step tasks.

---

## 🛠️ Installation & Setup

### 1. Prerequisites

-   Python 3.8+
-   Git

### 2. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-directory>
3. Set Up a Virtual Environment
Bash

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
4. Install Dependencies
The project's dependencies are listed in requirements.txt. Install them using pip:

Bash

pip install -r requirements.txt
5. Configure Environment Variables
This project requires API keys from OpenAI, NewsAPI, and Google Maps Platform.

Create a file named .env in the root of your project directory.

Add your API keys to the .env file as shown below:

Code snippet

OPENAI_API_KEY="sk-..."
NEWS_API_KEY="your_news_api_key"
GOOGLE_MAPS_API_KEY="your_google_maps_api_key"
🚀 Usage Guide
To launch the AI Supply Chain Manager, run the main.py script from your terminal:

Bash

python main.py
The application will start, and you will see the prompt: 🤖 AI Supply Chain Manager is online. How can I help you?

Type your requests into the prompt and press Enter.

To exit the application, type exit or quit.

Example Prompts:

Forecasting: "Forecast demand for product ID 151 for the next 90 days."

Optimization: "Given a forecast of 5000 units, what is the optimal reorder quantity?"

Logistics: "What is the driving time from 'Los Angeles, CA' to 'Phoenix, AZ'?"

Crisis Monitoring: "Check for news about 'port congestion' in Asia."

Multi-step Query: "Forecast demand for product 123 for 30 days and then calculate the optimal inventory reorder for it."

⚙️ Technical Details
Core Libraries
LangChain & LangChain-OpenAI: Provides the core framework for building the agent and its tools.

Prophet: A time-series forecasting library by Facebook used for the demand forecasting tool.

PuLP: A linear programming library used to model and solve the inventory optimization problem.

googlemaps: The official Python client for Google Maps API services, used for logistics planning.

newsapi-python: A Python client for NewsAPI, used for the crisis monitoring agent.

Pandas: Used for data manipulation and preparation for the Prophet forecasting model.

Agent Architecture
The application is built around a ZERO_SHOT_REACT_DESCRIPTION agent from LangChain. This agent architecture works as follows:

The agent is initialized with a set of tools, each with a clear name and description.

When the user provides a query, the agent uses the LLM to Reason about the query and the tool descriptions.

It selects the most appropriate tool and determines the input, then takes an Action by executing that tool's function.

It observes the result from the tool and repeats the Reason-Act loop until it has enough information to formulate a final answer for the user.

💡 Agent & Tool Design
The intelligence of this system lies in the composition of its specialized tools. The central agent acts as an orchestrator, relying on the clear descriptions of each tool to decide its course of action.

Demand Forecaster: "Use this to forecast future sales demand for a specific product ID. Input should be a product ID and the number of days to forecast."

Inventory Optimizer: "Use this to calculate the optimal reorder quantity for inventory. It takes the output from the Demand Forecaster as input."

Logistics Planner: "Use this to find the distance and travel time between two locations. Useful for planning shipping and delivery routes."

Crisis Agent: "Use this to scan for breaking news about global supply chain disruptions. Input should be keywords like 'port congestion' or 'trade dispute'."

🧠 Challenges & Solutions
Challenge 1: Orchestrating Diverse, Specialized Tasks
Problem: Supply chain management involves distinct and unrelated tasks like statistical forecasting, mathematical optimization, and real-time data lookups.
Solution: A central ReAct agent acts as an intelligent orchestrator. It decomposes high-level user requests (e.g., "Plan our inventory for next quarter") into a sequence of steps, calling the correct specialized tool for each part of the problem.

Challenge 2: Seamlessly Integrating Multiple External APIs
Problem: The application depends on three different external APIs (OpenAI, Google Maps, NewsAPI), each with its own key and client library.
Solution: API key management is centralized in a .env file and a utils/config.py module. This separates credentials from the application logic. Each tool function includes error handling and checks for missing API keys to ensure graceful failure.

Challenge 3: Chaining Tool Inputs and Outputs
Problem: The output of one tool (e.g., the demand forecast) must serve as a valid input for another (e.g., the inventory optimizer).
Solution: The tools are designed for interoperability. The inventory_optimizer function includes a simple parser specifically designed to extract the numerical demand from the natural language summary produced by the forecast_product_demand function.

📂 File Structure Overview
project-root/
│
├── main.py                     # Main application entry point, initializes and runs the agent.
├── requirements.txt            # Lists all Python dependencies.
├── .env                        # (User-created) Stores API keys.
│
├── agents/
│   ├── demand_forecaster.py    # Tool for forecasting product demand.
│   ├── inventory_optimizer.py  # Tool for calculating reorder quantities.
│   ├── logistics_planner.py    # Tool for planning shipping routes.
│   └── crisis_agent.py         # Tool for monitoring news for disruptions.
│
└── utils/
    └── config.py               # Loads environment variables from the .env file.
📄 License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it for personal or professional use.

🙌 Acknowledgments
LangChain for the powerful agent framework.

OpenAI for the core language model.

Meta Prophet for the forecasting library.

Google Maps Platform and NewsAPI for providing the real-time data services.












Tools

