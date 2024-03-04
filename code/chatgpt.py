# !pip install langchain -q
# !pip install --upgrade openai -q
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback

API_KEY = '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'
# API_KEY = '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'
def Prompt(input, template):
  print('-------------------Prompt-----------------')
  template_functions = {
    'Product Improvement': product_improvement_prompt,
    'Feedback Scoring': feedback_scoring_prompt,
    'Marketing Campaign': campaign_idea_prompt,
    'Feedback Summarize': feedback_summarize
  }
  if template in template_functions:
    result = template_functions[template](input, API_KEY)
    return result
  else:
    # If no template is specified or the user set to default then run the API without template
    return "Template not found"

def product_improvement_prompt(input, API_KEY):
  product_improvement_template = '''
    Here is a desciprtion of a lipstick
    {input}
    Propose upgrades that involve the addition or removal of components,
    features, or functionalities to enhance the overall lipstick experience. Consider advancements in cosmetic technology, emerging beauty trends, and consumer demands.
    Your suggestions should not only align with Maybelline's brand identity but also present tangible enhancements that address customer concerns and elevate the product.
    Think creatively about changes to appearance, functionality, or formulation that could set a new standard for Maybelline's lipstick line.
    Give top 2 ideas, and make it short.
  '''
  prompt = PromptTemplate(template=product_improvement_template,
                          input_variables=['input'])
  llm = ChatOpenAI(api_key=API_KEY,
                   model = 'gpt-3.5-turbo',
                   temperature=0.7)
  product_idea_chain = LLMChain(llm=llm, prompt=prompt)

  with get_openai_callback() as cb:
    prompt.format(input=input)
    result = product_idea_chain.run(input=input)
    # campaign_idea_prompt.format()
    # campagin_idea_result = campaign_idea_chain.run()
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")

    return result

def feedback_scoring_prompt(input, API_KEY):
  feedback_scoring_template = '''
    Rate each comment above in numerical form according to the Likert scale (1: dissatisfied, 5: satisfied)
    Column names are criteria, Lipstick texture, Color fastness, Price, Lipstick appearance, Packaging, Color rendering, Scent, and Delivery respectively. 
    Each comment is a line in the table. Analyze the true meaning of the sentence to rate based on attributes, not infer information in the sentence to evaluate attributes not mentioned in the feedback. 
    For criteria with no information, the assigned value is N/A. Attributes are evaluated numerically and percentages are converted to a Likert rating scale.
    - Lipstick texture: is the state of cosmetics when applied to the skin of lipstick( also understand the quality or substance of the lipstick),
      such as matte, dry, soft, smooth, silky, powdery, liquid, texture, sticky, clumpy, light on lips, moisturizing lipstick…
    - Color Fastness: is the longevity of the color(examples of attributes such as  long lasting,  matte, fading, fast fading, tint,  no drift, matte lipstick, no matte,...)
    - Price: (examples of attributes such as expensive, cheap, reasonable)
    - Lipstick appearance: related to the product in terms of lipstick shell, product volume, weight, lipstick cap described for example: firm grip, light, heavy, little, much, sturdy, dirty, old…
    - Packaging: related to how Maybelline packages and prepares products to send to customers described for example carefully wrapping, careless, careful, not thorough, sketchy, torn , broken, not having a packaging box. 
    - Color rendering: is the display of color when applied to the lips that reflects the actual color compared to the product's described color like term of color described for example: beautiful lipstick, beautiful color, standard color, darker or lighter color, wrong color,...
    - Scent: means fragrance (examples of attributes such as fragrant, pungent, etc.)
    - Delivery: is only the act of taking goods and shipping them to customers, not mentioning the entire delivery process. Wrong product delivered, missing product, color mismatch, wrong code, missing gift, no gifts are NOT in delivery but all related to Packaging errors. Described as: careful, careless, slow, fast delivery.


    Here is the list of comment:
    {input}

    The output should be a json format
  '''
  prompt = PromptTemplate(template=feedback_scoring_template,
                          input_variables=['input'])
  llm = ChatOpenAI(api_key=API_KEY,
                    model = 'gpt-3.5-turbo',
                    temperature=0.7)
  product_idea_chain = LLMChain(llm=llm, prompt=prompt)

  with get_openai_callback() as cb:
    prompt.format(input=input)
    result = product_idea_chain.run(input=input)
    # campaign_idea_prompt.format()
    # campagin_idea_result = campaign_idea_chain.run()
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")

    return result

