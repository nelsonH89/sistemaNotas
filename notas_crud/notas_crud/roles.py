from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {'criar_metas': True, 'ver_metas': True}
    
class Aluno(AbstractUserRole):
    available_permissions = {'acessar_notas': True, 'ver_turmas': True}    