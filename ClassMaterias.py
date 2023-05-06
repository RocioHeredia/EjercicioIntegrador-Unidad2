class Materia: 
    __dni:str
    __nombre:str
    __fecha:str
    __nota:float
    __aprobacion:str

    def __init__(self, v1:str, v2:str, v3:str, v4:str, v5:str)->None:
        self.__dni=v1
        self.__nombre=v2
        self.__fecha=v3
        self.__nota=float(v4)
        self.__aprobacion=v5

    def __str__(self)->str:
        return f"{self.__dni, self.__nombre, self.__fecha, self.__nota, self.__aprobacion}"

    def get_nom(self)->str:
        return self.__nombre
    
    def get_Aproba(self)->str:
        return self.__aprobacion
    
    def get_nota(self)->float:
        return self.__nota
    
    def get_Dni(self)->str:
        return self.__dni
    
    def get_fecha(self)->str:
        return self.__fecha