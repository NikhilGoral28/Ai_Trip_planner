from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT

from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.expence_calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConverterTool

from langgraph.graph import StateGraph, MessageGraph, END, START
from langgraph.prebuilt import ToolNode,tools_condition




class GraphBuilder():

    def __init__(self):
        pass

    def agent_function(self):
        pass

    def build_graph(self):
        pass

    def __call__(self):
        pass