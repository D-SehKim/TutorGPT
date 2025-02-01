from openai import OpenAI
from dotenv import load_dotenv
import random
import json
import os

load_dotenv()

'''
loading API key along with model
To run the Program, you must have a .env file in this directory with a sufficient API_key titled "API_KEY"
'''
client = OpenAI(
    api_key=os.getenv("API_KEY"),
)

'''
Prompt that the system will follow, to edit, add a slash and tell system how to react
'''
MESSAGES=[
    {
        "role": "system", 
        "content": "You are a helpful math tutor, \
                    always attempting to teach an answer instead of giving it outright.  \
                    If the user asks to explain a problem, try to always guide to an answer step-by-step, as simply as possible.  \
                    If the user asks to create or analyze, try to keep your response to only the nessecary details \
                    Try to type your responses in plaintext.  If the user ever types 'QUIT' then thank them for \
                    their time and for using TutorGPT as that is the way of signalling to program end."
    }
    ]

def call_gpt(prompt):
    '''
    Calls TutorGPT.  TutorGPT has memory and will remember previous calls along with it's answers.  
    This is in an attempt to limit duplication in problem generation.  

    prompt (string): The prompt to call GPT with.

    returns (string): the message that GPT responded to the prompt with.  
    '''
    MESSAGES.append({
        "role": "user",
        "content": prompt
    })
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=MESSAGES
    )
    MESSAGES.append({
        "role": "assistant",
        "content": completion.choices[0].message.content
    })
    return completion.choices[0].message.content

''',
3 different prompt templates to prompt GPT with.  
'''
PROMPTS = {
    "g": "Create a new algebra word problem similar to this along with the solution: {problem}",
    "e": "Explain the steps to solve this algebra problem: {problem}",
    "a": "Analyze potential mistakes a student might make with this problem: {problem}",
}


def use_prompt_templates(dataset_path):
    '''
    loads the datasets and prompts GPT with a random chance to choose 1 of the 3 of the prompt template
    Stores GPT's answers in a JSON file with format of: 
    Prompt: (g: generate, e: explain, a: analyze)
    Repsonse: (GPT's response)

    Use call_gpt(prompt) to prompt gpt, (it returns a string)

    Due to the complex nature of the responses and the differing nuances that can occur, we have 
    decided that the best way to evaluate responses is manually with humans.  

    In order to reduce fatuigue of manually sifting through 500 different responses, we have decided to randomly
    select 50 different responses from GPT for each prompt type.  This way, we can collect a decent sample size
    and make sure that we get a accurate sample of the population of the responses.  
    '''
    # TODO: dataset size is 195 (dolphin) + 143 (draw) + 128 (kushman) = 466

    # Ensure the dataset has enough problems 
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found at: {dataset_path}")
    with open(dataset_path, "r") as f:
        dataset = json.load(f)

    if len(dataset) < 150:
        raise ValueError("Dataset must contain at least 150 entries.")

    # Process each prompt type
    problems = [item["sQuestion"] for item in dataset if "sQuestion" in item]

    if len(problems) < 150:
        raise ValueError("Dataset must contain at least 150 valid entries with 'sQuestion' field.")
    
    random.shuffle(problems)
    prompts_by_type = {
        "g": problems[:50],
        "e": problems[50:100],
        "a": problems[100:150]
    }
    
    responses = []

    # Generate GPT responses
    print('generating responses')
    for prompt_type, items in prompts_by_type.items():
        for data in items:
            data = data.strip()
            if not data:
                continue

            prompt = PROMPTS[prompt_type].format(problem=data)

            # Call GPT to get a response
            response = call_gpt(prompt)  # Assuming call_gpt is defined elsewhere

            # Store the prompt and response
            responses.append({
                "Prompt": f"({prompt_type}) {prompt}",
                "Response": response
            })

    # Save all responses to a JSON file
    print('saving respnsses')
    with open("output.json", "w") as f:
        json.dump(responses, f, indent=4)

    print(f"All responses saved to output_file")
    


def main():
    print("Welcome to TutorGPT!\n")
    use_prompt_templates("datasets/draw.json")


if __name__ == "__main__":
    main()
