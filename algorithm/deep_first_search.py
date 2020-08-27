graph={}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def deep_first_search(name):
    stack=[]
    stack.append(name)
    searched=[]
    while stack:
        person = stack.pop()
        print(person)
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                searched.append(person)
                persons = graph[person]
                for p in persons:
                    if p not in searched:
                        stack.append(p)
    return False

def person_is_seller(name):
    return name[-1] == 'm'
