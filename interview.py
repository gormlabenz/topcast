from server.podcast_chunk import PodcastChunk
from server.configs import intro_config, interview_config, conclusion_config, summary_config
from server.openai_classes import OpenAIApiBase
import asyncio

async def generate_textItems():
  input_text = """OpenAI is an American artificial intelligence (AI) research laboratory consisting of the non-profit OpenAI Incorporated and its for-profit subsidiary corporation OpenAI Limited Partnership. OpenAI conducts AI research with the declared intention of promoting and developing a friendly AI. OpenAI systems run on an Azure-based supercomputing platform from Microsoft.[5][6][7]

OpenAI was founded in 2015 by Ilya Sutskever, Greg Brockman, Trevor Blackwell, Vicki Cheung, Andrej Karpathy, Durk Kingma, John Schulman, Pamela Vagata, and Wojciech Zaremba, with Sam Altman and Elon Musk serving as the initial board members.[8][1][9] Microsoft provided OpenAI LP with a $1 billion investment in 2019 and a $10 billion investment in 2023.[10][11]"""

  openai = OpenAIApiBase(interview_config["system_prompt"], interview_config["messages"], interview_config["get_message"], interview_config["extract"])
  textItems = await openai.create_chat_completion(input_text)
  
  print("textItems", textItems)
  
asyncio.run(generate_textItems())
