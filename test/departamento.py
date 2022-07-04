class Departamento:
  def __init__(self,nombre,descripcion,hora_atencion):
    self.departamento=nombre
    self.descripcion=descripcion
    self.Hatención= hora_atencion
    
  def mostrarDepa(self):
    print("Departamento: {} {}:00 ".format(self.departamento,self.Hatención))

if __name__ == "__main__":
  cli = Departamento("Financiero","se encarga dl finaciamiento","5")
  cli.mostrarDepa()

     