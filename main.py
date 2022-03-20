import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

### CopyRight www.github.com/M-PRERNA ###

# activate the sysytem

def activate_analysis():
    data = pd.read_csv('company_sales_data.csv')
    print('---------------------------WELCOME TO COMPANY SALES INVENTORY---------------------------\n')
    print('****************************************************************************************\n')
    print('****************************************************************************************\n')
    print('****************************************************************************************\n')
    print('                                   COMMAND PALLETE                                      \n')
    print('****************************************************************************************\n')
    print('Press 1: To have a snapshot of the data\n')
    print('Press 2: To display total profits of each month\n')
    print('Press 3: To display the number of units sold per month for each product\n')
    print('Press 4: To read product sales data of each month and show it using a SCATTER plot\n')
    print('Press 5: To read product sales data of each month and show it using a BAR plot\n')
    print('Press 6: Calculate total sale data for last year for each product and show it using a Pie chart\n')
    print('Press 7: All products comparison sub plot\n')
    print('Press 8: QUIT\n')
    print('****************************************************************************************\n')
    # user input
    user_input = int(input("Enter your choice:  "))
    if(user_input == 1):
        show_data(data)
    elif(user_input == 2):
        tot_prof_months(data)
    elif(user_input == 3):
        sale_products(data)
    elif(user_input == 4):
        prod_specific_scatter(data)
    elif(user_input == 5):
        prod_specific_bar(data)
    elif(user_input == 6):
        tot_sale_pie_chart(data)
    elif(user_input == 7):
        all_prod_comparison_subplots(data)
    elif(user_input == 8):
        print('---------------------------END OF PROGRAM---------------------------------')
    else:
        print('Please enter a valid response!!!!!')

# Display the intial rows of the csv
def show_data(data):
    # pass
    print('showing snapshot of data\n')
    print(data.head())
    print('\n')
    print('Data Description:\n')
    print(data.describe())
    print('\n')
    activate_analysis()
    

# Display the number of units sold each month
def tot_prof_months(data):
    # print('show data')
    print('Displaying the number of units sold per month for each product:\n')
    profitList = data ['total_profit'].tolist()
    monthList  = data ['month_number'].tolist()

    plt.plot(monthList, profitList, label = 'Profit data of last year', 
            color='r', marker='o', markerfacecolor='k', 
            linestyle='--', linewidth=3)
      
    plt.xlabel('Month Number')
    plt.ylabel('Profit in dollar')
    plt.legend(loc='lower right')
    plt.title('Company Sales data of last year')
    plt.xticks(monthList)
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.show()
    activate_analysis()


