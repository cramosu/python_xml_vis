"""
Simple XML visualizer for personal use. Allows parsing to txt and csv.
To load an XML, enter the filename (without the extension) on the textfield

by cramosu
"""

import xml.etree.ElementTree as ET
import tkinter as tk
import tkinter.scrolledtext as tkst
import csv

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(fill = 'both', expand = 'yes')
        self.createWidgets()
    
    def createWidgets(self):
        self.send_entry = tk.Entry(self)
        self.send_entry.pack(padx = 3, pady = 3)
        self.cam_xml = tk.Button(self, text = 'Cambiar XML', command = lambda: self.getXMLData(self.send_entry.get()))
        self.cam_xml.pack(padx = 3, pady = 3)
        self.exptxt = tk.Button(self, text = 'Exportar a TXT', fg = 'blue', command = lambda: self.toTXT(self.txt.get('1.0', 'end-1c'), self.send_entry.get()))
        self.exptxt.pack(padx = 3, pady = 3)
        self.expcsv = tk.Button(self, text = 'Exportar a CSV', fg = 'green', command = lambda: self.toCSV(self.txt.get('1.0', 'end-1c'), self.send_entry.get()))
        self.expcsv.pack(padx = 3, pady = 3)
        self.txt = tkst.ScrolledText(self, height = 20 , width = 20)
        self.txt.pack(padx = 3, pady = 3, fill=tk.BOTH, expand = True)
        self.QUIT = tk.Button(self, text = "Salir", fg = "red", command = main.destroy).pack(padx = 3, pady = 3, side = 'bottom')
    
    def getXMLData(self, nombre):
        tree=ET.parse(nombre + '.xml')
        root = tree.getroot()
        text = ''
        text = str(root.tag)
        for c1 in root:
            if(c1.text != None):
                text = text + "\n\t" + str(c1.tag) + "\t\t\t" + str(c1.text)
            else:
                text = text + "\n\t" + str(c1.tag)
            for c2 in c1:
                if(c2.text != None):
                    text = text + "\n\t\t" + str(c2.tag) + "\t\t\t" + str(c2.text)
                else:
                    text = text + "\n\t\t" + str(c2.tag)
                for c3 in c2:
                    if(c3.text != None):
                        text = text + "\n\t\t\t" + str(c3.tag) + "\t\t\t" + str(c3.text)
                    else:
                        text = text + "\n\t\t\t" + str(c3.tag)
        self.txt.delete('1.0','end-1c')
        self.txt.insert('1.0',text)
    
    def toTXT(self, texto, nombre):
        exp_n = nombre + ".txt"
        with open(exp_n, 'w') as out:
            out.write(texto + '\n')	

    def toCSV(self, texto,nombre):
        exp_n = nombre + ".csv"
        with open(exp_n, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='\t', dialect='excel')
            spamwriter.writerow([texto])

main = tk.Tk()
main.title("Visualizador XML")
main.geometry("1024x576")
app = Application(master=main)
app.mainloop()
