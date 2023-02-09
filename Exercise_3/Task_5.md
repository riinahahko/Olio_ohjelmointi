Create a class Dice and make an object of it. You shall be able to roll the dice, get the result (number between 1 –6) and set and get its color. Add at least 1 extra feature.
Design your program using pseudocode.Document your code properly (with good comments) and pay attention to the clarity of the output prints

Initialize class Dice with paramiter value {
    initialize method rollTheDice with parameter self {
        initialize variable diceSide with random value between 1 and 6
        
    }
    initialize method pickColor with parameter self {
        initialize list colors with random colors as values 
        initialize variable colorPick with random value 
        initialize variable color and assign colorPick as the selector for a value from colors, assign value to color
    }
    initialize method getSideandColor with parameter self {
        return diceSide, color
    }
    initialize method iForgot with parameter self {
        return i forgot 
    }
    initialize method iRemember with parameter self {
        return i remember
    }
}

initialize function main()
    create object Dice1 from class Dice
    call Dice1.rollTheDice() 
    initialize variable randomInt with random number from 0 to 1 
    if randomInt = 1 
    call Dice1 iForgor 
    initialize variable remeber with random number from 0 to 1 
    if remember = 1 
    else if remember = 0 
    return 0
    call Dice1.iRemember
    call.Dice1.pickColor()
    call Dice1,getSideAndColor()