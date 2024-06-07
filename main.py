from gpt4all import GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", device='gpu')
from text import prompt

#next steps:
#feed the data into the LLM and generate some analysis from the synthetic data.
#create a multi-shot format to give it a template to follow

def stop_on_token_callback(token_id, token_string):
    # one sentence is enough:
    if '|' in token_string:
        return False
    else:
        return True

output = model.generate(f"Describe disneyworld, type '|' when you are done with "
                        "this prompt and ready to move onto the next one. Don't type that until after"
                        "this prompt is completed, not before.", callback=stop_on_token_callback,
                        n_batch=10, temp=1, max_tokens=10000)
print(output)


#next steps
#test the integration with libreoffice's API
#test the chat feature with gpt4all
#obtain a local image generation ai
#make a simple script to generate synthetic data
