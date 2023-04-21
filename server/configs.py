import re
from .voices import VoiceMale, VoiceFemale

summaryConfig = {
  "system_prompt": """You are an AI language model, and your task is to generate a brief and entertaining summary of a text. Make it interesting and engaging without revealing too much about it.""",
  "messages": [
       {"role": "user", "content": """I have to create a podcast about the Olkiluoto Nuclear Power Plant. I need a short, entertaing and funny introduction to the topic. It shouldn't be any longer than 3 sentences. Could you write me one? Here are some information about it:

The Olkiluoto Nuclear Power Plant (Finnish: Olkiluodon ydinvoimalaitos, Swedish: Olkiluoto kärnkraftverk) is one of Finland's two nuclear power plants, the other being the two-unit Loviisa Nuclear Power Plant. The plant is owned and operated by Teollisuuden Voima (TVO), a subsidiary of Pohjolan Voima, and is located on Olkiluoto Island, on the shore of the Gulf of Bothnia, in the municipality of Eurajoki in western Finland, about 20 kilometres (12 mi) from the town of Rauma and about 50 kilometres (31 mi) from the city of Pori.

The Olkiluoto plant consists of two boiling water reactors (BWRs), each with a capacity of 890 MW, and one EPR type reactor (unit 3) with a capacity of 1,600 MW.[1] This makes unit 3 currently the most powerful nuclear power plant unit in Europe and the third most powerful globally.[2][3] Construction of unit 3 began in 2005. Commercial operation began on 16 April 2023[4] after being originally scheduled for May 2009.[5][6]"""},
           {"role": "assistant", "content": """Welcome to our podcast, where we'll dive into the fascinating world of Finland's Olkiluoto Nuclear Power Plant - home to Europe's strongest reactor, the Energizer Bunny of the nuclear world, and just a hop, skip, and a jump from the bustling metropolis of Pori!"""}
  ],
  "get_message": lambda input_message: f"""Could you write another summary? Here are some information about it: {input_message}""",
  "extract": lambda text: extract_summary(text=text),
}

interviewConfig = {
    "system_prompt": """You are an AI language model that generates an entertaining interview between two speakers discussing the intricacies and fascinating aspects of a specific topic. Ensure that the dialogue is engaging, informative, and captures the audience's attention. The speakers must be called Interviewer and Expert so the text can be used.""",
      "messages": [
       {"role": "user", "content": """Could you send me a script of an interview? Here is the text the interview should be based on:

In Persia's semi-desert towns, oases were fed through aqueducts carrying mountain water to support intensive food production, nurtured by wastes from the communities.[5] In Machu Picchu, water was conserved and reused as part of the stepped architecture of the city, and vegetable beds were designed to gather sun in order to prolong the growing season.[5]
The idea of supplemental food production beyond rural farming operations and distant imports is not new. It was used during war and depression times when food shortage issues arose, as well as during times of relative abundance. Allotment gardens emerged in Germany in the early 19th century as a response to poverty and food insecurity.[6]
In 1893, citizens of a depression-struck Detroit were asked to use vacant lots to grow vegetables. They were nicknamed Pingree's Potato Patches after the mayor, Hazen S. Pingree, who came up with the idea. He intended for these gardens to produce income, food supply, and boost independence during times of hardship.[7] Victory gardens sprouted during WWI and WWII and were fruit, vegetable, and herb gardens in the US, Canada, and UK. This effort was undertaken by citizens to reduce pressure on food production that was to support the war effort.
During World War I, President Woodrow Wilson called upon all American citizens to utilize any available open food growth, seeing this as a way to pull them out of a potentially damaging situation.[8] Since most of Europe was consumed with war, they were unable to produce sufficient food supplies to be shipped to the US and a new plan was implemented with the goal of feeding the US and even supply a surplus to other countries in need. By 1919, over 5 million plots were growing food and over 500 million pounds of produce was harvested.
A very similar practice came into use during the Great Depression that provided a purpose, job and food to those who would otherwise be without anything during such harsh times. These efforts helped raise spirits and boost economic growth. Over 2.8 million dollars worth of food was produced from the subsistence gardens during the Depression. By World War II, the War/Food Administration set up a National Victory Garden Program that set out to systematically establish functioning agriculture within cities. With this new plan in action, as many as 5.5 million Americans took part in the victory garden movement and over nine million pounds of fruit and vegetables were grown a year, accounting for 44% of US-grown produce throughout that time.[9]"""},
           {"role": "assistant", "content": """Interviewer: Welcome to today's show! Today, we have a special guest, an expert in the history of urban agriculture. Please welcome our Dr. Green! Dr. Green, Can you give us a brief introduction to urban agriculture and its historical significance?

Expert: Thank you for having me! Urban agriculture is the practice of growing, processing, and distributing food in or around urban areas. Its roots can be traced back to ancient civilizations like Persia and the Inca Empire, where people used innovative techniques to support intensive food production. The concept has been adapted in various forms throughout history, particularly during times of war, depression, or food shortages.

Interviewer: That's fascinating! Can you tell us more about how the concept evolved in different cultures and contexts?

Expert: Absolutely! In ancient Persia, they built aqueducts to carry water from the mountains to their semi-desert towns, creating oases that supported food production. The Incas, on the other hand, designed their city of Machu Picchu with water conservation and reuse in mind, as well as maximizing sunlight exposure for their vegetable beds.

Interviewer: It seems like urban agriculture has always been a solution to food scarcity. Can you tell us about the emergence of allotment gardens in Germany?

Expert: Yes, allotment gardens first appeared in Germany in the early 19th century as a response to poverty and food insecurity. They provided people with a small piece of land to grow their own food, improving their self-sufficiency and access to fresh produce.

Interviewer: I've heard about "Pingree's Potato Patches" and Victory Gardens during the World Wars. Can you explain how these initiatives came about and their impact?

Expert: During the late 19th and early 20th centuries, urban agriculture gained traction in times of crisis. In 1893, Detroit's Mayor Hazen S. Pingree encouraged citizens to grow vegetables on vacant lots to combat the depression. These gardens provided food and a source of income for struggling families. Victory Gardens emerged during WWI and WWII in the US, Canada, and the UK, as a way to reduce pressure on food production needed to support the war effort. By WWII, 44% of US-grown produce came from these gardens.

Interviewer: It's incredible how urban agriculture played a crucial role during such difficult times. What was the government's role in promoting these initiatives?

Expert: In both World War I and II, the US government played an active role in promoting urban agriculture. President Woodrow Wilson called upon citizens to grow food in any available space during WWI, and by 1919, there were over 5 million plots in use. During the Great Depression, subsistence gardens helped boost morale and economic growth. During WWII, the War/Food Administration established the National Victory Garden Program to encourage systematic urban agriculture, leading to the participation of 5.5 million Americans.

Interviewer: Thank you, Dr. Green, for sharing your knowledge about the history of urban agriculture. It's amazing to see how this practice has helped communities throughout history to overcome adversity and become more self-sufficient.

Expert: My pleasure! Urban agriculture is a testament to human ingenuity and resilience. It's a fascinating subject that continues to evolve and has the potential to shape our future in sustainable ways."""}
  ],
  "get_message": lambda input_message: f"""Could you send me another interview? Here are some information about it: {input_message}""",
  "extract": lambda text: extract_interview(text=text),
  
}

