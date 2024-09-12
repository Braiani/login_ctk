from SqlHandler import SqlHandler

class Usuarios:
    def __init__(self, connector: SqlHandler) -> None:
        self.usuario = ''
        self.nome = ''
        self.mensagem = ''
        self.photo = ''
        self.perfil = ''
        self.descricao = ''
        self.connector = connector
        self.logado = False

    def __str__(self):
        return f'Usuário: {self.usuario}, Nome: {self.nome}, Perfil: {self.perfil}'

    def perfis_disponiveis(self):
        sql = self.connector
        query = """
            select
                id,
                nome
            from
                perfil
        """

        return sql.exec_query(query=query, commit=False)

    def validar_login(self, usuario: str, senha: str):
        sql = self.connector
        query = """
            select
                usuarios.nome as nome,
                usuarios.usuario as usuario,
                usuarios.mensagem as mensagem,
                usuarios.photo as foto,
                perfil.nome as perfil,
                perfil.descricao as descricao
            from 
                usuarios 
            JOIN
                perfil ON usuarios.perfil_id = perfil.id
            where 
                usuarios.usuario = %s
                and usuarios.senha = %s
        """

        params = (usuario, senha)

        response = sql.exec_query(query=query, params=params, commit=False)
        
        if not response:
            return False

        response = response[0]
        self.usuario = response.get('usuario')
        self.nome = response.get('nome')
        self.mensagem = response.get('mensagem')
        self.photo = response.get('foto')
        self.perfil = response.get('perfil')
        self.descricao = response.get('descricao')

        return True

    def cadastrar_usuario(self, nome: str, usuario: str, senha: str, perfil_id: int, mensagem: str='', photo: str=''):
        sql = self.connector
        query = """
            insert into usuarios (nome, usuario, senha, mensagem, photo, perfil_id)
            values (%s, %s, %s, %s, %s, %s)
        """

        params = (nome, usuario, senha, mensagem, photo, perfil_id)

        return sql.exec_query(query=query, params=params, commit=True)

    def get_nome(self):
        return self.nome

    def get_usuario(self):
        return self.usuario

    def get_mensagem(self):
        return self.mensagem

    def get_photo(self):
        return self.photo

    def get_perfil(self):
        return self.perfil

    def get_descricao(self):
        return self.descricao


if __name__ == "__main__":
    import Main
    
    Main