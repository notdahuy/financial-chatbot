
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

from tools import get_stock_price, news_search_tool

SYSTEM_PROMPT = "Bạn là một trợ lý tài chính thông minh. Bạn có khả năng truy cập giá cổ phiếu và tìm kiếm tin tức."

load_dotenv()
gemini_flash = init_chat_model("google_genai:gemini-2.5-flash", temperature=0)
tools = [get_stock_price, news_search_tool]
agent = create_agent(
    model=gemini_flash,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
)

response = agent.invoke({
    "messages": [
        HumanMessage(content="Giá cổ phiếu Microsoft hiện tại là bao nhiêu?")
    ]
})

final_answer = response["messages"][-1].content
print(final_answer)





