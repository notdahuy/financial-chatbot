import yfinance as yf
from langchain.tools import tool
from langchain_tavily import TavilySearch
from dotenv import load_dotenv
import os

load_dotenv()

@tool
def get_stock_price(ticker_symbol: str) -> str:
    """
    Get current stock price by ticker symbol
    Use this tool ONLY when the user explicitly asks for stock prices.
    """
    try:
        ticker = yf.Ticker(ticker_symbol)
        data = ticker.history(period="1d", interval="1m")
        if data.empty:
            return f"{ticker_symbol} has no data."

        price = data['Close'].iloc[-1]
        return f"{ticker_symbol} price {price:.2f}"
    except Exception as e:
        return f"Error while getting data: {e}"

news_search_tool = TavilySearch(
    max_results=3,
    topic="finance",
    description=(
        "Search for the most recent news articles about a given company or keyword. "
        "Use this tool ONLY when the user asks for news, updates, or recent information."
    ),
)