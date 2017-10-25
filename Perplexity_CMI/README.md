Objective: Find CMI(Code Mixing Index) for every utterance and divide the data into chunks based on the CMI values.

Files:
"1_train_data.json": Contains an json object. It has nearly 10k tweets with tags attached to each word.

"2_1_preprocess.py": Preprocess the data - Retreives the data from the 'text' and 'lang_tagged_text' attributes and stores them in the respective files(3_text.txt and 3_lang_tagged_text.txt).

"2_2_CMI.py": Finds CMI for every utterance(Cu) and stores the values in order in file "3_CMI_values.txt" using the tags of each utterance that were stored in "3_lang_tagged_text.txt"

"2_3_dataToChunks.py": Based on the CMI values stored in "3_CMI_values.txt", it divides the data in "3_text.txt" into 10 different chunks based on the CMI values in the range of 10 from 0 to 100.

Folders:
"Chunks" folder contains 10 text files and the data in each file is stored based on their CMI values ("2_3_dataToChunks.py" does this job)

"CMIv2programme" folder contains pre-written files for 
