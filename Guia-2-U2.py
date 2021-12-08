# Guía 2 de la Unidad 2 / Programación 1 / Matías Fonseca
import pandas as pd
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class VentanaPrincipal():

    def __init__(self):
        
        # print("constructor")
        builder = Gtk.Builder()
        builder.add_from_file("guia2-U2.ui")
        
        # Configuración ventana principal.
        self.ventana = builder.get_object("principal")
        self.ventana.set_default_size(1080, 600)
        self.ventana.set_title("Medicamentos PVC")
        self.ventana.connect("destroy", Gtk.main_quit)

        # Configuración del Tree View para visualizar los datos.
        self.tree = builder.get_object("drogas")

        self.data_df = pd.read_csv("drug200.csv")

        if self.tree.get_columns():
            for column in self.tree.get_columns:
                self.tree.remove_column(column)
        
        largo_columnas = len(self.data.columns)
        modelo = Gtk.ListStore(*(largo_columnas * [str]))
        self.tree.set_model(model=modelo)

        cell = Gtk.CellRendererText()

        for item in range(len(self.data.columns)):
            column = Gtk.TreeViewColumn(self.data.columns[item],
                                        cell,
                                        text=item)
            self.tree.append_column(column)
            column.set_sort_column_id(item)

        for item in self.data.values:
            line = [str(x) for x in item]
            modelo.append(line)

        # Configuración de los botones de la ventana.
        # Botón para ir al resumen de los datos.
        self.boton_resumen = builder.get_object("resume")
        self.boton_resumen.set_label("Información")
        self.boton_resumen.connect("clicked", self.resumen_datos)

        # Botón para agregar más datos.
        self.boton_agregar = builder.get_object("add")
        self.boton_agregar.set_label("Agregar datos")
        self.boton_agregar.connect("clicked", self.agregar_datos)

        # Botón para eliminar los datos.
        self.boton_eliminar = builder.get_object("delete")
        self.boton_eliminar.set_label("Eliminar datos seleccionados")
        self.boton_eliminar.connect("clicked", self.eliminar_datos)
        
        self.ventana.show_all()

    def eliminar_datos(self, btn=None):
        print("CLICK")
        model, it = self.tree.get_selection().get_selected()
        # Por si no se seleccionada nada.
        if model is None or it is None:
            print("Seleccione los datos que desea eliminar")
            return
        #print(self.data_df.get_selection().get_selected())  

    def agregar_datos(self, btn=None):
        print("CLICK")

    def resumen_datos(self, btn=None):
        print("CLICK")
        # print(self.data_df.count())


            

        




if __name__ == "__main__":
    # Se llama a la Ventana inicial y principal del programa.
    VentanaPrincipal()
    Gtk.main()
