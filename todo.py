import json
import os
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue") 

root = customtkinter.CTk()
root.geometry("500x300")

def login():
    print("Test")

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady=20, padx= 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame, text="Applicazione Agenda") #si può mettere dfont
label.pack(pady = 12,padx = 10)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text="Todo1")
entry1.pack(pady=12,padx = 10)

entry2 = customtkinter.CTkEntry(master = frame, placeholder_text="Todo2")
entry2.pack(pady=12,padx = 10)

button = customtkinter.CTkButton(master = frame,text="Login",command = login)

button.pack(pady = 12,padx = 12)

checkbox = customtkinter.CTkCheckBox(master = frame, text = "Remember Me")
checkbox.pack(pady=12, padx = 10)

root.mainloop()

TODO_FILE = "file.json"

# Carica i todos all'inizio (se il file esiste)
if os.path.exists(TODO_FILE):
    with open(TODO_FILE, "r") as infile:
        todos = json.load(infile)
else:
    todos = []

def visualizzazione(todos):
    if not todos:
        print("Nessun todo presente!")
    else:
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo}")

def salva_todos(todos):
    with open(TODO_FILE, "w") as outfile:
        json.dump(todos, outfile, indent=2)

while True:
    command = input("\nInserire istruzione (V per visualizzare, T per aggiungere todo, R per rimuovere, Q per chiudere)\n> ")
    
    if command == "V":
        visualizzazione(todos)
    
    elif command == "T":
        todo = input("Inserire todo: \n> ")
        todos.append(todo)
        salva_todos(todos)  # Salva SUBITO
        print(f"✅ Aggiunto: {todo}")
    
    elif command == "R":
        todo = input("Inserire todo da rimuovere: \n> ")
        if todo in todos:
            todos.remove(todo)
            salva_todos(todos)  # Salva SUBITO
            print(f"🗑️ Rimosso: {todo}")
        else:
            print("❌ Todo non presente")
    
    elif command == "Q":
        salva_todos(todos)  # Salva prima di uscire
        print("👋 Arrivederci!")
        break
    
    else:
        print("❌ Comando non valido! Usa V, T, R o Q")

