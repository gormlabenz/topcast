from .base import ChatGPTThemeBase
from topcast.models import TTSItem

class Summary(ChatGPTThemeBase):
  def __init__(self):
    super().__init__()
    
    self.system_prompt = "You are an AI language model, and your task is to generate a brief and entertaining summary of a text. Make it interesting and engaging."   
    self.messages = [
       {"role": "user", "content": """I have to create a podcast about the Olkiluoto Nuclear Power Plant. I need a short, entertaing and funny summary to the topic. Here are some information about it:

The Olkiluoto Nuclear Power Plant (Finnish: Olkiluodon ydinvoimalaitos, Swedish: Olkiluoto kärnkraftverk) is one of Finland's two nuclear power plants, the other being the two-unit Loviisa Nuclear Power Plant. The plant is owned and operated by Teollisuuden Voima (TVO), a subsidiary of Pohjolan Voima, and is located on Olkiluoto Island, on the shore of the Gulf of Bothnia, in the municipality of Eurajoki in western Finland, about 20 kilometres (12 mi) from the town of Rauma and about 50 kilometres (31 mi) from the city of Pori.

The Olkiluoto plant consists of two boiling water reactors (BWRs), each with a capacity of 890 MW, and one EPR type reactor (unit 3) with a capacity of 1,600 MW.[1] This makes unit 3 currently the most powerful nuclear power plant unit in Europe and the third most powerful globally.[2][3] Construction of unit 3 began in 2005. Commercial operation began on 16 April 2023[4] after being originally scheduled for May 2009.[5][6]"""},
           {"role": "assistant", "content": """
Cancel
Welcome to this week's podcast episode, where we're diving into the world of Finnish nuclear power and giving you a hilarious lowdown on the Olkiluoto Nuclear Power Plant! Nestled on Olkiluoto Island, this bad boy of a power plant churns out electricity like there's no tomorrow. Located just a hop, skip, and a jump away from the towns of Rauma and Pori, it's Finland's hottest (and most radioactive) vacation destination!

Run by the energy whizzes at Teollisuuden Voima (TVO), the Olkiluoto plant boasts two boiling water reactors that'll make your tea in no time, along with one EPR type reactor that's got some serious juice—1,600 MW of capacity, to be exact! In fact, unit 3 is so powerful, it's the European heavyweight champion of nuclear reactors and ranks third worldwide. Talk about a Finnish power trip!

But it wasn't all smooth sailing for this Finnish marvel. Unit 3's construction kicked off in 2005, and it was supposed to be up and running by May 2009. But, like an overambitious DIY project, it took a tad longer than expected, finally getting down to business on April 16, 2023. Better late than never, right?

So, grab your Geiger counters and protective gear, because we're about to embark on an entertaining and electrifying journey into the heart of Finland's Olkiluoto Nuclear Power Plant!"""}
  ]
 
  def create_content(self, input_content: str):
    return  f"""Could you write another summary? Here are some information about it: {input_content}"""
  
  def extract_content(self, response_content: str):
    return [TTSItem(text=response_content, gender="female")]