def campaign_idea_prompt(input, API_KEY):
  campaign_idea_template = '''
    Maybelline recently received valuable feedback on its lipstick range, including insightful product improvement suggestions.
    As a seasoned marketing expert, your task is to ideate innovative marketing campaigns that capitalize on these improvements and resonate with the target audience.
    Consider the upgraded lipstick features such as enhanced color range, improved texture, longer-lasting power, and innovative packaging.
    Craft compelling campaign ideas that highlight these improvements and communicate Maybelline's commitment to providing an exceptional lipstick experience.
    Think about creative angles, such as leveraging influencers to showcase the upgraded lipsticks, developing engaging social media challenges,
    or even collaborating with beauty experts for exclusive tutorials. Your goal is to generate excitement, build anticipation, and position Maybelline as a trendsetter in the beauty industry.
    Feel free to incorporate user testimonials, before-and-after visuals, and any other elements that can effectively communicate the enhanced qualities of Maybelline's lipstick line.
    Your campaign ideas should not only drive brand awareness but also encourage customer engagement and product adoption.
    Remember to tailor the campaigns to align with Maybelline's brand identity and values. Your creative input will play a crucial role in ensuring the success of these marketing initiatives.
    Let your imagination run wild, and propose ideas that will leave a lasting impact on Maybelline's audience.

    Here is the input from the users
    {input}

    Give top 2 idea, and make it short
  '''
  prompt = PromptTemplate(template=campaign_idea_template,
                          input_variables=['input'])
  llm = ChatOpenAI(api_key=API_KEY,
                   model = 'gpt-3.5-turbo',
                   temperature=0.7)
  product_idea_chain = LLMChain(llm=llm, prompt=prompt)
  
  with get_openai_callback() as cb:
    prompt.format(input=input)
    result = product_idea_chain.run(input=input)
    # campaign_idea_prompt.format()
    # campagin_idea_result = campaign_idea_chain.run()
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")

    return result

def feedback_summarize(input, API_KEY):
  feedback_summarize_template = '''
    "Given the following list of feedback, please provide a concise summary that captures the main information, 
    both positive and negative aspects, and highlight key keywords. Make it a short parapgrah
    The goal is to understand the overall sentiment and key points of the feedback."

    **Feedback List:**
    {input}
    **Instructions for ChatGPT:**

    - Summarize the main information of all the feedback.
    - Identify positive aspects mentioned in the feedback.
    - Identify negative aspects mentioned in the feedback.
    - Highlight key keywords that are frequently mentioned.
  '''

  prompt = PromptTemplate(template=feedback_summarize_template,
                          input_variables=['input'])
  llm = ChatOpenAI(api_key=API_KEY,
                   model = 'gpt-3.5-turbo',
                   temperature=0.7)
  product_idea_chain = LLMChain(llm=llm, prompt=prompt)
  
  with get_openai_callback() as cb:
    prompt.format(input=input)
    result = product_idea_chain.run(input=input)
    # campaign_idea_prompt.format()
    # campagin_idea_result = campaign_idea_chain.run()
    print(f"Total Tokens: {cb.total_tokens}")
    print(f"Prompt Tokens: {cb.prompt_tokens}")
    print(f"Completion Tokens: {cb.completion_tokens}")
    print(f"Total Cost (USD): ${cb.total_cost}")

    return result

def main():    
  input = 'Super Stay Matte Ink Lipstick'
  template = 'Marketing Campaign Idea'
  result = Prompt(input, template)

if __name__ == '__main__':
  main()





feedback_scoring_backup_prompt = '''
    Evaluate comments using a Likert scale (1-5) in a table with criteria columns: Lipstick Texture, Color Fastness, Price, Lipstick Appearance, Packaging, Color Rendering, Scent, and Delivery. 
    Assign numerical values based on provided definitions for each criterion. Consider only explicit information in comments; use N/A for criteria with no information. 
    Convert percentages to Likert ratings. 
    For Lipstick Texture, consider states like matte, dry, soft, etc. 
    For Color Fastness, evaluate attributes such as longevity, matte, fading, etc. 
    Assess Price as expensive, cheap, or reasonable. 
    Evaluate Lipstick Appearance based on product shell, volume, weight, etc. 
    Examine Packaging for descriptions like careful, careless, torn, etc. 
    Evaluate Color Rendering in terms of actual color vs. described color. 
    Assess Scent for attributes like fragrant, pungent, etc. 
    For Delivery, focus solely on shipping, considering attributes like careful, careless, slow, fast.
'''