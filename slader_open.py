import webbrowser
def slader():
    page_number = "asd"
    while page_number.lower()[0] != "q" or page_number.lower() !="quit":
        page_number = input("Page number: ")
        question_number = input("Questionnumber: ")
        slader = "https://www.slader.com/textbook/9781118230718-fundamentals-of-physics-10th-edition/{}/exercises/{}/".format(page_number,question_number)
        webbrowser.open(slader)

def main():
    slader()

if __name__ == "__main__":
    main()
