"""
# Quiz5:Dictionary
# Quiz5_Wenhui_Yang
# Wenhui Yang
# 4/18/2019
"""
def main():
    # create quizDitn
    quizDitn = {}
    quizDitn["Accord"] = 23.44
    quizDitn["Camry"] = 25.00
    quizDitn["Mustang"] = 19.05
    quizDitn["Sebring"] = 23.81
    # a list of keys
    print("keys:", list(quizDitn.keys()))
    # check Highlander
    print("Check if Highlander is in dictionary:")
    print(quizDitn.get("Highlander", "this item is not in dictionary"))
    # change MPG of Camery to 26.8
    quizDitn.update({"Camry":26.8})
    # add a new model
    quizDitn.update({"Prius":45.5})
    # create copyDitn
    copyDitn = {}
    copyDitn = dict(quizDitn)
    # delete items 
    del quizDitn["Mustang"]
    del quizDitn["Sebring"]
    # modify copyDitn
    copyDitn.update({"Accord":27.40,"Cayenne":19.08,"Forte":26.05})
    # merge 
    quizDitn.update(copyDitn)
    # ask user to enter a model 
    model = input("Please enter a model name and get its value: ")
    model = model.title()
    listofkeys = list(quizDitn.keys())
    if model not in listofkeys:
        print("This model is not in dictionary")
    else:
        print("The model",model,"has value:",quizDitn[model])
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
