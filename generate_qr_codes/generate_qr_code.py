import qrcode


def generate_qr_code(url='https://google.com', name='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return 'QR code created!'

def main():
    generate_qr_code(url='https://houseshop.herokuapp.com/swagger/', name='swagger')



if __name__ == '__main__':
    main()