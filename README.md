# Get_IPs_from_file

Simple python script to:

- Extract IPs from a text file entered as a script argument
- Find all IPs within text file using Regex
- Check each IP is valid IPv4 address
- Output file with a list of validated IPv4 addresses using input file name


Example usage:
```
python3 get_ips_from_file.py text-with-ips.txt
```
Example output file name:
```
text-with-ips-VALIDATED_IPs.txt
```
