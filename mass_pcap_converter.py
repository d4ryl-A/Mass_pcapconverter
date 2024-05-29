#!/usr/bin/env python3
import os

def run_hcxpcapngtool_on_folder(folder_path, output_candidates):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' not found.")
        return

    # Define output file name for ESSID
    output_essid = "essid.wordlist"

    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pcap"):
            # Construct the full path to the pcap file
            pcap_file = os.path.join(folder_path, file_name)

            # Construct the command
            command = f"hcxpcapngtool \"{pcap_file}\" -o {output_candidates} -E {output_essid}"

            # Run the command
            os.system(command)

if __name__ == "__main__":
    folder_path = input("Enter the path to the folder containing pcap files: ")
    output_candidates = "candidates.hc222000"
    run_hcxpcapngtool_on_folder(folder_path, output_candidates)
