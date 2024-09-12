from Utils import Utils
from Usuarios import Usuarios
from App import App

class Principal(Utils):
    def __init__(self, usuario: Usuarios, connector):
        super().__init__(connector)
        self.usuario = usuario
        self.app = App(width=1200, height=800)
        self.janela = self.app.janela
        self.app.set_title('Area Logada')
        self.app.set_backgorund('black')

    def desenhar_elementos(self):
        self.app.janela.bind('<Escape>', lambda e: self.sair())
        self.app.janela.grid_columnconfigure(0, weight=1)
        self.app.janela.grid_columnconfigure(1, weight=2)
        self.app.janela.grid_columnconfigure(2, weight=1)

        main_frame = self.app.adicionar_frame(position={
            'grid': {
                'row': 0,
                'column': 1,
                'columnspan': 2,
                'padx': 50,
                'sticky': 'nsew'
            }
        }, options={
            'config': {
                'fg_color': 'black'
            }
        })

        elementos = {
            'welcome': {
                'label': f'Bem-vindo {self.usuario.get_nome()}!',
            },
            'usuario': {
                'label': f'- Seu Usuário de acesso é: {self.usuario.get_usuario()}!',
            },
            'perfil': {
                'label': f'- Seu Perfil de acesso é: {self.usuario.get_perfil()}!',
            },
            'mensagem': {
                'label': f'- Sua Mensagem pessoal é: {self.usuario.get_mensagem()}!',
            }
        }
        row = 0

        for item, elemento in elementos.items():
            self.app.adicionar_label(elemento.get('label'), position={
                'grid': {
                    'row': row,
                    'column': 0,
                    'pady': 20,
                    'sticky': 'nwes',
                    'padx': 20
                }
            }, options={
                'config': {
                    'font': ('Arial', 32),
                    'bg_color': 'black'
                },
                'master': main_frame
            })
            row += 1


    def sair(self):
        self.app.janela.destroy()

if __name__ == "__main__":
    import Main

    Main