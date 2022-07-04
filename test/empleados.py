# from abc import ABC,abstractclassmethod
# class Empleado(ABC):
  # def __init__(self,nom_empleado,CL,correo,celular,estadoCivil,departamento):
    # self.nom_empleado = nom_empleado
    # self.CL = CL
    # self.correo = correo
    # self.celular = celular
    # self.estadoCivil = estadoCivil
    # self.departamento = departamento

class Empleado():
  def __init__(self,ced,nom,tel,depa,email,estadoCivil):
    self.nombre = nom
    self.cedula = ced
    self.correo = email
    self.celular = tel
    self.depa = depa
    self.estadoCivil = estadoCivil

  def validaCedula(self):
    if len(self.cedula == 10):
      return self.cedula
    else:
      return "9999999999"
  def mostrarEmpleado(self):
    print("Empleado: {} {} {} {} {}".format(self.cedula,self.nombre,self.correo,self.celular,self.depa))
    
class EmpleadoObrero(Empleado):
  def __init__(self,ced,nom,tel,depa,email,estadoCivil,hExtra,descripcion,contrato=True):
    self.hextra=hExtra
    self.descri=descripcion
    self.__contrato= contrato
    super().__init__(ced,nom,tel,dir,email,depa,estadoCivil,descripcion,hExtra)

  def mostrarEmpleado(self):
    contra = "Contrato Vigente" if self.__contrato else "Sin Contrato"
    super().mostrarEmpleado()
    print("{}".format(contra))
# class ClienteCoorporativo(Cliente):
  # def __init__(self,ced,nom,tel,dir,email,contrato=True):
        # super().__init__(ced,nom,tel,dir,email)
        # self.__contrato= contrato
    # 
  # def mostrarCliente(self):
        # contra = "Contrato Vigente" if self.__contrato else "Sin Contrato"
        # super().mostrarCliente()
        # print("{}".format(contra))
        # 
# class ClientePersonal(Cliente):
  # def __init__(self,ced,nom,tel,dir,email,promocion=False):
        # super().__init__(ced,nom,tel,dir,email)
        # self.__promocion=promocion
    # 
  # @property
  # def promocion(self):
        # if self.__promocion == True:
            # self.__promocion=0.10
        # else:
            # self.__promocion=0
        # return self.__promocion
  # @promocion.setter
  # def promocion(self,value):
        # if value == True:
            # self.__promocion=0.10
        # else:
            # self.__promocion=0
# 
  # def mostrarCliente(self):
    # print("Cliente: {} {} {} {}".format(self.cedula,self.nombre,self.correo,self.__promocion))
        # 
    # 
# if __name__ == "__main__":
    # cli = ClienteCoorporativo("0907184162","Maritza","0994766904","Guayaquil","mh@gmail.com",True)
    # cli.mostrarCliente()
if __name__ == "__main__":
  cli = EmpleadoObrero("1206859819","Elkins","2","3","alito@unemi.edu.ec","2","X")
  cli.mostrarEmpleado()



  
  
