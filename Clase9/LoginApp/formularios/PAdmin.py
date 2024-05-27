import json
import tkinter as tk
import uuid
import webbrowser
from tkinter import messagebox, ttk

import util.generic as utl
from formularios.Login import *


class PAdmin(tk.Tk):
    def __init__(self, name="", username="", email=""):
        self.name = name
        self.username = username
        self.email = email
        self.tipo_action ="Guardar"
        self.tipo_user = ""
        super().__init__()
        self.title("Panel Administrativo")
        self.resizable(False, False)
        # Obtener las dimensiones de la pantalla
        self.ancho_pantalla = self.winfo_screenwidth() #método para obtener Ancho
        self.alto_pantalla = self.winfo_screenheight() #método para obtener Alto

        # Establecer el tamaño completo de la ventana
        self.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}")
        
        menubar = tk.Menu(self)
        menuuser = tk.Menu(menubar, tearoff=0)
        menuuser.add_command(label="Administracion de Usuarios", command=self.main_usuarios)
        menubar.add_cascade(label="Usuarios", menu=menuuser)

        menuclientes = tk.Menu(menubar, tearoff=0)
        menuclientes.add_command(label="Administracion de Cliente", command=self.main_clientes)  
        menubar.add_cascade(label="Clientes", menu=menuclientes)

        menucategorias = tk.Menu(menubar, tearoff=0)
        menucategorias.add_command(label="Administracion de reservas", command=self.main_reservas)  
        menubar.add_cascade(label="Reservas", menu=menucategorias)

        menucanchas = tk.Menu(menubar, tearoff=0)
        menucanchas.add_command(label="Administracion de canchas", command=self.main_canchas)  
        menubar.add_cascade(label="canchas", menu=menucanchas)

        menuventas = tk.Menu(menubar, tearoff=0)
        menuventas.add_command(label="Administracion de Ventas", command=self.main_ventas)  
        menubar.add_cascade(label="Ventas", menu=menuventas)

        self.config(menu=menubar)

        # frame user_info

        self.frame_user_info = tk.Frame(self, bd=0,relief=tk.SOLID, width=200)
        self.frame_user_info.pack(side=tk.LEFT, padx=4, pady=5,fill="y")
        texto=tk.Label(self.frame_user_info, text="PANEL ADMINISTRATIVO", font=('Times', 20))
        texto.pack(padx=20,pady=4)
        self.usrimg = utl.leer_imagen(r"imagenesuserinfo.png", (128, 128))
        self.imgfacebook = utl.leer_imagen(r"imagenes\face.png", (32, 32))
        self.imglinkedin = utl.leer_imagen(r"imagenes\linkedin.png", (32, 32))
        self.imgwebsite = utl.leer_imagen(r"imagenes\website.png", (32, 32))
        self.imglogout = utl.leer_imagen(r"imagenes\logout.png", (32, 32))
        tk.Label(self.frame_user_info,image=self.usrimg).pack(padx=30,pady=4)
        tk.Label(self.frame_user_info, text=self.name, font=('Times', 14)).pack(padx=40,pady=4)
        tk.Label(self.frame_user_info, text=self.email, font=('Times', 14)).pack(padx=50,pady=4)
        tk.Button(self.frame_user_info,image=self.imgfacebook, command=self.abrirface).place(x=100,y=300)
        tk.Button(self.frame_user_info,image=self.imglinkedin, command=self.abrirlink).place(x=140,y=300)
        tk.Button(self.frame_user_info,image=self.imgwebsite, command=self.abrirweb).place(x=180,y=300)
        tk.Button(self.frame_user_info,image=self.imglogout, command=self.logout).place(x=220,y=300)
        
        #frame_data
        
        self.frame_data = tk.Frame(self, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_data.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)
        textobienvenida=tk.Label(self.frame_data, text="BIENVENIDO AL SISTEMA", font=('Times', 20))
        textobienvenida.pack(padx=20,pady=4)

        #frame_dinamyc
        self.frame_dinamyc = tk.Frame(self.frame_data, bd=0,relief=tk.SOLID, width=f"{self.ancho_pantalla-200}")
        self.frame_dinamyc.pack(side=tk.RIGHT, padx=4, pady=5, fill="both", expand=1)

    def main_usuarios(self):
        self.formulario_usuario()
        self.listar_usuarios()
    
        
    def formulario_usuario(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="\uf0c9 REGISTRO DE USUARIOS", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=30)
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Cedula:", font=('Times',14))
        labelcedula.place(x=70, y=100)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=40)
        self.ccedula.place(x=220, y=100)

        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre completo:", font=('Times',14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=40)
        self.cnombre.place(x=220, y=130)

        labelusuario = tk.Label(self.frame_dinamyc,text="Username:", font=('Times',14))
        labelusuario.place(x=70,y=160)
        self.cusuario = tk.Entry(self.frame_dinamyc, width=40)
        self.cusuario.place(x=220,y=160)

        labelclave = tk.Label(self.frame_dinamyc,text="Contraseña:", font=('Times',14))
        labelclave.place(x=500,y=100)
        self.cclave = tk.Entry(self.frame_dinamyc, width=40, show="*")
        self.cclave.place(x=600, y=100)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Correo:", font=('Times',14))
        labelcorreo.place(x=500,y=130)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=40)
        self.ccorreo.place(x=600, y=130)

        labeltipo = tk.Label(self.frame_dinamyc, text="Rol:", font=('Times',14))
        labeltipo.place(x=500,y=160)
        self.listatipo = tk.Listbox(self.frame_dinamyc, selectmode="Single", width=40, height=2)
        self.listatipo.place(x=600,y=160)
        self.listatipo.insert(1, "Administrador")
        self.listatipo.insert(2, "Vendedor")

        btnguardar = tk.Button(self.frame_dinamyc, text="\uf0c7 GUARDAR", font=('Times',14), command=self.save_user)
        btnguardar.place(x=870, y=130)
    
    def listar_usuarios(self):
        tk.Label(self.frame_dinamyc,text="\uf00b LISTADO DE USUARIOS", font=('Times',16),fg="#9fa8da").place(x=70, y=200)
        self.tablausuarios = ttk.Treeview(self.frame_dinamyc, columns=("NombreCompleto", "Username", "Email", "Rol"))
        self.tablausuarios.heading("#0", text="Cedula")
        self.tablausuarios.heading("NombreCompleto", text="Nombre Completo")
        self.tablausuarios.heading("Username", text="Usuario")
        self.tablausuarios.heading("Email", text="Email")
        self.tablausuarios.heading("Rol", text="Rol")
        with open(r"db_users.json", "r", encoding='utf-8') as self.file:
                self.db_users = json.load(self.file)
                for usuarios in self.db_users["users"]:
                    self.tablausuarios.insert("", "end", text=f'{usuarios["id"]}',values=(f'{usuarios["name"]}',f'{usuarios["username"]}',f'{usuarios["email"]}', f'{usuarios["role"]}'))
        self.tablausuarios.place(x=70, y=250)
        btneliminar = tk.Button(self.frame_dinamyc, text="\uf0c7 Eliminar", font=('Times',14), command=self.delete_user)
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="\uf0c7 Actualizar", font=('Times',14), command=self.update_user)
        btnupdate.place(x=200, y=520)

    def save_user(self):
        for index in self.listatipo.curselection():
            self.tipo_user = self.listatipo.get(index)
        if self.ccedula.get() =="" or self.cnombre.get() == "" or self.cusuario.get() == "" or self.ccorreo.get() == "" or self.cclave.get() == "" or self.tipo_user == "":
            messagebox.showinfo('Info',"Debe llenar todos los campos",parent=self)
            return 
        else:
                with open(r"db_users.json", "r", encoding='utf-8') as self.file:
                        self.db_users = json.load(self.file)

                        if self.tipo_action == "Actualizar":

                            for usuarios in self.db_users["users"]:
                                if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                                    usuarios["name"] = self.cnombre.get()
                                    usuarios["username"] = self.cusuario.get()
                                    usuarios["password"] =  self.cclave.get()
                                    usuarios["email"] = self.ccorreo.get()
                                    usuarios["role"] = self.tipo_user
                                    with open(r'db_users.json', 'w') as jf: 
                                        json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                                        messagebox.showinfo('Info',"Usuario actualizado con exito",parent=self)
                                        #self.listar_usuarios()
                                        self.limpiar_panel(self.frame_dinamyc)
                    
                        else:
                            self.db_users["users"].append({
                                            'id': self.ccedula.get(),
                                            'name': self.cnombre.get(),
                                            'username': self.cusuario.get(),
                                            'password': self.cclave.get(),
                                            'email': self.ccorreo.get(),
                                            'role':self.tipo_user
                                            })
                            with open(r'db_users.json', 'w') as jf: 
                                json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                                messagebox.showinfo('Info',"Usuario registrado con exito",parent=self)
                                self.limpiar_panel(self.frame_dinamyc) 


    def delete_user(self):
        with open(r"db_users.json", "r", encoding='utf-8') as self.file:
                self.db_users = json.load(self.file)
                for usuarios in self.db_users["users"]:
                    if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.db_users["users"].remove(usuarios)
                        with open(r'db_users.json', 'w') as jf:
                            json.dump(self.db_users, jf, indent=4, ensure_ascii=True)
                            messagebox.showinfo('Info',"Usuario eliminado con exito",parent=self)
                            self.limpiar_panel(self.frame_dinamyc)
                            break



    def update_user(self):
        with open(r"db_users.json", "r", encoding='utf-8') as self.file:
                self.db_users = json.load(self.file)
                for usuarios in self.db_users["users"]:
                    if usuarios["id"] == self.tablausuarios.item(self.tablausuarios.selection())["text"]:
                        self.ccedula.delete(0, tk.END)
                        self.ccedula.insert(0, usuarios["id"])
                        self.ccedula.config(state="disabled")
                        self.cnombre.delete(0, tk.END)
                        self.cnombre.insert(0,usuarios["name"])
                        self.cusuario.delete(0, tk.END)
                        self.cusuario.insert(0,usuarios["username"])
                        self.cclave.delete(0, tk.END)
                        self.cclave.insert(0,usuarios["password"])
                        self.ccorreo.delete(0, tk.END)
                        self.ccorreo.insert(0,usuarios["email"])
                        self.tipo_action = "Actualizar"

    def main_clientes(self):
        self.formulario_clientes()
        self.listar_clientes()

    def formulario_clientes(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="\uf0c9 REGISTRO DE CLIENTES", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=30)
        
        labelcedula = tk.Label(self.frame_dinamyc,text="Cedula:", font=('Times',14))
        labelcedula.place(x=70, y=100)
        self.ccedula = tk.Entry(self.frame_dinamyc, width=40)
        self.ccedula.place(x=220, y=100)

        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre completo:", font=('Times',14))
        labelnombre.place(x=70, y=130)
        self.cnombre = tk.Entry(self.frame_dinamyc, width=40)
        self.cnombre.place(x=220, y=130)

        labelcorreo = tk.Label(self.frame_dinamyc,text="Correo:", font=('Times',14))
        labelcorreo.place(x=500,y=130)
        self.ccorreo = tk.Entry(self.frame_dinamyc, width=40)
        self.ccorreo.place(x=600, y=130)
        
        labelnumero = tk.Label(self.frame_dinamyc,text="Numero:", font=('Times',14))
        labelnumero.place(x=500,y=130)
        self.cnumero = tk.Entry(self.frame_dinamyc, width=40)
        self.cnumero.place(x=600, y=130)

        btnguardar = tk.Button(self.frame_dinamyc, text="\uf0c7 GUARDAR", font=('Times',14), command=self.save_user)
        btnguardar.place(x=870, y=130)
        
    def listar_clientes(self):
        tk.Label(self.frame_dinamyc,text="\uf00b LISTADO DE CLIENTES", font=('Times',16),fg="#9fa8da").place(x=70, y=200)
        self.tablaclientes = ttk.Treeview(self.frame_dinamyc, columns=("NombreCompleto", "Numero", "Email"))
        self.tablaclientes.heading("#0", text="Cedula")
        self.tablaclientes.heading("NombreCompleto", text="Nombre Completo")
        self.tablaclientes.heading("Numero", text="")
        self.tablaclientes.heading("Email", text="Email")
        with open(r"db_clientes.json", "r", encoding='utf-8') as self.file:
                self.db_clientes = json.load(self.file)
                for clientes in self.db_clientes["users"]:
                    self.tablaclientes.insert("", "end", text=f'{clientes["id"]}',values=(f'{clientes["name"]}',f'{clientes["numero"]}',f'{clientes["email"]}'))
        self.tablaclientes.place(x=70, y=250)
        btneliminar = tk.Button(self.frame_dinamyc, text="\uf0c7 Eliminar", font=('Times',14), command=self.delete_clientes)
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="\uf0c7 Actualizar", font=('Times',14), command=self.update_clientes)
        btnupdate.place(x=200, y=520)

    def save_cliente(self):
        for index in self.listatipo.curselection():
            self.tipo_user = self.listatipo.get(index)
        if self.ccedula.get() =="" or self.cnombre.get() == "" or self.cnumero.get() == "" or self.ccorreo.get() == "" or self.cclave.get() == "" or self.tipo_user == "":
            messagebox.showinfo('Info',"Debe llenar todos los campos",parent=self)
            return 
        else:
                with open(r"db_clientes.json", "r", encoding='utf-8') as self.file:
                        self.db_clientes = json.load(self.file)

                        if self.tipo_action == "Actualizar":

                            for clientes in self.db_clientes["users"]:
                                if clientes["id"] == self.tablaclientes.item(self.tablaclientes.selection())["text"]:
                                    clientes["name"] = self.cnombre.get()
                                    clientes["username"] = self.cusuario.get()
                                    clientes["password"] =  self.cclave.get()
                                    clientes["email"] = self.ccorreo.get()
                                    with open(r'db_clientes.json', 'w') as jf: 
                                        json.dump(self.db_clientes, jf, indent=4, ensure_ascii=True)
                                        messagebox.showinfo('Info',"Cliente actualizado con exito",parent=self)
                                        #self.listar_clientes()
                                        self.limpiar_panel(self.frame_dinamyc)
                    
                        else:
                            self.db_clientes["clientes"].append({
                                            'id': self.ccedula.get(),
                                            'name': self.cnombre.get(),
                                            'username': self.cusuario.get(),
                                            'password': self.cclave.get(),
                                            'email': self.ccorreo.get(),
                                            'numero':self.cnumero.get(),
                                            })
                            with open(r'db_clientes.json', 'w') as jf: 
                                json.dump(self.db_clientes, jf, indent=4, ensure_ascii=True)
                                messagebox.showinfo('Info',"Cliente registrado con exito",parent=self)
                                self.limpiar_panel(self.frame_dinamyc) 


    
    def delete_clientes(self):
            with open(r"db_clientes.json", "r", encoding='utf-8') as self.file:
                self.db_clientes= json.load(self.file)
                for clientes in self.db_clientes["clientes"]:
                    if clientes["id"] == self.tablaclientes.item(self.tablaclientes.selection())["text"]:
                        self.db_clientes["clientes"].remove(clientes)
                        with open(r'db_clientes.json', 'w') as jf:
                            json.dump(self.db_clientes, jf, indent=4, ensure_ascii=True)
                            messagebox.showinfo('Info',"Cliente eliminado con exito",parent=self)
                            self.limpiar_panel(self.frame_dinamyc)
                            break

        
    def update_clientes(self):
            with open(r"db_clientes.json", "r", encoding='utf-8') as self.file:
                self.db_clientes = json.load(self.file)
                for clientes in self.db_clientes["clientes"]:
                    if clientes["id"] == self.tablaclientes.item(self.tablaclientes.selection())["text"]:
                        self.ccedula.delete(0, tk.END)
                        self.ccedula.insert(0, clientes["id"])
                        self.ccedula.config(state="disabled")
                        self.cnombre.delete(0, tk.END)
                        self.cnombre.insert(0,clientes["name"])
                        self.cusuario.delete(0, tk.END)
                        self.cusuario.insert(0,clientes["username"])
                        self.cclave.delete(0, tk.END)
                        self.cclave.insert(0,clientes["password"])
                        self.ccorreo.delete(0, tk.END)
                        self.ccorreo.insert(0,clientes["email"])
                        self.tipo_action = "Actualizar"

    def main_canchas(self):
        self.formulario_cancha()
        self.listar_canchas()

    def formulario_cancha(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc,text="\uf0c9 REGISTRO DE CANCHAS", font=('Times',16),fg="#9fa8da")
        labelform.place(x=70, y=30)
        
        labelnombre = tk.Label(self.frame_dinamyc,text="Nombre:", font=('Times',14))
        labelnombre.place(x=70, y=100)
        self.cnombre_cancha = tk.Entry(self.frame_dinamyc, width=40)
        self.cnombre_cancha.place(x=220, y=100)

        labelubicacion = tk.Label(self.frame_dinamyc,text="Ubicación:", font=('Times',14))
        labelubicacion.place(x=70, y=130)
        self.cubicacion_cancha = tk.Entry(self.frame_dinamyc, width=40)
        self.cubicacion_cancha.place(x=220, y=130)

        labeltipo = tk.Label(self.frame_dinamyc,text="Tipo:", font=('Times',14))
        labeltipo.place(x=70, y=160)
        self.ctipo_cancha = tk.Entry(self.frame_dinamyc, width=40)
        self.ctipo_cancha.place(x=220, y=160)

        btnguardar = tk.Button(self.frame_dinamyc, text="\uf0c7 GUARDAR", font=('Times',14), command=self.save_cancha)
        btnguardar.place(x=470, y=130)

    def listar_canchas(self):
        tk.Label(self.frame_dinamyc,text="\uf00b LISTADO DE CANCHAS", font=('Times',16),fg="#9fa8da").place(x=70, y=200)
        self.tablacanchas = ttk.Treeview(self.frame_dinamyc, columns=("Nombre", "Ubicación", "Tipo"))
        self.tablacanchas.heading("#0", text="ID")
        self.tablacanchas.heading("Nombre", text="Nombre")
        self.tablacanchas.heading("Ubicación", text="Ubicación")
        self.tablacanchas.heading("Tipo", text="Tipo")
        # Here, fetch and display your "canchas" data, similar to how users are displayed in the listar_usuarios function
        self.tablacanchas.place(x=70, y=250)
        btneliminar = tk.Button(self.frame_dinamyc, text="\uf0c7 Eliminar", font=('Times',14), command=self.delete_cancha)
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="\uf0c7 Actualizar", font=('Times',14), command=self.update_cancha)
        btnupdate.place(x=200, y=520)

    def save_cancha(self):
        nombre_cancha = self.cnombre_cancha.get()
        ubicacion_cancha = self.cubicacion_cancha.get()
        tipo_cancha = self.ctipo_cancha.get()

        if not nombre_cancha or not ubicacion_cancha or not tipo_cancha:
            messagebox.showinfo('Info', "Por favor, complete todos los campos.", parent=self)
            return

        try:
            with open(r"db_canchas.json", "r", encoding='utf-8') as file:
                canchas_data = json.load(file)
        except FileNotFoundError:
            canchas_data = {"canchas": []}

        new_id = str(uuid.uuid4())

        nueva_cancha = {
            "id": new_id,
            "nombre": nombre_cancha,
            "ubicacion": ubicacion_cancha,
            "tipo": tipo_cancha
        }

        canchas_data["canchas"].append(nueva_cancha)

        with open(r'db_canchas.json', 'w') as file:
            json.dump(canchas_data, file, indent=4, ensure_ascii=True)

        messagebox.showinfo('Info', "Cancha registrada con éxito.", parent=self)
        self.listar_canchas()

    def delete_cancha(self):
        if not self.tablacanchas.selection():
            messagebox.showinfo('Info', "Seleccione una cancha para eliminar.", parent=self)
            return

        selected_item = self.tablacanchas.selection()[0]
        cancha_id = self.tablacanchas.item(selected_item, "text")

        with open(r"db_canchas.json", "r", encoding='utf-8') as file:
            canchas_data = json.load(file)

        for cancha in canchas_data["canchas"]:
            if cancha["id"] == cancha_id:
                canchas_data["canchas"].remove(cancha)
                break

        with open(r'db_canchas.json', 'w') as file:
            json.dump(canchas_data, file, indent=4, ensure_ascii=True)

        messagebox.showinfo('Info', "Cancha eliminada con éxito.", parent=self)
        self.listar_canchas()

    def update_cancha(self):
        if not self.tablacanchas.selection():
            messagebox.showinfo('Info', "Seleccione una cancha para actualizar.", parent=self)
            return

        selected_item = self.tablacanchas.selection()[0]
        cancha_id = self.tablacanchas.item(selected_item, "text")

        with open(r"db_canchas.json", "r", encoding='utf-8') as file:
            canchas_data = json.load(file)

        for cancha in canchas_data["canchas"]:
            if cancha["id"] == cancha_id:
                cancha["nombre"] = self.cnombre_cancha.get()
                cancha["ubicacion"] = self.cubicacion_cancha.get()
                cancha["tipo"] = self.ctipo_cancha.get()
                break

        with open(r'db_canchas.json', 'w') as file:
            json.dump(canchas_data, file, indent=4, ensure_ascii=True)

        messagebox.showinfo('Info', "Cancha actualizada con éxito.", parent=self)
        self.listar_canchas()

    def main_reservas(self):
        self.formulario_reserva()
        self.listar_reservas()

    def formulario_reserva(self):
        self.limpiar_panel(self.frame_dinamyc)
        labelform = tk.Label(self.frame_dinamyc, text="\uf0c9 REGISTRO DE RESERVAS", font=('Times', 16), fg="#9fa8da")
        labelform.place(x=70, y=30)

        labelnombre = tk.Label(self.frame_dinamyc, text="Nombre:", font=('Times', 14))
        labelnombre.place(x=70, y=100)
        self.cnombre_reserva = tk.Entry(self.frame_dinamyc, width=40)
        self.cnombre_reserva.place(x=220, y=100)

        labelfecha = tk.Label(self.frame_dinamyc, text="Fecha:", font=('Times', 14))
        labelfecha.place(x=70, y=130)
        self.cfecha_reserva = tk.Entry(self.frame_dinamyc, width=40)
        self.cfecha_reserva.place(x=220, y=130)

        labelhora = tk.Label(self.frame_dinamyc, text="Hora:", font=('Times', 14))
        labelhora.place(x=70, y=160)
        self.chora_reserva = tk.Entry(self.frame_dinamyc, width=40)
        self.chora_reserva.place(x=220, y=160)

        labelcancha = tk.Label(self.frame_dinamyc, text="Cancha:", font=('Times', 14))
        labelcancha.place(x=70, y=190)
        self.ccancha_reserva = tk.Entry(self.frame_dinamyc, width=40)
        self.ccancha_reserva.place(x=220, y=190)

        btnguardar = tk.Button(self.frame_dinamyc, text="\uf0c7 GUARDAR", font=('Times', 14), command=self.save_reserva)
        btnguardar.place(x=470, y=130)

    def listar_reservas(self):
        tk.Label(self.frame_dinamyc, text="\uf00b LISTADO DE RESERVAS", font=('Times', 16), fg="#9fa8da").place(x=70, y=220)
        self.tablareservas = ttk.Treeview(self.frame_dinamyc, columns=("Nombre", "Fecha", "Hora", "Cancha"))
        self.tablareservas.heading("#0", text="ID")
        self.tablareservas.heading("Nombre", text="Nombre")
        self.tablareservas.heading("Fecha", text="Fecha")
        self.tablareservas.heading("Hora", text="Hora")
        self.tablareservas.heading("Cancha", text="Cancha")
        # Fetch and display your reservations data similar to how users and canchas are displayed
        self.tablareservas.place(x=70, y=250)
        btneliminar = tk.Button(self.frame_dinamyc, text="\uf0c7 Eliminar", font=('Times', 14), command=self.delete_reserva)
        btneliminar.place(x=70, y=520)
        btnupdate = tk.Button(self.frame_dinamyc, text="\uf0c7 Actualizar", font=('Times', 14), command=self.update_reserva)
        btnupdate.place(x=200, y=520)

    def save_reserva(self):
        nombre_reserva = self.cnombre_reserva.get()
        fecha_reserva = self.cfecha_reserva.get()
        hora_reserva = self.chora_reserva.get()
        cancha_reserva = self.ccancha_reserva.get()

        if not nombre_reserva or not fecha_reserva or not hora_reserva or not cancha_reserva:
            messagebox.showinfo('Info', "Por favor, complete todos los campos.", parent=self)
            return

        try:
            with open(r"db_reservas.json", "r", encoding='utf-8') as file:
                reservas_data = json.load(file)
        except FileNotFoundError:
            reservas_data = {"reservas": []}

        new_id = str(uuid.uuid4())

        nueva_reserva = {
            "id": new_id,
            "nombre": nombre_reserva,
            "fecha": fecha_reserva,
            "hora": hora_reserva,
            "cancha": cancha_reserva
        }

        reservas_data["reservas"].append(nueva_reserva)

        with open(r'db_reservas.json', 'w') as file:
            json.dump(reservas_data, file, indent=4, ensure_ascii=True)

        messagebox.showinfo('Info', "Reserva registrada con éxito.", parent=self)
        self.listar_reservas()

    def delete_reserva(self):
        if not self.tablareservas.selection():
            messagebox.showinfo('Info', "Seleccione una reserva para eliminar.", parent=self)
            return

        selected_item = self.tablareservas.selection()[0]
        reserva_id = self.tablareservas.item(selected_item, "text")

        with open(r"db_reservas.json", "r", encoding='utf-8') as file:
            reservas_data = json.load(file)

        for reserva in reservas_data["reservas"]:
            if reserva["id"] == reserva_id:
                reservas_data["reservas"].remove(reserva)
                break

        with open(r'db_reservas.json', 'w') as file:
            json.dump(reservas_data, file, indent=4, ensure_ascii=True)

        messagebox.showinfo('Info', "Reserva eliminada con éxito.", parent=self)
        self.listar_reservas()

    def update_reserva(self):
        if not self.tablareservas.selection():
            messagebox.showinfo('Info', "Seleccione una reserva para actualizar.", parent=self)
            return

        selected_item = self.tablareservas.selection()[0]
        reserva_id = self.tablareservas.item(selected_item, "text")

        with open(r"db_reservas.json", "r", encoding='utf-8') as file:
            reservas_data = json.load(file)

        for reserva in reservas_data["reservas"]:
            if reserva["id"] == reserva_id:
                reserva["nombre"] = self.cnombre_reserva.get()
                reserva["fecha"] = self.cfecha_reserva.get()
                reserva["hora"] = self.chora_reserva.get()
                reserva["cancha"] = self.ccancha_reserva.get()
                break

        with open(r'db_reservas.json', 'w') as file:
            json.dump(reservas_data, file, indent=4, ensure_ascii=True)

        messagebox.showinfo('Info', "Reserva actualizada con éxito.", parent=self)
        self.listar_reservas()


    def generar_factura(self):
        selected_reservation = self.tablareservas.selection()[0]
        reservation_id = self.tablareservas.item(selected_reservation, "text")
        reservation_details = self.get_reservation_details(reservation_id)

        if not reservation_details:
            messagebox.showinfo('Info', "No se encontraron detalles de la reserva.", parent=self)
            return

        total_amount = self.calculate_total_amount(reservation_details)

        invoice_id = self.generate_invoice_id()

        invoice = {
            "id": invoice_id,
            "reservation_id": reservation_id,
            "total_amount": total_amount,
        }

        self.save_invoice(invoice)
        self.listar_facturas()

    def get_reservation_details(self, reservation_id):
        return {
            "customer_name": "John Doe",
            "reservation_date": "2024-05-28",
            "court_name": "Court A",
            "court_price": 50,
            "hours_reserved": 2
        }

    def calculate_total_amount(self, reservation_details):
        court_price = reservation_details["court_price"]
        hours_reserved = reservation_details["hours_reserved"]
        total_amount = court_price * hours_reserved
        return total_amount

    def generate_invoice_id(self):
        return str(uuid.uuid4())[:8]

    def save_invoice(self, invoice):
        try:
            with open("invoices.json", "r", encoding="utf-8") as file:
                invoices_data = json.load(file)
        except FileNotFoundError:
            invoices_data = {"invoices": []}

        invoices_data["invoices"].append(invoice)

        with open("invoices.json", "w", encoding="utf-8") as file:
            json.dump(invoices_data, file, indent=4)

        messagebox.showinfo('Info', "Factura generada con éxito.", parent=self)

    def listar_facturas(self):
        self.limpiar_panel(self.frame_dinamyc)
        tk.Label(self.frame_dinamyc, text="\uf00b LISTADO DE FACTURAS", font=('Times', 16), fg="#9fa8da").place(x=70, y=30)

        try:
            with open("invoices.json", "r", encoding="utf-8") as file:
                invoices_data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo('Info', "No hay facturas disponibles.", parent=self)
            return

        self.tabla_facturas = ttk.Treeview(self.frame_dinamyc, columns=("ID", "Reserva", "Monto Total"))
        self.tabla_facturas.heading("#0", text="ID")
        self.tabla_facturas.heading("ID", text="ID")
        self.tabla_facturas.heading("Reserva", text="Reserva")
        self.tabla_facturas.heading("Monto Total", text="Monto Total")

        for invoice in invoices_data["invoices"]:
            self.tabla_facturas.insert("", "end", text=invoice["id"], values=(invoice["reservation_id"], invoice["total_amount"]))

        self.tabla_facturas.place(x=70, y=70)


    def limpiar_panel(self,panel):
    # Función para limpiar el contenido del panel
        for widget in panel.winfo_children():
            widget.destroy()
    def logout(self):
        self.destroy()

    def abrirface(self):
        url="https://www.facebook.com"
        webbrowser.open_new_tab(url)
    def abrirlink(self):
        url="https://www.linkedin.com"
        webbrowser.open_new_tab(url)
    def abrirweb(self):
        url= "https://itcloud.com.co"
        webbrowser.open_new_tab(url)