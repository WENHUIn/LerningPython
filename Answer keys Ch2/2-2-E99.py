## Calculate wieght loss during a triathlon.
cycling = float(input("Enter number of hours cycling: "))
running = float(input("Enter number of hours running: "))
swimming = float(input("Enter number of hours swimming: "))
pounds = (200 * cycling + 475 * running + 275 * swimming) / 3500
pounds =round(pounds, 1)
print("Weight loss:", pounds, "pounds")
