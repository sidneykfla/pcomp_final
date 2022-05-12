import json
import sys

class Rock:
    #def __init__(self):
    def play(self):
        #print("Your rock sits there, unable to move but moderately happier.")
        self.print_self()
        print("Your rock sits there, unable to move but moderately happier.")
        exec(open("set.py").read())

        
    def feed(self):
        #print("Your rock cannot eat but somehow adjusts its nourishment levels accordingly.")
        self.print_self()
        print("Your rock cannot eat but somehow adjusts its nourishment levels accordingly.")
        exec(open("set.py").read())
        
    def give_water(self):
        #print("Your rock...somehow drinks? It's not supposed to be able to do that. Thirst levels are adjusted accordingly.")
        self.print_self()
        print("Your rock...somehow drinks? It's not supposed to be able to do that.")
        exec(open("set.py").read())
        
    def print_self(self):
        for i in range(15):
            print()

        print("          /---------\ ")
        print("        /             \ ")
        print("       /               \ ")
        print("      /      -   -      \ ")
        print("      |                 |")
        print("       \       ---     / ")
        print("        \             /")
        print("          ----------- ")
        
        
    
def update(hunger_or_thirst):
    json_file_path = "stats.json"

    with open(json_file_path, 'r') as j:
         contents = json.loads(j.read())
       
    if contents[hunger_or_thirst] <= 7:
        contents[hunger_or_thirst] += 3
    else:
        contents[hunger_or_thirst] = 10
    
    with open("stats.json", "w") as jsonFile:
        json.dump(contents, jsonFile)
        
def print_hunger():
    json_file_path = "stats.json"

    with open(json_file_path, 'r') as j:
         contents = json.loads(j.read())
     
    print()
    print("Hunger level: " + str(contents['hunger']))
    print("Thirst level: " + str(contents['thirst']))
    
def print_thirst():
    json_file_path = "stats.json"

    with open(json_file_path, 'r') as j:
         contents = json.loads(j.read())
    
    print()
    print("Hunger level: " + str(contents['hunger']))
    print("Thirst level: " + str(contents['thirst']))
        

def main():
    if sys.argv[1] == "True":
        exec(open("cron1.py").read())
        # exec(open("cron2.py").read())
    
    rock = Rock()
    
    print("press w to quit")
    while True:
        action = input("How do you want to interact with your rock? ")
        while (action != "play" and action != "feed" and action != "give water" and action != "secret"):
            if action == "w":
                break
            elif action == "fight":
                print("Please don't fight your rock.")
                print()
            print("You can only 'play', 'feed', or 'give water' to your rock!")
            print()
            action = input("How do you want to interact with your rock? ")

        if action == "play":
            rock.play()
            print_hunger()

        elif action == "feed":
            update('hunger')
            rock.feed()
            print_hunger()
            

        elif action == "give water":
            update('thirst')
            rock.give_water()
            print_thirst()
            

        elif action == "w":
            break
    
    
        

if __name__ == "__main__":
    main()
