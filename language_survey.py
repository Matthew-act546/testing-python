from survey import AnonymousSurvey

question = "What is your programming langguage/s"

my_survey= AnonymousSurvey(question)
my_survey.show_question()

while True:
    response = input("(press q to quit)\nInput here: ")
    if response == 'q':
        break
    
    my_survey.store_responses(response)

print("Thank you for answering our survey anonymous!\nthese are the programming langguages that you know")
my_survey.show_results()