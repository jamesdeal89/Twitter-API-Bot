
# a basic implementation of a public fork of GPT3 AI. 
# dependencies: torch, transformers


from transformers import pipeline
    
def generate(prompt, length):
    # fetch GPT AI from it's source
    gptNEO = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

    # save a prompt for the AI
    question = prompt

    # process the prompt through the AI
    response = gptNEO(question, max_length=length, do_sample=True, temperature=0.9)

    # print the response
    return response[0]['generated_text']

