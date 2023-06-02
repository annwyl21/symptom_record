# Coursenotes: ChatGPT Prompt Engineering for Developers, DeepLearningAI, Andrew Ng
# https://learn.deeplearning.ai/chatgpt-prompt-eng

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

# PARAMETERS: temperature=0.0, max_tokens=64, top_p=1.0, frequency_penalty=0.0, presence_penalty=0.0, stop=["\n"]

# 1. `prompt`: This is the initial string of text that you provide to the model. The model uses this text as a basis to generate the subsequent text.

# 2. `max_tokens`: This is the maximum length of the generated text. If you set `max_tokens` to 100, the model will stop generating text after it has produced 100 tokens. A token can be as short as one character or as long as one word.

# 3. `temperature`: This parameter controls the randomness of the model's output. A higher value like 1.0 makes the output more diverse and creative, while a lower value like 0.1 makes the output more focused and deterministic.

# 4. `top_p`: This is a parameter for nucleus sampling, which is a strategy for generating diverse text. The `top_p` parameter specifies a cumulative probability cutoff. The model considers only the smallest set of words whose combined probability exceeds `top_p`, and then chooses randomly from that set.

# 5. `top_k`: This is a parameter for another sampling strategy. With `top_k` sampling, the model only considers the top k most probable next words when generating text. This strategy can help to prevent the model from generating highly improbable words.

# 6. `frequency_penalty`: This parameter encourages the model to use words that it doesn't use as often. A higher value makes the model more likely to use rare words.

# 7. `presence_penalty`: This parameter encourages the model to introduce new concepts rather than reusing concepts that are already in the text. A higher value makes the model more likely to introduce new ideas.

# 8. `best_of`: This parameter controls how many different completions the model generates for each prompt. The final result is the best one of these completions according to the model's own scoring system.

# TOP-P
# The parameter `top_p` refers to a sampling technique in natural language processing called nucleus sampling or `p`-sampling. 

# In language model like GPT, when generating text, the model assigns a probability to each possible next word. We could just choose the word with the highest probability each time, but this tends to lead to repetitive and sometimes non-sensical output. To introduce diversity and make the output more interesting, we can sample from this distribution instead of just choosing the maximum.

# `top_p` in this context represents the cumulative probability cut-off for nucleus sampling. In nucleus sampling, instead of sampling from the entire distribution, the model first eliminates options until the total cumulative probability exceeds the specified `top_p` value, and then picks randomly from among these remaining options.

# So, setting `top_p=1.0` would mean that you consider all possible next words (since the total probability sums up to 1.0), ordered by their probability. This is effectively the same as using regular sampling, where all options are considered but are picked with a frequency relative to their probability.

# However, if you set `top_p=0.9, for example, it means the model will only consider the smallest set of words whose combined probability is at least 0.9, thereby focusing on more probable options while still introducing some randomness into the choice.

# The key advantage of `top_p` sampling is that it balances the trade-off between diversity and quality of generated text better than alternatives such as temperature sampling or top-k sampling. It avoids overly random text (as can happen with high temperature) and overly deterministic or unsafe output (which can happen with top-k).

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

text = f"""
You should express what you want a model to do by \ 
providing instructions that are as clear and \ 
specific as you can possibly make them. \ 
This will guide the model towards the desired output, \ 
and reduce the chances of receiving irrelevant \ 
or incorrect responses. Don't confuse writing a \ 
clear prompt with writing a short prompt. \ 
In many cases, longer prompts provide more clarity \ 
and context for the model, which can lead to \ 
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \ 
into a single sentence.
```{text}```
"""
response = get_completion(prompt)
print(response)

# PRINCIPLES:

# be clear and specific
# use delimiters to separate the prompt from the user input
# ask for a structured output, eg html, json, etc
# check whether conditions are satisfied
# tell it what to do if it cant meet requirements
# few shot prompting, provide successful examples

# give the model time to think
# instruct the model to work out the solution before rushing to a conclusion
# 'First, work out your own solution, then compare your solution to the offered answer, then decide if the offered answer is correct"

# LIMITATIONS:

# hallucinations - fabricated ideas
# reduce hallucinations - 'First, find relevant information, then answer the question based on the relevant information'

# more reliable at following the instructions to create 3 sentences than a specific number of characters or words.
# decscribe the intended audience

#examples of prompts and test on multiple examples:
# At the end of the description, include every 7-character product id in the technical specification.
# after the descriotion, include a table that gives the products dimensions. the table should have 2 columns, the first colunm should be the product id, and the second column should be the products dimensions. give the table a name of "dimensions". format everything as html that can be used in a website, place the descritpin inside a <div> element.

# in the training video - google this code...
# from redlines import redlines
# diff = redlines(text, response)
# print(Markdown(diff.output_markdown))

# modify the temperature parameter to control the randomness of the model's output, 0 is predictable and reliably similar and 1 is unpredictable and wildly different.

# in the training video - google this code...
from redlines import redlines
diff = redlines(text, response)
print(Markdown(diff.output_markdown))
