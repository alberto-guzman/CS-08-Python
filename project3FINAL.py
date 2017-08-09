# defining main function


def main():
    choice = 0
    rep_dict = {}

    # cause it to quit if user chooses 7

    while choice != 7:
        choice = menu()
        print('\n')

        # show list

        if choice == 2:
            print("Recipient list:" + '\n')
            print('-------------------' + '\n')
            for key in rep_dict.keys():
                print(key)
            print('-------------------' + '\n')

         # add to list

        elif choice == 3:
            shortname = input('Short name:')
            fullname = input('Full name:')
            address = input_address()
            if shortname in rep_dict:
                print("Recipient exists" + '\n')
            else:
                name = Recipient(shortname)
                name.fullname = fullname
                name.address = address
                rep_dict[shortname] = name
                for key in rep_dict.keys():
                    print(key)

         # delete from list

        elif choice == 4:
            name = input('Name (blank to cancel):')
            if name in rep_dict:
                del rep_dict[name]
            elif name not in rep_dict:
                print('No such recipient')
            elif name == '':
                break

         # apply mail merge

        elif choice == 1:
            while True:
                try:
                    file_name = input("Template filename:")
                    file = open(file_name, 'r')
                    line = file.readline()
                    print("File Imported Successfully")
                    break
                except:
                    print("File was not Imported! Try again")
            content = ''
            while line != '':
                line = file.readline()
                content += line
            for i in rep_dict:
                output = "letter." + i + ".txt"
                file_dict = open(output, 'w')
                fill = rep_dict[i].mailmerge(content)
                file_dict.write(fill)
                file_dict.close()

         # export

        elif choice == 6:
            import pickle
            output_file = open('recipients.bin', 'wb')
            pickle.dump(rep_dict, output_file)
            output_file.close()
            print("Recipients exported to recipients.bin")

        # import

        elif choice == 5:
            import pickle
            while True:
                try:
                    input_file = open('recipients.bin', 'rb')
                    rep_dict = pickle.load(input_file)
                    input_file.close()
                    print("Recipients imported from recipients.bin")
                    break
                except:
                    print("Import was NOT succesful!! Try again")

# displays menu


def menu():
    print('Enter your choice:')
    print('1) Apply a main merge')
    print('2) List recipients')
    print('3) Add recipient')
    print('4) Delete recipient')
    print('5) Import recipient list')
    print('6) Export recipient list')
    print('7) Quit')
    while True:
        try:
            choice = int(input())
        except:
            print("Please enter a valid number!")
        if choice >= 1 and choice <= 7:
            print('\n')
            print('You selected', choice)
            print('\n')
            return choice
        else:
            print("Please enter a valid number!")


# defining the recipient Class

class Recipient:
    def __init__(self, shortname):
        self.__shortname = shortname
        self.fullname = ''
        self.address = ''

    @property
    def shortname(self):
        return self.__shortname

# need to complete this

    def mailmerge(self, text):
        print(self.__shortname)
        text = text.replace('{address}', self.address)
        text = text.replace('{fullname}', self.fullname)
        text = text.replace('{shortname}', self.shortname)
        return text

# defining input address funciton


def input_address():
    lines = []
    while True:
        line = input('Address:')
        if line:
            lines.append(line)
        else:
            break
    address = '\n'.join(lines)
    return address

# call to main
main()
