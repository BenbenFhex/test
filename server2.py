
def main():
    while True:
        server2 = input("")  # No prompt text
        with open("server2_data.txt", "w") as f:
            f.write(server2)

if __name__ == "__main__":
    main()


