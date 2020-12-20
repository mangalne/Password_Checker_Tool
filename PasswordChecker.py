import requests
import hashlib
import sys

def request_api_conn(hash_code5):
    url = 'https://api.pwnedpasswords.com/range/'+hash_code5
    res = requests.get(url)
    return res

def get_leaks_count(hashes, hash_to_be_matched):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash_parts, count in hashes:
        if(hash_parts == hash_to_be_matched):
            return count
    return 0


def password_checker_main(password):
    Sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    begin_hash_code, tail_hash_code = Sha1password[:5], Sha1password[5:]
    response = request_api_conn(begin_hash_code)
    leak_counts = get_leaks_count(response, tail_hash_code)
    if leak_counts:
        print(f"{password} has been breached by {leak_counts}, You should change your password")
    else:
        print(f"{password} is never leaked, You can carry on with this")



def password_checker():
    passwords = input("Enter the passwords ").split(',')
    for pwd in passwords:
        password_checker_main(pwd)
    return 'done'


if __name__ == '__main__':
    sys.exit(password_checker())
    # SYS.EXIT - make sure that you return back to command line




