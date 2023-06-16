# FIRST ATTEMPT CREATED FOLLOWING THE OPENAI TUTORIAL - SIGNIFICANTLY MODIFIED FOLLOWING OPEN AI PLAYGROUND EXPERIMENTS

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# SUGGESTED PARAMETERS FOR MY TOOL
# temperature: Use a low temperature, such as 0.1 or 0.2. This will make the model's outputs more deterministic and focused, sticking closer to what it perceives as the most likely outputs. This reduces randomness and can help avoid hallucinations.
# max_tokens: Set this parameter to a value that makes sense for your application. You want to allow the model to generate a complete summary, but setting max_tokens too high can lead to rambling or irrelevant details.
# frequency_penalty and presence_penalty: You may want to set these parameters to 0, to avoid encouraging the model to use rare words or introduce new concepts, both of which could lead to inaccuracies or hallucinations.

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0.0, max_tokens=64, frequency_penalty=0.0, presence_penalty=0.0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

prompt = f"""
Perform the following actions:
- Summarise the text delimited by triple backticks with a focus on change over time in symptoms, eg which are worsening or improving. This summary is intended to be read by a doctor or a VET in order to make a diagnosis, an onward referral or prescribe treatment from these symptoms.
- First, find out relevant symptoms from the information provided.
- Then, summarise the information based on the relevant symptoms.
- Use at most 3 sentences and include 1 extract.

- Identify the status of symptoms, are they improving or worsening?
- Identify the sentiment of the text, eg is it positive or negative?
- Separate your answers with line breaks.

Reread your summary before you return it to me and check that all the symptoms described do exist in the original text provided.

Use the following format:
Summary: <summary>
Sentiment: <sentiment>
Status: <status>
Time period: <time period>

Text:
```{text}```
"""
response = get_completion(prompt)
print(response)

# transforming text into a different language
language = 'spanish'
prompt_translation = f"""
{prompt}
1 - Reword the text summary as if you are explaining this to a 5-yr old.
2 - Translate the summary into {language}.

Text:
```{text}```
"""
response = get_completion(prompt_translation)
print(response)

# ChatGPT4 - wrote this prompt for me - use it as a test basis to see if my constructed prompt provides a superior summary
# Prompt_chatgpt4 = f"""
# Given the list of dates, times, and descriptions of medical symptoms for a person or a pet provided below, please generate a concise summary that accurately reflects this information. Your summary should collate the dates into a relevant time period, and only include details that are explicitly contained within the text. It's essential that no additional information or fabrications are included.
# {text}
# Please provide a succinct summary paragraph detailing the time frame and medical symptoms described above.
# """
