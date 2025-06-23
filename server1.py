def main():
    while True:
        server1 = input("")  # No prompt text
        with open("server1_data.txt", "w") as f:
            f.write(server1)

if __name__ == "__main__":
    main()


