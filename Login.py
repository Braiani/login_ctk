from Utils import Utils
import PIL.Image as Image
from App import App
from Usuarios import Usuarios

class Login(Utils):
    def __init__(self):
        super().__init__()
        self.app = App(width=1200, height=800)
        self.janela = self.app.janela
        self.app.set_title('Login')
        self.app.set_backgorund('black')
        self.app.theme('mica')
        self.entradas = {
            'usuario': '',
            'senha': ''
        }
        self.usuario_logado = None

    def logar(self):
        user = self.entradas.get('usuario', '').get()
        senha = self.entradas.get('senha', '').get()
        if user == '' or senha == '':
            self.app.message_box(message='Dados inválidos', title='Verifique os dados', type='error')
            return

        usuario = Usuarios(self.get_connection())
        if not usuario.validar_login(user, self.generate_md5(senha)):
            self.app.message_box('Usuário inválido', 'Erro', 'warning')
            return

        self.app.message_box('Logado com sucesso!')
        self.usuario_logado = usuario

        self.app.destroy()
        self.abrir_principal()

    def desenhar_elementos(self):
        image = Image.open(f"{self.get_base_path()}/mercado.jpg")

        self.app.adicionar_imagem(image=image, position={
            'grid': {
                'row': 0,
                'column': 0,
                'rowspan': 6
            }
        }, options={
            'size': ((self.app.width // 2), self.app.height)
        })

        main_frame = self.app.adicionar_frame(position={
            'grid': {
                'row': 0,
                'column': 1,
                'padx': 50,
                'sticky': 'nsew'
            }
        }, options={
            'config': {
                'fg_color': 'black'
            }
        })

        self.app.adicionar_label('Bem-vindo ao Sistema do Mercado!', position={
            'grid': {
                'row': 0,
                'column': 0,
                'pady': 80
            }
        }, options={
            'config': {
                'font': ('Arial', 32),
                'bg_color': 'black'
            },
            'opacity': 'black',
            'master': main_frame
        })

        elementos = {
            'usuario': {
                'label': 'Digite seu login: *',
                'entry': 'usuario'
            },
            'senha': {
                'label': 'Digite sua senha: *',
                'entry': 'senha',
                'show': '*'
            }
        }
        row = 1

        for item, elemento in elementos.items():
            self.app.adicionar_label(elemento.get('label'), position={
                'grid': {
                    'row': row,
                    'column': 0
                }
            }, options={
                'config': {
                    'font': ('Arial', 24),
                    'bg_color': 'black'
                },
                'opacity': 'black',
                'master': main_frame
            })
            row += 1

            entry = self.app.adicionar_entry(position={
                'grid': {
                    'row': row,
                    'column': 0,
                    'pady': 20
                }
            }, options={
                'config': {
                    'width': (self.app.width // 2) - 100,
                    'corner_radius': 32,
                    'show': elemento.get('show', '')
                },
                'master': main_frame
            })
            row += 1

            self.entradas.update({elemento.get('entry'): entry})
            entry.bind('<Return>', self.enter_pressionado)

        self.app.adicionar_button(position={
            'grid': {
                'row': 5,
                'column': 0,
                'pady': 20,
                'sticky': 'w'
            }
        }, options={
            'config': {
                'corner_radius': 32,
                'height': 50,
                'text': 'Logar',
                'command': lambda: self.logar()
            },
            'master': main_frame
        })

        self.app.adicionar_button(position={
            'grid': {
                'row': 5,
                'column': 0,
                'sticky': 'e',
                'pady': 20
            }
        }, options={
            'config': {
                'corner_radius': 32,
                'height': 50,
                'text': 'Cadastrar',
                'command': lambda: self.abrir_cadastro()
            },
            'master': main_frame
        })

    def enter_pressionado(self, event):
        self.logar()

    def abrir_cadastro(self):
        self.app.iconify()

        from Cadastrar import Cadastrar
        cadastro = Cadastrar(self.app, self.app, self.get_connection())
        cadastro.desenhar_elementos()
        cadastro.app.start()

    def abrir_principal(self):
        from Principal import Principal

        principal = Principal(self.usuario_logado, self.get_connection())
        principal.desenhar_elementos()
        principal.app.start()