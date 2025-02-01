# TutorGPT Project

**Overview**

TutorGPT is a Python-based program designed to interact with OpenAI's language model to generate, explain, and analyze algebra problems. This tool is built with educational use in mind, focusing on guiding students to better understand algebraic concepts. The system maintains memory of previous conversations to avoid duplication and improve interactions.

**Features**

- Problem Generation: Create new algebra word problems along with detailed solutions.

- Step-by-Step Explanations: Guide users through the process of solving algebra problems step by step.

- Mistake Analysis: Analyze potential mistakes students might make when solving algebra problems.

- Persistent Memory: Maintain conversation history to ensure context-aware interactions.

# Setup Instruction

**Prerequisites**

- Python 3.6 or higher

- An OpenAI API key

- python-dotenv library

**Installation**

- Clone this repository:
```bash
git clone <repository_url>
cd <repository_directory>
```

- Install dependencies:
```bash
pip install python-dotenv openai
```

- Create a .env file in the project directory and add your OpenAI API key:

```bash
API_KEY=your_openai_api_key_here
```

- Ensure that your dataset files are properly placed in a datasets directory.

# Usage

**Running the Program**

To start TutorGPT, run:

```bash
python start_gpt.py

```
# How It Works

- The program loads algebra problems from a specified dataset.

- It uses three prompt templates:

- Generate (g): Create a similar algebra word problem and provide a solution.

- Explain (e): Provide step-by-step guidance to solve a given problem.

- Analyze (a): Analyze potential mistakes students might make.

- The program randomly selects 50 problems for each prompt type.

- GPT responses are collected and stored in output.json for manual evaluation.

**Example .env File**

```bash
API_KEY=your_api_key_here
```

# Code Structure

- call_gpt(prompt): Interacts with OpenAI's API to generate responses.

- use_prompt_templates(dataset_path): Loads the dataset, selects random problems, prompts GPT, and stores responses.

- main(): Entry point for the program.

# Output

The generated responses are saved to output.json in the following format:
```python
[
  {
    "Prompt": "(g) Create a new algebra word problem similar to this...",
    "Response": "GPT-generated response here..."
  },
  {
    "Prompt": "(e) Explain the steps to solve this algebra problem...",
    "Response": "GPT explanation here..."
  }
]
```

# Important Notes

- The dataset size must be at least 150 entries, with valid sQuestion fields.

- Responses are evaluated manually to ensure educational quality.

- If the dataset is missing or insufficient, the program will raise appropriate errors.

- The program is built to use a datasetof questions, and a person to evaluate those answers.  If you would like to use it as an actual tutor. use the built in code and fork the repository to make a new main() function.  

# Potential Improvements

- Add automated response evaluation metrics.

- Incorporate a GUI for easier interaction.

- Support for additional problem types beyond algebra.

# License

This project is open-source and available under the MIT License.

