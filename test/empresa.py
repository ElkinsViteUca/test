class Empresa:
  def __init__(self,ruc,nombre,tel,dir,correo):
    self.ruc=ruc
    self.razonsocial=nombre
    self.tel=tel
    self.dir=dir
    self.correo=correo
    
if __name__ == "__main__":
  emp1=Empresa()
  emp2=Empresa("1206859810","Soldaditos","0991379125","Babahoyo","soldaditos@gmail.com")