# '''Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ).'''
def sale_products(data):
    monthList  = data ['month_number'].tolist()
    faceCremSalesData   = data ['facecream'].tolist()
    faceWashSalesData   = data ['facewash'].tolist()
    toothPasteSalesData = data ['toothpaste'].tolist()
    bathingsoapSalesData   = data ['bathingsoap'].tolist()
    shampooSalesData   = data ['shampoo'].tolist()
    moisturizerSalesData = data ['moisturizer'].tolist()
    plt.plot(monthList, faceCremSalesData,   label = 'Face cream Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, faceWashSalesData,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
    plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
    plt.plot(monthList, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)

    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.legend(loc='upper left')
    plt.xticks(monthList)
    plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
    plt.title('Sales data')
    plt.show()
    activate_analysis()


# '''Read toothpaste sales data of each month and show it using a scatter plot'''
def prod_specific_scatter(data):
    # print('show data')
    monthList  = data ['month_number'].tolist()
    print('Enter the product whose scatter plot you want: facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer\n')
    name = input('ENTER THE PRODUCT NAME: \n')
    if name=="facecream":
        faceCremSalesData = data['facecream'].tolist()
        plt.scatter(monthList, faceCremSalesData, label = 'Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' FACE CREAM Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
    elif name=="facewash":
        faceWashSalesData = data['facecream'].tolist()
        plt.scatter(monthList, faceWashSalesData, label = 'Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' FACE WASH Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
    elif name=="bathingsoap":
        bathingsoapSalesData = data['bathingsoap'].tolist()
        plt.scatter(monthList, bathingsoapSalesData, label = 'Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' bathingsoap Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
    elif name=="shampoo":
        shampooSalesData = data['shampoo'].tolist()
        plt.scatter(monthList, shampooSalesData, label = 'Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' shampoo Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
    elif name=="moisturizer":
        moisturizerSalesData = data['moisturizer'].tolist()
        plt.scatter(monthList, moisturizerSalesData, label = 'Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' moisturizer Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
    elif name=="toothpaste":
        toothPasteSalesData = data['toothpaste'].tolist()
        plt.scatter(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' Tooth paste Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
        activate_analysis()


# '''Read product sales data of each month and show it using a bar plot'''
def prod_specific_bar(data):
    monthList  = data ['month_number'].tolist()
    print('Enter the product whose BAR plot you want: facecream, facewash, toothpaste, bathingsoap, shampoo, moisturizer\n')
    name = input('ENTER THE PRODUCT NAME: \n')
    if name=="facecream":
        faceCremSalesData = data['facecream'].tolist()
        plt.bar(monthList, faceCremSalesData, label = 'Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' FACE CREAM Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
    elif name=="facewash":
        faceWashSalesData = data['facecream'].tolist()
        plt.bar(monthList, faceWashSalesData, label = 'Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' FACE WASH Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
    elif name=="bathingsoap":
        bathingsoapSalesData = data['bathingsoap'].tolist()
        plt.bar(monthList, bathingsoapSalesData, label = 'Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' bathingsoap Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
    elif name=="shampoo":
        shampooSalesData = data['shampoo'].tolist()
        plt.bar(monthList, shampooSalesData, label = 'Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' shampoo Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
    elif name=="moisturizer":
        moisturizerSalesData = data['moisturizer'].tolist()
        plt.bar(monthList, moisturizerSalesData, label = 'Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' moisturizer Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
    elif name=="toothpaste":
        toothPasteSalesData = data['toothpaste'].tolist()
        plt.bar(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
        plt.xlabel('Month Number')
        plt.ylabel('Number of units Sold')
        plt.legend(loc='upper left')
        plt.title(' Tooth paste Sales data')
        plt.xticks(monthList)
        plt.grid(True, linewidth= 1, linestyle="--")
        plt.show()
        activate_analysis()
    

# '''Calculate total sale data for last year for each product and show it using a Pie chart'''
def tot_sale_pie_chart(data):
    monthList  = data ['month_number'].tolist()

    labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
    salesData   = [data ['facecream'].sum(), data ['facewash'].sum(), data ['toothpaste'].sum(), 
             data ['bathingsoap'].sum(), data ['shampoo'].sum(), data ['moisturizer'].sum()]
    plt.axis("equal")
    plt.pie(salesData, labels=labels, autopct='%1.1f%%')
    plt.legend(loc='lower right')
    plt.title('Sales data')
    plt.show()
    activate_analysis()

# '''Read Bathing soap facewash of all months and display it using the Subplot'''
def all_prod_comparison_subplots(data):
    monthList  = data ['month_number'].tolist()
    bathingsoap   = data['bathingsoap'].tolist()
    faceWashSalesData   = data['facewash'].tolist()
    toothPasteSalesData = data ['toothpaste'].tolist()
    bathingsoapSalesData   = data ['bathingsoap'].tolist()
    shampooSalesData   = data ['shampoo'].tolist()
    moisturizerSalesData = data ['moisturizer'].tolist()

    f, axarr = plt.subplots(6, sharex=True)
    axarr[0].plot(monthList, bathingsoap, label = 'Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
    axarr[0].set_title('Sales data of  a Bathingsoap')
    
    axarr[1].plot(monthList, faceWashSalesData, label = 'Face Wash Sales Data', color='r', marker='o', linewidth=3)
    axarr[1].set_title('Sales data of  a facewash')
    
    axarr[2].plot(monthList, toothPasteSalesData, label = 'Tooth Paste Sales Data', color='r', marker='o', linewidth=3)
    axarr[2].set_title('Sales data of  a toothpaste')
    
    axarr[3].plot(monthList,bathingsoapSalesData , label = 'Bathing Soap Sales Data', color='r', marker='o', linewidth=3)
    axarr[3].set_title('Sales data of  a bathingsoap')
    
    axarr[4].plot(monthList, shampooSalesData , label = 'Shapmoo Sales Data', color='r', marker='o', linewidth=3)
    axarr[4].set_title('Sales data of  a shampoo')
    
    axarr[5].plot(monthList, moisturizerSalesData, label = 'Moisturizer Sales Data', color='r', marker='o', linewidth=3)
    axarr[5].set_title('Sales data of  a moisturizer')
    
    plt.xticks(monthList)
    plt.xlabel('Month Number')
    plt.ylabel('Sales units in number')
    plt.show()
    activate_analysis()


# the main method
if __name__ == "__main__":
    activate_analysis()
