from Agents import CalculatorAgent

calc = CalculatorAgent(token="hf_hub_token")
print(calc.run("What is sqrt(((4 + 4)^2)+1)/72?"))