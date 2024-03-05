key_balance = "balance"


def add_balance(account):
    '''
    sample code
    '''
    balance = sum(account["transactions"])
    account[key_balance] = balance
    return account


accounts = [
    {"name": "Manoj", "acc_no": "BNK123MYS", "transactions": [
        1200, -200, 300, -500, 500, 567, 456]},
    {"name": "Alice", "acc_no": "BNK456USA", "transactions": [
        1500, -300, 400, -600, 700, 300, 200]},
    {"name": "Bob", "acc_no": "BNK789CAN", "transactions": [
        2000, -400, 500, -700, 800, 400, 300]},
    {"name": "Emily", "acc_no": "BNK101UK", "transactions": [
        1800, -250, 350, -550, 600, 200, 150]},
    {"name": "John", "acc_no": "BNK202AUS", "transactions": [
        2200, -500, 600, -800, 900, 500, 400]},
    {"name": "Sophia", "acc_no": "BNK303GER", "transactions": [
        1300, -150, 250, -450, 550, 167, 356]},
    {"name": "David", "acc_no": "BNK404FRA", "transactions": [
        1700, -280, 380, -580, 680, 450, 320]},
    {"name": "Emma", "acc_no": "BNK505IND", "transactions": [
        1900, -320, 420, -620, 720, 470, 370]},
    {"name": "Michael", "acc_no": "BNK606JPN", "transactions": [
        2100, -450, 550, -750, 850, 550, 450]},
    {"name": "Olivia", "acc_no": "BNK707ITA", "transactions": [
        2400, -600, 700, -900, 1000, 600, 500]},
    {"name": "William", "acc_no": "BNK808ESP", "transactions": [
        2600, -700, 800, -1000, 1100, 700, 600]},
    {"name": "Ava", "acc_no": "BNK909BRA", "transactions": [
        2800, -800, 900, -1100, 1200, 800, 700]},
    {"name": "James", "acc_no": "BNK010RUS", "transactions": [
        3000, -900, 1000, -1200, 1300, 900, 800]},
    {"name": "Isabella", "acc_no": "BNK111ARG", "transactions": [
        3200, -1000, 1100, -1300, 1400, 1000, 900]},
    {"name": "Alexander", "acc_no": "BNK212EGY", "transactions": [
        3400, -1100, 1200, -1400, 1500, 1100, 1000]},
    {"name": "Mia", "acc_no": "BNK313NGA", "transactions": [
        3600, -1200, 1300, -1500, 1600, 1200, 1100]},
    {"name": "Benjamin", "acc_no": "BNK414SAU", "transactions": [
        3800, -1300, 1400, -1600, 1700, 1300, 1200]},
    {"name": "Charlotte", "acc_no": "BNK515TUR", "transactions": [
        4000, -1400, 1500, -1700, 1800, 1400, 1300]},
    {"name": "Elijah", "acc_no": "BNK616POL", "transactions": [
        4200, -1500, 1600, -1800, 1900, 1500, 1400]},
    {"name": "Amelia", "acc_no": "BNK717MEX", "transactions": [
        4400, -1600, 1700, -1900, 2000, 1600, 1500]}
]

new_accounts = list(map(add_balance, accounts))
# new_accounts_lambda = list(map(lambda account: account["balance"] = sum(
#   account["transactions"]), accounts))
print(new_accounts)
print("\n\n")
balance_less_than_5k = list(filter(
    lambda account: account[key_balance] < 5000, new_accounts))
print(balance_less_than_5k)


