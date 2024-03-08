import subprocess
import datetime
import os

def ping_ip(ip_address):
    try:
        result = subprocess.run(["ping", "-c", "10", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Error pinging {ip_address}: {e}"

def traceroute_ip(ip_address):
    try:
        result = subprocess.run(["traceroute", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Error tracing route to {ip_address}: {e}"

def mtr_ip(ip_address):
    try:
        result = subprocess.run(["/usr/sbin/mtr", "-r", "-c", "10", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return f"Error mtr route to {ip_address}: {e}"

def write_to_file(directory, filename, content):
    full_path = os.path.join(directory, filename)
    with open(full_path, "a") as file:
        file.write(content)

def main():
    # Specify the directory where you want to save the files
    output_directory = "/home/XL204913/script/netperf/result/"

    # Read IP addresses from a file (one IP per line)
    with open("/home/XL204913/script/netperf/ip_addresses.txt", "r") as ip_file:
        ip_addresses = ip_file.read().splitlines()

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    for ip in ip_addresses:
        ping_result = ping_ip(ip)
        traceroute_result = traceroute_ip(ip)
        mtr_result = mtr_ip(ip)

        # Create a filename based on IP address and timestamp
        filename = f"{ip}_{timestamp}.txt"

        # Write ping and traceroute results to the file
        write_to_file(output_directory, filename, f"Ping results for {ip}:\n{ping_result}\n\n")
        write_to_file(output_directory, filename, f"Traceroute results for {ip}:\n{traceroute_result}\n\n")
        write_to_file(output_directory, filename, f"MTR results for {ip}:\n{mtr_result}\n\n")

if __name__ == "__main__":
    main()

