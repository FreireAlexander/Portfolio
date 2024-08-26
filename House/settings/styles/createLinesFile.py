import os

PATH = "./Linetypes/LinesFiles"

def main():
    files = os.listdir(PATH)
    print(f"Files in Linetypes directory: {files}")
    print("Opening is .lin files in LinesFiles Directory")
    lineContent = ""
    for file in files:
        with open(PATH+f"/{file}", "r") as f:
            data = f.read()
            lineContent += data
        
        f.close()

    with open("temps.lin", "w") as linFile:
        linFile.write(lineContent)

    linFile.close()

if __name__ == "__main__":
    main()