from langchain.chains import LLMChain
from langchain.chains.question_answering.map_rerank_prompt import output_parser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

class Agent:
    model: str = "gemma3:4b"
    temperature: float = 0.7
    llm: ChatOllama = None
    promptTemplate: ChatPromptTemplate = ChatPromptTemplate.from_messages([
        ("system", "You must respond in Korean only. 반드시 한국어로만 답변하세요."),
        ("user", "{input}")
    ])

    # 체인 설정
    output_parser = StrOutputParser()
    chain = None

    def __init__(self):
        # LangChain Ollama 인스턴스 생성
        self.llm = ChatOllama(
            model=self.model,
            temperature=self.temperature,
        )

        self.chain = self.promptTemplate | self.llm | output_parser

        print("Ollama Loaded")

    def prompt(self, message):
        print("prompt >>> ", message)
        response = self.llm.invoke(message)
        return response

agent = Agent()