from .base import ChatGPTThemeBase
from topcast.models import TTSItem

class Introduction(ChatGPTThemeBase):
  def __init__(self):
    super().__init__()
    
    self.system_prompt = "You are an AI language model, and your task is to generate a brief and entertaining introductions of a text. Make it interesting and engaging without revealing too much about it." 
    self.messages = [
       {"role": "user", "content": """I have to create a podcast about the Olkiluoto Nuclear Power Plant. I need a short, entertaing and funny introduction to the topic. It shouldn't be any longer than 3 sentences. Could you write me one? Here are some information about it:

The Olkiluoto Nuclear Power Plant (Finnish: Olkiluodon ydinvoimalaitos, Swedish: Olkiluoto kärnkraftverk) is one of Finland's two nuclear power plants, the other being the two-unit Loviisa Nuclear Power Plant. The plant is owned and operated by Teollisuuden Voima (TVO), a subsidiary of Pohjolan Voima, and is located on Olkiluoto Island, on the shore of the Gulf of Bothnia, in the municipality of Eurajoki in western Finland, about 20 kilometres (12 mi) from the town of Rauma and about 50 kilometres (31 mi) from the city of Pori.

The Olkiluoto plant consists of two boiling water reactors (BWRs), each with a capacity of 890 MW, and one EPR type reactor (unit 3) with a capacity of 1,600 MW.[1] This makes unit 3 currently the most powerful nuclear power plant unit in Europe and the third most powerful globally.[2][3] Construction of unit 3 began in 2005. Commercial operation began on 16 April 2023[4] after being originally scheduled for May 2009.[5][6]"""},
           {"role": "assistant", "content": """Welcome to our podcast, where we'll dive into the fascinating world of Finland's Olkiluoto Nuclear Power Plant - home to Europe's strongest reactor, the Energizer Bunny of the nuclear world, and just a hop, skip, and a jump from the bustling metropolis of Pori!"""}
  ]
 
  def create_content(self, input_content: str):
    return  f"""Could you write another introduction? Here are some information about the topic: {input_content}"""
  
  def extract_content(self, response_content: str):
    return [TTSItem(text=response_content, gender="female")]
