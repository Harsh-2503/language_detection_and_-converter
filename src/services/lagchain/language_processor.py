from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import config
from langchain_core.runnables import RunnablePassthrough,RunnableParallel
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import config
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_openai.embeddings import OpenAIEmbeddings

output_parser = StrOutputParser()

try:
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=config.openAiKey)
except Exception as e:
    print("Error initializing ChatOpenAI model:", e)
    # Handle the error accordingly, maybe fallback to a default model or log the error.

try:
    language_chain = ChatPromptTemplate.from_template("Detect the Language {question}") | model | output_parser
    grammar_chain = ChatPromptTemplate.from_template("Identify and only specify the wrong grammar {question}") | model | output_parser
    translate_chain = ChatPromptTemplate.from_template("Translate to English {question}") | model | output_parser
except Exception as e:
    print("Error creating chat chains:", e)
    # Handle the error accordingly, maybe fallback to default chains or log the error.

try:
    map_chain = RunnableParallel(language=language_chain, grammar=grammar_chain, translate=translate_chain)
except Exception as e:
    print("Error creating RunnableParallel:", e)
    # Handle the error accordingly, maybe fallback to default chains or log the error.

