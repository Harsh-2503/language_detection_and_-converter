from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import config
from langchain_core.runnables import RunnablePassthrough,RunnableParallel
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_openai.embeddings import OpenAIEmbeddings

output_parser = StrOutputParser()

model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key= config.openAiKey)
language_chain = ChatPromptTemplate.from_template("Detect the Language {question}") | model | output_parser
grammar_chain = (
    ChatPromptTemplate.from_template("Indentify and only specify the wrong grammar {question}") | model | output_parser
)
translate_chain = ChatPromptTemplate.from_template("Translate to English {question}") | model | output_parser

map_chain = RunnableParallel(language=language_chain, grammar=grammar_chain, translate=translate_chain)

print(map_chain.invoke({"question": "こんにちは お元気ですか"}))