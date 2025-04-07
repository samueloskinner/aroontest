from typing import Dict, List
import autogen
from .main import fetch_stock_data, calculate_aroon, plot_aroon_indicators, analyze_aroon_signals

class AroonAnalyst:
    def __init__(self, config_path: str = "OAI_CONFIG_LIST"):
        # Load configurations
        config_list = autogen.config_list_from_json(config_path)
        llm_config = {"config_list": config_list, "cache_seed": 42}
        
        # Configure agents
        self.analyst = autogen.AssistantAgent(
            name="analyst",
            system_message="Technical analyst specialized in Aroon indicators",
            llm_config=llm_config
        )
        
        self.researcher = autogen.AssistantAgent(
            name="researcher",
            system_message="Financial data researcher and validator",
            llm_config=llm_config
        )
        
        self.coder = autogen.AssistantAgent(
            name="coder",
            system_message="Python expert in data analysis and visualization",
            llm_config=llm_config
        )

        # Create group chat
        self.group_chat = autogen.GroupChat(
            agents=[self.analyst, self.researcher, self.coder],
            messages=[],
            max_round=10
        )
        
        self.manager = autogen.GroupChatManager(
            groupchat=self.group_chat,
            llm_config=llm_config
        )

    async def analyze_stock(self, ticker: str, period: str = "1y") -> Dict:
        """
        Perform comprehensive stock analysis using multiple agents
        """
        task = f"""
        Analyze {ticker} using Aroon indicators:
        1. Fetch {period} historical data and validate its quality
        2. Calculate and interpret Aroon indicators
        3. Generate trading signals with confidence levels
        4. Create detailed visualization
        5. Provide actionable recommendations
        """
        
        # Initialize the chat
        result = await self.manager.run_chat(
            message=task,
            sender=self.analyst
        )
        
        return result

    async def optimize_strategy(self, ticker: str, period: str = "1y") -> Dict:
        """
        Optimize trading strategy parameters
        """
        task = f"""
        Optimize trading strategy for {ticker}:
        1. Test Aroon periods from 5 to 30 days
        2. Find optimal signal thresholds
        3. Validate results with cross-validation
        4. Report performance metrics
        """
        
        result = await self.manager.run_chat(
            message=task,
            sender=self.researcher
        )
        
        return result