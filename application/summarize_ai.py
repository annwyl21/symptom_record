import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Perform the following actions:\n- Summarise the text delimited by triple backticks with a focus on change over time in symptoms, eg which are worsening or improving. This summary is intended to be read by a doctor or a VET in order to make a diagnosis, an onward referral or prescribe treatment from these symptoms.\n- First, find out relevant symptoms from the information provided.\n- Then, summarise the information based on the relevant symptoms.\n- Use at most 3 sentences consisting of no more than 10 words.\n- Identify the status of symptoms, are they improving or worsening?\n- Identify the sentiment of the text, eg is it positive or negative\n- Separate your answers with line breaks.\nReread your summary before you return it to me and check that all the symptoms described do exist in the original text provided.\nUse the following format:\nSummary: <summary>\nSentiment: <sentiment>\nStatus: <status>\nTime period: <time period>\nText:\n```string```",
  temperature=0,
  max_tokens=493,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

