import requests
import json


def get_server_name(region):
    servers_name_db = {
        "bd": "Bangladesh",
        "br": "Brazil",
        "eu": "Europe",
        "hk": "Hong Kong",
        "id": "Indonesia",
        "in": "India",
        "me": "Middle East",
        "mo": "Macao",
        "my": "Malaysia",
        "ph": "Philippines",
        "pk": "Pakistan",
        "ru": "Russia",
        "sa": "Saudi Arabia",
        "sg": "Singapore",
        "th": "Thailand",
        "tw": "Taiwan",
        "vn": "Vietnam",
        "ind": "India"
    }
    short_name = region.lower()
    return servers_name_db.get(short_name, region)


def get_info(user_id):
    id = user_id
    cookies = {
        # Your cookies here
       '_ga': 'GA1.1.2123120599.1674510784',
        '_fbp': 'fb.1.1674510785537.363500115',
        '_ga_7JZFJ14B0B': 'GS1.1.1674510784.1.1.1674510789.0.0.0',
        'source': 'mb',
        'region': 'MA',
        'language': 'ar',
        '_ga_TVZ1LG7BEB': 'GS1.1.1674930050.3.1.1674930171.0.0.0',
        'datadome': '6h5F5cx_GpbuNtAkftMpDjsbLcL3op_5W5Z-npxeT_qcEe_7pvil2EuJ6l~JlYDxEALeyvKTz3~LyC1opQgdP~7~UDJ0jYcP5p20IQlT3aBEIKDYLH~cqdfXnnR6FAL0',
        'session_key': 'efwfzwesi9ui8drux4pmqix4cosane0y',
    }
    headers = {
        # Your headers here
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://shop2game.com',
        'Referer': 'https://shop2game.com/app/100067/idlogin',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'accept': 'application/json',
        'content-type': 'application/json',
        'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'x-datadome-clientid': '20ybNpB7Icy69F~RH~hbsvm6XFZADUC-2_--r5gBq49C8uqabutQ8DV_IZp0cw2y5Erk-KbiNZa-rTk1PKC900mf3lpvEP~95Pmut_FlHnIXqxqC4znsakWbqSX3gGlg',
    }
    json_data = {
        'app_id': 100067,
        'login_id': f'{id}',
        'app_server_id': 0,
    }
    try:
        res = requests.post('https://shop2game.com/api/auth/player_id_login', cookies=cookies, headers=headers, json=json_data)
        res.raise_for_status()  # Raise an error for HTTP errors
        response = res.json()
        name = response['nickname']
        region = response.get('region', 'Unknown')
        player_server = get_server_name(region)
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print(" Server Error ! ")
        print(" Please contact the admin. ! ")

        return None, None
    except (KeyError, json.JSONDecodeError) as e:
        # Handle JSON parsing errors or missing keys in the response
        print("Error ! Check UID ")

        return None, None
    except Exception as e:
        # Handle any other unexpected errors
        print("An unexpected error occurred:")
        print(" Please contact the admin. ! ")

        return None, None

    return name, player_server

def get_ban_info(user_id):
    cookies = {
        # Your cookies here
        '_gid': 'GA1.2.1130624825.1710338117',
        '_gat_gtag_UA_207309476_25': '1',
        '_ga_KE3SY7MRSD': 'GS1.1.1710338115.1.1.1710338131.0.0.0',
        '_ga_RF9R6YT614': 'GS1.1.1710338117.1.1.1710338132.0.0.0',
        '_ga': 'GA1.2.137519334.1710338115',
    }
    headers = {
        # Your headers here
         'authority': 'ff.garena.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        'referer': 'https://ff.garena.com/en/support/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'B6FksShzIgjfrYImLpTsadjS86sddhFH',
    }
    params = {
        'lang': 'en',
        'uid': user_id,
    }
    try:
        res = requests.get('https://ff.garena.com/api/antihack/check_banned', params=params, cookies=cookies, headers=headers)
        res.raise_for_status()  # Raise an error for HTTP errors
        response = res.json()
        status = response.get('status', 'Unknown')
        data = response.get('data', {})
        is_banned = data.get('is_banned', 'Unknown')
        if status == "success":
            if is_banned == 0:
                account_status = "Account Clear!"
            elif is_banned == 1:
                account_status = "Account banned!"
            else:
                account_status = "Unknown"
        else:
            account_status = "Unknown"
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print(" Server Error ! ")
        print(" Please contact the admin. ! ")

        return "Unknown"
    except (KeyError, json.JSONDecodeError) as e:
        # Handle JSON parsing errors or missing keys in the response
        print(" Please contact the admin. ! ")


        return "Unknown"
    except Exception as e:
        # Handle any other unexpected errors
        print("An unexpected error occurred:")
        print(" Please contact the admin. ! ")

        return "Unknown"

    return account_status

def main():
    user_id = input("Enter the user ID: ")
    name, player_server = get_info(user_id)
    if name is not None and player_server is not None:
        account_status = get_ban_info(user_id)
        print("User UID:", user_id)
        print("User nickname:", name)
        print("User region:", player_server)
        print("Account status:", account_status)

if __name__ == "__main__":
    main()
