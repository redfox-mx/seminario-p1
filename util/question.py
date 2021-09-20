INPUT_QUESTION = 1
OK_QUESTION = 2

def qinput(question):
    ans = input(question)
    return ans

def qok(question: str):
    question = question[:-1] if question[-1] == '?' else question
    ans = qinput(question.strip() + ' [ Enter / q] ? ')
    while ans != 'q' and ans != '':
        ans = qinput(question.strip() + ' [ Enter / q] ? ')
    
    return False if ans == 'q' else True
    