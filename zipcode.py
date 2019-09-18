from banner import banner
banner("ZIP CODE SORTER", "Mr. Baldus")

print("Welcome to the Newaygo County zip code sorter.")

go_again = True
while go_again:
    zip_code = int(input("Please enter a zip code: "))
    if zip_code == 49309:
        print(f"The zip code {zip_code} is for Bitely.")
    elif zip_code == 49312:
        print(f"The zip code {zip_code} is for Brohman.")
    elif zip_code == 49337:
        print(f"The zip code {zip_code} is for Croton and Newaygo.")
    elif zip_code == 49412:
        print(f"The zip code {zip_code} is for Fremont.")
    elif zip_code == 49413:
        print(f"The zip code {zip_code} is for Fremont.")
    elif zip_code == 49327:
        print(f"The zip code {zip_code} is for Grant.")
    elif zip_code == 49349:
        print(f"The zip code {zip_code} is for White Cloud.")
    else:
        print(f"The zip code {zip_code} is not in Newaygo County.")

    go_again = False
    if input("Would you like to enter another zip code (Y/N)? ") == "Y":
        print("")
        go_again = True

print("Thank you for using the Newaygo County Zip Code Sorter. Goodbye!")
