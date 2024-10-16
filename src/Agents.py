from transformers import pipeline
from transformers.agents import TransformersEngine, ReactJsonAgent
from tools import add_numbers, raise_to_power, subtract_numbers, multiply_numbers, divide_numbers, calculate_modulus

class CalculatorAgent(ReactJsonAgent):
    def __init__(self, token):
        pipe = pipeline(model="meta-llama/Llama-3.2-3B-Instruct", tokenizer="meta-llama/Llama-3.2-3B-Instruct", token=token, max_new_tokens=500)
        llm_engine = TransformersEngine(pipeline=pipe)

        #read in custom prompt file:
        with open("custom_prompt.txt", 'r') as file:
            lines = file.readlines()
            self.system_prompt = '\n'.join(line.strip() for line in lines)
        
        super().__init__(
            tools=[add_numbers, raise_to_power, subtract_numbers, multiply_numbers, divide_numbers, calculate_modulus],
            llm_engine=llm_engine,
            system_prompt=self.system_prompt
        )