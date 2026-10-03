import zipfile
import pandas as pd

def create_cleaned_dataset(input_file: str) -> pd.DataFrame:
    ## Load the dataset ##
    try:
        with zipfile.ZipFile(input_file, 'r') as z:
            with z.open(z.namelist()[0]) as f:
                file = pd.read_csv(f)
    except FileNotFoundError:
        print("File not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()
    else:
        print("File loaded successfully.")
    ## Cleaning ##

    # Remove the html tags from the review column
    file['Clean reviews'] = file['review_body'].str.replace(r'<[^<>]*>','',regex=True)# Removes HTML language
    # Remove a specific string that is repeated
    file['Clean reviews'] = file['Clean reviews'].str.replace('ASIN:','',regex=True)
    # Keep only English letters and spaces
    file['Clean reviews'] = file['Clean reviews'].str.replace(r'[^a-zA-Z\s]',' ',regex=True)
    # Drop all rows if they contain any null values
    file = file.dropna()

    ## Preprocessing ##

    # Further preprocessing the dataframe's 'review_body' column
    # Drop the old unprocessed 'review_body' column
    file = file.drop(columns=['review_body'])
    # Transform the 'review_date' column to a datetime python object
    file['review_date'] = pd.to_datetime(file['review_date'], format="mixed")
    file['review_date'] = file['review_date'].dt.strftime('%d/%m/%Y')
    file["review_date"] = pd.to_datetime(file["review_date"])
    # Convert the 'vine' and 'verified_purchase' columns to integers
    # Convert 'Vine' to a binary integer column
    file['vine'] = file['vine'].map({'Y':1,'N':0}).astype(int)
    file['verified_purchase'] = file['verified_purchase'].map({'Y':1,'N':0}).astype(int)
    # Drop unnecesary columns
    output_file = file.drop(columns=['customer_id','review_date','review_id','product_id','product_parent','product_title','product_category']) 
    return output_file

