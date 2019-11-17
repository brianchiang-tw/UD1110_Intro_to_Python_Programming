points = 174  # use this input to make your submission

# write your if statement here

def congrats_str( prize_name ):
    str = "Congratulations! You won a {}!".format(prize_name)
    return str
    
if points >= 1 and points <= 50:
    result = congrats_str("wooden rabbit")
elif points >= 51 and points <= 150:
    result = "Oh dear, no prize this time."
elif points >= 151 and points <= 180:
    result = congrats_str("wafer-thin mint")
elif points >= 181 and points <= 200:
    result = congrats_str("penguin")
    

print(result)