from larry.chat import Chat
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

#def test_chat():

    #def fn(context):
    #    return "hello world"
    
    #chat = Chat(fn = fn)
    #chat.launch()

def test_langchain():

    print(os.environ["OPENAI_API_KEY"])

    prompt_template = "What is a good name for a company that makes {product}?"

    llm = OpenAI(temperature=0)
    llm_chain = LLMChain(llm=llm, prompt=PromptTemplate.from_template(prompt_template))
    
    chat = Chat(runnable = llm_chain)
    chat.launch()