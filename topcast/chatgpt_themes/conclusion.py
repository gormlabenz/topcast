from .base import ChatGPTThemeBase
from topcast.models import TTSItem

class Conclusion(ChatGPTThemeBase):
  def __init__(self):
    super().__init__()
    
    self.system_prompt = "You are an AI language model that generates an entertaining conclusion about a text. Ensure that the conclusion is engaging, informative, and captures the audience's attention. The conclusion should be no longer than three sentences."
    self.messages = [
       {"role": "user", "content": """Could you send me a conclusion of an text? Here is the text:
        
In Persia's semi-desert towns, oases were fed through aqueducts carrying mountain water to support intensive food production, nurtured by wastes from the communities.[5] In Machu Picchu, water was conserved and reused as part of the chapterped architecture of the city, and vegetable beds were designed to gather sun in order to prolong the growing season.[5]
The idea of supplemental food production beyond rural farming operations and distant imports is not new. It was used during war and depression times when food shortage issues arose, as well as during times of relative abundance. Allotment gardens emerged in Germany in the early 19th century as a response to poverty and food insecurity.[6]
In 1893, citizens of a depression-struck Detroit were asked to use vacant lots to grow vegetables. They were nicknamed Pingree's Potato Patches after the mayor, Hazen S. Pingree, who came up with the idea. He intended for these gardens to produce income, food supply, and boost independence during times of hardship.[7] Victory gardens sprouted during WWI and WWII and were fruit, vegetable, and herb gardens in the US, Canada, and UK. This effort was undertaken by citizens to reduce pressure on food production that was to support the war effort.
During World War I, President Woodrow Wilson called upon all American citizens to utilize any available open food growth, seeing this as a way to pull them out of a potentially damaging situation.[8] Since most of Europe was consumed with war, they were unable to produce sufficient food supplies to be shipped to the US and a new plan was implemented with the goal of feeding the US and even supply a surplus to other countries in need. By 1919, over 5 million plots were growing food and over 500 million pounds of produce was harvested.
A very similar practice came into use during the Great Depression that provided a purpose, job and food to those who would otherwise be without anything during such harsh times. These efforts helped raise spirits and boost economic growth. Over 2.8 million dollars worth of food was produced from the subsistence gardens during the Depression. By World War II, the War/Food Administration set up a National Victory Garden Program that set out to systematically establish functioning agriculture within cities. With this new plan in action, as many as 5.5 million Americans took part in the victory garden movement and over nine million pounds of fruit and vegetables were grown a year, accounting for 44% of US-grown produce throughout that time.[9]"""},
           {"role": "assistant", "content": """In the face of adversity, humanity has historically turned to urban agriculture as a means of sustenance and resilience. From ancient Persia to the victory gardens of WWII, communities have united to grow food in times of hardship and abundance alike. The enduring legacy of these gardens highlights the power of ingenuity, collaboration, and resourcefulness in addressing global challenges."""}
  ]
 
  def create_content(self, input_content: str):
    return  f"""Could you send me another conclusion? Here is the text: 
  
  {input_content}
  
  """
  
  def extract_content(self, response_content: str):
    return [TTSItem(text=response_content, gender="female")]
