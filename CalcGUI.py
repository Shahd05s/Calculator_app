#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:39:59 2025

@author: shahdalharthy
"""
import tkinter as tk
from tkinter import messagebox
import math
from calc import Mathematics  # Importin backend class

#scientefec calculator class to create the GUI 
class ScientificCalculator:
    def __init__(self, root):
        self.root = root #Initialize the window 
        self.root.title("Scientific Calculator") #windows title 
        self.root.geometry("500x600") #set the windows geometry 
        self.root.config(bg="#293C4A") #bg colour 
         
        self.mathop = Mathematics()  # Initialize backend class
        
        self.expression = ""
        self.input_var = tk.StringVar() 
        
        #self.instructions=tk.Label(self.root, text="in order to use the Operations enter the value (number) first then click the button ex: (0.5 arcsin) ", font=("Aptos", 7),fg="white", bg="#2b2b2b")
        #self.instructions.grid(row=2, sticky="nsew")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Entry widget for displaying the user input and results
        entry = tk.Entry(self.root, textvariable=self.input_var, font=("Arial", 24), bd=10, relief=tk.FLAT, justify='right', bg="#2b2b2b", fg="white")
        entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=20, padx=10, pady=10, sticky="nsew")
        
        #instructions label
        instructions_label = tk.Label(self.root, text="In order to use the Operations enter the value (number) first then click the button ex: (0.5 arcsin)", font=("Arial", 11), bg="#293C4A", fg="white")
        instructions_label.grid(row=1, column=0, columnspan=5, pady=5)
        
        # Define button styling
        button_style = {"font": ("sans-serif", 20 ,"bold"), "width": 6, "height": 2,         "bg": "#3C3636", "fg": "#000", "bd": 1, "relief": tk.FLAT }
        special_button_style = {"font": ("sans-serif", 20 ,"bold"), "width": 6, "height": 2, "bg": "#BBB",    "fg": "#c20c0c", "bd": 1, "relief": tk.FLAT}  # Special styling for '=' and 'AC' buttons
        
        # Define calculator buttons and their grid positions
        buttons = [
            ('arcsin', 3, 0), ('arccos', 3, 1), ('arctan', 3, 2), ('log', 3, 3), 
            ('sin', 4, 0), ('cos', 4, 1), ('tan', 4, 2), ('x²', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('π', 5, 2), ('²√', 5, 3),
            ('7', 6, 0), ('8', 6, 1), ('9', 6, 2), ('DEL', 6, 3), ('AC', 6, 4),
            ('4', 7, 0), ('5', 7, 1), ('6', 7, 2), ('*', 7, 3), ('/', 7, 4),
            ('1', 8, 0), ('2', 8, 1), ('3', 8, 2), ('+', 8, 3), ('-', 8, 4),
            ('0', 9, 0), ('.', 9, 1), ('=', 9, 3)
        ] 

        

        # Create and position buttons on the grid
        for (text, row, col) in buttons:
            style = special_button_style if text in {"=", "AC"} else button_style
            tk.Button(self.root, text=text, **style,
                      command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col, padx=0.5, pady=0.5, sticky="nsew")
        
        # Configure row and column weights for responsiveness
        for i in range(8):
            self.root.grid_rowconfigure(i, weight=2)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=2)
    
    def on_button_click(self, button_text):
        # Handle button clicks
        if button_text == "=":
            self.calculate()
            
        elif button_text == "AC":
            self.expression = ""
            self.input_var.set("")  # Clear the display 
            
        elif button_text == "DEL":
            self.expression = self.expression[:-1]  # Remove last character
            self.input_var.set(self.expression)
            
        elif button_text == "π":
            self.expression += str(math.pi)
            self.input_var.set(self.expression)
            

        elif button_text in {"sin", "cos", "tan", "arcsin", "arccos", "arctan", "²√" , "x²","log"}:
            self.calculate_function(button_text)  # Handle trigonometric and square root functions
        else:
            self.expression += button_text  # Append character to expression
            self.input_var.set(self.expression)
            
    
    def calculate(self):
        # Evaluate the mathematical expression 
        try:

            result = eval(self.expression, {"__builtins__": None}, {"math": math, "pow": pow,
                           "sin": math.sin, "cos": math.cos, "tan": math.tan,
                           "sqrt": math.sqrt, "asin": math.asin, "acos": math.acos, "atan": math.atan})
            self.input_var.set(result)
            self.expression = str(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
    
    def calculate_function(self, func):
        # Perform trigonometric , square root, square and log calculations
        try:
            value = float(self.expression) if self.expression else ""
            if func == "sin":
                result = self.mathop.sine(value)                
            elif func == "cos":
                result = self.mathop.cosine(value)
            elif func == "tan":
                result = self.mathop.tangent(value)
            elif func == "²√": 
                result = self.mathop.square_root(value)
            elif func == "x²": 
                result = self.mathop.square(value)  
            elif func == "log":
                result = math.log10(value) if value > 0 else float('nan') 
            elif func == "arcsin": 
                result = self.mathop.arcsine(value) 
            elif func == "arccos": 
                result = self.mathop.arccos(value) 
            elif func == "arctan": 
                result = self.mathop.arctan(value) 
            
                
            self.input_var.set(result) 
            self.expression = str(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Function Input")

if __name__ == "__main__":
    # Initialize and run the application
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
