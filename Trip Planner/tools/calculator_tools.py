from langchain.tools import tool

class CalculatorTools():

    # decorator.
    @tool("Make a Calculation")
    def calculate(operation):
        """
        Useful to perform any mathematical calucaltions.
        The input should be a mathematical expression.
        Eg. 2+2, 3*4, 5/2, 10-5 etc
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Invalid operation. Please provide a valid mathematical expression."