# CodeLlamaAssistant
A versatile code assistant tool leveraging CodeLlama's Llama2 AI to enhance coding efficiency and accuracy for developers.


# Project Name: LokiLogic
This project is a multifaceted code assistant designed to aid developers in writing better code, learning new programming languages, and debugging efficiently. Created with the goal of enhancing the coding experience, it serves as an educational tool for those looking to expand their coding expertise while also offering robust debugging support. Whenever developers encounter errors, this assistant provides intelligent insights and solutions, streamlining the debugging process and reducing development time.

## Built With
- **Python**: The primary programming language used for developing the backend logic and functionalities.
- **Ollama**: Utilized for leveraging large language models efficiently with a focus on reducing computational demands and optimizing performance.
- **CodeLlama**: Integrated for advanced natural language processing capabilities, enhancing the interaction between the user and the code through sophisticated language models.
- **LangChain**: Applied to link various language models and services seamlessly, enabling more complex and versatile language-based applications.
- **Gradio**: Employed to create a user-friendly web interface that allows users to interact with the model easily, providing inputs and receiving outputs directly.

## Getting Started
### Prerequisites
- Python 3.x
- Ollama


### Installation

## STEP 01 - Clone the repository
Clone the repo
   ```bash
   git clone https://github.com/AmarnathaGowda/CodeLlamaAssistant.git
   ```

### STEP 02- OLLAMA Setup

* Download the Ollama CLI from the [official website](https://ollama.com)

![alt text](https://github.com/AmarnathaGowda/CodeLlamaAssistant/blob/main/asset/Ollama.png)

* On your favort terminal, run the following command to install the ollama

```bash
ollama run codellama
```
![alt text](https://github.com/AmarnathaGowda/CodeLlamaAssistant/blob/main/asset/ollama2.png)

* Once the installation is complete, run the following command to create the custom model

```bash
ollama create LokiLogic -f Modelfile
```


### STEP 03- Create a conda environment after opening the repository

```bash
conda create -n CodeLlamaAssistantEnv python -y
```

```bash
conda activate CodeLlamaAssistantEnv
```


### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```
```bash
open up localhost:
```