from Utils import Utils
import PIL.Image as Image
from App import App
from Usuarios import Usuarios


class Cadastrar(Utils):
    def __init__(self, surface: App, parent, connector):
        super().__init__(connector)
        self.connector = connector
        surface = surface.top_level()
        self.parent = parent
        self.app = App(width=1200, height=800, janela=surface)
        self.app.set_title('Cadastrar')
        self.app.set_backgorund('black')
        self.app.theme('mica')
        self.entradas = {
            'usuario': '',
            'senha': '',
            'nome': '',
            'mensagem': ''
        }

    def desenhar_elementos(self):
        self.app.janela.bind('<Escape>', lambda e: self.voltar())

        image = Image.open(f"{self.get_base_path()}/mercado.jpg")

        self.app.adicionar_imagem(image=image, position={
            'grid': {
                'row': 0,
                'column': 1,
            }
        }, options={
            'size': ((self.app.width // 2), self.app.height)
        })

        main_frame = self.app.adicionar_frame(position={
            'grid': {
                'row': 0,
                'column': 0,
                'padx': 50,
                'sticky': 'nsew'
            }
        }, options={
            'config': {
                'fg_color': 'black'
            }
        })

        self.app.adicionar_label('Bem-vindo ao Cadastro!', position={
            'grid': {
                'row': 0,
                'column': 0,
                'pady': 60
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
            'nome': {
                'label': 'Digite seu nome: *',
                'entry': 'nome'
            },
            'usuario': {
                'label': 'Digite seu login: *',
                'entry': 'usuario'
            },
            'senha': {
                'label': 'Digite sua senha: *',
                'entry': 'senha',
                'show': '*'
            },
            'mensagem': {
                'label': 'Digite uma mensagem:',
                'entry': 'mensagem',
            },
            'perfil': {
                'label': 'Selecione um perfil:',
                'combobox': 'perfil',
                'values': ['Administrador', 'Usuário', 'Convidado']
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

            if elemento.get('combobox', False):
                combobox = self.app.adicionar_combobox(position={
                    'grid': {
                        'row': row,
                        'column': 0,
                        'pady': 20
                    }
                }, options={
                    'config': {
                        'width': (self.app.width // 2) - 100,
                        'corner_radius': 32,
                        'values': elemento.get('values', []),
                        'justify': 'center',
                    },
                    'master': main_frame
                })

                combobox.set(elemento.get('label', ''))
                row += 1

                self.entradas.update({elemento.get('combobox'): combobox})

            if elemento.get('entry', False):
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
                'row': row,
                'column': 0,
                'pady': 20,
                'sticky': 'w'
            }
        }, options={
            'config': {
                'corner_radius': 32,
                'height': 50,
                'text': 'Salvar',
                'command': lambda: self.salvar()
            },
            'master': main_frame
        })

        self.app.adicionar_button(position={
            'grid': {
                'row': row,
                'column': 0,
                'sticky': 'e',
                'pady': 20
            }
        }, options={
            'config': {
                'corner_radius': 32,
                'height': 50,
                'text': 'Voltar',
                'command': lambda: self.voltar()
            },
            'master': main_frame
        })

    def salvar(self):
        usuario_model = Usuarios(self.connector)

        nome = self.entradas['nome'].get()
        usuario = self.entradas['usuario'].get()
        senha = self.entradas['senha'].get()
        mensagem = self.entradas['mensagem'].get()
        perfil = self.entradas['perfil'].get()
        perfil_id = 0

        for perfil_bd in usuario_model.perfis_disponiveis():
            if perfil_bd.get('nome') == perfil:
                perfil_id = perfil_bd.get('id')
                break


        if not perfil_id:
            self.app.message_box(title='Erro', message='Perfil inválido!', type='error')
            return

        if not nome or not usuario or not senha:
            self.app.message_box(title='Erro', message='Preencha todos os campos com *!', type='error')
            return

        usuario_cadastro = usuario_model.cadastrar_usuario(
            nome=nome,
            usuario=usuario,
            senha=self.generate_md5(senha),
            mensagem=mensagem,
            perfil_id=perfil_id,
            photo=''
        )

        if usuario_cadastro:
            self.app.message_box(title='Sucesso', message='Usuário cadastrado com sucesso!', type='info')
            self.voltar()
        else:
            self.app.message_box(title='Erro', message='Erro ao cadastrar usuário!', type='error')

    def voltar(self):
        self.app.destroy()
        self.parent.deiconify()

    def enter_pressionado(self, event=None):
        self.salvar()

if __name__ == "__main__":
    import Main

    Main