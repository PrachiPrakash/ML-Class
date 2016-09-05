import pandas as pd 

def main():
	df = pd.read_csv(r'/Users/prakash/DataSets/lending-club-data.csv')
	df['good_loan'] = df['bad_loans'].apply(lambda x: 1 if x==0 else -1)
	del df['bad_loans']

	features = ['grade',                     # grade of the loan
            'sub_grade',                 # sub-grade of the loan
            'short_emp',                 # one year or less of employment
            'emp_length_num',            # number of years of employment
            'home_ownership',            # home_ownership status: own, mortgage or rent
            'dti',                       # debt to income ratio
            'purpose',                   # the purpose of the loan
            'term',                      # the term of the loan
            'last_delinq_none',          # has borrower had a delinquincy
            'last_major_derog_none',     # has borrower had 90 day or worse rating
            'revol_util',                # percent of available credit being used
            'total_rec_late_fee',        # total late fees received to day
           ]

	target = 'good_loan'
	df = df[features + [target]]
	df.to_csv(r'./loan_dataset.csv')

main()