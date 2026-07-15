from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).parent.parent / "data" / "Salaries.csv"

def average_base_pay(df):
    return df['BasePay'].mean()

def highest_overtime_pay(df):
    return df['OvertimePay'].max()

def job_title_of_joseph_driscoll(df):
    return df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'].iloc[0]

def salary_of_joseph_driscoll(df):
    return df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'].iloc[0]

def highest_paid_person(df):
    return df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()]['EmployeeName'].iloc[0]

def lowest_paid_person(df):
    return df.loc[df['TotalPayBenefits'].idxmin()]['EmployeeName']

def average_base_pay_per_year(df):
    return df.groupby('Year')['BasePay'].mean()

def unique_job_titles(df):
    return df['JobTitle'].nunique()

def top_5_common_jobs(df):
    return df['JobTitle'].value_counts().head(5)

def job_titles_with_one_person_in_2013(df):
    return sum(df[df['Year'] == 2013]['JobTitle'].value_counts() == 1)

def job_titles_with_chief(df):
    return df['JobTitle'].str.contains('Chief', case=False, na=False).sum()

def correlation_between_job_title_length_and_salary(df):
    df['title_len'] = df['JobTitle'].apply(len) 
    return df[['title_len','TotalPayBenefits']].corr()

def main ():
    
    sal = pd.read_csv(DATA_FILE)

    #Check the head of the DataFrame.
    print(f"Head of the DataFrame:\n{sal.head()}")

    #Use the .info() method to find out how many entries there are.
    print("\nNumber of entries, returned through .info():")
    sal.info()

    #What is the average BasePay ?
    print(f"\nAverage BasePay: {average_base_pay(sal)}")

    #What is the highest amount of OvertimePay in the dataset ?
    print(f"\nHighest OvertimePay: {highest_overtime_pay(sal)}")

    #What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll).
    print(f"\nJob title of JOSEPH DRISCOLL: \n{job_title_of_joseph_driscoll(sal)}")

    #How much does JOSEPH DRISCOLL make (including benefits)?
    print(f"\nSalary of JOSEPH DRISCOLL: \n${salary_of_joseph_driscoll(sal):,.2f}")

    # What is the name of highest paid person (including benefits)?
    print(f"\nName of highest paid person: {highest_paid_person(sal)}")

    #What is the name of lowest paid person (including benefits)?
    print(f"\nName of lowest paid person: {lowest_paid_person(sal)}")

    #What was the average (mean) BasePay of all employees per year? (2011-2014) ?
    print(f"\nAverage BasePay per year:\n{average_base_pay_per_year(sal)}")

    #How many unique job titles are there?
    print(f"\nNumber of unique job titles: {unique_job_titles(sal)}")

    #What are the top 5 most common jobs?
    print(f"\nTop 5 most common jobs:\n{top_5_common_jobs(sal)}")

    #How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?)
    print(f"\nNumber of job titles represented by only one person in 2013: {job_titles_with_one_person_in_2013(sal)}")

    #How many people have the word Chief in their job title?
    print(f"\nNumber of people with 'Chief' in their job title: {job_titles_with_chief(sal)}")

    #Is there a correlation between length of the Job Title string and Salary?
    print(f"\nCorrelation between job title length and salary:\n{correlation_between_job_title_length_and_salary(sal)}")

if __name__ == "__main__":
    main()

