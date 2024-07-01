# This is a sample Python script.

#
# VARIABLES
#
roomId = []
roomLength = []
roomWidth = []
sumPerRoom = []
global index
addAdditionalRoom = True

def main():
    index = 0
    roomInput(index)

    sumAll = 0
    sumAvg = 0
    for i in range(len(roomId)):
        print(f"{roomId[i]}:\n - {roomLength[i]}m x {roomWidth[i]}m\n - {sumPerRoom[i]}m²")
        sumAll += sumPerRoom[i]

    sumAvg = (sumAll / len(roomId))
    print(f"\nGesamtfläche aller Räume: {sumAll}m²")
    print(f"Durchschnittsfläche: {sumAvg}m²")


def roomInput(index):
    while(addAdditionalRoom):
        roomId.insert(index, str(input("Raum-Bezeichnung: ")))

        roomLength.insert(index, int(input("Länge: ")))
        roomWidth.insert(index, int(input("Breite: ")))

        sumPerRoom.insert(index, (roomLength[index] * roomWidth[index]))

        inputVal =  input("Willst du einen weiteren Raum hinzufügen? (y/n)\n")

        if inputVal == "y":  # == True
            index += 1  # Since we want another room we
            continue

        break ## If n then it will break since you don't want to add a room

if __name__ == "__main__":
    main()