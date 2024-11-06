import tkinter as tk
from tkinter import messagebox

class KnapsackSolverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("0/1 Knapsack Problem Solver")

        self.items = []
        
        # GUI components
        self.num_items_label = tk.Label(root, text="Number of Items:")
        self.num_items_label.grid(row=0, column=0, padx=10, pady=5)

        self.num_items_entry = tk.Entry(root)
        self.num_items_entry.grid(row=0, column=1, padx=10, pady=5)

        self.weight_label = tk.Label(root, text="Weight of Item:")
        self.weight_label.grid(row=1, column=0, padx=10, pady=5)

        self.weight_entry = tk.Entry(root)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=5)

        self.value_label = tk.Label(root, text="Value of Item:")
        self.value_label.grid(row=2, column=0, padx=10, pady=5)

        self.value_entry = tk.Entry(root)
        self.value_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_item_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_item_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.solve_button = tk.Button(root, text="Solve Knapsack", command=self.solve_knapsack)
        self.solve_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.grid(row=5, column=0, padx=10, pady=5)

        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    def add_item(self):
        try:
            weight = int(self.weight_entry.get())
            value = int(self.value_entry.get())
            self.items.append((weight, value))
            self.weight_entry.delete(0, tk.END)
            self.value_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Item added: Weight={weight}, Value={value}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integers for weight and value")

    def solve_knapsack(self):
        try:
            num_items = int(self.num_items_entry.get())
            if num_items != len(self.items):
                messagebox.showerror("Input Error", f"Number of items entered does not match the number of items added ({len(self.items)} added)")
                return

            capacity = int(self.weight_entry.get()) # Repurposing weight entry for capacity input
            result = self.knapsack(self.items, capacity)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Maximum value: {result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid integer for capacity")

    def knapsack(self, items, capacity):
        n = len(items)
        dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
        for i in range(n + 1):
            for w in range(capacity + 1):
                if i == 0 or w == 0:
                    dp[i][w] = 0
                elif items[i-1][0] <= w:
                    dp[i][w] = max(items[i-1][1] + dp[i-1][w-items[i-1][0]], dp[i-1][w])
                else:
                    dp[i][w] = dp[i-1][w]
        return dp[n][capacity]

if __name__ == "__main__":
    root = tk.Tk()
    app = KnapsackSolverApp(root)
    root.mainloop()
