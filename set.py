

def main():
    import time
    import json
    import RPi.GPIO as GPIO

    json_file_path = "stats.json"

    with open(json_file_path, 'r') as j:
        contents = json.loads(j.read())
        hunger = contents['hunger']
        thirst = contents['thirst']

    # print(hunger)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
   


    if hunger > 0:
        GPIO.output(2, True)


        if hunger > 1:
            GPIO.output(3, True)

            if hunger > 2:
                GPIO.output(4, True)

                if hunger > 3:
                    GPIO.output(5, True)

                    if hunger > 4:
                        GPIO.output(6, True)

                        if hunger > 5:
                            GPIO.output(7, True)

                            if hunger > 6:
                                GPIO.output(8, True)

                                if hunger > 7:
                                    GPIO.output(9, True)

                                    if hunger > 8:
                                        GPIO.output(10, True)

                                        if hunger > 9:
                                            GPIO.output(11, True)


    if thirst > 0:
        GPIO.output(12, True)

        if thirst > 1:
            GPIO.output(25, True)
        

            if thirst > 2:
                GPIO.output(14, True)

                if thirst > 3:
                    GPIO.output(15, True)

                    if thirst > 4:
                        GPIO.output(16, True)

                        if thirst > 5:
                            GPIO.output(17, True)

                            if thirst > 6:
                                GPIO.output(23, True)

                                if thirst > 7:
                                    GPIO.output(24, True)

                                    






    time.sleep(5)
    exec(open("cleanup.py").read())
if __name__ == "__main__":
    main()