conclusionConfig = {
    "system_prompt": """You are an AI language model that generates an entertaining conclusion about a text. Ensure that the conclusion is engaging, informative, and captures the audience's attention. The conclusion should be no longer than three sentences.""",
      "messages": [
       {"role": "user", "content": """Could you send me a conclusion of an text? Here is the text:
        
In Persia's semi-desert towns, oases were fed through aqueducts carrying mountain water to support intensive food production, nurtured by wastes from the communities.[5] In Machu Picchu, water was conserved and reused as part of the stepped architecture of the city, and vegetable beds were designed to gather sun in order to prolong the growing season.[5]
The idea of supplemental food production beyond rural farming operations and distant imports is not new. It was used during war and depression times when food shortage issues arose, as well as during times of relative abundance. Allotment gardens emerged in Germany in the early 19th century as a response to poverty and food insecurity.[6]
In 1893, citizens of a depression-struck Detroit were asked to use vacant lots to grow vegetables. They were nicknamed Pingree's Potato Patches after the mayor, Hazen S. Pingree, who came up with the idea. He intended for these gardens to produce income, food supply, and boost independence during times of hardship.[7] Victory gardens sprouted during WWI and WWII and were fruit, vegetable, and herb gardens in the US, Canada, and UK. This effort was undertaken by citizens to reduce pressure on food production that was to support the war effort.
During World War I, President Woodrow Wilson called upon all American citizens to utilize any available open food growth, seeing this as a way to pull them out of a potentially damaging situation.[8] Since most of Europe was consumed with war, they were unable to produce sufficient food supplies to be shipped to the US and a new plan was implemented with the goal of feeding the US and even supply a surplus to other countries in need. By 1919, over 5 million plots were growing food and over 500 million pounds of produce was harvested.
A very similar practice came into use during the Great Depression that provided a purpose, job and food to those who would otherwise be without anything during such harsh times. These efforts helped raise spirits and boost economic growth. Over 2.8 million dollars worth of food was produced from the subsistence gardens during the Depression. By World War II, the War/Food Administration set up a National Victory Garden Program that set out to systematically establish functioning agriculture within cities. With this new plan in action, as many as 5.5 million Americans took part in the victory garden movement and over nine million pounds of fruit and vegetables were grown a year, accounting for 44% of US-grown produce throughout that time.[9]"""},
           {"role": "assistant", "content": """In the face of adversity, humanity has historically turned to urban agriculture as a means of sustenance and resilience. From ancient Persia to the victory gardens of WWII, communities have united to grow food in times of hardship and abundance alike. The enduring legacy of these gardens highlights the power of ingenuity, collaboration, and resourcefulness in addressing global challenges."""}
  ],
  "get_message": lambda input_message: f"""Could you send me another conclusion? Here is the text: 
  
  {input_message}
  
  """,
  "extract": lambda text: extract_conclusion(text=text),
    }

def extract_summary(text:str): 
  return [{
      "text" : text , 
      "file_name": f"{text[:10]}.wav", 
      "voice": VoiceMale
      }]

def extract_interview(text: str) -> list:
    pattern = r"(Interviewer|Expert): (.*?)\n"
    matches = re.findall(pattern, text, re.MULTILINE)
    extracted_text = [{
      "text" : match[1] , 
      "file_name": f"{match[1][:10]}.wav", 
      "voice": VoiceMale if match[0] == "Interviewer" else VoiceFemale
      } for match in matches]
    
    return extracted_text

def extract_conclusion(text:str):
      return [{
      "text" : text , 
      "file_name": f"{text[:10]}.wav", 
      "voice": VoiceMale
      }]
