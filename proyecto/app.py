import bd.base_datos as sqlbd
import bd.tablas as tbl

base_datos = sqlbd.BaseDatos(**sqlbd.acceso_bd)

base_datos.mostrar_tablas("world")