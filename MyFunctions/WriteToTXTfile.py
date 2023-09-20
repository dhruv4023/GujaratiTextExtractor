# import datetime
# import os
# import time


# def write_to_txt_file(data):
#     # Name of the output folder
#     output_folder = 'outputs'
#     time.sleep(1)
#     # Create the output folder if it doesn't exist
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     currrent_date_time=(str(datetime.datetime.now())[:19].replace(" ","_").replace(":","_"))
#     file_name=currrent_date_time+".txt"
    
#     # Specify the file path inside the output folder
#     output_file_path = os.path.join(output_folder, file_name)
#     # Open a .txt file in write mode
#     with open(output_file_path, 'w') as file:
#         # Write data to the file
#         file.write(data)
#     # The file will be automatically closed when the 'with' block exits
#     return  "data written at: "+'/output/'+currrent_date_time+'.txt'