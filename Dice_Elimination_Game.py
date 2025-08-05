import random

numbers = list(range(1, 13))  # numbers from 1 to 12

print("🎲 Welcome to the Dice Elimination Game!")
print("Goal: Remove all numbers from 1 to 12 using dice rolls.")
print("Rules:")
print("On each roll, you can remove:")
print(" - the sum of the dice (die1 + die2)")
print(" - or both dice results together (die1 and die2)\n")

while numbers:
    print(f"Remaining numbers: {numbers}")
    choice = input("Roll the Dice? (y/n): ").lower()
    
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        print(f"You rolled: ({die1}, {die2}) → sum = {roll_sum}")

        # gather valid moves
        valid_moves = {}
        if roll_sum in numbers:
            valid_moves['1'] = [roll_sum]
        if die1 in numbers and die2 in numbers:
            valid_moves['2'] = [die1, die2]

        if not valid_moves:
            print("❌ No valid moves! Game Over.")
            break

        # show options
        print("Valid moves:")
        for key, move in valid_moves.items():
            if len(move) == 2:
                print(f"{key}: Remove {move[0]} and {move[1]}")
            else:
                print(f"{key}: Remove {move[0]}")

        move = input("Choose an option (1/2): ")
        
        if move in valid_moves:
            for num in valid_moves[move]:
                numbers.remove(num)
            print(f"✅ Removed {valid_moves[move]}")
        else:
            print("Invalid choice! Try again.")

    elif choice == 'n':
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice, please enter y or n.")

if not numbers:
    print("🎉 Congratulations! You cleared all the numbers!")
