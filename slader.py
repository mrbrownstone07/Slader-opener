import webbrowser
def slader():
    print "#####\tThis is slader script .\n It works until You write \"quit\" or something starts with q\t#####"
    page_number = "asd"
    while page_number.lower()[0] != "q" or page_number.lower() != "quit":
        page_number = raw_input("Page number please  \n ")
        question_number = raw_input("Question number please \n")
        slader = "http://www.slader.com/textbook/9780495011668-stewart-calculus-early-transcendentals-6th-edition/"+page_number+"/exercises/"+question_number+"/"
        webbrowser.open(slader)
slader()
