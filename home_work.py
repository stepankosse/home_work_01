import hashlib
import csv
''' Программа подсчитывает хэш суммы строк исходного файла, исходные строки переводит в формат UTF-8 и подсчитывает 
хэш сумму строки. 
Результат записывает в новый файл.

'''


input_file = open("need_hashes.csv", "r")
rdr = csv.DictReader(input_file, delimiter=';', fieldnames=['text', 'hash', 'hashsumm'])
output_file = open("need_hashes4.csv", "w")
wrtr = csv.DictWriter(output_file, delimiter=';', fieldnames=['text', 'hash', 'hashsumm'])


for line in rdr:
    hsha1 = hashlib.sha1()
    hmd5 = hashlib.md5()
    hsha512 = hashlib.sha512()
    if line['hash'] == 'sha512':
        text_in_bite_code = line['text'].encode('utf-8')
        # print('text_in_bite_code: ',text_in_bite_code)
        hsha512.update(text_in_bite_code)
        # print('sha512.update(text_in_bite_code): ', hsha512.update(text_in_bite_code))
        res = hsha512.hexdigest()
        # print('Hashsumm sha512', res)
        try:
            line['hashsumm'] = res
            # print(line['hashsumm'])
        except:
            pass
    elif line['hash'] == 'sha1':
        text_in_bite_code = line['text'].encode('utf-8')
        # print('text_in_bite_code: ',text_in_bite_code)
        hsha1.update(text_in_bite_code)
        # print('hsha1.update(text_in_bite_code): ', hsha1.update(text_in_bite_code))
        res = hsha1.hexdigest()
        # print('Hashsumm sha1', res)
        try:
            line['hashsumm'] = res
            # print(line['hashsumm'])
        except:
            pass
    elif line['hash'] == 'md5':
        text_in_bite_code = line['text'].encode('utf-8')
        # print('text_in_bite_code: ',text_in_bite_code)
        hmd5.update(text_in_bite_code)
        # print('md5.update(text_in_bite_code): ', hmd5.update(text_in_bite_code))
        res = hmd5.hexdigest()
        # print('Hashsumm md5', res)
        try:
            line['hashsumm'] = res
            # print(line['hashsumm'])
        except:
            pass
    wrtr.writerow(line)
input_file.close()
output_file.close()
