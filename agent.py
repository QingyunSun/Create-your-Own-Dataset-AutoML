import os

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
api_key = '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'

# Set the environment variable
os.environ['OPENAI_API_KEY'] = api_key

import os
import pickle

# Set the path to the directory
dir_path = '.'

# Create a dictionary to store the pickle objects
pickle_dict = {}

# print("all files: ", os.listdir(dir_path))

def get_pickle_files(dir):
    # Walk through the files in the directory
    for filename in os.listdir(dir_path):
        # Ensure we're working with a pickle file
        if filename.endswith('.pkl'):
            with open(os.path.join(dir_path, filename), 'rb') as f:
                # Load the pickle file and store it in the dictionary
                pickle_obj = pickle.load(f)
                pickle_dict[filename] = pickle_obj

# Now, pickle_dict holds all of your loaded pickle objects
# Key is the filename and value is the pickle object


from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 3000,
    chunk_overlap  = 300,
    length_function = len,
    add_start_index = True,
)

def get_text(pickle_dict, filename, section):
# print(texts[0])
# print(texts[1])
    return text_splitter.create_documents([pickle_dict[filename].iloc[0][section]])



from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.chains import LLMChain

# p = """
# As a capable financial analyst, your task is to review a section from Apple Inc.'s latest SEC filing.
# This section contains information about the company's financial position, its recent performance, and future plans.
# Please create a list of questions that could be answered by the content of the filing, along with their respective answers.
# These questions should focus on key points such as financial health, risk factors, executive compensation, business operations, and forward-looking statements.
# Provide concise, clear answers for each question based on the information presented in the filing.

# {filing_content}
# """

p_v2 = """
As a capable financial analyst, your task is to review a section from Apple Inc.'s latest SEC filing.
This section contains specific financial data, including key details about the company's revenue, sources of income, and profitability.
Generate a series of time-sensitive questions that specifically reference the concrete numbers and data points within the filing related to Apple's revenue streams.
For each question, provide a corresponding answer that is directly informed by the specific data in the document.
The question-answer pairs should cover areas such as revenue growth, breakdown of revenue by product or service, the impact of external factors on revenue, and how revenue performance might influence future strategy.

For the output, please format the question-answer pairs as a JSON object.
Each question-answer pair should be a separate object, with the question as the 'question' key and the answer as the 'answer' key.

{filing_content}
"""

import json

def is_valid_json(json_string):
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False

def generate_qa_pairs_from_filing(filing_content):
  llm = ChatOpenAI(temperature=0.1, model_name='gpt-4')
  # llm = OpenAI(temperature=0.1)
  prompt = PromptTemplate(
      input_variables=["filing_content"],
      template = p_v2
  )
  chain = LLMChain(llm=llm, prompt=prompt)
  print(chain.run(filing_content))

def create_agent():
  llm = ChatOpenAI(temperature=0.1, model_name='gpt-4')
  # llm = OpenAI(temperature=0.1)
  prompt = PromptTemplate(
      input_variables=["filing_content"],
      template = p_v2
  )
  chain = LLMChain(llm=llm, prompt=prompt)
  return chain

# for t in texts:
#   generate_qa_pairs_from_filing(t.page_content)