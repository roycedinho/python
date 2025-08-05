class Expression:
    def __init__(self, expression):
        self.expression = expression
        
    def solve(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def display(self):
        result = self.solve()
        print(f"The result of '{self.expression}' is: {result}")

# Main Program
if __name__ == "__main__":
    expr_input = input("Enter a mathematical expression (e.g. 3+5*2): ")
    expr = Expression(expr_input)
    expr.display()
