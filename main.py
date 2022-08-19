# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests as requests


def manage_banned_accounts():
    with open('account_input.txt', 'r') as f:
        output = open('account_output.txt', 'w')
        for account in f.readlines():
            response = requests.get(
                url=f"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player={account}")
            if response.status_code == 200:
                output.write(account)
            if response.status_code == 404:
                print(f'{account} is not found on the highscores. Its either banned or locked')

        print("Done checking list of accounts. You can find unbanned accounts in account_output.txt file :-)")



if __name__ == '__main__':
    manage_banned_accounts()
