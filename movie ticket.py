#moive tickets:

print("\nWelcome to PVR cinimas!\n")

print(input("Choose your movie:"))

print("select the seats: ")

print(f"balcony{1}",f"Primium{2}",f"economy{3}",f"budjet{4}")

balcony=int(input("balcony:"))

Premium=int(input("Premium:"))

economy=int(input("economy:"))

budjet=int(input("budjet:"))

if balcony<=1:
   price_per_ticket=print("The price for balcony tickets is 250.00")

elif Premium<=2:
    price_per_ticket=print("The price for primium tickets is 200.00")

elif economy<=3:
    price_per_ticket=print("The price for economy tickets is 150.00")

elif budjet<=4:
    price_per_ticket=print("The price for buject tickets is 100.00")

else:
    print("Please select your seats!")
   
    
#movie ticket price calculation:
def calculate_total_cost(num_tickets, price_per_ticket):
    total_cost = num_tickets * price_per_ticket
    return total_cost
def main():
    print("Welcome to the Movie Ticket Calculator!")


    try:
        num_tickets = int(input("Enter the number of tickets: "))
        price_per_ticket = float(input("Enter the price per ticket: "))

        if num_tickets < 0 or price_per_ticket < 0:
            print("The number of tickets and the price per ticket must be non-negative.")
        else:
            total_cost = calculate_total_cost(num_tickets, price_per_ticket)
            print(f"The total cost for {num_tickets} ticket(s) at {total_cost:.2f} per ticket is {price_per_ticket:.2f}.")
    except ValueError:
        print("Please enter valid numbers for the number of tickets and the price per ticket.")

if __name__ == "__main__":
    main() 