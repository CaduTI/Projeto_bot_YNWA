class Agendamento:

    def __init__(self, data_consulta,tipo_consulta):
        self._data_consulta =data_consulta
        self._tipo_consulta = tipo_consulta
    @property
    def Get_data_consulta(self):
        return self._data_consulta

    @property
    def Get_tipo_consulta(self):
        return self._tipo_consulta
class Usuario():

    def __init__(self,nome):
        self._nome = nome
        self._cpf = None
        self._email = None

    @property
    def Getnome(self):
        return self._nome
    @property
    def Getcpf(self):
        return self._cpf
    @property
    def Getemail(self):
        return self._email