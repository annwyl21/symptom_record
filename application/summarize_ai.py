import os
import openai

openai.api_key = os.getenv("EllenOpenApiKey")

symptom_record = """Record of Symptoms over time<br>
06-06-2023 10:51<br>hip pain in right leg<br>
07-06-2023 21:15<br>difficulty standing from floor<br>
08-06-2023 09:10<br>trouble going to the toilet<br>
09-06-2023 08:00<br>painful to lie on right side in bed, pain located in right hip<br>
10-06-2023 12:00<br>stiff when standing up after sitting watching a film<br>
11-06-2023 11:30<br>left knee pain when walking to the shops<br>
13-06-2023 10:45<br>hip pain in right leg<br>
14-06-2023 07:30<br>stiff when getting up<br>
15-06-2023 06:30<br>stiff when getting up and pain in right hip when standing<br>
16-06-2023 10:10 <br>hip pain in right leg, difficulty using the stairs<br>"""

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Perform the following actions:\n- Summarise the text delimited by triple backticks with a focus on change over time in symptoms, eg which are worsening or improving. This summary is intended to be read by a doctor or a VET in order to make a diagnosis, an onward referral or prescribe treatment from these symptoms.\n- First, find out relevant symptoms from the information provided.\n- Then, summarise the information based on the relevant symptoms.\n- Use at most 3 sentences consisting of no more than 10 words.\n- Identify the status of symptoms, are they improving or worsening?\n- Identify the sentiment of the text, eg is it positive or negative\n- Separate your answers with line breaks.\nReread your summary before you return it to me and check that all the symptoms described do exist in the original text provided.\nUse the following format:\nSummary: <summary>\nSentiment: <sentiment>\nStatus: <status>\nTime period: <time period>\nText:\n```" + symptom_record + "```",
  temperature=0,
  max_tokens=493,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

