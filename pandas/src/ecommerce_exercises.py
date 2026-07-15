import pandas as pd
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "Ecommerce Purchases"

def average_purchase_price(df):
    return df['Purchase Price'].mean()

def highest_purchase_price(df):
    return df['Purchase Price'].max()

def lowest_purchase_price(df):
    return df['Purchase Price'].min()

def number_of_english_speakers(df):
    return df['Language'].eq('en').sum()

def number_of_lawyers(df):
    return df['Job'].eq('Lawyer').sum()

def number_of_purchases_am_pm(df):
    return df['AM or PM'].value_counts()

def top_5_common_jobs(df):
    return df['Job'].value_counts().head(5)

def purchase_price_for_lot(df, lot):
    return df[df['Lot'].eq(lot)]['Purchase Price'].iloc[0]

def email_for_credit_card(df, credit_card_number):
    return df[df['Credit Card'] == credit_card_number]['Email'].iloc[0]

def number_of_american_express_above_95(df):
    return df[(df['CC Provider'].eq('American Express')) & (df['Purchase Price']>95)].count()

def number_of_credit_cards_expiring_in_2025(df):
    return len(df[df['CC Exp Date'].str.endswith('25')])

def top_5_email_providers(df):
    return df['Email'].str.split('@').str[-1].value_counts().head(5)


def main ():

    ecom = pd.read_csv(DATA_FILE)

    #Check the head of the DataFrame.
    print(f"Head of the DataFrame:\n{ecom.head()}")

    #How many rows and columns are there? Use the .info() method to find out.
    print("\nNumber of entries, returned through .info():")
    ecom.info()

    #What is the average Purchase Price?
    print(f"\nAverage Purchase Price: {average_purchase_price(ecom):.2f}")

    #What were the highest and lowest purchase prices?
    print(f"\nHighest Purchase Price: {highest_purchase_price(ecom)}")
    print(f"\nLowest Purchase Price: {lowest_purchase_price(ecom)}")

    #How many people have English 'en' as their Language of choice on the website?
    print(f"\nNumber of English speakers: {number_of_english_speakers(ecom)}")

    #How many people have the job title of "Lawyer" ?
    print(f"\nNumber of Lawyers: {number_of_lawyers(ecom)}")

    #How many people made the purchase during the AM and how many people made the purchase during PM ?
    print(f"\nNumber of Purchases by AM/PM:\n{number_of_purchases_am_pm(ecom)}")

    #What are the 5 most common Job Titles?
    print(f"\nTop 5 Common Job Titles:\n{top_5_common_jobs(ecom)}")

    #Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?
    print(f"\nPurchase Price for Lot '90 WT': {purchase_price_for_lot(ecom, '90 WT')}")

    #What is the email of the person with the following Credit Card Number: 4926535242672853?
    print(f"\nEmail for Credit Card '4926535242672853': {email_for_credit_card(ecom, 4926535242672853)}")

    #How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
    print(f"\nNumber of American Express users with purchases above $95:\n{number_of_american_express_above_95(ecom)}")

    #How many people have a credit card that expires in 2025?
    print(f"\nNumber of people with credit cards expiring in 2025: {number_of_credit_cards_expiring_in_2025(ecom)}")

    #What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)?
    print(f"\nTop 5 most popular email providers:\n{top_5_email_providers(ecom)}")

if __name__ == "__main__":
    main()