import requests 
import json
import gradio as gr
from src.constent import *



histroy = []


def generate_response(prompt):
    histroy.append(prompt)
    final_prompt = "\n".join( histroy)

    data = {
        "model": "LokiLogic",
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url,headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)
    

interface = gr.Interface(fn = generate_response,inputs=gr.Textbox(lines=4,placeholder="Hi am LokiLogic, How can I help you !!"), outputs="text")

interface.launch()