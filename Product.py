product = {'ดินสอกด pentel':{'ราคา':50,'สี':'แดง'},
           'ยางลบ':{'ราคา':3,'สี':'เขียว'},
           'ดินสอสี':{'ราคา':100,'สี':'ส้ม'}}

while True:
    print('----------กรุณากรอกข้อมูลสินค้า-----------')
    p = input('ชื่อสินค้า: ')
    q = int(input('จำนวน: '))
    print('-----------')
    if p in product:
        print(f'สินค้า: {p} \nราคา: {product[p]['ราคา']} บาท \nสี: {product[p]['สี']}')
        print(f'จำนวน: {q} ชิ้น \nรวมเป็นเงินทั้งสิ้น: {product[p]['ราคา'] * q} บาท')
    else:
        print('ไม่มีสินค้าในระบบ')
    # ออกจาก loop โดยการกด ctrl+c (ตอนที่รันแล้ว)