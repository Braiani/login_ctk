import PIL.Image as Image
from PIL import ImageFilter
import customtkinter as ctk
from tkinter import messagebox
import pywinstyles

class App:
    def __init__(self, width:int=600, height:int=600, janela=None):
        if janela is None:
            janela = ctk.CTk()

        self.janela = janela
        self.images = []
        self.width = width
        self.height = height
        self.set_geometry(self.width,self.height)
        self.janela.resizable(False, False)

    def set_backgorund(self, color):
        self.janela.configure(fg_color=color)

    def theme(self, theme):
        pywinstyles.apply_style(self.janela, theme)

    def set_title(self, title):
        self.janela.title(title)

    @staticmethod
    def set_blur(img: Image, blur: int):
        if img.mode not in ('RGB', 'L'):
            img = img.convert('RGB')
        return img.filter(ImageFilter.GaussianBlur(blur))
    
    def set_geometry(self, width, height):
        screen_width = self.janela.winfo_screenwidth()
        screen_height = self.janela.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.janela.geometry(f"{width}x{height}+{x}+{y}")
    
    @staticmethod
    def set_opacity(element, color):
        pywinstyles.set_opacity(element, color=color)

    def adicionar_label(self, text, position:dict, options: dict={}):
        master = options.get('master', self.janela)

        label = ctk.CTkLabel(master, text=text)
        if options.get('config', False):
            label.configure(**options['config'])
        
        if options.get('opacity', False):
            self.set_opacity(label, options['opacity'])
        
        self.set_position(label, position=position)

    def adicionar_entry(self, position:dict, options: dict={}):
        master = options.get('master', self.janela)
        
        entry = ctk.CTkEntry(master=master)

        if options.get('config', False):
            entry.configure(**options['config'])

        self.set_position(entry, position=position)

        return entry
    @staticmethod
    def set_position(
        element: ctk.CTkButton | ctk.CTkLabel | ctk.CTkEntry | ctk.CTkFrame | ctk.CTkComboBox,
        position: dict
        ):
        if position.get('grid', False):
            element.grid(**position['grid'])
            return

        if position.get('place', False):
            element.place(**position['place'])
            return

        if position.get('pack', False):
            element.pack(**position['pack'])
            return

    def adicionar_imagem(self, image, position:dict, options: dict={}):
        master = options.get('master', self.janela)

        if options.get('size', False):
            img = ctk.CTkImage(image, size=options.get('size'))
        else:
            img = ctk.CTkImage(image)
        if options.get('image_options', False):
            img.configure(**options['image_options'])
        
        self.images.append(img)

        label = ctk.CTkLabel(master, text='', image=img)
        if options.get('label_options', False):
            label.configure(**options['label_options'])
        
        self.set_position(label, position=position)
    
    def adicionar_frame(self, position: dict, options: dict ={}):
        master = options.get('master', self.janela)

        frame = ctk.CTkFrame(master)

        if options.get('config', False):
            frame.configure(**options['config'])
        
        self.set_position(element=frame, position=position)

        return frame

    def adicionar_button(self, position: dict, options: dict ={}):
        master = options.get('master', self.janela)

        btn = ctk.CTkButton(master=master)

        if options.get('config', False):
            btn.configure(**options['config'])
        
        self.set_position(element=btn, position=position)

    def adicionar_combobox(self, position: dict, options: dict = {}):
        master = options.get('master', self.janela)

        combo = ctk.CTkComboBox(master=master)

        if options.get('config', False):
            combo.configure(**options['config'])

        self.set_position(element=combo, position=position)
        return combo

    def message_box(self, message, title = 'Informação', type = 'info'):
        if type == 'info':
            messagebox.showinfo(title=title, message=message)
        elif type == 'error':
            messagebox.showerror(title=title, message=message)
        elif type == 'warning':
            messagebox.showwarning(title=title, message=message)

    @staticmethod
    def top_level():
        return ctk.CTkToplevel()

    def iconify(self):
        self.janela.iconify()

    def start(self):
        self.janela.mainloop()

    def destroy(self):
        self.janela.destroy()

    def deiconify(self):
        self.janela.deiconify()


if __name__ == "__main__":
    import Main
    
    Main