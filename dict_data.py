data = {
    '120': {
        'ad' : '',
        'soyad' : '',
        'sinif' : ''
    },
    '125':{
        'ad': '',
        'soyad':'',
        'sinif':''
    },
    '130':{
        'ad': '',
        'soyad':'',
        'sinif':''
    }   
}
choice = 5
while choice != 0:
    choice = int(input('[1] ogrenci bilgisi \n[2] bilgi kaydet\n[0] cikis\n:'))

    if choice == 2:
        
        student_no = input('ogrenci numarasi giriniz: ')
        data[student_no]['ad'] = input(f'{student_no} numarali ogrencinin adini giriniz: ')
        data[student_no]['soyad'] = input(f'{student_no} numarali ogrencinin soyadini giriniz: ')
        data[student_no]['sinif'] = input(f'{student_no} numarali ogrencinin sinifini giriniz: ')
    elif choice == 1:
        view_no = input('ogrenci no: ')
        print(f'ad: {data[view_no]["ad"]} \nsoyad: {data[view_no]["soyad"]}\nsinif: {data[view_no]["sinif"]}')
    else:
        print('hatali tuslama, yeniden deneyin: ')
        continue
        




