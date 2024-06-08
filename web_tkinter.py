from tkinter import *
import tkinterweb
import sys

class Browser(Tk):
    def __init__(self):
        super(Browser,self).__init__()
        self.title("Tk Browser")
        try:
            browser = tkinterweb.HtmlFrame(self)
            browser.load_website("https://www.google.com")
            browser.pack(fill="both",expand=True)
        except Exception:
            sys.exit()
            
            
def main():
    browser = Browser()
    browser.mainloop()
    
if __name__ == "__main__":
    main()