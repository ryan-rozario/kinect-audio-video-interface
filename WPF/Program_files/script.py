import requests
import base64
import time
import sys
"""This is to play the video"""
def play(ip, port, authorization):
    try:
        final_url='http://'+str(ip)+':'+str(port)+'/requests/status.xml?command=pl_play'
        print(final_url)
        header={'Authorization':authorization}
        print(authorization,'-authorization')
        r=requests.get(final_url,headers=header)
    except:
        print('Connection issue...')

"""This is to stop the video"""
def pause(ip, port, authorization):
    try:
        header={'Authorization':authorization}
        final_url='http://'+str(ip)+':'+str(port)+'/requests/status.xml?command=pl_pause'
        r=requests.get(final_url,headers=header)
    except:
        print('Connection issue...')

"""This is to increase or decrease the volume
    flag - it can be + or -
    value - number by which volume needs to be changed
"""
def volume(ip,port, authorization, flag, value):
    try:
        header={'Authorization':authorization}
        final_url='http://'+str(ip)+':'+str(port)+'/requests/status.xml?command=volume&val='+str(flag)+str(value)
        r=requests.get(final_url,headers=header)
    except :
        print('Connetion issue...')
def main():
    gesture=sys.argv[1]
    passwd=sys.argv[2]
    passwd=':'+passwd
    authorization='Basic '+base64.b64encode(passwd.encode()).decode()
    print(authorization)
    if gesture == 'SwipeLeft':
        pause('127.0.0.1','8080',authorization)
    elif gesture == 'SwipeRight':
        play('127.0.0.1','8080',authorization)

    # Testing play function
    # play('127.0.0.1','8080',authorization)
    # time.sleep(15)
    # Testing pause function
    # pause('127.0.0.1','8080',authorization)
    # Testing volume function
    # volume('127.0.0.1', '8080', authorization, '-', '100')
    # volume('127.0.0.1', '8080', authorization, '+', '100')
if __name__ == '__main__':
    main()
