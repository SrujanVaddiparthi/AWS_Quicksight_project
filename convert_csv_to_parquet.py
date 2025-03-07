import pandas as pd
import os

def convert_parquet_to_csv(filepath):
    
    #converts a .parquet file to a .csv file with the same name.
   
    try:
        filepath_csv = os.path.splitext(filepath)[0] + ".csv"
        pd.read_parquet(filepath).to_csv(filepath_csv, index=False)
        print(f"CSV file created: {filepath_csv}")
        return filepath_csv
    except Exception as e:
        print(f"Error: {e} | File: {filepath}")
        return None

def convert_csv_to_parquet(filepath):
    
    #converts a .parquet file to a .csv file with the same name.
   
    try:
        filepath_parquet = os.path.splitext(filepath)[0] + ".parquet"
        pd.read_csv(filepath).to_parquet(filepath_parquet, index=False)
        print(f"parquet file created: {filepath_parquet}")
        return filepath_parquet
    except Exception as e:
        print(f"Error: {e} | File: {filepath}")
        return None

def main():
    # #directory of parquet files
    # data_dir = "/Users/wangtiles/ITT_offline_research/numpy_ndarray_trial/Dataframes_2/FFT_Processed_2/pumpfreq_X_Condition_X_FFT_Level_Data"

    # #list all parquet files
    # parquet_files = [f for f in os.listdir(data_dir) if f.endswith(".parquet")]

    # if not parquet_files:
    #     print("No .parquet files found in the directory.")
    #     return

    # print(f"Found {len(parquet_files)} Parquet files. Converting to CSV...")

    # # convert parquet to CSV
    # for file in parquet_files:
    #     file_path = os.path.join(data_dir, file)
    #     convert_parquet_to_csv(file_path)

    # print(" DONE!")
    convert_csv_to_parquet("/Users/wangtiles/AWS_Quicksight_project/ai4i2020.csv")

    # convert_parquet_to_csv("/Users/wangtiles/ITT_offline_research/numpy_ndarray_trial/Dataframes_2/FFT_Processed_2/LOW_HIGH_Level_Data/log_reg_confusion_matrix_(LOW)_scaled.parquet")


if __name__ == '__main__':
    main()


