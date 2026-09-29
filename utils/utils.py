import csv


class state:
    def creat_account(self, username, password):

        with open("database.csv", "a", newline="") as file:
            writer = csv.writer(file)
            # genarate userid fuction {here}
            writer.writerow([None, username, password, 0, 0])

    def get_balance(acc_type, user_id):
        with open("database.csv", "r") as file:
            reader = csv.reader(file)

            for traget_user in reader:
                if traget_user[0] == user_id:
                    # should i put int here as pratik
                    balance = traget_user[acc_type]
                    return balance

    def set_balance(acc_type, user_id, U_balance):
        all_rows = []
        with open("database.csv", "r") as file:
            reader = csv.reader(file)

            for target_user in reader:
                if target_user[0] == user_id:
                    # balance= get_balance(acc_type,user_id)
                    # why does it not works [can't i call the function?]
                    balance = int(target_user[acc_type])
                    balance += U_balance
                    target_user[acc_type] = balance
                all_rows.append(target_user)

        with open("database.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(all_rows)

