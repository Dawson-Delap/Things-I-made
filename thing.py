import tkinter as tk
t = 2 
while t > 0:
    t = t ** t

    def create_window(title):
        # Create the main application window
        window = tk.Tk()
        window.title(title)
        
        # Create a label with the word "BANANA" in yellow text
        label = tk.Label(window, text="BANANA", font=("Arial", 50), fg="yellow")
        label.pack(padx=20, pady=20)
        
        # Set the window size
        window.geometry("400x200")
        
        return window

    def main():
        num_windows = t  # Change this number to create the desired number of windows
        
        # Create multiple windows
        windows = []
        for i in range(num_windows):
            title = f"Banana Window {i+1}"
            windows.append(create_window(title))
        
        # Run the application
        tk.mainloop()

    if __name__ == "__main__":
        main()
