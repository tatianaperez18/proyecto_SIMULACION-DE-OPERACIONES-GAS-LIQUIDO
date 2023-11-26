from customtkinter import *
from tkinter import PhotoImage, StringVar

# en esta funcion se calculan los gramos del gas
def calcular_gramos_gas(presion_parcial, constante_henry, cantidad_agua, gas_deseado, PM_agua, masa_molecular):
    #calcular la concentracion del gas
    x = presion_parcial / constante_henry[gas_deseado]
    #se hace una relacion molar, debido a que es una mezcla no ideal
    masa_gas = (x / (1 - x)) * (masa_molecular[gas_deseado] / PM_agua) * cantidad_agua
    # se retorna la funcion dada
    return masa_gas

#funcion para calcular la opcion de calcular la presion parcial
def calcular_presion_parcial(gramos_gas, gramos_agua, gas_deseado, masa_molecular, PM_agua):
    #se calculan los moles de cada componente y para hallar la concentracion son los moles del gas sobre los moles totales, la suma entre el gas y el liquido
    x = (gramos_gas / masa_molecular[gas_deseado]) / ((gramos_gas / masa_molecular[gas_deseado]) + (gramos_agua / PM_agua))
    # segun la ley de Henry para hallar la presion se usa la concentracion multiplicada por la constante dada a 20º
    P = x * constante_henry[gas_deseado]
    #se retorna la precion parcial calculada
    return P

def calcular():
    # acceder y utilizar el valor registrado por el usuario
    gas_deseado = gas_deseado_var.get().upper()  
    opcion = opcion_var.get()

# condicion si se cumple la entrada del usuario
    if opcion == 'la cantidad de gas disuelto en agua':
        presion_parcial = float(presion_parcial_entry.get()) 
        cantidad_agua = float(cantidad_agua_entry.get())
        # llama a la funcion creada
        calculo_si = calcular_gramos_gas(presion_parcial, constante_henry, cantidad_agua, gas_deseado, PM_agua, masa_molecular)
        # se imprime el resultado con dos decimales
        resultado_si_var.set("La cantidad de gas {} en gramos que se disolverá en el agua es: {:.2f} g".format(gas_deseado, calculo_si))
        resultado_no_var.set("")  # Limpiar el resultado "no"

# si no se cumple evalua la otra condicion  
    else:
        gramos_gas = float(gramos_gas_entry.get())
        gramos_agua = float(gramos_agua_entry.get())
        calculo_no = calcular_presion_parcial(gramos_gas, gramos_agua, gas_deseado, masa_molecular, PM_agua)
        resultado_no_var.set("La presión parcial del gas {} es: {:.2f} atm".format(gas_deseado, calculo_no),)
        resultado_si_var.set("")  # Limpiar el resultado "si"


c_negro = '#010101'
c_morado = '#7f5af0'
c_verde = '#2cb67d'
c_gris = '#f0f0f0'

# Diccionario de las constantes de Henry
constante_henry = {
    'H2S': 483,
    'CO2': 1420,
    'CO': 53600,
    'C2H6': 26300,
    'CH4': 37600
}

PM_agua = 18  # Peso molecular del agua

# Diccionario de los pesos moleculares
masa_molecular = {  # Peso molecular en g/mol
    'H2S': 34.08,
    'CO2': 44.01,
    'CO': 28.01,
    'C2H6': 30.08,
    'CH4': 16.05
}

app = CTk()
app.geometry("990x600")
app.minsize(480, 500)
app.title("Calculadora absorcion de Gases en Agua")

# Variables para almacenar la selección del usuario
gas_deseado_var = StringVar()
opcion_var = StringVar()
resultado_si_var = StringVar()
resultado_no_var = StringVar()

logo = PhotoImage(file='imagenes/logo_proyecto.png')

set_appearance_mode("dark")

logo= PhotoImage(file = 'imagenes/logo_proyecto.png')

CTkLabel(master=app, text="Gas deseado:", font=("sans rerif", 12), text_color= c_verde).place(relx= 0.5, rely = 0.05, anchor="center")
combobox= CTkComboBox(master=app, values=list(constante_henry.keys()), variable=gas_deseado_var)
combobox.place(relx= 0.5, rely = 0.1, anchor="center")

CTkLabel(master=app, text="¿Que desea calcular?", font=("sans rerif", 12), text_color= c_verde).place(relx= 0.5, rely = 0.15, anchor="center")
combobox2 = CTkComboBox(master=app, values=["la cantidad de gas disuelto en agua", "la presion parcial del gas"], variable=opcion_var)
combobox2.place(relx= 0.5, rely = 0.2, anchor="center")

presion_parcial_entry = CTkEntry(master=app, placeholder_text='presion parcial del gas', border_color= c_verde, fg_color= c_negro, width= 220, height= 40)
cantidad_agua_entry = CTkEntry(master=app, placeholder_text='gramos agua', border_color= c_verde, fg_color= c_negro, width= 220, height= 40)
gramos_gas_entry = CTkEntry(master=app, placeholder_text=' gramos gas', border_color= c_verde, fg_color= c_negro, width= 220, height= 40)
gramos_agua_entry = CTkEntry(master=app, placeholder_text='gramos agua', border_color= c_verde, fg_color= c_negro, width= 220, height= 40)

CTkLabel(master=app, text="Presión parcial del gas (atm):").place(relx= 0.3, rely = 0.3, anchor="center")
presion_parcial_entry.place(relx= 0.5, rely = 0.3, anchor="center")

CTkLabel(master=app, text="Cantidad de agua (gramos):").place(relx= 0.3, rely = 0.4, anchor="center")
cantidad_agua_entry.place(relx= 0.5, rely = 0.4, anchor="center")

CTkLabel(master=app, text="Gramos de gas disueltos (gramos):").place(relx= 0.28, rely = 0.5, anchor="center")
gramos_gas_entry.place(relx= 0.5, rely = 0.5, anchor="center")

CTkLabel(master=app, text="Cantidad de agua (gramos):").place(relx= 0.3, rely = 0.6, anchor="center")
gramos_agua_entry.place(relx= 0.5, rely = 0.6, anchor="center")

calcular_button = CTkButton(master=app, text= "calcular", corner_radius=32, fg_color= c_verde, hover_color=c_morado,
                 border_color= c_negro, border_width=2, command=calcular)
calcular_button.place(relx= 0.5, rely = 0.7, anchor="center")


CTkLabel(master=app, textvariable=resultado_si_var).place(relx= 0.5, rely = 0.8, anchor="center")


CTkLabel(master=app, textvariable=resultado_no_var).place(relx= 0.5, rely = 0.8, anchor="center")


app.mainloop()