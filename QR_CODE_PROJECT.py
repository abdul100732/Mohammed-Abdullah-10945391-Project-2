
import PySimpleGUI as sg
import qrcode 
import os


layout =[
        
        # [sg.Text('Enter a Link,Text or Website to Generate a QR CODE ',text_color='Black',justification='center')],
        [sg.Input(key='WEB')],
        [sg.Button('GENERATE QR CODE',key='GENERATE'),sg.Button('EXIT',key='EXIT')],
        [sg.Image(key='Image', size=(50, 50))],
        
        
        
           
         ]

        
window=sg.Window('QR CODE APP', layout)

def generate_qr_code(link):
        qr=qrcode.QRCode(
                version=1,
                box_size=8.5,
                border=8.5
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill='black',back_color='white')
        file_name= 'qr_code' + '.png'
        path= os.path.join(os.getcwd(), file_name)
        img.save(path)
        return path


while True:
       event,values=window.read()
       if event==sg.WIN_CLOSED or event== 'EXIT':
               break
       if event== 'GENERATE':
               WEB= values['WEB']
               qr_code_image_path= generate_qr_code(WEB)
               window['Image'].update(filename=qr_code_image_path)


        
window.close()