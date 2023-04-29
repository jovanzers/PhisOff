import requests, os
os.system('')
cookies = {
    '1': 'rXG5iF7pBiv50U0Seoj6Ed',
}

headers = {
    'content-type': 'application/json',
    'origin': 'https://myinfolayanan-app.net',
    'referer': 'https://myinfolayanan-app.net/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

params = {
    'm': 'SubmitDataFormInput',
}

json_data = {
    'query': 'mutation ActionForm($input_0:SubmitDataFormInput!) {submitDataForm(input:$input_0) {clientMutationId,...F0}} fragment F0 on SubmitDataFormPayload {formID,dataFormID,publicDataEdge {node {publicData,id},cursor}}',
    'variables': {
        'input_0': {
            'ID': '1680263211922_2293',
            'url': 'https://myinfolayanan-app.net/',
            'data': {
                'button': {
                    'ID': 'i196668855',
                    'size': 'large',
                    'text': 'Masuk',
                    'usage': 'toReport',
                    'colors': {
                        'button': '#E53935',
                    },
                    'design': 'fill',
                    'radius': 4,
                    'shadow': 0,
                    'fontFace': 'default',
                    'usageFireEvent': 'none',
                },
                'lines': [
                    {
                        'ID': 'i196668859',
                        'name': 'Nama pengguna::',
                        'value': 'CARI_REZEKI_HALAL_BRO',
                        'inputType': 'text',
                    },
                    {
                        'ID': 'i196668860',
                        'name': 'Password::',
                        'value': 'CARI_REZEKI_HALAL_BRO',
                        'inputType': 'text',
                    },
                ],
            },
            'clientMutationId': '0',
        },
    },
}

json_data_otp = {
    'query': 'mutation ActionForm($input_0:SubmitDataFormInput!) {submitDataForm(input:$input_0) {clientMutationId,...F0}} fragment F0 on SubmitDataFormPayload {formID,dataFormID,publicDataEdge {node {publicData,id},cursor}}',
    'variables': {
        'input_0': {
            'ID': '1680264965157_8275',
            'url': 'https://myinfolayanan-app.net/n',
            'data': {
                'button': {
                    'ID': 'i196669534',
                    'size': 'large',
                    'text': 'Masuk',
                    'usage': 'toReport',
                    'colors': {
                        'button': '#ffffff',
                    },
                    'design': 'ghost',
                    'radius': 4,
                    'shadow': 0,
                    'fontFace': 'default',
                    'usageFireEvent': 'none',
                },
                'lines': [
                    {
                        'ID': 'i196669538',
                        'name': 'OTP Email pulsa::',
                        'value': 'CARI_REZEKI_HALAL_BRO',
                        'inputType': 'text',
                    },
                ],
            },
            'clientMutationId': '0',
        },
    },
}

no = 0
sukses = 0
gagal = 0
try:
    while True:
        response = requests.post('https://myinfolayanan-app.net/_/graph', params=params, cookies=cookies, headers=headers, json=json_data)
        otp = requests.post('https://myinfolayanan-app.net/_/graph', params=params, cookies=cookies, headers=headers, json=json_data_otp)
        no += 1
        print(f'\33[33m{no} request terkirim\033[0m')
        try:
            if response.json().get('data') and otp.json().get('data'):
                print(f'Response: \33[32mSukses\033[0m {otp.text}')
                sukses += 1
            else:
                print('Response: \33[31mGagal\033[0m (web maintenance / dll.)')
                gagal += 1
        except requests.exceptions.JSONDecodeError:
            print('Response: \33[31mGagal\033[0m (web maintenance / dll.)')
            gagal += 1
except KeyboardInterrupt:
    print(f'\n\33[33mTotal: {no} requests\033[0m')
    print(f'\33[32mSukses: {sukses} requests\033[0m')
    print(f'\33[31mGagal: {gagal} requests\033[0m')
